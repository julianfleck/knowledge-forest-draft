"""Schema for a fetched resource, the handoff from the crawler to the parser."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

SourceFormat = Literal["html", "pdf", "docx", "xlsx", "pptx", "md", "txt"]
"""Normalized resource format. The crawler picks an adapter from this value."""

FetchMethod = Literal["static", "rendered", "direct", "local"]
"""How the resource was retrieved.

- ``static``: HTTP GET, body extracted from the raw HTML.
- ``rendered``: Headless-browser render, body extracted from the rendered DOM.
- ``direct``: HTTP GET, content used directly (PDF, Office documents).
- ``local``: Read from a local file path.
"""


class SourceMetadata(BaseModel):
    """Best-effort metadata recovered from the source.

    Every field is optional — not every format exposes every field. Adapters
    may attach format-specific fields beyond the ones listed here; the model
    is configured to accept and preserve them.
    """

    title: str | None = None
    author: str | None = None
    published_at: str | None = None
    site_name: str | None = None
    page_count: int | None = None
    url: str | None = None

    model_config = ConfigDict(extra="allow")


class CrawledResource(BaseModel):
    """A fetched resource as structured markdown plus source metadata.

    Produced by the crawler. Consumed by the parser as the input to the
    summary / embedding / tagging pass.
    """

    url: str
    source_format: SourceFormat
    markdown: str
    fetched_at: datetime
    fetch_method: FetchMethod
    metadata: SourceMetadata = Field(default_factory=SourceMetadata)
