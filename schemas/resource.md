# Resource Record

How a shared resource is persisted. Used in two places:

1. **Group garden** (shared repo, owned by atlasresearch) — every
   share produces one record.
2. **Personal garden** (each participant's private repo) — a
   record is written when their personal agent executes a `kept`.

The shape below is the **group garden** form. In a personal
garden, the path and filename are the personal agent's choice —
the agent owns its human's garden structure. The frontmatter
stays the same, with an added `kept` block recording who kept it
and why.

## Path convention (group garden only)

```
resources/<YYYY>/<MM>/<correlation_id>.md
```

Personal gardens are per-agent. The agent decides where to put
the record.

## File format

Markdown with YAML front-matter.

```markdown
---
correlation_id: "1226543210987654321"
created_at: 2026-04-23T15:30:10Z
source:
  shared_by: corey
  shared_in: "#knowledge-forest"
  shared_at: 2026-04-23T15:30:00Z
context_frame:
  who: corey
  when: 2026-04-23T15:30:00Z
  why: null
  what: https://example.com/alexander.pdf
  where: "#knowledge-forest"
  how: discord-share
resource:
  url: https://example.com/alexander.pdf
  title: A Pattern Language
  description: "Alexander et al., 1977."
---

> **Corey** shared this in `#knowledge-forest` on 2026-04-23.
>
> "reminded me of Julian's mind-palace thread"
```

## Personal garden — added `kept` block

When a personal agent persists a record, it appends a `kept`
block to the frontmatter:

```yaml
kept:
  by: julian
  at: 2026-04-23T15:47:02Z
  from_briefing: bf_01HZXYZ789      # if triggered from a briefing
  from_event: evt_kept_01HZ...      # if triggered from a resource.kept event
  method: reaction | reply | agent  # discord reaction, discord reply, or direct-to-agent
  note: "<human's rationale if they gave one>"
```

The `note` is a natural place for the human's `why` — what the
six-dimension frame left as `null` at share time.
