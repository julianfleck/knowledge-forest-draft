# discord-bot

Captures activity in a dedicated Discord channel and emits
structured events to the webhook server.

**Owner:** atlasresearch.

## Responsibilities

- Listen in one dedicated channel.
- On a message containing a URL, emit a `resource.shared` event
  per [`schemas/webhook-event.md`](../../schemas/webhook-event.md).
- On a bookmark-style reaction to a prior share, or a reply that
  matches a configured keep verb, emit a `resource.kept` event
  referencing the original share's `correlation_id`.
- Set `correlation_id = <Discord message id>` so the webhook
  server can dedup retries.
- Optionally resolve a URL preview (title, description) on
  shares.
- Optionally reply on the share with a link to a prior thread
  when the webhook server tells it the URL was already kept.

## Interfaces

- **Out:** HTTP POSTs to the webhook server's `/events`, signed
  with `X-KF-Signature`.
- **In:** none beyond the Discord gateway.

## POC boundaries

- Single guild, single channel.
- Passive capture plus reaction/reply recognition — no slash
  commands.
- At-least-once delivery with retry on non-2xx.
