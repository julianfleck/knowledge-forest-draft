# Personal-Agent Response Schema — v1 (draft, YES-with-spec)

**Author:** @kf-lead · **Status:** draft · **Date:** 2026-04-17
**Produced by:** each personal research agent
**Consumed by:** the orchestrator agent (for group_signal + measurement)

## Decision: YES, MVP needs this schema

The task brief asked me to decide. My call is **yes**, but with the
minimum viable shape — four enum actions and a telemetry stub.

### Why YES

1. **`group_signal.marked_relevant_count` in the handover briefing
   has no source otherwise.** If we don't collect responses, the
   field is dead weight. Removing it removes the "three people
   marked this relevant" affordance Julian called out in the
   briefing (§2, event flow step 4).
2. **The experiment's hypothesis requires instrumentation.**
   Christina wants to measure whether manual "why" reduces
   overload (briefing §6.5). Measurement without response data is
   impossible. Defer the *metric* to post-MVP; don't defer the
   *hooks* that let us compute it later.
3. **Handover fidelity demands a closed loop.** If @orchestrator
   sends N briefings and never learns which were surfaced, it
   can't improve synthesis, can't dedup near-identical reshares,
   can't avoid noisy repeats. The architecture degrades.

### What keeps MVP costs down

- Four actions, no sub-states: `ack | surfaced | marked_relevant | ignored`.
- No mandatory human-engagement tracking (it's a nullable field).
- No complex timing SLAs; the 15-minute scheduled tick of personal
  agents is the de-facto cadence.
- No acknowledgement-of-acknowledgement. Orchestrator doesn't
  confirm receipt; responses are append-only to the group event log.

## Transport

- Append to the group event log (CAM-aligned shared GitHub repo).
  One JSON object per response, one line, timestamp-ordered.
- Also deliverable directly to @orchestrator for immediate
  group_signal aggregation. @kf-eng decides whether the group log
  IS the delivery mechanism or a parallel write; schema is
  transport-agnostic.

## Required fields

| Field | Type | Notes |
|---|---|---|
| `schema_version` | string | `"1"` |
| `response_id` | string | ULID, personal-agent-assigned |
| `briefing_id` | string | The briefing this responds to |
| `responder` | object | `{agent, known_identity}` |
| `decided_at` | string (ISO-8601 UTC) | When the personal agent made the call |
| `action` | enum | `ack` \| `surfaced` \| `marked_relevant` \| `ignored` |
| `reason` | string | One-sentence rationale. Required — forces the manual-effort discipline on the agent side too. |

### Optional fields

| Field | Type | Notes |
|---|---|---|
| `human_engagement` | enum-or-null | `null` \| `opened` \| `dismissed` \| `saved`. Filled asynchronously once human reacts. |
| `telemetry` | object | See below. |
| `amended_why` | string | If the recipient *adds* a `why` to the frame, it lands here. Orchestrator MAY use it to enrich future briefings. |

### Action semantics

| Action | When |
|---|---|
| `ack` | Briefing received, parsed, not acted on (yet or at all). Minimum-viable response so orchestrator can confirm delivery. |
| `surfaced` | Personal agent surfaced this to the human (through whatever personal-agent UX channel). |
| `marked_relevant` | Stronger than `surfaced` — the agent (or the human, via the agent) explicitly flagged this as mattering. Feeds `group_signal`. |
| `ignored` | Agent decided not to surface. `reason` MUST be non-empty — this is where the hypothesis-test signal lives. |

Multiple responses to the same `briefing_id` ARE permitted (e.g.
`ack` at t0, `surfaced` at t1, `marked_relevant` at t2). Each is a
separate log entry; orchestrator aggregates by (briefing_id,
responder).

### Telemetry sub-object

```
{
  "synthesis_confidence_agreed": true,
  "grounded_reads_verified": null,
  "latency_ms": 12430
}
```

- `synthesis_confidence_agreed`: did the personal agent's internal
  sense of relevance agree with `relevance_synthesis.confidence`?
  Used to calibrate orchestrator synthesis over time.
- `grounded_reads_verified`: optional integrity check — personal
  agent MAY verify the commit_sha + read_paths still match the
  garden. `null` = didn't check. `true` = checked, matched.
  `false` = checked, mismatch (escalate).
- `latency_ms`: time from `briefing.created_at` to `decided_at`.

## Example payload

```json
{
  "schema_version": "1",
  "response_id": "resp_01HZXYZ790",
  "briefing_id": "bf_01HZXYZ789",
  "responder": {
    "agent": "@personal-julian",
    "known_identity": "julian"
  },
  "decided_at": "2026-04-17T15:31:12Z",
  "action": "surfaced",
  "reason": "matched the mind-palace topic cluster with medium-high confidence and arrived in response to Julian's own thread",
  "human_engagement": null,
  "telemetry": {
    "synthesis_confidence_agreed": true,
    "grounded_reads_verified": null,
    "latency_ms": 12430
  }
}
```

## Failure modes

| Condition | Personal-agent behavior |
|---|---|
| Briefing fails schema validation | Respond `ack` with `action=ack`, `reason="schema_rejected: <field>"`. Do not process. |
| Synthesis wildly contradicts agent's local read | Respond `ignored` with reason. Optionally set `telemetry.synthesis_confidence_agreed=false` to flag calibration drift. |
| Human adds a `why` after receipt | Send a follow-up response with `action=marked_relevant` (or `surfaced`) and `amended_why` filled. |

## Timing expectation (soft)

- `ack` within 1 minute of receipt (or next scheduled tick,
  whichever is first).
- Final action within 15 minutes (one scheduled tick). If unable,
  log a `ack` with `reason="deferred"` so the briefing isn't
  orphaned.

## Open questions

1. Is `reason` truly required? There's tension with "low-friction" — but the whole hypothesis is that manual effort reduces overload. Requiring a sentence from the agent mirrors that discipline on the machine side. Flagging for Christina + Julian review.
2. Does `marked_relevant` spawn a follow-up broadcast to other personal agents ("Julian marked this relevant")? Proposed: no in v1 — orchestrator only uses it for `group_signal` in *future* briefings.
3. Human-engagement signals (opened / dismissed / saved) require a personal-agent UX hook. Where does that hook live? Almost certainly out of scope for v1 — leave the field, don't build the plumbing.

## Non-goals for v1

- No SLA enforcement.
- No back-pressure / rate-limiting of responses.
- No cross-agent response dependencies ("wait for Christina's agent before responding").
- No richer action taxonomy. Four actions, period. Iterate based on observed gaps.
