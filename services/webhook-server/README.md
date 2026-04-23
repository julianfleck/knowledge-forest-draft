# webhook-server

The hub. Receives events from the Discord bot, holds the
subscription registry, invokes the orchestrator, routes keeps,
and fans briefings out to personal agents.

## Responsibilities

- **Inbound events** — accept `resource.shared` and
  `resource.kept` events from the bot per
  [`schemas/webhook-event.md`](../../schemas/webhook-event.md).
  Verify HMAC, validate, persist, dedup by `correlation_id`.
- **Subscriptions** — accept register requests from personal
  agents per
  [`schemas/subscription.md`](../../schemas/subscription.md).
- **On `resource.shared`** — invoke the orchestrator; collect
  briefings; deliver each to the matching subscriber.
- **On `resource.kept`** — route the event to the keeper's
  personal agent (via their subscription stream) so the agent can
  persist the record to the private garden.
- **Responses** — accept `surfaced | kept | ignored` responses
  from personal agents per
  [`schemas/agent-response.md`](../../schemas/agent-response.md).
- **Group log** — append every event, briefing, and response to
  a shared log the group can inspect.

## Non-responsibilities

- No reasoning. The orchestrator decides relevance and priority.
- No writes to any garden.
- No Discord-specific logic beyond trusting the bot.

## HTTP endpoints

| Method | Path             | Purpose                                   |
|--------|------------------|-------------------------------------------|
| POST   | `/events`        | Inbound from the bot (both event types).  |
| POST   | `/subscriptions` | Register a personal agent.                |
| POST   | `/responses`     | Personal-agent response.                  |
| GET    | `/log`           | Read-only group event log.                |

All requests signed with HMAC in `X-KF-Signature`.

## Addressing

Each briefing carries `recipient.agent_id` and `priority` ∈
{`normal`, `mention`}. The server delivers on the stream matching
`agent_id`, mirroring priority in the `X-KF-Priority` header. A
`resource.kept` event is delivered on exactly one stream — the
keeper's — as a plain event pass-through (not a briefing).

## POC boundaries

- File- or SQLite-backed storage. No external DB.
- Sequential HTTP fanout. No queue.
- At-least-once delivery with bounded retry.
- No rate limiting, no streaming transport.
