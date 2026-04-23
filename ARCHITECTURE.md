# Architecture

## Goal

Test one hypothesis: wrapping each resource shared in a group
Discord channel with a six-dimension context frame
(`who` / `when` / `why` / `what` / `where` / `how`) and routing a
short, personalised briefing to each participant reduces
information overload in group knowledge sharing.

The whole system exists to produce one artifact — the briefing —
and to learn whether participants find it useful.

## Diagram

```
       ┌───────────┐
       │  Discord  │   humans share resources here
       └─────┬─────┘
             │ share
             ▼
       ┌───────────┐
       │    Bot    │   captures the share
       └─────┬─────┘
             │ event
             ▼
     ┌───────────────┐
     │ Webhook       │   receives events,
     │ Server        │   holds subscriptions,
     │               │   fans briefings out
     └───┬───────▲───┘
         │       │
   invoke│       │briefings
         ▼       │
     ┌───────────┴───┐
     │ Orchestrator  │   reads each subscriber's garden,
     │               │   composes one briefing per subscriber
     └───────────────┘
             │
             │ (via webhook server)
             ▼
     ┌───────────────────────────────┐
     │ Personal Agents (one per      │
     │ participant): decide whether  │
     │ to surface                    │
     └───────────────────────────────┘
```

## Services

### Discord bot

Listens in a single dedicated channel. On any message with a URL,
POSTs one structured event to the webhook server. Does not frame,
score, or route — just captures.

### Webhook server

The hub. Three jobs:

1. Accept inbound events from the bot.
2. Hold the subscription registry — who subscribes to what stream.
3. Deliver briefings the orchestrator produces to each subscriber
   over HTTP.

Per-agent addressing: each personal agent registers with a stable
`agent_id` and a delivery URL. Every briefing is addressed to
exactly one `agent_id`.

### Orchestrator

The reasoning core. On each new event, for each subscribed
participant:

1. Reads that participant's private knowledge garden at `HEAD`.
2. Writes a one-paragraph relevance note grounded in what it read.
3. Emits a briefing including the frame, the note, and a list of
   the garden paths it read (the "garden-read promise").

If the sharer mentioned a specific participant, that participant's
briefing is marked `priority: mention`. Everyone else gets
`priority: normal`.

### Personal agent

One per participant. Subscribes to its own stream. Two
responsibilities:

- On each incoming briefing, decide whether to **surface** it to
  its human. Mentions are a strong hint; the agent owns the final
  call.
- On human instruction, **keep** a resource: write it into the
  human's private knowledge garden and report the keep back to the
  webhook server.

"Keep" is the bridge between the shared forest (everything
broadcast into the channel) and each human's private garden
(what they actually weeded in). It is the single manual signal
the system treats as ground truth for relevance.

## How they interlock

Walkthrough of a single share:

1. **Share.** Corey posts a link in `#knowledge-forest` and
   writes: _"@julian this reminded me of your mind-palace thread."_
2. **Capture.** The bot sees the message, POSTs an event to the
   webhook server with the URL, the message text, and the
   sharer's identity.
3. **Invoke.** The webhook server persists the event (deduped on
   Discord message id) and hands it to the orchestrator along
   with the current subscription list.
4. **Frame + read.** The orchestrator fills the six-dimension
   frame from the event (`why` stays empty unless Corey wrote a
   reason). For each subscriber, it reads that person's garden
   and writes a short relevance note.
5. **Route.** The orchestrator produces one briefing per
   subscriber. Julian's briefing is marked `priority: mention`
   because Corey named him; the others are `priority: normal`.
6. **Deliver.** The webhook server POSTs each briefing to its
   subscriber's delivery URL, signed with that subscription's
   secret.
7. **Decide.** Each personal agent receives, reads the briefing,
   and decides whether to surface to its human. Julian's agent
   treats the mention as a strong signal. Corey's and
   Christina's agents decide from the relevance note alone.
8. **Store.** The webhook server appends the event and the
   briefings it emitted to a shared group log so the group can
   inspect the system's behaviour later.
9. **Keep (optional, human-initiated).** Julian decides to keep
   the resource. He can signal this two ways:
   - React on the share in Discord (bookmark-style emoji) or
     reply with a keep verb. The bot emits a `resource.kept`
     event to the webhook server, which routes it to Julian's
     personal agent.
   - Tell his personal agent directly through whatever channel
     they share.

   Either way, Julian's personal agent writes a record into his
   private garden (path is the agent's choice) and POSTs a
   `kept` response to the webhook server. The keep lands in the
   group log.

10. **Re-share of a kept resource.** If someone later reshares a
    URL Julian already kept, the orchestrator skips Julian when
    composing briefings. The bot MAY post a reply on the new
    share linking to the earlier thread.

The contract between services is what keeps this simple: the bot
only knows Discord, the webhook server only knows delivery, the
orchestrator only knows reasoning, and each personal agent only
knows its own human. Replace any one of them without touching the
others.

## Open design questions

- **Auto-keep.** Does the agent ever keep without explicit human
  instruction (e.g. on very-high-confidence + mention)? To
  discuss with atlasresearch. POC-lean answer: no — manual keep
  is the relevance ground truth, parallel to the manual `why`.
