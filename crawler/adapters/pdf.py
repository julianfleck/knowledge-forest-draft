"""Convert PDF documents to markdown and extract source metadata.

Reads the PDF's document-info dictionary for title / author / publish date and
a page count, then renders the body as markdown.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

from crawler.models import AdapterResult


class PdfAdapter:
    def from_bytes(
        self,
        content: bytes,
        *,
        source_url: str | None = None,
        source_format: str | None = None,
    ) -> AdapterResult:
        # pymupdf4llm reads from a path; spool the bytes through a temp file.
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=True) as tmp:
            tmp.write(content)
            tmp.flush()
            return self.from_path(Path(tmp.name))

    def from_path(self, path: Path) -> AdapterResult:
        import pymupdf4llm

        markdown = pymupdf4llm.to_markdown(str(path))
        metadata = _extract_pdf_metadata(path)
        return AdapterResult(markdown=markdown.strip(), metadata=metadata)


def _extract_pdf_metadata(path: Path) -> dict:
    import pymupdf

    metadata: dict = {}
    try:
        doc = pymupdf.open(str(path))
    except Exception:
        return metadata

    try:
        info = doc.metadata or {}
        if info.get("title"):
            metadata["title"] = info["title"]
        if info.get("author"):
            metadata["author"] = info["author"]
        if info.get("creationDate"):
            metadata["published_at"] = _normalize_pdf_date(info["creationDate"])
        if doc.page_count:
            metadata["page_count"] = doc.page_count
    finally:
        doc.close()

    return metadata


def _normalize_pdf_date(raw: str) -> str:
    # PDF dates look like "D:20240315120000+00'00'". Return the raw string if
    # we can't cheaply massage it into something readable.
    if raw.startswith("D:") and len(raw) >= 16:
        try:
            yyyy = raw[2:6]
            mm = raw[6:8]
            dd = raw[8:10]
            return f"{yyyy}-{mm}-{dd}"
        except IndexError:
            return raw
    return raw
