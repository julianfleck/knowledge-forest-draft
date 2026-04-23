# Handover Briefing

**Flow:** orchestrator → (webhook-server) → personal-agent

One briefing per (event × subscriber). Carries the orchestrator's
promise: "I have read this person's garden at this commit, and
here is why I think the share might matter to them."

## Shape

```json
{
  "briefing_id": "<ULID>",
  "created_at": "<ISO-8601 UTC>",
  "priority": "normal | mention",
  "recipient": { "agent_id": "julian" },
  "triggering_event": { "correlation_id": "<discord message id>" },
  "resource": {
    "url": "https://...",
    "title": "...",
    "shared_by": "corey",
    "shared_in": "#knowledge-forest",
    "shared_at": "<ISO-8601 UTC>",
    "message_text": "<the original Discord message>"
  },
  "context_frame": { ... see context-frame.md ... },
  "relevance_note": "<one paragraph: why this might matter to the recipient, grounded in their garden>",
  "garden_read": {
    "repo": "github.com/julian/private-garden",
    "commit_sha": "abc123deadbeef",
    "read_paths": ["notes/mind-palace.md", "notes/memory-architecture.md"],
    "read_at": "<ISO-8601 UTC>"
  }
}
```

## Priority

- `normal` — public share, no direct address.
- `mention` — the sharer named this recipient in
  `resource.message_text`. Agents treat mentions as a strong
  surface signal.

Agents own the final surface/keep/ignore decision. Priority is a
hint, not an order.

## The garden-read promise

`garden_read` names the repo, commit SHA, and full list of paths
the orchestrator read while writing `relevance_note`. A personal
agent MAY trust the promise and act without re-reading. Agents
that verify re-read `read_paths` at `commit_sha`.

If the orchestrator could not read the garden at all, it does not
emit a briefing. If it read but found nothing relevant, it emits a
briefing with a short negative `relevance_note` — negatives feed
the hypothesis test.

## Example

```json
{
  "briefing_id": "bf_01HZXYZ789",
  "created_at": "2026-04-23T15:31:00Z",
  "priority": "mention",
  "recipient": { "agent_id": "julian" },
  "triggering_event": { "correlation_id": "1226543210987654321" },
  "resource": {
    "url": "https://example.com/alexander.pdf",
    "title": "A Pattern Language",
    "shared_by": "corey",
    "shared_in": "#knowledge-forest",
    "shared_at": "2026-04-23T15:30:00Z",
    "message_text": "@julian reminded me of your mind-palace thread"
  },
  "context_frame": {
    "who": "corey",
    "when": "2026-04-23T15:30:00Z",
    "why": null,
    "what": "https://example.com/alexander.pdf",
    "where": "#knowledge-forest",
    "how": "discord-share"
  },
  "relevance_note": "Alexander's pattern language is cited directly in your mind-palace notes as prior art for 'grammar of loci' thinking. The share arrived in reply to your own thread.",
  "garden_read": {
    "repo": "github.com/julian/private-garden",
    "commit_sha": "abc123deadbeef",
    "read_paths": ["notes/mind-palace.md", "notes/memory-architecture.md"],
    "read_at": "2026-04-23T15:30:45Z"
  }
}
```
