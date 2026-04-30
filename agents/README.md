# agents

## What this module does

Holds the actual agents. In knowledge-forest there are two kinds:

- **supervisor** — one per group/channel. Watches share events
  arriving from `chat/`, runs the where-match against the channel
  fingerprint, decides which users' personal agents (if any) the
  resource should be flagged to.
- **personal-agent-N** — one per human user. Receives flagged
  resources from the supervisor, runs the how/why match against
  the user's own fingerprint, and either:
  - stays silent (the resource is just ambient context)
  - flags it to the user in their DM ("you might want this")
  - waits for the user to keep it (manual-only)

Both are stateful in the sense that they carry handover context
(their snapshot, their recent decisions). `orchestration/` owns
how they actually run.

## What lives here

- `supervisor/` — template + system prompt + handover format
- `personal-agent/` — template instantiated per user
- `templates/` — shared briefing scaffolding (state-snapshot slot,
  context-frame slot, prior-events slot)

## Who talks to it

- `routing/` decides which agent gets a given event
- `chat/` is where outputs land (DMs, thread replies)
- `event-log/` is what they emit when they keep something
- `fingerprint/` provides the snapshots they need to reason

## Decided

- **Manual keep only (Q4).** Personal agents do NOT auto-write to
  the personal knowledge garden. The user pulls the trigger.
- BUT: personal agents SHOULD flag worthwhile content matching the
  user profile, even if they can't keep it themselves. Suggesting
  is fine, persisting is not.

## Open question

- **Q5: How/Why human-required?** When someone shares a resource,
  does a human MUST write a sentence (sender-side `why`), or can
  the agent infer it from the resource + channel context?
  Trade-off: friction vs meaning fidelity. Christina insists
  human; Julian leans agent-fills-gaps. Still discussing.
