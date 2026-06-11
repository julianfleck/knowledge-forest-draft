# crawler

## What this module does

Takes a URL or a local file path and returns the resource's
content as structured markdown plus whatever source metadata was
on it (title, author, publish date, site name when extractable).

This is the fetch-and-format layer. It knows nothing about
topics, tags, embeddings, channels, or users — it just delivers
clean markdown that downstream modules can reason over.

`crawler/` feeds `parser/`. The parser then does the reasoning
work (summary, embedding, tags, named entities, eventually
chunking) on top of the markdown the crawler produced.

## How it works (sketch)

For each input:

1. **Sniff the format.** Content-type for URLs, extension for
   local files. Falls back to extension on the URL path if the
   server lies about content-type.
2. **Fetch.** Simple HTTP download for binary formats. For HTML
   the fetcher runs a two-tier strategy: a static fetch first
   (HTTP GET + readable-body extraction), then a rendered fetch
   (headless browser + readable-body extraction) when the static
   tier returns suspiciously little content. The rendered tier
   catches pages whose body is injected by client-side
   JavaScript.
3. **Dispatch to a format adapter.** One adapter per family of
   formats; each converts its inputs to markdown and extracts
   what source metadata it can:
   - `html` — readable-body extraction + JSON-LD / OpenGraph /
     article meta.
   - `pdf` — markdown rendering + the document-info dictionary
     (title, author, publish date, page count).
   - `office` — `.docx` / `.xlsx` / `.pptx` conversion.
   - `text` — pass-through for `.md` / `.txt`.
4. **Emit a `CrawledResource` record.** Fields: `url`,
   `source_format`, `markdown`, `metadata`, `fetched_at`,
   `fetch_method`.

## Output shape

```python
@dataclass
class CrawledResource:
    url: str               # http(s):// or file://
    source_format: str     # "html" | "pdf" | "docx" | "xlsx" | "pptx" | "md" | "txt"
    markdown: str
    metadata: dict         # title, author, published_at, site_name (best-effort)
    fetched_at: datetime
    fetch_method: str      # "static" | "rendered" | "direct" | "local"
```

## Library choices

Best-of-breed per format:

| Format | Library |
|--------|---------|
| HTML / web | `trafilatura` (+ `playwright` for the rendered tier) |
| PDF | `pymupdf4llm` |
| docx / xlsx / pptx | `markitdown` |
| md / txt | pass-through |

`trafilatura` is the strongest open-source readable-body
extractor for HTML and emits markdown directly. `pymupdf4llm`
produces markdown tuned for downstream language-model consumption
and can fall back to OCR for scanned PDFs. `markitdown` handles
the Office formats with first-party support for the OOXML shapes.
`markitdown` can also handle PDF and HTML, but its per-format
quality is lower than the specialized libraries above, so it's
only used where it's the strongest option.

## Who talks to it

- [`parser/`](../parser/) calls `Crawler.fetch(source)` and reads
  markdown from the returned `CrawledResource`. The parser owns
  everything that happens to the markdown after this point:
  summary, embedding, tags, named entities, eventual chunking.
- [`chat/`](../chat/) does not call the crawler directly; it
  passes share events (URLs / uploads) into the pipeline and the
  parser is responsible for invoking the crawler.

## Open questions

- **Headless browser dependency.** `playwright` requires a
  Chromium download (~150MB) and a separate `playwright install`
  step. Acceptable for the POC, but worth revisiting if we want
  to ship as a thin function-style deployment.
- **OCR for scanned PDFs.** `pymupdf4llm` layout mode supports
  Tesseract OCR but the prerequisites are heavyweight
  (Tesseract + OpenCV). Off by default; turn on per-call when a
  PDF has no text layer.
- **Rate limiting / politeness.** No throttling yet. Fine for
  POC volumes (handful of shares per day) but a real
  implementation needs at minimum a per-host concurrency cap.
