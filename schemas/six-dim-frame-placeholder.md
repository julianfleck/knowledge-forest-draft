# Six-Dimension Context Frame — PLACEHOLDER

**Author:** @kf-lead · **Status:** placeholder (awaiting Christina)
**Date:** 2026-04-17

## Why this doc exists

Christina is drafting the six-dimension frame. Per SOUL + MISSION:
I do NOT design it from scratch. I review + negotiate her draft.
This placeholder captures:

1. The role the frame plays in the rest of the system (so we can
   tell if the draft fits).
2. The open questions I'd ask Christina on receipt.
3. The escalation path if the draft doesn't land in ~3 days.

## The frame's role downstream

The six-dim frame is referenced by two schemas I've drafted today:

- `context_frame` sub-object in the **handover briefing** carries
  an instance of the frame for each shared resource.
- `amended_why` in the **personal-agent response** is a mutation
  to one field of the frame.

Whatever shape Christina proposes, those two schemas will version-
lock to it via `schema_ref: "six-dim-frame@vN"`. The frame is
**the** downstream contract — its evolution strategy determines
how often the briefing schema bumps.

## What I expect to see in her draft (my read, negotiable)

- Six top-level fields: `who`, `when`, `why`, `what`, `where`, `how`.
- Each field's value is either a string, a structured sub-object,
  or null.
- `why` is the ONLY field that must be manually authored in MVP
  (briefing §3). The other five are auto-extractable from the
  webhook event or inferrable.
- The frame is serializable as YAML (for human edit in markdown
  front-matter) AND as JSON (for wire transport).

## Open questions I'll bring to Christina

### Structural
1. **Atomicity.** Is a frame tied to (resource × occurrence) — i.e. each re-share gets a new frame — or to the resource itself, accreting `who/why` tuples over time?
2. **Identifier.** Does each frame have a stable ID, or is its identity derived from `(what.url, when)`?
3. **Serialization.** YAML front-matter primary, JSON derived? Or vice versa? Does it matter for the human-editing workflow?
4. **Nesting.** Is `who` a single author, or can it carry multiple (e.g. "Corey shared, attributed to Alexander")? If multiple: how does that interact with `why` authorship?

### `why` field specifically (the load-bearing one)
5. **Free-text vs. tagged.** Is `why` open prose, or a controlled vocabulary? Open prose is harder to aggregate; tags lose nuance.
6. **Author attribution within `why`.** Multiple humans can add `why` to the same frame. Do we store `{author, why_text, added_at}[]` or coalesce into a single field?
7. **Empty state.** What's the canonical "no why yet" value — missing field, empty string, `null`, explicit `{pending: true}`? This affects how `relevance_synthesis.why_field_present` is computed.
8. **Mutability.** Once a `why` is written, is it editable? Append-only? History-preserving? The group event log gives us audit for free if we pick append-only.

### Inferred fields
9. **`how`.** Is `how` "how this resource was encountered" (discord-share, feed-subscription, crawl) or "how this relates to the garden" (keyword-match, topic-cluster, explicit-link)? Different semantics, different downstream uses.
10. **`where`.** Channel-level granularity only, or message-thread granularity? Group-level only, or extensible to "where in garden" too?
11. **`when`.** Event time (share moment) vs. first-encountered time vs. resource publication time — how many of these do we need?

### Governance
12. **Validation.** Hard-schema validation (reject non-conforming frames), or soft (coerce, warn)? My lean: hard at group-garden entry, soft at personal-garden.
13. **Evolution.** Are fields addable without breaking old frames? Is there a `schema_version` baked into each frame instance, or only at the spec level?
14. **Privacy.** The `who` field is low-stakes. The `why` field could contain sensitive personal reasoning. Does the frame itself need access control, or does GitHub repo privacy suffice?

### Meta
15. **Where does this spec live?** My current plan: canonical spec in the atlasresearch repo (clean spec, committed by Julian), thinking/iteration in `~/.metasphere/agents/@kf-lead/artifacts/`. Confirm with Christina that the repo is the right landing zone for her draft.

## Escalation plan

- If Christina's draft does not land by **2026-04-20** (72h), ping @orchestrator with a reminder. Do not draft a substitute.
- If the draft lands but leaves critical questions (1, 5, 7, 12) unanswered, annotate the draft with specific questions + propose a first-pass answer on each. Send back through @orchestrator.
- If the draft lands and answers everything cleanly, lock the shape as `six-dim-frame@v1`, update the briefing + response schemas' `schema_ref`, and dispatch the Phase 2 eng contract.

## Non-goals for me on this file

- NOT proposing a frame shape here. That's Christina's.
- NOT pre-empting the review by drafting an "alternative." The
  review conversation happens on her draft; this doc is the
  question list I bring to it.
