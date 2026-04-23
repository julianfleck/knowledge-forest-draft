# Handover Briefing Schema — v1 (draft)

**Author:** @kf-lead · **Status:** draft · **Date:** 2026-04-17
**Produced by:** the orchestrator agent (one per shared resource × recipient)
**Consumed by:** each personal research agent (one per human)

## Role

The handover briefing is the **central artifact of the project**.
It is what @orchestrator hands each personal agent to say: *"Corey
shared this. Here is the 6-dim frame for it. I have read this
person's garden, and here is why I think it might matter."*

This schema encodes the contract under which the personal agent is
allowed to *trust without re-reading* the garden. The "I read the
garden" promise is load-bearing — if a personal agent doesn't
trust it, the whole architecture degrades into every agent
re-reading everything, which is what we're trying to avoid.

## Design constraints (from SOUL + briefing)

- **Membranes, not walls.** Briefings expose *pointers* into the
  recipient's garden, not the garden itself. Excerpts that are
  actually load-bearing for synthesis ARE embedded — because they
  are already exposed by virtue of being in the synthesis.
- **The "why" field is load-bearing.** `context_frame.why` is the
  one dimension Christina hypothesizes reduces overload through
  manual effort. If `why` is null, the briefing MUST flag that the
  relevance synthesis is running without the human-filled why.
- **Honor the garden-read promise explicitly.** The schema has a
  `garden_provenance` object that names the repo, the commit,
  the paths read, and the excerpts used. A personal agent that
  cannot verify these fields is allowed to reject the briefing
  and escalate.

## Transport

- Briefings are delivered to personal agents via the same channel
  the metasphere-agents research-agent pattern uses: append to the
  personal agent's inbox (filesystem or harness-native message
  queue — choice is @kf-eng's, but the schema is transport-agnostic).
- One briefing per (shared resource × recipient). N recipients ⇒ N
  briefings, each with its own provenance.

## Required fields

| Field | Type | Notes |
|---|---|---|
| `schema_version` | string | `"1"` for v1. |
| `briefing_id` | string | Orchestrator-assigned ULID. |
| `created_at` | string (ISO-8601 UTC) | |
| `recipient` | object | `{agent, known_identity}` — addressing. |
| `triggering_event` | object | `{event_id, correlation_id}` from webhook. |
| `resource` | object | Carried forward from webhook `what` + context. |
| `context_frame` | object | 6-dim frame for this resource (see 6-dim placeholder doc). |
| `relevance_synthesis` | object | Orchestrator's why-this-matters note. |
| `garden_provenance` | object | The load-bearing promise. |

### Optional fields

| Field | Type | Notes |
|---|---|---|
| `group_signal` | object | Social weight: others who marked relevant. |
| `expected_action` | enum | Soft guidance, not command. |
| `deadline_hint` | string (ISO-8601) | When surfacing becomes stale. |

### Sub-object shapes

`recipient`:
```
{
  "agent": "@personal-julian",
  "known_identity": "julian"
}
```

`resource` (pulled from the webhook event):
```
{
  "url": "https://...",
  "preview": { ... },                    // from webhook, may be {fetch_error: ...}
  "shared_by": "corey",
  "shared_in": "#knowledge-forest",
  "shared_at": "2026-04-17T15:30:00Z",
  "context_message": "<verbatim Discord text>"
}
```

