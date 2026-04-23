# schemas

The wire formats and storage records shared between services.

## Wire

| Schema                                           | Flow                            |
|--------------------------------------------------|---------------------------------|
| [`webhook-event.md`](./webhook-event.md)         | discord-bot → webhook-server    |
| [`subscription.md`](./subscription.md)           | personal-agent ↔ webhook-server |
| [`handover-briefing.md`](./handover-briefing.md) | webhook-server → personal-agent |
| [`agent-response.md`](./agent-response.md)       | personal-agent → webhook-server |

## Nested / stored

| Schema                                   | Used in                                   |
|------------------------------------------|-------------------------------------------|
| [`context-frame.md`](./context-frame.md) | Briefings and resource records.           |
| [`resource.md`](./resource.md)           | Group garden and personal gardens.        |

## Conventions

- Timestamps are ISO-8601 UTC with a `Z` suffix.
- HTTP bodies are `application/json`.
- HTTP payloads are signed with `X-KF-Signature: sha256=<hex>`
  using the appropriate shared secret.
- IDs are ULIDs unless they're Discord snowflakes (messages,
  users, channels, guilds).
