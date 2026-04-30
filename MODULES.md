# Knowledge Forest POC — module sketch

This file proposes the **module structure** for the kf-poc — a
2-week MVP testing whether a 6-dimension context frame around
shared resources reduces information overload for atlasresearch
(Christina, Corey, Josh).

The READMEs in each module are the design surface. **Code follows
once the contracts are settled.** Schemas already drafted live in
[`schemas/`](./schemas/); module READMEs reference them.

This sketch is the output of the 2026-04-30 alignment pass. It
postdates [`briefing.md`](./briefing.md) (project context) and the
04-17 vintage schemas in [`schemas/`](./schemas/). Where the 04-23
meeting moved decisions or surfaced new requirements, the relevant
module README flags it.

## Modules (proposed)

| Module | Owner | What it does |
|--------|-------|--------------|
| [`schemas/`](./schemas/) | @kf-lead | Contractual integration shapes (4 drafts from 04-17 + the 6-dim placeholder from Christina) |
| [`routing/`](./routing/README.md) | @kf-eng | Decides which agent handles which incoming event |
| [`orchestration/`](./orchestration/README.md) | @kf-eng | How agents run (claude-code-key + tmux, metasphere-style) |
| [`agents/`](./agents/README.md) | @kf-lead | supervisor + personal-agent-N templates |
| [`chat/`](./chat/README.md) | @kf-lead | Discord client + thread-per-share-event bridge |
| [`event-log/`](./event-log/README.md) | @kf-lead | Append-only resource history (git-commit-log shape) |
| [`fingerprint/`](./fingerprint/README.md) | @kf-lead | Per-channel + per-user semantic snapshots |

This is a **proposal**, not a commitment. Two of these modules
(`event-log/`, `fingerprint/`) go beyond Julian's initial sketch
— they were called out explicitly in the 2026-04-23 meeting as
named needs. `schemas/` is preserved (plural) from the existing
04-17 drafts. **Tell us if this is over-modularized.**

## Decided (locked since the 2026-04-30 reply)

- **Q1: No event-log branching** for the POC. Linear history per
  resource.
- **Q2: Thread-per-share-event** in Discord. The bot opens a thread
  on every message containing a resource; replies become context
  events on the same log.
- **Q4: Manual keep only.** Personal agents may flag matching
  content; the user always pulls the trigger on what enters the
  personal knowledge garden.
- **Q6: Per-channel + per-user fingerprints**, updated after N
  share events. Tracking how the snapshot shifts between updates
  is itself signal.

## Open for the meeting

Each open question lives in the relevant module README. Quick
index:

- **Q3 — frame recursion**: zero or one layer? The 04-17
  six-dim-frame-placeholder didn't anticipate this. Need to update
  `schemas/six-dim-frame-placeholder.md` once Christina lands her
  draft.
- **Q5 — `how`/`why` human-required**: gate or hint? See
  [`agents/README.md`](./agents/README.md). The 04-17 briefing
  said `why` is the only manual field; 04-23 + 04-30 reopened it.
- **Fingerprint shape**: keyword list vs LLM interpretation vs
  hybrid? Julian leans LLM-as-simpler. See
  [`fingerprint/README.md`](./fingerprint/README.md).
- **Harness architecture**: tmux+claude-code recommended;
  alternatives sketched. See
  [`orchestration/README.md`](./orchestration/README.md).
- **Module shape itself**: is this 7-module split right? Should
  `event-log/` fold into `chat/`? Should `fingerprint/` fold into
  `agents/`? Discuss.

## What's NOT here

- **Schema refresh for 04-23 + 04-30 decisions.** The existing
  schemas in [`schemas/`](./schemas/) predate the directionality
  insight (sender vs recipient sides), the recursion question, and
  the append-only event-log shape. They need a refresh — but per
  the persona's stance, schema design awaits Christina's frame
  draft + meeting alignment. Holding.
- **Code.** None. README-level only. Code follows once contracts
  settle.
