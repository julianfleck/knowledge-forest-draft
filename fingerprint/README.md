# fingerprint

## What this module does

Computes "what does this channel care about?" and "what does this
person care about?" — semantic snapshots that the supervisor and
personal agents need before they can do any meaningful matching
between an incoming resource and a group or person.

These snapshots are exactly what the **Layer 2 of `where`** in
the six-dimension frame is matched against. Without them, the
"semantic match" field has nothing to compare to; the supervisor
and personal agents can't decide whether to surface a resource.

## How it works (sketch)

Two snapshot types, both per-target:

- **per-channel snapshot** — a roll-up of the tags, keywords, and
  named entities surfaced by the channel's recent share events.
  Tells the supervisor what the channel as a whole is talking
  about right now.
- **per-user snapshot** — the same kind of roll-up, but for one
  user's personal knowledge garden plus the resources they've
  kept. Tells a personal agent what its human is currently
  engaged with.

Both update **after every N share events**, not on every event.
Tracked over time, the snapshots show how the narrative shifts
between updates — that delta is itself signal: the channel is
moving from "clean energy policy" toward "field engineering",
say, or the person's interest is widening from "funding" into
"installation".

Snapshots are passed to agents in their briefing, not pulled
live at decision time. That makes the agent's reasoning cheaper
and reproducible.

## How a snapshot is computed (open question — decide in the meeting)

Two candidate shapes:

1. **A keyword / topic list with weights.** Compute term
   frequency / inverse document frequency (TF-IDF) over the
   share events, or have a language model tag each resource
   with topics and aggregate. Output is a flat ranked list.
   Easy to read, easy to compare, but flat — "clean energy
   policy" and "windmill construction" can both bucket as
   `clean_energy` and lose the activity nuance the meeting
   flagged as the heart of the `how` field.

2. **A short language-model interpretation.** A paragraph the
   model writes describing what the channel or user cares about,
   regenerated every N events. Captures nuance, harder to compare
   programmatically, more expensive to compute (but only
   periodically).

Julian's current lean is option 2 — simpler to achieve, even if
more costly. A hybrid is possible: a language-model paragraph
for human reading, a derived keyword set for matching arithmetic.

## Who talks to it

- [`event-log/`](../event-log/) is the source of truth that gets
  read
- [`agents/`](../agents/) consume snapshots in their briefings
- The snapshot update is triggered after every N share events
  have landed
