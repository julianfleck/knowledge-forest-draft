from pathlib import Path
from typing import Protocol

from crawler.models import AdapterResult


class Adapter(Protocol):
    """Convert a source (bytes or a file path) to markdown + metadata.

    ``source_url`` is informational — adapters may include it in the returned
    metadata but should not fetch from it.

    ``source_format`` is the normalized format string (``"docx"``, ``"pdf"``,
    ...). Adapters that handle multiple formats may use it to disambiguate
    inputs (for example, picking the right temp-file suffix for a downstream
    library that dispatches on extension). Single-format adapters can ignore
    it.
    """

    def from_bytes(
        self,
        content: bytes,
        *,
        source_url: str | None = None,
        source_format: str | None = None,
    ) -> AdapterResult: ...

    def from_path(self, path: Path) -> AdapterResult: ...
