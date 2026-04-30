# fingerprint

## What this module does

Reasons over parsed resources in a context — either a channel or
a single user — to answer two related questions:

- **Match.** Given an incoming parsed resource and this channel
  / user, how well does it overlap with what the channel as a
  whole / this person cares about right now?
- **Snapshot.** Given the parsed resources that have moved
  through this channel / this user's garden recently, what does
  the channel / this person care about?

The match score is what populates **Layer 2 of `where`** in the
six-dimension frame. The snapshot is the rolling state that match
is computed against; the supervisor and personal agents read it
in their briefings.

This module does not extract content from a resource — that's
[`parser/`](../parser/)'s job. Fingerprint takes parsed-resource
records as input and produces per-target reasoning on top of them.

## How it works (sketch)

Two snapshot types, both per-target:

- **per-channel fingerprint** — a roll-up of the tags, keywords,
  and named entities the parser surfaced across the channel's
  recent share events. Tells the supervisor what the channel as a
  whole is talking about right now.
- **per-user fingerprint** — the same kind of roll-up, but for
  one user's personal knowledge garden plus the resources they've
  kept. Tells a personal agent what its human is currently
  engaged with.

Both update **after every N share events**, not on every event.
Tracked over time, the fingerprints show how the narrative shifts
between updates — that delta is itself signal: the channel is
moving from "clean energy policy" toward "field engineering",
say, or the person's interest is widening from "funding" into
"installation".

The match step is separate from snapshot maintenance: when a new
parsed resource arrives, fingerprint compares it against the
relevant per-target snapshot (channel context for the supervisor,
user context for a personal agent) and produces the Layer 2
score. Snapshots themselves are passed to agents in their
briefings, not pulled live at decision time. That makes the
agent's reasoning cheaper and reproducible.

## How a fingerprint is computed (open question — decide in the meeting)

Two candidate shapes:

1. **A keyword / topic list with weights.** Aggregate the
   parser's tags / keywords / entities across the relevant
   resources, weighted by frequency (TF-IDF or similar). Output
   is a flat ranked list. Easy to read, easy to compare, but flat
   — "clean energy policy" and "windmill construction" can both
   bucket as `clean_energy` and lose the activity nuance the
   meeting flagged as the heart of the `how` field.

2. **A short language-model interpretation.** A paragraph the
   model writes describing what the channel or user cares about,
   regenerated every N events from the parsed-resource records.
   Captures nuance, harder to compare programmatically, more
   expensive to compute (but only periodically).

Julian's current lean is option 2 — simpler to achieve, even if
more costly. A hybrid is possible: a language-model paragraph
for human reading, a derived keyword set for matching arithmetic.

## Who talks to it

- [`parser/`](../parser/) provides the parsed-resource records
  that fingerprint reasons over
- [`event-log/`](../event-log/) is the source of truth for which
  parsed resources belong to which channel / user
- [`agents/`](../agents/) consume fingerprints in their briefings
  and the per-resource match score in Layer 2 of `where`
- The fingerprint update is triggered after every N share events
  have landed
