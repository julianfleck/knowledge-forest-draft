# event-log

## What this module does

Stores the running history of what happens to each shared
resource. Every share, every keep, every "I added context later"
reply becomes another entry on that resource's log.

The metaphor is a git commit log. Each event is a commit on the
resource: a timestamp, an author (the agent or human that
emitted it), a parent reference to the previous event on this
resource, and a body that is the six-dimension context frame at
that moment.

For the POC: linear history per resource, no branching.

## What lives here (sketch)

- An event store keyed by resource URL
- Two event types in the POC:
  - `sharing.event` — emitted when someone first shares a resource
  - `keep.event` — emitted when a recipient saves the resource
    into their personal knowledge garden
- Both events carry the same six-dimension frame, populated from
  the emitter's perspective (sharer for `sharing.event`, recipient
  for `keep.event`)
- Replies on the share's Discord thread (see
  [`../chat/`](../chat/)) become additional context events on the
  same log

## Who talks to it

- [`chat/`](../chat/) writes events when a share is posted in
  Discord, or when a thread reply adds context
- [`agents/`](../agents/) write events when they keep a resource
  into the personal knowledge garden
- [`parser/`](../parser/) writes a parsed-resource record onto
  each share event — the body, tags, keywords, and named entities
  that populate Layer 2 of `what`
- [`fingerprint/`](../fingerprint/) reads parsed-resource records
  off the log to maintain the channel and per-user fingerprints

## Open questions

- **Storage shape.** One markdown file per resource (append-only),
  JSON Lines, or a small SQLite database? Default leaning is
  file-based — easy to inspect by eye, easy to commit to a
  private GitHub repo, easy to audit. Decide once we know how
  `parser/` writes parsed records and how `fingerprint/` reads
  them back.
- **Multi-resource share events.** Sometimes someone shares two
  things at once (e.g. an article and a related draft map). Do
  we emit one event with multiple resource references, or N
  parallel events? Defer.
