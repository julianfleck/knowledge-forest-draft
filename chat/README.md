# chat

## What this module does

Connects the system to where humans actually talk. The first
target is **Discord** — the bot watches a designated channel,
picks up messages that contain shareable resources (links, file
uploads), and turns them into share events the rest of the system
can act on.

For the POC this is a straightforward Discord bot integration —
one of the standard libraries (`discord.py` for Python, or
`discord.js` for Node.js) wired up to listen for the events we
care about. No bespoke bot framework needed.

The shape is platform-agnostic enough that other places (Signal,
Slack, etc.) could be added later, but the POC is Discord-only.

## How it works

For every message that contains a resource, the bot opens a
**Discord thread** on that message. Replies on the thread become
additional context events on the same resource's log (see
[`../event-log/`](../event-log/)). Threading keeps related
conversation consolidated and out of the main channel's noise.

Threading is the chosen pattern. Other platforms inherit the
metaphor — if the platform has threads (e.g. Slack), use them; if
not, fall back to message references or quote-replies.

## What it owns

- A Discord client class that handles the connection, the message
  events, and the thread creation
- A small "is this a resource?" detector for each incoming
  message (extracts URLs and file uploads)
- The bridge that turns Discord events into write operations
  against [`../event-log/`](../event-log/), and turns agent
  outputs into Discord messages (DMs, thread replies)

## Who talks to it

- [`routing/`](../routing/) reads the events this module emits
  and decides which agents to wake
- [`agents/`](../agents/) write outputs back through this module
- [`event-log/`](../event-log/) is the persistence layer
  downstream of every event

## Open

- Threading is decided for share events. Open: do we also thread
  on KEEP events (a recipient saying "I kept this resource into
  my garden") or do those just go to direct messages? Default
  leaning: DM-only, to avoid cluttering the share thread with
  many "I kept this" replies.
