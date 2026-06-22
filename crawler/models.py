"""Module-internal data shapes used by adapters and the orchestrator.

Cross-module contracts (``CrawledResource``, ``SourceMetadata``, ...) live in
``schemas/`` so producers and consumers reference the same definition.
"""

from dataclasses import dataclass, field


@dataclass
class AdapterResult:
    """What an adapter returns: markdown plus any source metadata it extracted.

    Adapters return a plain dict for metadata; the orchestrator validates and
    promotes it to the typed ``SourceMetadata`` shape when it builds the final
    ``CrawledResource``.
    """

    markdown: str
    metadata: dict = field(default_factory=dict)
