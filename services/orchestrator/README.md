# orchestrator

The reasoning core. Consumes one `resource.shared` event and
produces one briefing per subscribed personal agent, skipping
participants who already kept this URL.

Implemented as a Claude-Code-style agent session with read access
to each participant's knowledge garden, the group event log, and
a fixed set of tools.

## Responsibilities

- Parse the inbound event.
- Extract mentions from the Discord message text (`<@id>` and
  free-text `@handle`) and resolve them to `agent_id`s via a
  static identity config.
- Check the group event log: if a subscriber has already kept
  this URL, skip them — don't emit a briefing.
- For each remaining subscribed `agent_id`:
  - Read that participant's knowledge garden at `HEAD`.
  - Write a one-paragraph relevance note grounded in the paths
    read.
  - Emit a briefing per
    [`schemas/handover-briefing.md`](../../schemas/handover-briefing.md)
    with `priority = "mention"` if the `agent_id` was mentioned,
    otherwise `"normal"`.
- Fill the six-dimension frame. `why` stays `null` unless the
  share's message already contained one.

## Non-responsibilities

- No handling of `resource.kept` events — those are routed by the
  webhook server straight to the keeper's personal agent.
- No delivery.
- No subscription state.
- No writes to any garden.
- No surface/keep/ignore decisions.

## Garden-read promise

Every briefing includes `garden_read` with the repo, commit SHA,
and the complete list of paths read. `relevance_note` must be
grounded in those paths. If a garden cannot be read (auth, 404,
timeout), the orchestrator emits no briefing for that subscriber
and logs the skip.

## Prompts

See [`prompts/`](./prompts).

## POC boundaries

- One orchestrator instance.
- Synchronous garden reads per event.
- Identity map is a static YAML file in the repo.
- Already-kept check is a naive scan of the group log keyed on
  `(agent_id, url)`.
