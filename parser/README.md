# parser

## What this module does

Reasons over the markdown that [`crawler/`](../crawler/) hands
it, and produces the per-resource artifact every downstream
module needs: a short summary of what the resource argues /
shows / does, an embedding of that summary, structured tags
(topic, activity, artifact type), keywords, named entities — the
per-resource "what is this?" answer.

This is the per-resource read. It runs once per share event.
Roll-ups across many resources (per-channel, per-user) are
[`fingerprint/`](../fingerprint/)'s job, not the parser's. The
parser knows nothing about who the channel is or who the user
is; it just reads the thing in front of it.

Fetching, format conversion (HTML, PDF, Office), and headless-
browser fallback are not the parser's job either — that's
[`crawler/`](../crawler/). The parser starts from clean
markdown.

## How it works (sketch)

For each incoming share event:

1. Ask [`crawler/`](../crawler/) for the resource — returns a
   `CrawledResource` (markdown + source metadata + format).
2. Summarize — a short language-model pass that answers "what
   does this resource argue / show / do?" in a few sentences.
3. Embed the summary — a vector that fingerprint uses for
   cosine prefilter against channel/user fingerprints.
4. Tag it — a topic / activity / artifact-type pass, plus a
   keyword and named-entity pass over the body. The activity /
   artifact axes are what separate "windmill field engineering"
   from "clean-energy policy paper" instead of bucketing both as
   `clean_energy`.
5. Emit a **parsed-resource record** — the URL, the source
   metadata the crawler surfaced, the summary, the embedding,
   the tags / keywords / named entities.

The parsed-resource record is what `fingerprint/` reasons over,
what `agents/` see in their briefings, and what populates
**Layer 2 of `what`** in the six-dimension frame.

## Open questions

- **Chunking.** The parser may eventually break the markdown
  into sensible units (sections, paragraphs, or semantic
  chunks) so fingerprint can match at sub-resource granularity.
  Skipped for the POC — single summary + single embedding per
  resource is the floor we want to validate first.
- **How tags / keywords / NER are done** — full language-model
  pass over the body, library extractors (spaCy NER, KeyBERT
  keywords) plus a small classifier for the topic / activity /
  artifact axes, or a hybrid. Julian's lean: a single language-
  model pass for summary + tags, library extractors for keywords
  / NER. Decide once we've seen 10–20 real shares run through.
- **Embedding model** — `text-embedding-3-small` is the cheap
  default; revisit if recall on real atlasresearch shares is
  poor.

## Who talks to it

- [`crawler/`](../crawler/) is the parser's only input source —
  one `CrawledResource` per share event
- [`chat/`](../chat/) hands the parser each new share event
  (URL or file upload it pulled out of a Discord message); the
  parser calls the crawler under the hood
- [`event-log/`](../event-log/) stores the parsed-resource
  record alongside the share event — the record populates the
  `what` field of the frame on that event
- [`fingerprint/`](../fingerprint/) consumes parsed-resource
  records to maintain channel and user fingerprints, and to
  score an incoming resource against one of them
- [`agents/`](../agents/) read the parsed-resource record in
  their briefings
