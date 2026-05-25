# Architectural Drift Report

**Дата:** 2026-05-25  
**Purpose:** Identify divergence between intended architecture and repository reality

---

## 1. Concept Drift

| Intended concept | Drift observed | Severity |
|------------------|----------------|----------|
| Single canonical spine (Claude harness) | Three corpora + two sandboxes compete for attention | Medium |
| Digital twin = identity + memory | Notes exist; replay/versioning absent — term ahead of contracts | Medium |
| Control plane = orchestration | Brain OS uses CP for full product stack naming | Low (isolated) |
| Verification = hooks + subagents | MobileAgent adds visual A/B/C — not yet in curated | Expected gap |
| Memory = taxonomy types | Hermes adds char limits / frozen injection — not curated | Planned gap |

---

## 2. Taxonomy Drift

| Expected | Actual | Action |
|----------|--------|--------|
| 13 sections stable | Stable ✅ | Freeze numbering |
| 10_research catalogs all sources | Only Claude + Harness in policy | Update policy |
| experiments outside taxonomy | Correct ✅ | Maintain |
| governance at repo root | Was missing; now `governance/` | Consolidate refs |
| Promotion docs at root | PROMOTION_REVIEW.md root-only | Link from governance/ |

**No unauthorized section created** — drift risk is **future**, not present.

---

## 3. Duplicated Abstractions

| Abstraction | Instances | Risk |
|-------------|-----------|------|
| Orchestration | 00/orchestration, Brain OS CP, Hermes Kanban | Medium — keep separate provenance |
| Routing | cognitive-router, choose_mode, Claude tool routing | Medium |
| Trace | TraceRecord, Claude telemetry, agent loop | Low |
| Multi-agent roles | Claude subagents, Brain 4-role, Mobile Manager/Executor | High if merged blindly |
| Memory scoring | Claude recall, Hermes FTS, Brain formula, Mobile InfoPool | Medium |

**Rule:** duplicate **ideas** OK in research layer; duplicate **canonical definitions** forbidden.

---

## 4. Branding Drift

| Brand | Where | Drift type |
|-------|-------|------------|
| CAIM, MirrorMind, System-1.5, VGP2 | Brain OS | Plane names without IPC — **branding-only** |
| Brain OS | Books/brain-os | Implies production-ready — mitigated by review/ |
| «Knowledge OS» | README | Accurate |
| «Cognitive platform» | Brain OS source tone | Hype — filter on promotion |
| GUI-Owl | MobileAgent | Model brand — stay research |

---

## 5. Ontology Divergence

| Cluster | Claude ontology | Brain OS ontology | Compatible? |
|---------|-----------------|-------------------|-------------|
| Agent loop | query() generator | task lifecycle FSM | Partial — map don't merge |
| Memory types | user/feedback/project/reference | profile/episodic/semantic/… | Different schemes — **do not unify** without mapping doc |
| Multi-agent | subagent, swarm, task | Kanban, delegate, 4-role | Complementary with scoring |
| Verification | stop hooks | evaluation-engine scores | Different layers |

**Recommendation:** maintain **explicit mapping notes** in `10_research/` when promoting — never silent merge.

---

## 6. Terminology Inconsistency

| Term | Variants found | Canonical term |
|------|----------------|----------------|
| Control plane | Brain OS, orchestration | **orchestration** in Agent-OS; CP = Brain OS research only |
| Harness | Agent harness, GUI harness | **harness** + modality qualifier |
| Twin | digital twin, profile, agent_id | **digital twin** (06); profile = Hermes research |
| Trace | TraceRecord, decision_trace_ref | **trace** with context tag |
| Mode | execution mode, api_mode | **execution mode** (Brain); **api_mode** (Claude) — don't conflate |

---

## 7. Overlapping Patterns

| Pattern A | Pattern B | Resolution |
|-----------|-----------|------------|
| prompt-cache-as-constraint | frozen memory snapshot | Cross-link; complementary |
| error-recovery-ladder | Mobile A/B/C recovery | Extend ladder with visual branch |
| subagents | Kanban workers | Different primitives — both valid |
| trace-first (Brain) | execution-feedback (Claude) | Merge conceptually in 03, separate sources |
| deterministic routing | adaptive routing v0.3 | Promote deterministic only |

---

## 8. Weak Provenance

| Area | Issue |
|------|-------|
| Early agent-os notes | Sources cite Claude but no section granularity |
| 07_projects/ | May lack source paths |
| Comparison docs in experiments | Good provenance ✅ |
| brain-os extracted | Strong Provenance tables ✅ |
| PROMOTION_REVIEW | Strong source paths ✅ |

---

## 9. Research Leakage into Curated Layer

**Audit result:** **No leakage detected** in `agent-os/` from Brain OS, Hermes, or MobileAgent content.

Curated layer remains Claude-derived. Drift risk is **forward-looking** if Phase 1.2 executed without gate.

---

## 10. Drift Score

| Category | Drift level 0–5 |
|----------|-----------------|
| Taxonomy structure | 1 (stable) |
| Canonical content | 2 (partial extraction) |
| Terminology | 3 (multi-corpus) |
| Branding | 3 (Brain OS, planes) |
| Provenance | 2 |
| Research isolation | 1 (good) |

**Overall drift:** **Low–moderate** — controllable with governance Phase 1.2+.

---

## Up

- [CANONICAL_DIRECTION.md](CANONICAL_DIRECTION.md)
- [GOVERNANCE_GAPS.md](GOVERNANCE_GAPS.md)
