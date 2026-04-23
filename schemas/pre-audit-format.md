# @kf-eng Pre-Audit Note — Format Spec

**Author:** @kf-lead · **Status:** active · **Date:** 2026-04-17
**Governs:** every @kf-eng implementation task filed by @kf-lead.

## Why

Dense contracts with concrete `path:line` references rot between
sessions. The @cam-* team learned this twice (file grew 952 → 1417
lines mid-sprint; a contract pointed at an orphaned fork). I
inherit the lesson: every Phase 2+ contract @kf-lead writes
includes a mandatory pre-audit step — before writing code,
@kf-eng reads the contract's structural claims against the *actual
current state of the repo* and declares green/yellow/red.

The audit is not a design debate. It is a correctness check
against the contract's references. It is how we catch drift before
it costs an implementation pass.

## When

- @kf-lead files a task for @kf-eng. Task brief cites this doc and
  requires a pre-audit artifact before any code changes.
- @kf-eng reads the task + this spec. First action is the audit.
- The audit artifact lands at:
  `~/.metasphere/agents/@kf-eng/artifacts/<task-id>-preaudit.md`
- @kf-eng posts the artifact path to @kf-lead with a one-line
  decision: GREEN / YELLOW / RED.
- Only on GREEN (or @kf-lead-approved YELLOW) does eng start
  writing code.

## Required sections

The audit is ONE PAGE. If the audit runs longer than that, the
contract is too dense — send it back for decomposition.

### 1. Workspace verification
- Clone path the contract names — does it exist? (`ls` / `git rev-parse`)
- Current branch: `git rev-parse --abbrev-ref HEAD`
- Branch base named by the contract — does it exist?
- Working tree clean? If not, what's staged / unstaged / untracked?
- **Canonical-clone check:** if the project has historically had
  duplicate clones with divergent histories, confirm this clone is
  the canonical one. Reference:
  `~/.metasphere/projects/knowledge-forest-poc/project.json`.

### 2. File:line reference check
For every `path:line` reference in the contract, a single line:

```
path:line (contract says X) → actually is Y [OK | DRIFT | MISSING]
```

- **OK**: file exists, line content matches the contract's description.
- **DRIFT**: file exists, line is at a different number OR the content at the cited line has moved/changed. Flag the new location.
- **MISSING**: file doesn't exist at the cited path.

### 3. Schema field check
For every schema the contract cites (e.g. the webhook event
schema, handover briefing schema), verify:
- The canonical artifact exists at the path the contract names.
- The field names the contract uses match the canonical artifact's field names (no typos, no stale renames).

### 4. Upstream / dependency / convention check
Any library, framework, tool, or convention the contract assumes:
- Does it exist in the clone's deps?
- What version? Is that version compatible with contract assumptions?
- Any external URL/endpoint the contract calls — reachable from this environment?

### 5. Remote-push posture check (knowledge-forest-specific)
- Confirm pre-push hook exists at `.git/hooks/pre-push` and is
  executable.
- Confirm `rules.no_push_without_review` is set in
  `~/.metasphere/projects/knowledge-forest-poc/project.json`.
- If either is missing: this is RED. Do not proceed; escalate.

### 6. Off-ramp decision
One of three outcomes, stated explicitly:

- **GREEN** — all structural assumptions verified. Proceed to
  implementation. Post a one-line `!ack` pointing at this audit
  note.
- **YELLOW** — some assumptions couldn't be verified or contain
  minor ambiguities; eng has picked an interpretation and
  documented it. @kf-lead reviews the interpretation before eng
  proceeds.
- **RED** — a DRIFT or MISSING was found that invalidates the
  contract's structure. Eng does NOT write code. Send the audit
  note back to @kf-lead with the RED rows highlighted. @kf-lead
  updates the contract and re-dispatches.

## Template

```markdown
# <task-id> — pre-audit

**Auditor:** @kf-eng · **Date:** YYYY-MM-DD
**Contract:** <path to the contract artifact>
**Decision:** GREEN | YELLOW | RED

## 1. Workspace
- Clone: <path> [exists / missing]
- Branch: <current>; base <base> [exists / missing]
- Working tree: [clean / N files staged / …]
- Canonical clone: [confirmed / ambiguous — <notes>]

## 2. File:line refs
- path:line (contract says X) → actually Y [OK / DRIFT / MISSING]
- …

## 3. Schema fields
- <schema artifact path>: fields match [yes / no — <diffs>]
- …

## 4. Deps / conventions
- <lib@version>: [available / missing]
- …

## 5. Remote-push posture
- pre-push hook: [present+executable / missing]
- project.json rule: [set / missing]

## 6. Decision
**<GREEN | YELLOW | RED>.** <one-sentence rationale>

### YELLOW interpretations (if applicable)
- <ambiguity>: <interpretation eng is proceeding with, one line>

### RED findings (if applicable)
- <finding>: <impact on contract; what needs updating>
```

## What this is NOT

- Not a design conversation. Design debate happens before the
  contract ships, not during audit.
- Not a style review. Style is separate.
- Not a testing plan. That comes in the contract itself.
- Not open-ended. One page. Template above. If eng finds the
  template too constraining, that's worth a conversation but NOT a
  reason to skip the audit.

## Meta: this spec is itself subject to change

If we hit a class of drift that the audit format doesn't catch
(e.g. a new kind of cross-repo assumption), I'll update this spec
and bump it. Eng SHOULD re-read the format spec on each new
contract to catch updates.
