"""Convert Microsoft Office documents (.docx, .xlsx, .pptx) to markdown."""

from __future__ import annotations

import tempfile
from pathlib import Path

from crawler.models import AdapterResult

_FORMAT_SUFFIX = {
    "docx": ".docx",
    "xlsx": ".xlsx",
    "pptx": ".pptx",
}


class OfficeAdapter:
    def from_bytes(
        self,
        content: bytes,
        *,
        source_url: str | None = None,
        source_format: str | None = None,
    ) -> AdapterResult:
        suffix = _FORMAT_SUFFIX.get(source_format or "", ".bin")
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=True) as tmp:
            tmp.write(content)
            tmp.flush()
            return self.from_path(Path(tmp.name))

    def from_path(self, path: Path) -> AdapterResult:
        from markitdown import MarkItDown

        converter = MarkItDown()
        result = converter.convert(str(path))

        metadata: dict = {}
        title = getattr(result, "title", None)
        if title:
            metadata["title"] = title

        return AdapterResult(
            markdown=(result.text_content or "").strip(),
            metadata=metadata,
        )
