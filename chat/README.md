# chat

## What this module does

Connects the system to where humans actually talk — Discord for
the POC, but designed so other platforms (Signal, Slack, Telegram)
are not foreclosed.

Everything the world sees of the system happens here: a share
event arrives because someone posted a link in Discord; a flag
from a personal agent shows up here as a DM; the supervisor's
"I noted this" reply lands here.

## How it works (sketch)

For every message that contains a resource (link, upload, etc.),
the bot opens a Discord thread on that message. Replies on that
thread become additional context events on the same resource's
log (see `event-log/`). This keeps related context consolidated
and out of the main channel's torrent.

Threading is decided for Discord (Q2). Other platforms inherit
the metaphor — if a platform has threads, use them; if not, fall
back to message references.

## What it owns

- A `DiscordClient` (or similar) class that handles the connection
  + message events + thread creation
- A `Resource` extractor that detects when a message contains a
  shareable thing
- The bridge that turns Discord events into `event-log/` writes
  (and outputs from agents into Discord messages)

## Who talks to it

- `routing/` reads incoming events and dispatches to agents
- `agents/` write outputs back through chat (DMs, thread replies)
- `event-log/` is the persistence layer downstream of every event

## Open

- Threading is decided for share events. Open: do we also thread
  on KEEP events ("I kept this") or do those just go to DMs?
