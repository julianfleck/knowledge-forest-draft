from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CrawledResource:
    url: str
    source_format: str
    markdown: str
    fetched_at: datetime
    fetch_method: str
    metadata: dict = field(default_factory=dict)


@dataclass
class AdapterResult:
    markdown: str
    metadata: dict = field(default_factory=dict)
