"""Convert HTML to markdown and extract source metadata.

The adapter starts from HTML that has already been fetched — it does no
network work of its own. Conversion strips boilerplate and produces a
readable-body markdown. Metadata extraction prefers JSON-LD where present,
falls back to OpenGraph and article meta tags.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from crawler.models import AdapterResult


class HtmlAdapter:
    def from_bytes(
        self,
        content: bytes,
        *,
        source_url: str | None = None,
        source_format: str | None = None,
    ) -> AdapterResult:
        html = content.decode("utf-8", errors="replace")
        return self.from_html(html, source_url=source_url)

    def from_path(self, path: Path) -> AdapterResult:
        return self.from_html(path.read_text(encoding="utf-8", errors="replace"))

    def from_html(
        self,
        html: str,
        *,
        source_url: str | None = None,
        prerendered_markdown: str | None = None,
    ) -> AdapterResult:
        markdown = prerendered_markdown or _extract_markdown(html)
        metadata = _extract_metadata(html, source_url=source_url)
        return AdapterResult(markdown=markdown, metadata=metadata)


def _extract_markdown(html: str) -> str:
    import trafilatura

    extracted = trafilatura.extract(
        html,
        output_format="markdown",
        include_links=True,
        include_tables=True,
        favor_precision=False,
    )
    return (extracted or "").strip()


def _extract_metadata(html: str, *, source_url: str | None) -> dict:
    """Best-effort metadata: prefer JSON-LD, fall back to OpenGraph / article meta."""
    metadata: dict = {}

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")

    # Tier 1: JSON-LD
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "")
        except (json.JSONDecodeError, TypeError):
            continue
        _merge_jsonld(metadata, data)
        if metadata:
            break

    # Tier 2: OpenGraph / article meta
    if not metadata.get("title"):
        og_title = soup.find("meta", property="og:title")
        if og_title and og_title.get("content"):
            metadata["title"] = og_title["content"]
    if not metadata.get("title") and soup.title and soup.title.string:
        metadata["title"] = soup.title.string.strip()

    if not metadata.get("site_name"):
        og_site = soup.find("meta", property="og:site_name")
        if og_site and og_site.get("content"):
            metadata["site_name"] = og_site["content"]

    if not metadata.get("author"):
        for selector in [
            ("meta", {"name": "author"}),
            ("meta", {"property": "article:author"}),
        ]:
            tag = soup.find(*selector)
            if tag and tag.get("content"):
                metadata["author"] = tag["content"]
                break

    if not metadata.get("published_at"):
        for selector in [
            ("meta", {"property": "article:published_time"}),
            ("meta", {"name": "publish-date"}),
            ("meta", {"name": "date"}),
        ]:
            tag = soup.find(*selector)
            if tag and tag.get("content"):
                metadata["published_at"] = _normalize_date(tag["content"])
                break

    if source_url and "url" not in metadata:
        metadata["url"] = source_url

    return metadata


def _merge_jsonld(metadata: dict, data) -> None:
    # JSON-LD can be a dict, a list, or a @graph-wrapped dict.
    if isinstance(data, list):
        for item in data:
            _merge_jsonld(metadata, item)
        return
    if not isinstance(data, dict):
        return
    if "@graph" in data and isinstance(data["@graph"], list):
        for item in data["@graph"]:
            _merge_jsonld(metadata, item)
        return

    type_ = data.get("@type")
    article_types = {"Article", "NewsArticle", "BlogPosting", "WebPage", "Report"}
    if type_ not in article_types and not isinstance(type_, list):
        return
    if isinstance(type_, list) and not (article_types & set(type_)):
        return

    if "headline" in data and "title" not in metadata:
        metadata["title"] = data["headline"]
    if "datePublished" in data and "published_at" not in metadata:
        metadata["published_at"] = _normalize_date(data["datePublished"])
    if "author" in data and "author" not in metadata:
        author = data["author"]
        if isinstance(author, dict):
            metadata["author"] = author.get("name")
        elif isinstance(author, list) and author:
            first = author[0]
            metadata["author"] = first.get("name") if isinstance(first, dict) else first
        else:
            metadata["author"] = author
    if "publisher" in data and "site_name" not in metadata:
        publisher = data["publisher"]
        if isinstance(publisher, dict):
            metadata["site_name"] = publisher.get("name")
        else:
            metadata["site_name"] = publisher


def _normalize_date(raw: str) -> str:
    raw = raw.strip()
    # Try ISO 8601; if parse fails, just return the raw string.
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00")).isoformat()
    except ValueError:
        return raw
