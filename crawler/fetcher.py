"""HTTP fetching for binary downloads and HTML pages.

HTML uses a two-tier strategy:

- **Static fetch.** Pull the page over HTTP, extract the readable body. Cheap
  and deterministic; works for any server-rendered page.
- **Rendered fetch.** Load the page in a headless browser, wait for content
  selectors, then extract the readable body from the rendered DOM. Catches
  pages whose content is injected by client-side JavaScript.

The rendered tier is only used when the static tier returns suspiciously
little text — see ``SHORT_BODY_THRESHOLD``.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

import httpx

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (knowledge-forest crawler) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"
)

# Static extraction is treated as failed and the rendered tier kicks in when
# the extracted text is shorter than this. Catches JS-injected pages where the
# static HTML is essentially empty.
SHORT_BODY_THRESHOLD = 200

# Selectors the headless browser waits for before grabbing content. Best-effort:
# the first one that matches wins; if none match we just take the full body.
CONTENT_SELECTORS = [
    "article",
    "main",
    "[role=main]",
    ".content",
    "#content",
    ".post-content",
    ".article-content",
]


@dataclass
class HtmlFetch:
    """Result of fetching an HTML page.

    ``markdown`` is the extracted readable body. ``raw_html`` is the HTML the
    extractor ran against (useful for a follow-up metadata pass). ``fetch_method``
    is ``"static"`` or ``"rendered"``.
    """

    markdown: str
    raw_html: str | None
    fetch_method: str


@dataclass
class BinaryFetch:
    """Result of downloading a non-HTML resource (PDF, Office doc, etc)."""

    content: bytes
    content_type: str
    fetch_method: str  # always "direct" for now


def download_binary(url: str, *, timeout: float = 30.0) -> BinaryFetch:
    """Download a URL as raw bytes plus its content-type header."""
    with httpx.Client(
        follow_redirects=True,
        timeout=timeout,
        headers={"User-Agent": DEFAULT_USER_AGENT},
    ) as client:
        response = client.get(url)
        response.raise_for_status()
        return BinaryFetch(
            content=response.content,
            content_type=response.headers.get("content-type", ""),
            fetch_method="direct",
        )


def fetch_html(url: str, *, timeout: float = 30.0) -> HtmlFetch:
    """Fetch an HTML page as markdown, escalating to a headless browser if needed."""
    static = _fetch_html_static(url, timeout=timeout)
    if static is not None and len(static.markdown) >= SHORT_BODY_THRESHOLD:
        return static

    rendered = _fetch_html_rendered(url, timeout=timeout)
    if rendered is not None:
        return rendered

    # Both tiers failed to find substantial content. Return whatever the
    # static tier got, even if short — better than nothing.
    if static is not None:
        return static

    raise RuntimeError(f"Could not fetch HTML from {url}")


def _fetch_html_static(url: str, *, timeout: float) -> HtmlFetch | None:
    """Pull the page over HTTP and extract readable content from the raw HTML."""
    import trafilatura

    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return None

    markdown = _extract_readable_markdown(downloaded)
    if not markdown:
        return None

    return HtmlFetch(markdown=markdown, raw_html=downloaded, fetch_method="static")


def _fetch_html_rendered(url: str, *, timeout: float) -> HtmlFetch | None:
    """Render the page in a headless browser, then extract readable content."""
    # The headless browser API is synchronous, so it's pushed onto a worker
    # thread to stay safe under callers that may be running an asyncio loop.
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(_render_in_browser, url, timeout)
        rendered_html = future.result()

    if not rendered_html:
        return None

    markdown = _extract_readable_markdown(rendered_html)
    if not markdown:
        return None

    return HtmlFetch(markdown=markdown, raw_html=rendered_html, fetch_method="rendered")


def _render_in_browser(url: str, timeout: float) -> str | None:
    """Open the URL in headless Chromium, wait for content, return the DOM HTML."""
    from playwright.sync_api import sync_playwright

    timeout_ms = int(timeout * 1000)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            context = browser.new_context(user_agent=DEFAULT_USER_AGENT)
            page = context.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)

            for selector in CONTENT_SELECTORS:
                try:
                    page.wait_for_selector(selector, timeout=2000, state="attached")
                    break
                except Exception:
                    continue

            return page.content()
        finally:
            browser.close()


def _extract_readable_markdown(html: str) -> str | None:
    """Strip boilerplate from HTML and return the article body as markdown."""
    import trafilatura

    extracted = trafilatura.extract(
        html,
        output_format="markdown",
        include_links=True,
        include_tables=True,
        favor_precision=False,
    )
    if not extracted:
        return None
    return extracted.strip()
