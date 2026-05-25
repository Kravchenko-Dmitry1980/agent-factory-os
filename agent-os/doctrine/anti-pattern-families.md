# Anti-pattern Families

Grouped failure modes from curated `09_antipatterns/` plus operational inverse lessons (reference only). Each family: symptoms, root causes, mitigations, dangerous escalations.

Cross-walk: [canonical-principles.md](canonical-principles.md) § Principle 8

---

## Verification Failures

**Symptoms:** Task marked done with wrong outcome; GUI click without UI delta proof; retry loops burn budget without verify progress; critic pass treated as ground truth.

**Root causes:** Model self-report trusted; transport success conflated with progress; missing stop hooks / visual verification; LLM critic substituted for harness verify.

**Curated members:**

- [[unverified-gui-clicks]]
- [[infinite-retry-loops]] (partial — when retry replaces verify)

**Operational inverse (reference):** critic-as-fake-verification (`Books/swarm-playbooks/`)

**Mitigation patterns:**

- [[fail-closed-agent-loop]]
- [[visual-verification]]
- [[verification-before-writeback]]
- [[execution-verification]]

**Dangerous escalations:** Auto-publish after critic; skip verify “for speed”; report critic pass-rate as SLA.

---

## Memory Failures

**Symptoms:** Prompt cost spikes; agent “forgets” what it saved; stale repo copy in memory; unbounded store growth.

**Root causes:** Mid-session injection; no char limits; writing what should be read live; cache-busting prompt edits.

**Curated members:**

- [[unbounded-memory-growth]]
- [[mid-session-memory-injection]]
- [[memory-as-crutch]]
- [[cache-busting-sections]]

**Operational inverse:** CLAUDE.md as memory plane

**Mitigation patterns:**

- [[frozen-memory-snapshot]]
- [[memory-char-limits]]
- [[memory-aware-execution]]
- [[verification-before-writeback]]
- [[prompt-cache-as-constraint]]

**Dangerous escalations:** Auto-writeback all chat; recursive skill/memory spawn ([[recursive-self-improvement]]).

---

## Governance Failures

**Symptoms:** Research cited as canonical; unscored copy into agent-os; duplicate definitions; promotion skip.

**Root causes:** No promotion pipeline; wikilink discipline collapse; glossary bodies duplicating concepts.

**Curated members:** (doctrine-level — promotion skip, research leakage)

**Operational inverse:** prompt-only governance, personality-over-architecture

**Mitigation patterns:**

- Promotion pipeline ([governance/PROMOTION_STRATEGY.md](../../governance/PROMOTION_STRATEGY.md))
- [canonical-vs-research-map](../graph/canonical-vs-research-map.md)
- [semantic-linking-rules](../graph/semantic-linking-rules.md)

**Dangerous escalations:** Phase 1.4 mistaken for promotion phase (NR1); swarm verbatim copy (NR2).

---

## Orchestration Failures

**Symptoms:** God orchestrator module; premature multi-agent swarm; lost tasks on crash; prompt-chain plans.

**Root causes:** Wrong coordination primitive; no durable queue; no contracts; complexity before MVP.

**Curated members:**

- [[central-orchestrator-god-object]]
- [[recursive-self-improvement]]
- [[infinite-retry-loops]]

**Operational inverse:** premature-agent-swarm, orchestration-without-contracts, prompt-chain-fragility

**Mitigation patterns:**

- [[kanban-vs-delegate]]
- [[durable-task-coordination]]
- [[subagent-tool-restrictions]]
- [[self-describing-tools]]

**Dangerous escalations:** 8-agent default topology (NR3); unbounded spawn depth.

---

## GUI Failures

**Symptoms:** Clicks on wrong elements; sleep-based automation; hardcoded coordinates; no post-action verify.

**Root causes:** Poor perception; brittle harness; unverified progress credit.

**Curated members:**

- [[brittle-gui-automation]]
- [[unverified-gui-clicks]]

**Mitigation patterns:**

- [[gui-agent-loop]]
- [[visual-verification]]
- [[visual-grounding]]
- [[fail-closed-agent-loop]]

**Dangerous escalations:** Separate unverified GUI path from code path governance; third taxonomy spine without verification cluster.

---

## Tutorial-driven Failures

**Symptoms:** Install scaffold treated as architecture; framework stack (Next/Express) copied as design; prompt sequence = system spec.

**Root causes:** Beginner material mistaken for production reference; skipping MVP validation.

**Curated members:** (implicit — no dedicated curated file)

**Operational inverse:** tutorial-driven-architecture, install scaffold as architecture

**Mitigation patterns:**

- [[progressive-skill-disclosure]]
- Staged evolution (operational reference)
- Research isolation principle

**Dangerous escalations:** Promote tutorial prompts to canonical patterns without scoring.

---

## Autonomy Failures

**Symptoms:** External harm; runaway cost; self-modifying policy; bypass review paths.

**Root causes:** Unrestricted tools; no approval gates; recursive improvement without rollback.

**Curated members:**

- [[recursive-self-improvement]]

**Operational inverse:** unbounded-agent-autonomy, automation-without-review

**Mitigation patterns:**

- [[permission-modes]]
- [[subagent-tool-restrictions]]
- [[fail-closed-defaults]]
- Governance-before-autonomy doctrine

**Dangerous escalations:** “Fully autonomous” marketing; critic removes human review.

---

## Taxonomy Failures

**Symptoms:** New numbered sections for every modality; glossary definitions duplicating concepts; diagram nodes without curated bodies.

**Root causes:** Repository size mistaken for architecture depth; inflation over consolidation.

**Curated members:** (governance-level — see TAXONOMY_REVIEW)

**Mitigation patterns:**

- One concept per file ([agent-os/README.md](../README.md))
- Glossary = pointers only
- Semantic clusters cross-cut folders
- Phase 1.4 doctrine **without** new taxonomy sections

**Dangerous escalations:** `13_gui-agents/` before threshold; ontology product confusion (NR5).

---

## Sources

- `agent-os/09_antipatterns/`
- `governance/CONSOLIDATION_CANDIDATES.md` § Anti-pattern Families
- `Books/swarm-playbooks/anti-patterns/` (reference)
- `governance/SEMANTIC_DRIFT_ANALYSIS.md`

See also: [diagrams/anti-pattern-families.md](diagrams/anti-pattern-families.md)