`context_frame` (6-dim; finalized once Christina's draft lands):
```
{
  "schema_ref": "six-dim-frame@v1",
  "who": "corey",
  "when": "2026-04-17T15:30:00Z",
  "why": null,                           // MANUAL; null until someone fills it
  "what": "https://...",
  "where": "#knowledge-forest",
  "how": "discord-share"
}
```

`relevance_synthesis`:
```
{
  "summary": "<one-paragraph why-this-matters-to-recipient>",
  "grounded": true,                      // false if garden_provenance.read_paths == []
  "confidence": "medium",                // low | medium | high
  "reasoning": "<one paragraph of orchestrator reasoning>",
  "why_field_present": false             // mirrors context_frame.why != null
}
```

`garden_provenance` — **the load-bearing promise**:
```
{
  "garden_repo": "github.com/julian/private-garden",
  "commit_sha": "abc123deadbeef",
  "read_paths": [
    "notes/mind-palace.md",
    "notes/memory-architecture.md"
  ],
  "excerpts": [
    {
      "path": "notes/mind-palace.md",
      "anchor": "# Loci method",
      "text": "<verbatim snippet used in synthesis>",
      "chars": 187
    }
  ],
  "read_at": "2026-04-17T15:30:45Z",
  "promise": "Orchestrator asserts read_paths were read at commit_sha; relevance_synthesis is grounded in these reads. Receiver MAY trust without re-reading."
}
```

Semantics of the promise:
- `read_paths` is the *complete* list of paths that informed the
  synthesis. Not a sample. Not a truncated list.
- `excerpts` is the subset of those reads that directly justify
  `relevance_synthesis.summary`. An empty `excerpts` means the
  synthesis is based on reads but quotes none of them.
- `commit_sha` is the garden state at read time. If the garden
  advanced between `read_at` and `created_at`, the briefing remains
  valid against the snapshot at `commit_sha`.
- If `read_paths == []`: the personal agent MUST treat the briefing
  as ungrounded (can still surface on strong heuristic match with
  external signals, but with appropriate caveat).

`group_signal` (optional):
```
{
  "marked_relevant_count": 3,
  "marked_relevant_by": ["julian", "christina", "alex"]
}
```

`expected_action`:
- enum: `"surface"` | `"surface_or_ignore"` | `"store_silently"` | `"respond_only"`
- Default: `"surface_or_ignore"`. This is guidance; the personal
  agent owns the final call.

## Example payload

```json
{
  "schema_version": "1",
  "briefing_id": "bf_01HZXYZ789",
  "created_at": "2026-04-17T15:31:00Z",
  "recipient": {
    "agent": "@personal-julian",
    "known_identity": "julian"
  },
  "triggering_event": {
    "event_id": "evt_01HZABC123",
    "correlation_id": "1226543210987654321"
  },
  "resource": {
    "url": "https://example.com/alexander-pattern-language.pdf",
    "preview": {
      "title": "A Pattern Language",
      "description": "Christopher Alexander et al., 1977.",
      "image_url": null,
      "fetched_at": "2026-04-17T15:30:02Z"
    },
    "shared_by": "corey",
    "shared_in": "#knowledge-forest",
    "shared_at": "2026-04-17T15:30:00Z",
    "context_message": "this reminded me of Julian's mind-palace thread"
  },
  "context_frame": {
    "schema_ref": "six-dim-frame@v1",
    "who": "corey",
    "when": "2026-04-17T15:30:00Z",
    "why": null,
    "what": "https://example.com/alexander-pattern-language.pdf",
    "where": "#knowledge-forest",
    "how": "discord-share"
  },
  "relevance_synthesis": {
    "summary": "Corey shared Alexander's pattern-language paper. It resonates with your mind-palace notes from March 2026 and your memory-architecture reading list.",
    "grounded": true,
    "confidence": "medium",
    "reasoning": "Two of your notes cite pattern-language as prior art; one explicitly flags Alexander. The share arrived in response to your mind-palace thread.",
    "why_field_present": false
  },
  "garden_provenance": {
    "garden_repo": "github.com/julian/private-garden",
    "commit_sha": "abc123deadbeef",
    "read_paths": [
      "notes/mind-palace.md",
      "notes/memory-architecture.md"
    ],
    "excerpts": [
      {
        "path": "notes/mind-palace.md",
        "anchor": "# Loci method",
        "text": "Alexander's pattern-language is the closest thing we have to a 'grammar of loci' for institutional knowledge.",
        "chars": 96
      }
    ],
    "read_at": "2026-04-17T15:30:45Z",
    "promise": "Orchestrator asserts read_paths were read at commit_sha; relevance_synthesis is grounded in these reads. Receiver MAY trust without re-reading."
  },
  "group_signal": {
    "marked_relevant_count": 1,
    "marked_relevant_by": ["corey"]
  },
  "expected_action": "surface_or_ignore",
  "deadline_hint": "2026-04-17T16:30:00Z"
}
```

## Failure modes

| Condition | Orchestrator behavior |
|---|---|
| Recipient has no garden repo configured | Emit briefing with `garden_provenance.read_paths = []`, `relevance_synthesis.grounded = false`. Personal agent decides. |
| Orchestrator couldn't read the garden (repo 404, auth expired) | Do NOT emit briefing. Append to orchestrator retry queue. Log. Escalate if fails 3× consecutively. |
| `context_frame.why` is null at emit time | Emit anyway, but `relevance_synthesis.why_field_present = false`. Personal agent MAY down-weight confidence. |
| Synthesis produced zero signal (no relevant notes) | Emit briefing with short `relevance_synthesis.summary` explicitly saying so. Not a silent drop — the hypothesis test needs to see negatives. |
| Schema version mismatch at receiver | Personal agent rejects; orchestrator version-locks with every personal agent it serves. |

## Open questions

1. Should `garden_provenance.excerpts` be size-capped? Long excerpts leak garden content. Proposed cap: 500 chars per excerpt, max 5 excerpts per briefing.
2. Does `garden_provenance` need a signature? MVP says no — we trust orchestrator as the only author. Add if we ever introduce peer orchestrators.
3. Cross-agent `context_frame.why` — if Julian fills a `why` after receipt, does that amend the briefing or spawn a new one? (Deferred to the response-schema doc.)
4. Does the personal agent get the raw webhook event too, or only the briefing? Proposed: briefing only, with `triggering_event` as a pointer. Reduces surface area.

## Non-goals for v1

- No pub-sub. Direct addressed delivery per briefing.
- No priority levels beyond `deadline_hint`.
- No multi-recipient briefings (one briefing per recipient, even if the same synthesis would fan out identically).
- No embedding of the full garden diff. Paths + excerpts only.
