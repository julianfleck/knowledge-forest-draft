# event-log

## What this module does

Stores the append-only history of what happens to each shared
resource. Every share, every keep, every "I added context later"
reply becomes another entry on the resource's log.

The metaphor is a git commit log: each event is a commit, with a
timestamp, an author (the agent that emitted it), a parent ref
to the previous event on this resource, and a body that is the
context frame at that moment.

For the POC: linear history per resource, no branching (Q1).

## What lives here (sketch)

- An event store keyed by resource URI
- Two event types in the POC: `sharing.event` and `keep.event`
- Both carry the same context-frame shape (see `schema/`),
  populated from sender or recipient perspective
- Replies on the share's Discord thread (see `chat/`) become
  additional context events on the same log

## Who talks to it

- `chat/` writes events when something is shared in Discord, or
  when a thread reply adds context
- `agents/` (supervisor + personal agents) write events when they
  keep a resource into the personal knowledge garden
- `fingerprint/` reads events to compute channel + user snapshots

## Open questions

- **Storage shape**: one markdown file per resource (append-only),
  jsonl, or SQLite? Default leaning is file-based per metasphere's
  observability principle. Decide once we know how `fingerprint/`
  reads it.
- **Multi-resource share events**: Christina's "article + draft
  map shared together" case — one event with N resource refs, or
  N parallel events? Defer.
