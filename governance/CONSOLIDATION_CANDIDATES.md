# Consolidation Candidates — Phase 1.4

**Purpose:** Items Phase 1.4 should synthesize into doctrine — **not promote as new atomic notes** without separate gate.

---

## Architecture Principles

| Candidate | Source | Why consolidate | Risk | Priority |
|-----------|--------|-----------------|------|----------|
| Verification-first | Claude ch05; [[visual-verification]]; swarm critique-vs-verification | Scattered across 3 clusters + swarm warnings | Critic mistaken for verify | **P0** |
| Governance-before-autonomy | [[recursive-self-improvement]]; swarm safe-autonomy | Ops wants speed; docs say freeze | Unbounded autonomy | **P0** |
| Bounded memory | [[memory-char-limits]]; [[frozen-memory-snapshot]]; swarm anti CLAUDE.md-as-memory | Core production invariant | Mid-session injection regression | **P0** |
| Fail-closed execution | [[fail-closed-defaults]]; [[fail-closed-agent-loop]] | Two notes — doctrine must disambiguate | Merge confusion | **P0** |
| Provenance-first | graph/provenance-graph; PROMOTION_LOG | Multi-corpus repo needs single rule | Research marked canonical | **P0** |
| Promotion discipline | PROMOTION_STRATEGY; promotion-governance cluster | Prevents leakage | Skipping scoring | **P0** |
| HITL boundaries | swarm hitl/*; brain-os human-escalation (research) | Ops corpus strong; canonical thin | 8-agent topology bleed | **P1** |
| Anti-pattern adjacency | graph semantic-linking-rules | Every AP needs fix pattern | Orphan warnings | **P1** |
| Dual golden path | [[query-loop]] ∥ [[gui-agent-loop]] | Positioning clarity | GUI runtime creep | **P1** |
| Durable vs ephemeral orchestration | [[kanban-vs-delegate]] | Single decision doctrine | Wrong primitive | **P1** |

---

## Operational Lifecycle

Synthesize from: Claude loop, swarm `lifecycle/orchestration-lifecycle.md`, graph verification cluster.

| Stage | Canonical anchors | Swarm input (reference only) | Risk |
|-------|-------------------|------------------------------|------|
| Goal / intake | task envelope (research) | ЗАДАЧА checklist | Tutorial coupling |
| Routing | [[memory-aware-execution]]; kanban-vs-delegate | queue-backed-execution | Queue without contracts |
| Planning | [[planning]]; progressive skill disclosure | plan approval phase | Heuristic thresholds |
| Execution | query-loop / gui-agent-loop | execution feedback loop | Skip verify |
| Verification | verification + visual-verification + fail-closed-agent-loop | review-gate | Critic = verify |
| Review | execution-verification | critique-before-publish | LLM-only QA |
| Escalation | human-escalation-gate (research) | escalation-to-human | No SLA |
| Approval | permission-modes; swarm approval-before-external-action | HITL UX patterns | External action harm |
| Writeback | verification-before-writeback | — | Unverified memory |

**Deliverable recommendation:** `governance/OPERATIONAL_LIFECYCLE.md` — stage table + canonical wikilinks + explicit «swarm = operational reference».

---

## Anti-pattern Families

| Family | Members (curated) | Swarm inverse lessons | Priority |
|--------|-------------------|----------------------|----------|
| Memory failure | unbounded-memory-growth, mid-session-memory-injection, memory-as-crutch, cache-busting-sections | CLAUDE.md as memory plane | P0 |
| Verification failure | unverified-gui-clicks, infinite-retry-loops (partial) | critic-as-fake-verification | P0 |
| Orchestration failure | recursive-self-improvement, central-orchestrator-god-object | premature-agent-swarm, orchestration-without-contracts | P0 |
| GUI failure | brittle-gui-automation, unverified-gui-clicks | tutorial-driven-architecture | P1 |
| Governance failure | (doctrine) promotion skip, research leakage | prompt-only governance, personality-over-architecture | P0 |
| Tutorial-driven failure | — | tutorial-driven-architecture, install scaffold as architecture | P1 |
| Autonomy failure | recursive-self-improvement | unbounded-agent-autonomy, automation-without-review | P0 |

**Deliverable recommendation:** `governance/ANTIPATTERN_FAMILIES.md`

---

## System Positioning

### Agent-OS IS

- Engineering knowledge OS for **agent harness architecture**
- Curated atomic notes with governance-first promotion
- Claude production spine + governed research extensions
- Semantic graph for navigation (not intelligence simulation)
- Anti-pattern + pattern paired discipline

### Agent-OS IS NOT

- Runtime platform (Hermes, MobileAgent, swarm stack)
- Ontology product or graph database
- RAG/embedding pipeline (yet)
- Digital twin operational system (no replay)
- Default «8-agent swarm» blueprint
- Tutorial or install scaffold documentation
- Critic-as-verification substitute

**Deliverable recommendation:** `governance/SYSTEM_POSITIONING.md`

---

## Swarm SAFE FUTURE (Phase 1.4 reference only — not promote)

From `Books/swarm-playbooks/review/promotion-candidates.md` — cite in doctrine as **operational alignment**, promote only after separate scoring:

| Concept | Aligns with | Phase 1.4 action |
|---------|-------------|------------------|
| human-in-the-loop-approval | human-escalation research / verification | Reference in HITL doctrine |
| progressive-autonomy | staged rollout principle | Lifecycle stage |
| review-gate | verification cluster | Lifecycle stage |
| queue-backed-execution | durable-task-coordination | Orchestration doctrine |
| approval-before-external-action | fail-closed + permissions | Principle cross-walk |
| critique-limitations | verification-first | **Mandatory** if critic mentioned |

---

## Up

- [PHASE_1_4_READINESS.md](PHASE_1_4_READINESS.md)
- [FREEZE_RECOMMENDATIONS.md](FREEZE_RECOMMENDATIONS.md)
