# Webhook Event

**Flow:** discord-bot → webhook-server
**Transport:** HTTP POST to `/events`, JSON body, HMAC-SHA256 in
`X-KF-Signature: sha256=<hex>` using a shared secret.

Two event types. The webhook server dedups by `correlation_id`,
so at-least-once retries are safe.

| `event_type`      | When                                                         |
|-------------------|--------------------------------------------------------------|
| `resource.shared` | A resource was shared in the channel.                        |
| `resource.kept`   | A participant signalled "keep this" via Discord (reaction or reply to a prior share). |

## `resource.shared`

```json
{
  "event_type": "resource.shared",
  "correlation_id": "<discord message id>",
  "occurred_at": "<ISO-8601 UTC>",
  "channel": {
    "guild_id": "<discord snowflake>",
    "channel_id": "<discord snowflake>",
    "channel_name": "#knowledge-forest"
  },
  "sharer": {
    "discord_user_id": "<snowflake>",
    "discord_username": "corey",
    "agent_id": "corey"
  },
  "url": "https://...",
  "title": "<url preview title or null>",
  "description": "<url preview description or null>",
  "message_text": "<the Discord message, verbatim>"
}
```

## `resource.kept`

Emitted when a participant reacts on a prior share with the
configured bookmark emoji, or replies to it with a keep verb.

```json
{
  "event_type": "resource.kept",
  "correlation_id": "<discord id of the reaction or reply>",
  "occurred_at": "<ISO-8601 UTC>",
  "channel": {
    "guild_id": "<discord snowflake>",
    "channel_id": "<discord snowflake>",
    "channel_name": "#knowledge-forest"
  },
  "keeper": {
    "discord_user_id": "<snowflake>",
    "discord_username": "julian",
    "agent_id": "julian"
  },
  "target": {
    "correlation_id": "<original share's message id>",
    "url": "<resource url, for convenience>"
  },
  "method": "reaction | reply",
  "note": "<reply text if method=reply, else null>"
}
```

`target.correlation_id` points back to the `resource.shared`
event. The webhook server uses it to route the keep to the right
personal agent and to prevent duplicate keeps.

## Server response (both event types)

| Condition                  | Response                                           |
|----------------------------|----------------------------------------------------|
| Accepted                   | `202 {status: "accepted"}`                         |
| Duplicate `correlation_id` | `200 {status: "deduped"}`                          |
| Missing required field     | `400 {error, field}`                               |
| Invalid HMAC               | `401`                                              |

## Example — `resource.shared`

```json
{
  "event_type": "resource.shared",
  "correlation_id": "1226543210987654321",
  "occurred_at": "2026-04-23T15:30:00Z",
  "channel": {
    "guild_id": "1220000000000000000",
    "channel_id": "1220000000000000001",
    "channel_name": "#knowledge-forest"
  },
  "sharer": {
    "discord_user_id": "1220000000000000002",
    "discord_username": "corey",
    "agent_id": "corey"
  },
  "url": "https://example.com/alexander.pdf",
  "title": "A Pattern Language",
  "description": "Alexander et al., 1977.",
  "message_text": "@julian reminded me of your mind-palace thread"
}
```

## Example — `resource.kept`

```json
{
  "event_type": "resource.kept",
  "correlation_id": "1226543299999999999",
  "occurred_at": "2026-04-23T15:47:00Z",
  "channel": {
    "guild_id": "1220000000000000000",
    "channel_id": "1220000000000000001",
    "channel_name": "#knowledge-forest"
  },
  "keeper": {
    "discord_user_id": "1220000000000000004",
    "discord_username": "julian",
    "agent_id": "julian"
  },
  "target": {
    "correlation_id": "1226543210987654321",
    "url": "https://example.com/alexander.pdf"
  },
  "method": "reaction",
  "note": null
}
```
