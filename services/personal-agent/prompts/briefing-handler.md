# Payload Handler — personal agent

Run once per incoming payload. Produces one or more HTTP POSTs to
`/responses`.

## 1. Receive & verify

- Read `X-KF-Signature`, `X-KF-Priority`, body.
- Recompute HMAC over the body with the subscription secret.
  Reject on mismatch.
- Identify the payload:
  - A handover briefing has `briefing_id` at the top level.
  - A keep event has `event_type: "resource.kept"`.
- Dedup briefings by `briefing_id`, events by `correlation_id`.

## 2a. Briefing path — decide

Trust the garden-read promise in `garden_read` unless you have a
reason not to. Use `relevance_note`, `priority`, and
`context_frame.why` (if non-null) to pick an action:

- `priority == "mention"` → default **surface**. Only ignore with
  a concrete reason.
- `priority == "normal"` →
  - If `relevance_note` reads as a genuine match → **surface**.
  - If the orchestrator's note is weak or negative → **ignore**.

You always own the final call.

### Surface

Pass the resource and a short framing to your human through your
chosen channel (for the POC, a DM from the Discord bot).

Then POST `/responses` with `action = "surfaced"`.

### Ignore

If you decide not to surface, POST `/responses` immediately with
`action = "ignored"` and a real `reason`. The group log needs the
negative signal.

## 2b. Keep event path — persist

A `resource.kept` event means your human signalled a keep via
Discord (reaction or reply). Act on it without asking:

1. Write a resource record into your human's private garden.
   Path and filename are your choice; you own the garden's
   structure. Follow
   [`schemas/resource.md`](../../../schemas/resource.md) with a
   `kept` block recording `method` (`reaction` | `reply`),
   `from_event` (the event's `correlation_id`), and the human's
   `note` if `method = reply`.
2. Commit and push.
3. POST `/responses` with `action = "kept"`, `garden_path`
   pointing at the record, and `reason` capturing the intent.

## 3. Keep by direct instruction

If your human tells you to keep a resource during a conversation
(not via Discord), do the same thing with `method: agent`:

1. Write the record. If the keep was triggered by a briefing you
   previously surfaced, set `from_briefing` to that briefing's
   id. Otherwise omit it.
2. Commit, push, and POST `/responses` with `action = "kept"`,
   `garden_path`, and a `reason` that captures what the human
   said.

## Response pairing

A single briefing can produce both `surfaced` and later `kept` —
each is its own response entry. Keep events always produce
exactly one `kept` response.
