# Knowledge Forest POC — module sketch

This file proposes the module structure for the Knowledge Forest
POC — a 2-week MVP testing whether a small structured frame
around shared resources reduces information overload for
atlasresearch (Christina, Corey, Julian).

The READMEs in each module are the design surface. Code follows
once the contracts are settled. Until then, schemas live as
markdown plus example JSON in [`schemas/`](./schemas/), and
modules live as READMEs that describe what each part does and
how it talks to the others.

## Modules + ownership

| Module | Owner | What it does |
|--------|-------|--------------|
| [`schemas/`](./schemas/) | All | The shared shapes — the six-dimension context frame, webhook event payloads, agent handover briefings |
| [`routing/`](./routing/README.md) | Julian | Decides which agent handles which incoming event |
| [`orchestration/`](./orchestration/README.md) | Julian | Spawns and runs the agents (one persistent terminal session per agent) |
| [`agents/`](./agents/README.md) | Christina/Julian | The supervisor + per-user personal agent templates |
| [`parser/`](./parser/README.md) | Christina/Julian | Reads a shared resource and extracts its content, tags, keywords, and named entities |
| [`fingerprint/`](./fingerprint/README.md) | Christina/Julian | Reasons over parsed resources in a channel or user context — rolling snapshots + per-resource match scores |
| [`chat/`](./chat/README.md) | Corey | Discord client + the thread-per-share-event bridge |
| [`event-log/`](./event-log/README.md) | Corey | Append-only history of what happened to each shared resource + webhook |

Ownership is the **action lead** for the module. The split is meant to put each person on the surfaces they're already most engaged with: Christina on the meaning-axis (the agent's reasoning + the per-resource parse + the fingerprint roll-up), Corey on the engineering surfaces (the bot + the storage log), Julian on the integration shapes + how everything is run.

## Decisions to date

From the 2026-04-23 meeting and follow-ups:

- **No event-log branching for the POC.** Linear history per
  resource.
- **Thread-per-share-event in Discord.** The bot opens a thread
  on every message that contains a resource; replies become
  context events on the same log.
- **Manual keep only.** Personal agents may flag matching
  content; the user always pulls the trigger on what enters
  their personal knowledge garden.
- **Per-channel and per-user fingerprints, updated every N share
  events.** Tracking how the snapshot shifts between updates is
  itself signal.
- **`why` is the only human-authored field of the six-dimension
  frame.** All five other fields are automatic or derived.

## Open for the meeting

Each open question lives in the relevant README. Quick index:

- **Frame recursion** — should a `why` value itself be parseable
  as a nested frame, capped at one layer? See
  [`schemas/six-dim-frame.md`](./schemas/six-dim-frame.md).
- **Parser shape** — library extractors vs language-model read
  for the per-resource content + tag pass? See
  [`parser/README.md`](./parser/README.md). Julian's current
  lean: library-only with a language-model fallback when the
  extractor returns a suspiciously short body.
- **Fingerprint shape** — keyword list vs language-model
  interpretation vs hybrid for the per-target roll-up over the
  parser's output? See
  [`fingerprint/README.md`](./fingerprint/README.md). Julian's
  current lean: language-model interpretation, simpler to
  achieve.
- **Harness architecture** — terminal-session-per-agent is the
  current recommendation; alternatives are sketched. See
  [`orchestration/README.md`](./orchestration/README.md).
- **Module shape itself** — is this 8-module split right?
  Should `event-log/` fold into `chat/`? Should `parser/` fold
  back into `fingerprint/`? Should `fingerprint/` fold into
  `agents/`? Worth a 5-minute discussion.

## Module shape

Julian's first sketch named four modules (`routing/`,
`orchestration/`, `agents/`, `chat/`) plus an open *what else?*
This proposal adds four more:

- `schemas/` — kept as its own folder because the integration
  shapes are the load-bearing artifacts; humans and agents both
  read them.
- `event-log/` — surfaced explicitly in the meeting as a needed
  storage layer (the "git-commit-log per resource" shape).
- `parser/` — the per-resource read. Splitting it out from
  `fingerprint/` keeps per-resource extraction (one URL → one
  parsed record) separate from the per-target reasoning that
  uses those records.
- `fingerprint/` — surfaced in the meeting as the source of the
  semantic match in the `where` Layer 2; reasons over the
  parser's output, given a channel or user context.

If this feels over-modularized, the fold-in candidates are: `event-log/` → `chat/`, `parser/` → `fingerprint/` (collapses the split), and `fingerprint/` → `agents/` (if we go the llm-route, this is essentially a scheduled agent).