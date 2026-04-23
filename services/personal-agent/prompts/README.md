# personal-agent prompts

Prompts for one personal research agent. Each file is a
Claude-Code-style prompt fragment; the bring-up harness
concatenates them in a documented order.

| File                 | Purpose                                                           |
|----------------------|-------------------------------------------------------------------|
| `system-prompt.md`   | Identity, role, trust model, decision procedure.                  |
| `garden-seed.md`     | (Per-participant) Pointers into the human's private garden.       |
| `briefing-handler.md`| Step-by-step instructions for processing one incoming briefing.   |
| `response-template.md`| Schema-pinned template for the agent's response payload.          |

`garden-seed.md` is intentionally owned by each participant — it
names repo paths and any per-human conventions the agent should
know about. It lives in each participant's private garden, not in
this repo.

The decision procedure is deliberately short so the agent can be
audited. Keep changes narrow; discuss before broadening.
