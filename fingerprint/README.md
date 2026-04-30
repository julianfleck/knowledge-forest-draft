# fingerprint

## What this module does

Computes "what does this channel care about?" and "what does this
person care about?" — semantic snapshots that the supervisor and
personal agents need before they can do any meaningful matching
between an incoming resource and a group or person.

Without these snapshots, "fingerprint matching" is a hollow phrase.
Without "where does this fit?", agents can't route. Without "what
does this person already engage with?", agents can't decide
whether to flag or stay quiet.

## How it works (sketch)

Two snapshot types, both per-target:

- **per-channel snapshot** — top topics/themes from the channel's
  recent share events
- **per-user snapshot** — top topics/themes from the user's
  personal knowledge garden + their kept events

Both update **after N share events**, not on every event (Q6
decided). Tracked over time, the snapshots show how the narrative
moves — that delta itself is signal for what the channel/person
is shifting toward.

Snapshots are passed in the handover briefing (see `schema/`),
not pulled live by the agent at decision time. Cheaper, more
reproducible.

## Who talks to it

- `event-log/` is the source of truth that gets read
- `agents/` consume snapshots in their handover briefings
- The fingerprint update is triggered by `routing/` after every
  Nth share event lands

## Open question — most important to resolve in the meeting

**What IS a fingerprint, concretely?** Two options:

1. **Keyword/topic list** — TF-IDF or LLM-tagged keywords with
   weights. Easy to read, easy to compare, but flat. "Clean
   energy policy" and "windmill construction" may both tag as
   `clean_energy` and lose the activity nuance the meeting flagged
   as the heart of the `how` field.

2. **LLM-generated interpretation** — a short paragraph the LLM
   writes describing what the channel/user cares about. Captures
   nuance, harder to compare programmatically, more expensive to
   compute but only every N events.

Julian's lean: option 2 is simpler to achieve. Worth weighing
"more expensive" against the simpler comparison story.

A hybrid is possible: LLM-paragraph for human reading, derived
keyword set for matching arithmetic.
