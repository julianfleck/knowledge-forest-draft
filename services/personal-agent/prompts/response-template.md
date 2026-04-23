# Response Template — personal agent

Emit one JSON object matching
[`schemas/agent-response.md`](../../../schemas/agent-response.md).

```json
{
  "briefing_id": "<briefing id, or null>",
  "event_correlation_id": "<resource.kept event id, or null>",
  "responder": { "agent_id": "<AGENT_ID>" },
  "decided_at": "<ISO-8601 UTC>",
  "action": "surfaced | kept | ignored",
  "reason": "<one sentence, specific>",
  "garden_path": "<your chosen path in the private garden>"
}
```

- `reason` is required for every action.
- `garden_path` is required only when `action = "kept"`. Omit
  otherwise.
- Exactly one of `briefing_id` or `event_correlation_id` is set.
  `surfaced` and `ignored` always trace a briefing. `kept` traces
  a briefing (agent-originated after a prior surface) or the
  `resource.kept` event (Discord-originated).

## Reason examples

Good:

- `"mentioned me and matched the mind-palace cluster"`
- `"julian reacted with the bookmark in discord; extends his mind-palace notes"`
- `"julian asked me to keep this; it extends his mind-palace notes"`
- `"no mention, garden read found no relevant notes"`
- `"near-duplicate of a briefing julian already kept yesterday"`

Bad:

- `""`
- `"looks relevant"`
- `"not relevant"`
