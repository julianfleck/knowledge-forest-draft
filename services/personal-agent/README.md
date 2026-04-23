# personal-agent

One instance per participant. Subscribes to its own stream on
the webhook server, receives briefings and keep events, surfaces
briefings worth surfacing, and persists kept resources to the
participant's private garden.

Implemented as a Claude-Code-style session tied to one human.
Each participant runs their own — no multi-tenant agent.

## Responsibilities

- **Subscribe** at startup: register `(agent_id, delivery_url,
  secret)` with the webhook server per
  [`schemas/subscription.md`](../../schemas/subscription.md).
- **Receive** incoming payloads at `delivery_url`. Verify HMAC.
  Two kinds of payload:
  - Handover briefings (schema:
    [`handover-briefing.md`](../../schemas/handover-briefing.md)).
  - `resource.kept` events relayed from Discord (schema:
    [`webhook-event.md`](../../schemas/webhook-event.md)).
- **Decide** on each briefing per
  [`schemas/agent-response.md`](../../schemas/agent-response.md):
  `surfaced`, `kept`, or `ignored`. `priority: mention` is a
  strong hint toward surfacing.
- **Surface** to the human through the agent's chosen channel
  (POC default: a DM from the Discord bot).
- **Keep** on signal — two triggering paths:
  - **Discord-originated.** Webhook server delivered a
    `resource.kept` event for this human.
  - **Agent-originated.** The human told the agent directly.

  In both cases, the agent writes a record into the human's
  private garden (path and filename are the agent's choice) and
  POSTs a `kept` response.
- **Respond** to the webhook server with one response per action.

## Trust model

The briefing's `garden_read` block carries the garden-read
promise: repo, commit SHA, paths read. The agent MAY trust the
promise and act without re-reading.

## Skill surface

The agent ships with a [`SKILL.md`](./SKILL.md) template. Prompts
live in [`prompts/`](./prompts).

## POC boundaries

- One agent per human. Agents do not talk to each other.
- Surfacing channel: Discord DM for the POC.
- Webhook-triggered wake + periodic tick (every ~15 minutes) for
  any deferred work.
- Never auto-keeps. Keep is always human-initiated.
- The agent owns the structure of its human's private garden.
