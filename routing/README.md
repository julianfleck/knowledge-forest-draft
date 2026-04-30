# routing/

Where routing decisions live. A routing decision answers one
question: *this incoming event — which agent(s) should see it,
and in what role?* Routing sits upstream of `../chat/` (which
renders and delivers messages to humans) and `../orchestration/`
(which wakes the agents that were chosen).

## What gets routed

The Discord bot emits events into this system: messages,
reactions, mentions, channel-joins. Each event needs a
**destination set** — the list of agents that should receive it.
Three common patterns:

- **Direct mention** of a personal agent → that participant's
  personal agent only.
- **Broadcast in a forest channel** → every personal agent
  subscribed to that channel; each decides independently whether
  to surface it to its human.
- **System event** (join, leave, topic change) → updates ambient
  state, possibly fanned out to all personal agents.

The routing module produces a `(event, [destinations])` pair. It
does not deliver the event and it does not wake the agents — it
only decides who should be reached.

## Does the orchestrator live here?

Open question. Two shapes are on the table:

- **Stateless router.** Routing is a pure function called by the
  Discord webhook handler — no long-running process. Cleanest if
  every routing decision can be made from the event alone.
- **Orchestrator daemon.** A long-running process that holds
  cross-event state — rate limits, deduplication windows, "this
  user already saw this in another channel" memory. Necessary
  only if routing depends on what happened in *previous* events.

**Recommendation: start stateless.** For the 2-week MVP, every
event we currently know about is locally decidable from the
event itself. If we discover routing needs cross-event memory
(e.g., "don't double-deliver the same broadcast across
overlapping channels"), promote to a daemon later. If the
daemon does materialize, it lives in this module.

## How routing interacts with the rest

```
Discord event → [ routing/ ] → (event, [agent-ids])
                     │
                     ▼
              [ orchestration/ ] wakes the chosen agents
                     │
                     ▼
              [ chat/ ] delivers the rendered surface
```

`routing/` knows about agent identities and which agents are
subscribed to which channels. It does not know how agents are
spawned or how their output is rendered. It reads from the
agent registry that `orchestration/` maintains, and writes
nothing back.
