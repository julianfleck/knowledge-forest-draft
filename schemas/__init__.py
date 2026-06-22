"""Shared cross-module data shapes.

Each module-spanning contract — the artifacts modules hand off to each other —
lives here as a pydantic model so both producer and consumer reference the
same definition.

Module-internal types (helper records, intermediate values) stay in their
owning module instead.
"""

from schemas.crawled_resource import (
    CrawledResource,
    FetchMethod,
    SourceFormat,
    SourceMetadata,
)

__all__ = [
    "CrawledResource",
    "FetchMethod",
    "SourceFormat",
    "SourceMetadata",
]
