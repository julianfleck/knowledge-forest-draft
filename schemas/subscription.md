# Subscription

**Flow:** personal-agent → webhook-server (register); then
webhook-server → personal-agent for each briefing delivery.

Each personal agent registers exactly once with a stable
`agent_id`. Every briefing is addressed to one `agent_id`.

## Register

```
POST /subscriptions
Content-Type: application/json
```

Body:

```json
{
  "agent_id": "julian",
  "delivery_url": "https://agents.internal/hooks/julian",
  "secret": "<shared secret used for delivery HMAC>"
}
```

Response `201 {status: "registered"}`. Re-registering with the
same `agent_id` replaces the stored record.

## Delivery

For each briefing addressed to `agent_id`, the webhook server
POSTs to the registered `delivery_url`:

```
POST <delivery_url>
Content-Type: application/json
X-KF-Signature: sha256=<hex>        // HMAC of body, subscription secret
X-KF-Priority: normal | mention     // mirrors briefing.priority
```

Body: a handover briefing (see
[`handover-briefing.md`](./handover-briefing.md)).

Delivery is at-least-once. Personal agents dedup by
`briefing.briefing_id`.
