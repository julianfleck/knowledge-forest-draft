"""Fetch URLs and local files; return them as structured markdown.

Public surface:

    from crawler import Crawler
    resource = Crawler().fetch("https://example.com/article")
    resource = Crawler().fetch("/path/to/document.pdf")

``Crawler.fetch`` returns a ``CrawledResource`` containing the resource as
markdown plus any source metadata that was extractable (title, author,
publish date, site name).

See ``crawler/README.md`` for the design.
"""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from crawler.adapters import get_adapter
from crawler.adapters.html import HtmlAdapter
from crawler.fetcher import download_binary, fetch_html
from crawler.models import CrawledResource
from crawler.sniff import sniff_from_content_type, sniff_from_extension

__all__ = ["Crawler", "CrawledResource"]


class Crawler:
    """Fetches a URL or local file and returns it as structured markdown.

    For URLs, the fetch method is picked based on the resource's apparent
    format: HTML pages go through the two-tier HTML fetcher (static, then a
    headless browser as fallback); binary formats are downloaded directly.
    Local files skip the network and read straight from disk.

    Format detection prefers the server's ``Content-Type`` header where
    available, with a fallback to the URL or file extension.
    """

    def __init__(self, *, timeout: float = 30.0) -> None:
        self.timeout = timeout

    def fetch(self, source: str | Path) -> CrawledResource:
        if _is_local_path(source):
            return self._fetch_local(Path(source))
        return self._fetch_url(str(source))

    def _fetch_url(self, url: str) -> CrawledResource:
        # If the URL extension doesn't point at a binary format, treat it as
        # HTML and let the HTML fetcher decide static vs rendered.
        guessed = sniff_from_extension(url)

        if guessed in (None, "html"):
            html = fetch_html(url, timeout=self.timeout)
            html_adapter: HtmlAdapter = get_adapter("html")  # type: ignore[assignment]
            result = html_adapter.from_html(
                html.raw_html or "",
                source_url=url,
                prerendered_markdown=html.markdown,
            )
            return CrawledResource(
                url=url,
                source_format="html",
                markdown=result.markdown,
                metadata=result.metadata,
                fetched_at=_now(),
                fetch_method=html.fetch_method,
            )

        # Binary formats: download bytes and dispatch to a format adapter.
        binary = download_binary(url, timeout=self.timeout)
        source_format = sniff_from_content_type(binary.content_type) or guessed
        adapter = get_adapter(source_format)
        result = adapter.from_bytes(
            binary.content, source_url=url, source_format=source_format
        )
        return CrawledResource(
            url=url,
            source_format=source_format,
            markdown=result.markdown,
            metadata=result.metadata,
            fetched_at=_now(),
            fetch_method=binary.fetch_method,
        )

    def _fetch_local(self, path: Path) -> CrawledResource:
        source_format = sniff_from_extension(path)
        if source_format is None:
            raise ValueError(f"Cannot determine format for local file: {path}")
        adapter = get_adapter(source_format)
        result = adapter.from_path(path)
        return CrawledResource(
            url=f"file://{path.resolve()}",
            source_format=source_format,
            markdown=result.markdown,
            metadata=result.metadata,
            fetched_at=_now(),
            fetch_method="local",
        )


def _is_local_path(source: str | Path) -> bool:
    if isinstance(source, Path):
        return True
    return not (source.startswith("http://") or source.startswith("https://"))


def _now() -> datetime:
    return datetime.now(UTC)
