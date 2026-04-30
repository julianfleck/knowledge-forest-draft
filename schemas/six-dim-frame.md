# Six-Dimension Context Frame (6×2)

A small, structured frame attached to every shared resource. Six
fields × two layers each — twelve slots total — arranged so that
the second layer of every field carries the directional reading:
how this resource looks from where you're standing.

## Shape

| Field | Type | Source | Layer 1 | Layer 2 |
|-------|------|--------|---------|---------|
| **who** | string | automatic | The sharer (agent ID or Discord username) | The receiver(s) |
| **when** | ISO-8601 UTC timestamp | automatic | The share timestamp | The phase the resource is in (draft, published, etc.) |
| **why** | string \| null | **manual** | The sharer's written rationale. `null` until filled. | Context — the derived sense of why this matters in this group |
| **what** | string | automatic | The resource URL | Context — tags / keywords / topics extracted from the resource by [`../parser/`](../parser/) |
| **where** | string | automatic | The channel the resource was shared in | Semantic match against the channel fingerprint or the user fingerprint, computed by [`../fingerprint/`](../fingerprint/) (see below) |
| **how** | string | automatic | Relevance with respect to personal context or group context | Subjective content — the reading lens, the activities/verbs the resource implies |

`why` is the only field a human writes. The other five are
extracted from the share event itself or derived from the
resource and the receiver's context.

## The two layers

The two layers correspond to a directionality split:

- **Layer 1** answers *what does this resource look like, on its
  own?* It's the same for everyone — sharer, receiver, observer.
- **Layer 2** answers *what does this resource mean from where
  I'm standing?* It's directional. The Layer 2 of `who` is the
  receiver list. The Layer 2 of `where` is how this resource maps
  to the receiver's mental space.

A frame is always emitted from a perspective. A sharing event
emits the frame from the sharer's perspective; a keep event (when
a recipient saves the resource into their personal knowledge
garden) emits the same frame shape from the recipient's
perspective.

## The `where` field — extra detail

`where` carries two distinct things:

- **Layer 1 — the channel.** Plain: which Discord channel was the
  resource shared in.
- **Layer 2 — the semantic match.** A score (or short text) for
  how well the resource overlaps with the **channel fingerprint**
  (when the supervisor is reading on behalf of the channel) or
  the **user fingerprint** (when a personal agent is reading on
  behalf of its human).

The Layer 2 score is a comparison: the tags, keywords, and named
entities the channel or person mentions most often (the per-target
fingerprint), against the tags, keywords, and named entities
[`../parser/`](../parser/) extracted from this specific resource.
High overlap → high score. Low overlap → low score.

The split between the two modules: [`../parser/`](../parser/)
owns the per-resource extraction (one URL → one parsed record);
[`../fingerprint/`](../fingerprint/) owns both the per-target
roll-up of those records over time and the match step that
compares an incoming parsed record against the relevant
fingerprint.

## Open questions

- **Frame recursion.** A `why` value is a piece of natural
  language — it could itself be parsed as a frame (who is being
  addressed in the why-message? what's the rationale-of-the-
  rationale?). Open: do we allow one layer of recursion, or keep
  the frame flat for the POC? Discussed in the 2026-04-23
  meeting; not yet decided.
- **`why` empty state.** What's the canonical "no why yet"
  representation: missing field, empty string, `null`, or an
  explicit `{pending: true}`? Default leaning: `null`.
- **`why` mutability.** Once written, is `why` editable, or
  append-only with history? The append-only event log gives us
  history for free if we pick append-only — see
  [`../event-log/README.md`](../event-log/README.md).
- **`how` Layer 1 vs Layer 2.** "Relevance with respect to
  personal/group context" (Layer 1) and "subjective content"
  (Layer 2) overlap conceptually. We need 1–2 worked examples to
  see whether they're really two distinct slots or one slot with
  two framings.
