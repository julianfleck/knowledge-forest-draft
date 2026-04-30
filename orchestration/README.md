# orchestration/

How the agents in this project are run. This module owns process
lifecycle — spawning, waking, sleeping. It does not own what the
agents *do* (`../agents/`) or how messages reach humans
(`../chat/`).

## Operating model

One subscription to **Claude Code** (Anthropic's terminal-based
coding agent that runs from your shell), shared across all
agents. Each agent identity is a long-running session inside
**tmux** (a terminal multiplexer that keeps shell sessions alive
in the background). Spawning an agent: render its template into
a per-agent directory, start a tmux session, run `claude` inside
it. Waking an agent: send keystrokes into that session.

The reason for one tmux session per agent is observability. A
human can attach to any session and watch the agent's reasoning
stream live — useful during the atlasresearch trial when we want
to see *why* a personal agent surfaced (or didn't surface)
something.

## Per-agent layout & templates

Each agent gets a directory under
`~/.knowledge-forest/agents/<agent-id>/` containing `AGENTS.md`
(persona + instructions, rendered from a template), `state/`
(self-writes), and `inbox/` (messages queued for the next wake).
Templates live in `orchestration/templates/<agent-type>/`. At
spawn, the orchestrator copies the template in and substitutes
`<agent-id>`, the human owner's display name, and per-instance
config.

## Personal agents (one per participant)

Each atlasresearch participant gets a dedicated **personal
agent** spawned at onboarding — the participant's proxy in the
forest. It consumes incoming events on their behalf, applies
their context frame, and decides what surfaces. 1:1 with humans.
Template at `orchestration/templates/personal/`.

## Lifecycle

- **spawn** — render template, create directory, start tmux, run
  `claude`. One-time per identity.
- **wake** — push the next message into the idle prompt.
- **sleep** — turn finishes; tmux session stays alive.
- **respawn** — only on state wipe or template change.

## OPEN QUESTION — harness architecture

The recommendation is Claude Code + tmux (above). Alternatives
worth naming before we commit:

- **Call Anthropic's HTTP API directly, no Claude Code wrapper.**
  Each agent turn is a stateless API call; we manage history
  ourselves. Wins on programmatic control and scale; loses the
  observable REPL and forces us to re-implement what Claude Code
  already gives us (tool use, subagents, hooks).
- **Anthropic's Claude Agent SDK.** Long-lived agents managed by
  Anthropic, persisted server-side. Wins on built-in memory and
  no tmux to manage; loses local visibility, and the surface is
  newer than the 2-week timeline really wants.
- **One shared Claude Code session, prefix-routed.** A single
  `claude` process; messages get prefixed by recipient and
  routed internally. Cheapest to start, but collapses every
  agent's identity into one context window — defeats the
  per-participant proxy model entirely.

**Recommendation: Claude Code + tmux.** The atlasresearch trial
benefits from human-observable agent reasoning during sessions;
this approach gives us that for free. Revisit if we hit tmux
session limits or if no one ever opens the REPLs.
