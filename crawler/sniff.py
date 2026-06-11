"""Map content-types / extensions to a normalized ``source_format`` string."""

from pathlib import Path
from urllib.parse import urlparse

_EXTENSION_FORMAT = {
    ".pdf": "pdf",
    ".docx": "docx",
    ".xlsx": "xlsx",
    ".pptx": "pptx",
    ".md": "md",
    ".markdown": "md",
    ".txt": "txt",
    ".html": "html",
    ".htm": "html",
}

_CONTENT_TYPE_FORMAT = {
    "application/pdf": "pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "xlsx",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": "pptx",
    "application/msword": "docx",
    "application/vnd.ms-excel": "xlsx",
    "application/vnd.ms-powerpoint": "pptx",
    "text/markdown": "md",
    "text/plain": "txt",
    "text/html": "html",
    "application/xhtml+xml": "html",
}


def sniff_from_extension(path_or_url: str | Path) -> str | None:
    if isinstance(path_or_url, Path):
        suffix = path_or_url.suffix.lower()
    else:
        # URL: pull the path component, then its suffix
        parsed = urlparse(str(path_or_url))
        suffix = Path(parsed.path).suffix.lower()
    return _EXTENSION_FORMAT.get(suffix)


def sniff_from_content_type(content_type: str) -> str | None:
    # Strip charset etc.: "text/html; charset=utf-8" -> "text/html"
    main = content_type.split(";", 1)[0].strip().lower()
    return _CONTENT_TYPE_FORMAT.get(main)
