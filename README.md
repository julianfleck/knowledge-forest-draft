# knowledge-forest

A two-week MVP for group knowledge sharing with context.

Every resource dropped in a dedicated Discord channel gets wrapped
in a six-dimension context frame (`who` / `when` / `why` / `what` /
`where` / `how`) and routed to each participant's personal agent
with a synthesized relevance note.

## Structure

- [`ARCHITECTURE.md`](./ARCHITECTURE.md) — goal, diagram,
  services, and how they interlock.
- [`services/`](./services) — one folder per service, each with a
  README that describes its role, interfaces, and MVP boundaries.
  - [`discord-bot`](./services/discord-bot) — share capture.
  - [`webhook-server`](./services/webhook-server) — event hub,
    subscription registry, fanout.
  - [`orchestrator`](./services/orchestrator) — garden read,
    briefing composition, routing decisions.
  - [`personal-agent`](./services/personal-agent) — per-participant
    consumer. Includes a `SKILL.md` template.
- [`schemas/`](./schemas) — wire format and storage contracts shared
  between services.

## Status

Pre-implementation scaffold. The READMEs are starting points for
alignment; treat them as negotiable until the first implementation
pass.
