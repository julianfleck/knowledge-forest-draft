# identity-config

Maps Discord handles to stable `agent_id`s. Used by the
orchestrator to resolve `@mentions` in share messages and to
enrich `event.who.agent_id` when the bot could not.

Shipped as YAML in the repo. Updated by hand when a participant
joins.

```yaml
# services/orchestrator/prompts/identity-config.yaml
version: 1
participants:
  - agent_id: julian
    discord_user_id: "1220000000000000002"
    discord_username: julian
    aliases: ["@julian", "julianfleck"]
    garden_repo: "github.com/julian/private-garden"

  - agent_id: corey
    discord_user_id: "1220000000000000003"
    discord_username: corey
    aliases: ["@corey"]
    garden_repo: "github.com/corey/private-garden"

  - agent_id: christina
    discord_user_id: "1220000000000000004"
    discord_username: christina
    aliases: ["@christina"]
    garden_repo: "github.com/christina/private-garden"
```

## Resolution rules

- Prefer `discord_user_id` — unambiguous.
- Fall back to case-insensitive match against `discord_username`
  or any `aliases`.
- If a mention can't be resolved, log and continue. Do not emit a
  `mention` briefing for an unresolved handle.

## Privacy

`garden_repo` is the only sensitive field here and it's already
known to the orchestrator (which has clone credentials). Keep this
file in the shareable repo only if the group agrees — otherwise
keep it in a private ops repo and reference by path.
