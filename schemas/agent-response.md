# Agent Response

**Flow:** personal-agent → webhook-server

One response per briefing. Records what the personal agent did
and why. Appended to the group event log.

## Actions

| Action     | Meaning                                                                  |
|------------|--------------------------------------------------------------------------|
| `surfaced` | Agent passed the briefing to its human through its chosen channel.       |
| `kept`     | Agent wrote the resource into the human's private garden. Triggered either by a `resource.kept` event relayed from Discord, or by direct human instruction to the agent. |
| `ignored`  | Agent decided not to surface.                                            |

A single briefing can produce more than one response over its
lifetime — e.g. `surfaced` first, then `kept` later. Each is its
own entry.

## Shape

```json
{
  "briefing_id": "<briefing_id if tracing a briefing, else null>",
  "event_correlation_id": "<resource.kept event id if triggered by one, else null>",
  "responder": { "agent_id": "julian" },
  "decided_at": "<ISO-8601 UTC>",
  "action": "surfaced | kept | ignored",
  "reason": "<one sentence>",
  "garden_path": "notes/kept/alexander-pattern-language.md"
}
```

- `reason` is required on every response. It's the overload
  signal — write a real sentence.
- `garden_path` is required on `kept` and omitted otherwise.
  The agent chooses the path; the webhook server just logs it.
- Exactly one of `briefing_id` or `event_correlation_id` is
  set. `surfaced` and `ignored` always trace a briefing.
  `kept` traces a briefing (agent-originated, after a prior
  surface) or an event (Discord-originated reaction/reply).

## Delivery

```
POST /responses
Content-Type: application/json
X-KF-Signature: sha256=<hex>        // HMAC using subscription secret
```

## Example

```json
{
  "briefing_id": null,
  "event_correlation_id": "1226543299999999999",
  "responder": { "agent_id": "julian" },
  "decided_at": "2026-04-23T15:47:02Z",
  "action": "kept",
  "reason": "julian reacted with the bookmark emoji in discord; extends his mind-palace notes",
  "garden_path": "notes/kept/alexander-pattern-language.md"
}
```
