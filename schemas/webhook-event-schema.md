# Webhook Event Schema — v1 (draft)

**Author:** @kf-lead · **Status:** draft · **Date:** 2026-04-17
**Consumed by:** the orchestrator agent
**Produced by:** GuildBot (atlasresearch / Josh) via HTTP POST

## Role

This is the schema for the single event GuildBot POSTs to the
orchestrator whenever a user shares a resource in the dedicated
Discord channel. It is the *entry point* of the whole flow: one
share → one event → one orchestrator wake → N handover briefings.

Design lens: handover fidelity. GuildBot promises a specific shape;
the orchestrator must be able to fail closed when that shape is not
honored. We also care about delivery semantics — HTTP is lossy, and
Corey called out in the meeting that he doesn't want a chatty
"always pulling" feel (briefing §6.4). At-least-once + dedup is
cheap insurance.

## Transport

- HTTP POST, `Content-Type: application/json`, body = one JSON
  object matching this schema.
- Endpoint owned by the orchestrator (HTTPS, stable URL; URL itself
  is configured per-deployment, not hard-coded in GuildBot).
- Auth: shared-secret HMAC header `X-KF-Signature:
  sha256=<hex>`. Secret distributed out of band. Optional for the
  very first bring-up but **required** before the POC leaves
  Julian's laptop. Noted as a deferred must-have in open questions.

## Required fields

| Field | Type | Notes |
|---|---|---|
| `schema_version` | string (SemVer major) | `"1"` for v1. Receiver rejects on major mismatch. |
| `event_type` | string (enum) | MVP has exactly one: `discord.resource_shared`. |
| `event_id` | string (GuildBot-assigned ULID/UUID) | Uniquely identifies this delivery attempt. Not the dedup key. |
| `correlation_id` | string | Stable across retries. MVP = Discord message ID. THIS is the dedup key. |
| `occurred_at` | string (ISO-8601 UTC) | When the share happened in Discord. |
| `source` | object | see below |
| `who` | object | see below |
| `what` | object | see below |
| `context` | object | see below |

### Optional fields

| Field | Type | Notes |
|---|---|---|
| `signature` | string | HMAC; also sent as header. Duplicating into the body lets us persist it on the orchestrator side for replay. |
| `where.channel_name` | string | Human-readable channel name if differs from `source.channel_id`. |

### Sub-object shapes

`source`:
```
{
  "bot": "guildbot",
  "bot_version": "x.y.z",
  "guild_id": "<discord snowflake>",
  "channel_id": "<discord snowflake>",
  "channel_name": "#knowledge-forest"
}
```

`who` (the sharer):
```
{
  "discord_user_id": "<snowflake>",
  "discord_username": "corey",
  "known_identity": "corey@atlasresearch"   // optional; resolved via config map
}
```

`what` (the shared resource):
```
{
  "url": "https://...",
  "preview": {                              // optional — absent OR {fetch_error: "..."}
    "title": "...",
    "description": "...",
    "image_url": "...",
    "fetched_at": "<ISO-8601 UTC>"
  },
  "attachments": []                         // reserved for future; MVP always []
}
```

`context` (the surrounding Discord message):
```
{
  "message_text": "<raw message content>",
  "reply_to": null                          // or { "message_id": "...", "author": "..." }
}
```

## Example payload

```json
{
  "schema_version": "1",
  "event_type": "discord.resource_shared",
  "event_id": "evt_01HZABC123",
  "correlation_id": "1226543210987654321",
  "occurred_at": "2026-04-17T15:30:00Z",
  "source": {
    "bot": "guildbot",
    "bot_version": "0.3.1",
    "guild_id": "1220000000000000000",
    "channel_id": "1220000000000000001",
    "channel_name": "#knowledge-forest"
  },
  "who": {
    "discord_user_id": "1220000000000000002",
    "discord_username": "corey",
    "known_identity": "corey@atlasresearch"
  },
  "what": {
    "url": "https://example.com/alexander-pattern-language.pdf",
    "preview": {
      "title": "A Pattern Language",
      "description": "Christopher Alexander et al., 1977.",
      "image_url": null,
      "fetched_at": "2026-04-17T15:30:02Z"
    },
    "attachments": []
  },
  "context": {
    "message_text": "this reminded me of Julian's mind-palace thread",
    "reply_to": null
  },
  "signature": "sha256=deadbeef..."
}
```

## Failure modes (what the orchestrator does)

| Condition | Response | Action |
|---|---|---|
| Missing required field | `400 {error, field, event_id?}` | Drop; do NOT partially process. |
| `schema_version` major mismatch | `400 {error: "schema_version_unsupported", supported: ["1"]}` | Drop. |
| Invalid HMAC (when enforced) | `401` | Drop; log. |
| Malformed / unreachable URL in `what.url` | `200 {status: "accepted"}` | Accept event; `what.preview = {fetch_error: "<reason>"}`; synthesis is allowed to proceed with URL only. |
| Duplicate `correlation_id` | `200 {status: "deduped", existing_event_id: "<id>"}` | No new briefings fired. Idempotent. |
| Well-formed but orchestrator is down | HTTP error | GuildBot is expected to retry (at-least-once). Dedup handles the consequence. |

## Delivery semantics (contract)

- **At-least-once.** GuildBot MAY retry on non-2xx or timeout.
- **Idempotent at the orchestrator.** Two POSTs with the same
  `correlation_id` produce the same side effects as one.
- **Ordering: none promised.** Personal agents must not rely on
  receive order matching share order.
- **Batching: not supported in v1.** One share → one event. This is
  the simplest shape; if we discover batching is needed, v2.

## Open questions (for atlasresearch / Josh)

1. Does GuildBot already assign a stable event ID we should piggyback on, or do we mint one?
2. What is GuildBot's retry policy today? Can we count on idempotent retry, or do we need to add server-side rate limiting?
3. Is there a preview pipeline already, or does the orchestrator need to fetch URL previews itself?
4. When is HMAC achievable? Bring-up without auth is acceptable for a demo day but not for leaving Julian's laptop.

## Non-goals for v1

- No access control beyond HMAC.
- No batching.
- No event-type pluralization (only `discord.resource_shared`).
- No signed payload encryption — the body is private-ish but not secret.
- No inline 6-dimension frame. That frame is filled *by the orchestrator* after the event is received, not by GuildBot.

## Version discipline

- `schema_version` is the only allowed breakage axis.
- Adding optional fields does NOT bump `schema_version`.
- Removing a field, changing a field's type, or renaming a field DOES bump it.
- Receiver rejects unknown major versions; MAY accept unknown optional fields silently.
