from crawler.adapters.base import Adapter
from crawler.adapters.html import HtmlAdapter
from crawler.adapters.office import OfficeAdapter
from crawler.adapters.pdf import PdfAdapter
from crawler.adapters.text import TextAdapter

__all__ = [
    "Adapter",
    "HtmlAdapter",
    "OfficeAdapter",
    "PdfAdapter",
    "TextAdapter",
    "get_adapter",
]


_REGISTRY: dict[str, Adapter] = {}


def get_adapter(source_format: str) -> Adapter:
    if not _REGISTRY:
        _bootstrap_registry()
    try:
        return _REGISTRY[source_format]
    except KeyError as exc:
        raise ValueError(f"No adapter registered for format: {source_format!r}") from exc


def _bootstrap_registry() -> None:
    html = HtmlAdapter()
    office = OfficeAdapter()
    pdf = PdfAdapter()
    text = TextAdapter()

    _REGISTRY.update(
        {
            "html": html,
            "pdf": pdf,
            "docx": office,
            "xlsx": office,
            "pptx": office,
            "md": text,
            "txt": text,
        }
    )
