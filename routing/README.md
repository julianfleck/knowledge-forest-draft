# routing/

Where routing decisions live. A routing decision answers one
question: *this incoming event — which agent(s) should see it, and
in what role?* Routing is upstream of `../chat/` (which renders
and delivers) and `../orchestration/` (which wakes the chosen
agents).

## What gets routed

Discord (or whatever GuildBot edge surface we settle on) emits
events: messages, reactions, mentions, channel-joins. Each event
needs a destination set:

- **direct mention** of a personal agent → that participant's
  personal agent only.
- **broadcast in a forest channel** → every personal agent
  subscribed to that channel; each decides independently whether
  to surface it to its human.
- **system event** (join/leave/topic-change) → the forest's
  ambient state, possibly fan-out to all personal agents.

The routing module produces a `(event, [destinations])` pair. It
does not deliver and it does not wake — it decides.

## Does the orchestrator live here?

Open question. Two shapes:

- **Stateless router.** Routing is a pure function called by the
  webhook handler. No long-running process. Cleanest if every
  routing decision is local to a single event.
- **Orchestrator daemon.** A long-running process that holds
  cross-event state — rate limits, deduplication, fan-in
  windows, "this user already saw this in another channel."
  Necessary if routing depends on memory of recent events.

**Recommended lean: start stateless.** For the 2-week MVP, every
event we know about is locally decidable. If we discover routing
needs cross-event memory (e.g., "don't double-deliver the same
broadcast across overlapping channels"), promote to a daemon
later. The daemon, if it materializes, lives in this module.

## How routing interacts with the rest

```
Discord event → [ routing/ ] → (event, [agent-ids])
                     │
                     ▼
              [ orchestration/ ] wakes chosen agents
                     │
                     ▼
              [ chat/ ] delivers rendered surface
```

`routing/` knows agent identities and channel subscriptions. It
does not know how agents are spawned or how they render. Reads
the registry the orchestrator maintains; writes nothing back.
