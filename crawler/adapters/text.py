"""Pass-through adapter for already-textual formats (markdown, plain text)."""

from __future__ import annotations

from pathlib import Path

from crawler.models import AdapterResult


class TextAdapter:
    def from_bytes(
        self,
        content: bytes,
        *,
        source_url: str | None = None,
        source_format: str | None = None,
    ) -> AdapterResult:
        return AdapterResult(markdown=content.decode("utf-8", errors="replace").strip())

    def from_path(self, path: Path) -> AdapterResult:
        return AdapterResult(markdown=path.read_text(encoding="utf-8", errors="replace").strip())
