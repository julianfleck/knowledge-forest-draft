# parser

## What this module does

Reads a single shared resource and extracts a structured
representation of its content. Given a URL or a file upload, the
parser produces the per-resource artifact every downstream module
needs: the resource's text, its tags, its keywords, its named
entities — the per-resource "what is this?" answer.

This is the per-resource read. It runs once per share event.
Roll-ups across many resources (per-channel, per-user) are
[`fingerprint/`](../fingerprint/)'s job, not the parser's. The
parser knows nothing about who the channel is or who the user is;
it just reads the thing in front of it.

## How it works (sketch)

For each incoming share event:

1. Fetch the resource — HTTP for URLs, local for file uploads.
2. Extract a plain-text body — readability extraction for web
   pages, text-layer or OCR for PDFs, transcript for video where
   feasible, raw content for plain text.
3. Tag it — a topic / keyword / named-entity pass over the body.
4. Emit a **parsed-resource record** — the URL, the extracted
   body, the tags / keywords / named entities, and any source
   metadata (title, author, publish date) the fetch surfaced.

The parsed-resource record is what `fingerprint/` reasons over,
what `agents/` see in their briefings, and what populates
**Layer 2 of `what`** in the six-dimension frame.

## How parsing is done (open question — decide in the meeting)

Two candidate shapes:

1. **Library-only.** Use existing extractors (readability,
   trafilatura, pdfminer, etc.) plus a topic / NER pass with a
   small model. Cheap, deterministic, predictable failure modes.
   Loses on weird formats (paywalls, JS-only pages, image-heavy
   PDFs).

2. **Language-model read.** Hand the fetched body to a language
   model and ask for the body, tags, and entities in one call.
   More flexible, more expensive, harder to reproduce.

Julian's current lean is option 1 for the POC, with a
language-model fallback when the library extractor returns a
suspiciously short body.

## Who talks to it

- [`chat/`](../chat/) hands the parser each new share event
  (URL or file upload it pulled out of a Discord message)
- [`event-log/`](../event-log/) stores the parsed-resource record
  alongside the share event — the record populates the `what`
  field of the frame on that event
- [`fingerprint/`](../fingerprint/) consumes parsed-resource
  records to maintain channel and user fingerprints, and to score
  an incoming resource against one of them
- [`agents/`](../agents/) read the parsed-resource record in
  their briefings
