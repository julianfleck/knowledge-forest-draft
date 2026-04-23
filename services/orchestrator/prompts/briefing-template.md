# Briefing Template — orchestrator

Emit one JSON object per subscriber, matching
[`schemas/handover-briefing.md`](../../../schemas/handover-briefing.md).

```json
{
  "briefing_id": "<fresh ULID>",
  "created_at": "<ISO-8601 UTC>",
  "priority": "normal | mention",
  "recipient": { "agent_id": "<AGENT_ID>" },
  "triggering_event": { "correlation_id": "<event.correlation_id>" },
  "resource": {
    "url": "<event.url>",
    "title": "<event.title or null>",
    "shared_by": "<event.sharer.agent_id or discord_username>",
    "shared_in": "<event.channel.channel_name>",
    "shared_at": "<event.occurred_at>",
    "message_text": "<event.message_text>"
  },
  "context_frame": {
    "who": "<event.sharer.agent_id>",
    "when": "<event.occurred_at>",
    "why": null,
    "what": "<event.url>",
    "where": "<event.channel.channel_name>",
    "how": "discord-share"
  },
  "relevance_note": "<one paragraph, grounded in garden_read.read_paths>",
  "garden_read": {
    "repo": "<participant's garden repo>",
    "commit_sha": "<sha at read time>",
    "read_paths": ["<path>", "..."],
    "read_at": "<ISO-8601 UTC>"
  }
}
```

## Rules

- `priority = "mention"` iff this recipient's `agent_id` was named
  in `event.message_text` (resolved via `identity-config`).
- `relevance_note` must be grounded in `read_paths`. If you read
  the garden and found nothing relevant, write a short negative
  note saying so.
- If the garden could not be read at all, do not emit a briefing
  for that subscriber.
