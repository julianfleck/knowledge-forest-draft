# knowledge-forest-poc — project briefing

**Source**: Transcript at `/home/openclaw/.metasphere/attachments/19230/transcript-christina-julian-corey-membranes.txt` (1092 lines). Participants: Julian Fleck + Christina + Corey (atlasresearch). Date: captured by orchestrator via Explore-agent recon 2026-04-17.

**Use**: Input to @metasphere-lead's knowledge-forest team bootstrap. Reference for @kf-lead / @kf-eng once the team is live.

---

## 1. What is knowledge-forest-poc?

A 2-week MVP testing whether a lightweight **six-dimension context frame** (who, when, why, what, where, how) wrapped around each shared resource reduces information overload in small-group knowledge sharing. Current baseline: Slack/Discord/email drops links with no framing, so recipients can't tell *why* something matters.

Christina's framing: "the knowledge forest is anything you could pick up, [vs] knowledge gardens you weeded out". Forest = raw shared stream; garden = curated personal knowledge. The "membranes" in the filename refers to the boundary design: permeable enough that knowledge flows across the group without fully enmeshing each person's private garden. You see shared context; you don't have to expose your whole garden.

## 2. Architecture

| Component | Owner | Notes |
|---|---|---|
| Discord bot (based on Josh's GuildBot) | atlasresearch / Josh leads | Voice of the orchestrator. Captures share events, publishes to webhook. One dedicated channel. |
| Webhook (HTTP POST endpoint) | Shared | Triggered on Discord share. Event schema = one of our design outputs. |
| Orchestrator agent | Us (metasphere side) | Single persistent Claude Code session. Listens to webhook. Queries each user's knowledge garden. Synthesizes relevance. Produces "handover briefings" to personal agents. Maintains group event log. |
| Personal research agents (Christina, Corey, Julian) | Us (metasphere side) | One Claude Code session per person. Scheduled (every ~15min) + webhook-triggered. Context-injected from that person's knowledge garden. Surfaces relevant recommendations to the human. |
| Personal knowledge gardens | Each person (private GitHub repos) | Bootstrap FRESH — don't use existing bloated repos. Obsidian/LogSeq/VS Code front-matter in markdown files. Front-matter schema = our design output. |
| Group knowledge garden | atlasresearch (shared private GitHub repo, ARG-hosted) | Event log + contextualized resources. |

**Human-facing surface**: Discord only (for the experiment). Everything else is agents reading/writing GitHub repos + agents passing briefings via webhook.

**Event flow example** (from transcript, Corey-shares-Alexander-paper scenario):
1. Corey posts link in Discord → GuildBot publishes: `{who: corey, when: ts, what: url + preview, context: msg_text}`
2. Webhook fires → orchestrator wakes
3. Orchestrator queries Julian's knowledge garden (mind-palace / memory-architecture notes), synthesizes relevance
4. Orchestrator constructs briefing: "Corey shared X. Here's why it might matter to Julian: ... three people marked this relevant."
5. Julian's personal agent receives briefing, decides whether to surface to Julian.

## 3. "Contractual integration points between agents"

Julian's phrasing (1:44:04 in transcript): *"figuring out the like actual templates for these agents and what they look like and like designing the like integration points. Like what does the handover briefing look like? So that we can contractualize that between the different agents."*

**Not legal contracts, not cryptographic contracts. Machine-readable agreements about data flow.** The concrete design objects:

- **Six-dimension frame schema**: YAML/JSON spec defining who/when/why/what/where/how fields, granularity, sub-fields. Christina said she'd draft; not yet concrete.
- **Webhook event schema**: what GuildBot sends when a resource is shared.
- **Handover briefing schema**: what the orchestrator sends to each personal agent (resource + context frame + synthesized relevance note + promise: "I've read this person's garden, this is why I think it matters").
- **Personal agent response schema**: does the agent acknowledge, surface, store, or ignore? (Undefined — may not be needed for MVP.)

**The "why" field** is the important one. It's the one field that's MANUALLY filled by humans (at least in MVP), based on Christina's hypothesis that forcing manual cognitive effort reduces information overload. The other five dimensions can be auto-extracted or inferred.

## 4. Overlap with existing work

- **Metasphere-agents patterns**: Persistent research-agent pattern (scheduled cron + context injection via pre/post hooks) is exactly what personal agents need. **Reuse, don't rebuild.**
- **RAGE/Recurse**: Julian positioned Recurse as a "representation layer for knowledge units". Each six-dimension context frame = one atomic unit that could feed Recurse later. **Not a dependency for MVP; note integration path.**
- **CAM (Collective Agent Memory)**: The group event log on GitHub IS a form of CAM — shared memory all agents can query. **Align with CAM patterns.**
- **Pre/post-command hook architecture**: Julian explicitly referenced at 56:24 — same architecture, adapted to webhook transport.
- **Access control**: ZK proofs, granular access — **EXPLICITLY DEFERRED**. Private GitHub repos + GitHub-native access control is enough for MVP. Don't touch.

## 5. Deliverables

**atlasresearch side:**
- Private GitHub repo (ARG) for MVP code + docs
- Josh's GuildBot (shared; they decide how much to modify)
- Community coordination (Christina owns; out of our scope)

**Our side (metasphere):**
- Orchestrator agent code (Claude Code session + webhook handler)
- Personal research agent templates (3 initial instances)
- Integration schema docs (webhook event shape, handover briefing shape)
- Context-injection setup (seeding each personal agent with the person's knowledge garden)
- Markdown front-matter schema

**Shared:**
- Six-dimension frame definition (Christina drafts; Corey + Julian review)
- GuildBot integration (Josh builds/maintains bot; we integrate webhook)

**Timeline**: 2-week MVP automation-first + lightweight manual input. Optional 2nd 2-week phase: richer manual "why" + behavioral analysis. No hard deadline; sprint-cadence.

## 6. Open questions (need Julian's call before or during team execution)

1. **Josh's availability**: Christina said "he'll be needed for writing those contracts" but he's "in chaos for another week or two". Is he load-bearing? Blocker if not?
2. **Six-dimension schema granularity**: Christina's draft pending. Sub-fields? ID formats?
3. **Agent seeding mechanism**: "Seed from knowledge garden" is vague. How to bootstrap without hallucinating relevance? High-friction area.
4. **Webhook reliability**: Batching / retry / dedup — Corey noted "don't want it always pulling". Design call.
5. **Automation vs manual comparison measurement**: Christina wants to measure whether manual "why" reduces overload. How? Metric undefined.
6. **Discord as frontend**: Experiment-only or intended UX? Affects whether we over-invest in Discord-specific affordances.
7. **GuildBot current state**: Corey's copy is outdated; Josh has made changes. We don't know the integration surface.

## 7. Team-shape implications (not team design — that's @metasphere-lead's call)

**Roles implied by the transcript:**

- **Protocol/orchestrator architect** (probably @kf-lead): owns handover schema, event schema, orchestrator choreography. The "contractual integration points" designer Julian named. Skill: agent systems thinking + API schema design. Not an ontology modeler; more "how do these things talk?".
- **Discord/webhook/bot wiring** (probably @kf-eng): GuildBot integration, HTTP handler, event-driven state management. Not pure plumbing — needs Claude-Code-savvy person because webhook triggers a Claude session with all its lifecycle concerns.
- **Agent seeding specialist**: knowledge-garden→context pipeline, prompt engineering, relevance debugging. Highest-friction area. Could fold into @kf-eng or be a distinct persona.
- **Schema / front-matter designer**: six-dimension frame, markdown spec, event-log schema. Bridges Christina's conceptual model (frame semantics hinted) to JSON. Could fold into @kf-lead.

**Recommended minimum team (per Julian's "small team" directive)**: 2 personas — @kf-lead + @kf-eng. Lead owns protocol + schema design. Eng owns implementation + seeding.

**Optional**: @kf-critic if Julian wants the RSS/edge-case-hunting discipline from the @cam-* model. For a 2-week MVP, might be overhead; the CAM team added it because CAM is production infrastructure. Knowledge-forest is exploratory.

**Is "contractual integration points designer" a separate persona?** My read: NO. It's @kf-lead's primary responsibility. Making it a dedicated persona risks diluting the lead role and creating routing ambiguity. But flag for @metasphere-lead to decide.
