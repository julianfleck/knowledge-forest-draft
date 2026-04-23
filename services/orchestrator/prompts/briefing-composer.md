# Briefing Composer — orchestrator

Runs once per inbound event. Produces a list of briefings.

## 1. Validate

Schema-check the event against
[`webhook-event.md`](../../../schemas/webhook-event.md). On
failure, return an empty list.

## 2. Resolve mentions

Parse `event.message_text` for `<@discord_user_id>` and free-text
`@handle` references. Map each to an `agent_id` via
`identity-config`. Let `MENTIONED = { agent_id, … }`. Unresolved
handles are logged, not fatal.

## 3. Fill the frame once

```yaml
who: <event.sharer.agent_id or discord_username>
when: <event.occurred_at>
why: null
what: <event.url>
where: <event.channel.channel_name>
how: discord-share
```

`why` stays `null`. Do not invent a why.

## 4. For each subscription

1. `priority = "mention"` if `subscription.agent_id ∈ MENTIONED`
   else `"normal"`.
2. Read the subscriber's garden at `HEAD`. Record `commit_sha`.
3. Pick the paths most likely relevant (naive fulltext match over
   `*.md` is fine for the POC).
4. Write a one-paragraph `relevance_note` grounded in those paths.
   If nothing relevant, write a short negative note.
5. Assemble the briefing per
   [`briefing-template.md`](./briefing-template.md).

## 5. Failure

- Garden unreadable (auth, 404, timeout) → skip the briefing for
  that subscriber; log the skip; retry on next event or tick.
- Any per-subscriber failure is isolated. Other subscribers still
  get their briefings.

## 6. Return

A list of briefings. The webhook server delivers.
