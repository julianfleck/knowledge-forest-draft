# Six-Dimension Context Frame

The frame wrapped around every shared resource. Referenced inline
in briefings and stored in resource records.

## Shape

| Field   | Type           | Source    | Notes                                    |
|---------|----------------|-----------|------------------------------------------|
| `who`   | string         | automatic | Sharer (`agent_id` or discord username). |
| `when`  | ISO-8601 UTC   | automatic | Share timestamp.                         |
| `why`   | string \| null | **manual**| Human rationale. `null` until filled.    |
| `what`  | string         | automatic | Resource URL.                            |
| `where` | string         | automatic | Shared-in channel name.                  |
| `how`   | string         | automatic | Arrival mode. POC: `"discord-share"`.    |

`why` is the only human-authored field. The others are extracted
from the webhook event.

## Example

```json
{
  "who": "corey",
  "when": "2026-04-23T15:30:00Z",
  "why": null,
  "what": "https://example.com/alexander.pdf",
  "where": "#knowledge-forest",
  "how": "discord-share"
}
```
