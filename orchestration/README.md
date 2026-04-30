# orchestration/

How knowledge-forest-poc agents are run. Owns process lifecycle —
spawning, waking, sleeping. Does not own what agents *do*
(`../agents/`) or how messages are delivered (`../chat/`).

## Operating model (Julian's lean)

One Claude Code subscription key, multiple tmux sessions. Each
agent identity is a long-running tmux session running a `claude`
REPL in its own working dir. Spawning an agent = render template
into a per-agent dir, start a tmux session, run `claude`. Waking
an agent = send keystrokes to its tmux session. Same operational
shape as metasphere; we borrow the model, not the code.

## Per-agent layout & templates

Each agent gets `~/.kf-poc/agents/<agent-id>/` with `AGENTS.md`
(persona, rendered from template), `state/` (self-writes), and
`inbox/` (queued messages). Templates live in
`orchestration/templates/<agent-type>/`; at spawn, the orchestrator
copies the template in and substitutes `<agent-id>`, the human
owner's display name, and per-instance config.

## Personal-agent-N

Each atlasresearch participant gets a dedicated **personal agent**
spawned at onboarding. It's the participant's proxy in the
forest — consumes incoming events on their behalf, applies their
context frame, decides what surfaces. 1:1 with humans. Template
under `orchestration/templates/personal/`.

## Lifecycle

- **spawn** — render template, create per-agent dir, start tmux,
  run `claude`. One-time per identity.
- **wake** — REPL idle; push next message into the prompt.
- **sleep** — REPL turn finishes; tmux session stays alive.
- **respawn** — only on state wipe or template change.

## OPEN QUESTION — harness architecture

Julian's lean is claude-code-key + tmux. Alternatives worth naming:

- **Anthropic API direct.** Stateless calls, we own the history.
  Wins: programmatic, scales past local tmux. Loses: no
  observable REPL; we re-implement what Claude Code already does.
- **Claude Agent SDK.** Managed agents, server-side persistence.
  Wins: built-in memory, no tmux. Loses: less visibility, newer
  surface, may not match the 2-week MVP timeline.
- **One shared session, prefix-routed.** Single Claude Code
  instance; `@personal-jane` routed internally. Wins: cheapest.
  Loses: collapses agent identities into one context window —
  defeats the per-participant proxy model.

**Recommended: tmux.** atlasresearch wants human-observable agent
reasoning during sessions; tmux gives us that for free. Revisit
if we hit session limits or the audience never opens the REPLs.
