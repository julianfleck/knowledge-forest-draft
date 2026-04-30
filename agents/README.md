# agents

## What this module does

Holds the agents that read incoming share events and decide what
to do with them. There are two kinds:

- **supervisor** — one per group / channel. Watches share events,
  measures how well each resource matches the group's interests,
  and decides which users (if any) should be told about it.
- **personal-agent** — one per human user. Receives flagged
  resources from the supervisor, measures how well each resource
  matches its human's interests, and either:
  - stays silent (the resource is just ambient context),
  - flags it to the user in their direct messages
    ("you might want this"),
  - or waits for the user to keep it.

Both kinds are stateful — they carry the snapshot they were
briefed with and a record of their recent decisions. How agents
are actually spawned and run is the
[`orchestration/`](../orchestration/) module's job.

## What lives here

- `supervisor/` — the supervisor's prompt template, briefing
  format, system instructions
- `personal-agent/` — the personal agent's template, instantiated
  once per human user
- `templates/` — shared briefing scaffolding (slots for the state
  snapshot, the context frame, prior events on this resource)

## Who talks to it

- [`routing/`](../routing/) decides which agent gets a given event
- [`chat/`](../chat/) is where outputs land (DMs, thread replies)
- [`event-log/`](../event-log/) is what they emit when they keep
  something
- [`parser/`](../parser/) provides the per-resource parsed
  record (text, tags, keywords, named entities) for each
  incoming share event
- [`fingerprint/`](../fingerprint/) provides the per-channel /
  per-user snapshot they reason against, plus the Layer 2
  `where` match score for each parsed resource

## Decisions

- **Manual keep only.** Personal agents never auto-write to the
  human's personal knowledge garden. The user pulls the trigger.
- **Agents may flag.** Personal agents should point out matching
  content to their human, even though they can't keep it
  themselves. Suggesting is fine; persisting without permission
  is not.
- **`why` is the only human-authored field.** Per the
  six-dimension frame spec, `why` is the field a human writes.
  The other five fields (including `how`) are automatic or
  derived from the resource and the receiver's context.

## Open question

The 04-23 meeting raised whether `how` and `why` both need human
input for meaning to be present. The current spec settles it:
`why` is human, `how` is derived. The remaining empirical
question — *can derivation alone capture meaning, or are we
losing something a human sentence carries?* — is worth checking
during the POC against real shared resources. Worth re-discussing
if the derived `how` regularly looks off.
