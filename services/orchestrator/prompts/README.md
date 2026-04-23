# orchestrator prompts

Prompts for the single orchestrator agent. Concatenated in this
order:

| File                    | Purpose                                                       |
|-------------------------|---------------------------------------------------------------|
| `system-prompt.md`      | Identity, role, routing rules, garden-read promise.           |
| `identity-config.md`    | Mapping from Discord handles / `@mentions` to `agent_id`s.    |
| `briefing-composer.md`  | Step-by-step: from inbound event to N briefings.              |
| `briefing-template.md`  | Schema-pinned template for a single briefing payload.         |

`identity-config.md` is a small YAML file that ships in the repo
and is updated by hand when a new participant joins.
