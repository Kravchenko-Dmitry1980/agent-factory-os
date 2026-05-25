# Phase 3 — Minimal Scope (Agent Builder Kit v0.1)

**Principle:** smallest safe Builder Kit — **specifications and checklists**, not runtime.

---

## Phase 3.0 name

**Agent Builder Kit v0.1**

---

## IN scope (v0.1)

| Deliverable | Type | Notes |
|-------------|------|-------|
| Agent template specification | MD spec | Fields: purpose, inputs, tools, limits |
| Workflow template specification | MD spec | Steps, gates, human points |
| Safety gate template | MD spec | fail-closed, approval, verify |
| Memory boundary template | MD spec | From bounded-memory-agent |
| Evaluation checklist template | MD spec | From evaluation quality-gates |
| Observability trace template | MD spec | Canonical events subset |
| Change proposal template | MD | Link `evolution/change-proposals/change-template.md` |
| Human approval policy | MD | When human required |
| Anti-pattern checklist | MD | From agent-os 09 + curriculum |
| **One demo agent template** | MD + optional reference to existing demo | **Not new Python framework** |

---

## OUT of scope (v0.1)

| Item | Why |
|------|-----|
| Full agent factory | Needs UX, registry, generation — later |
| No-code platform | Productization |
| Digital twin builder | DIGITAL_TWIN_DEFER |
| CV builder | CV_AGENT_FUTURE |
| Marketplace / SaaS | Product |
| Production runtime | Local lab only |
| LangGraph / workflow engine | Framework drift |
| RAG / MCP / graph DB | FREEZE |
| Multi-agent swarm template | Safety not proven at scale |
| Code generator (default) | Requires explicit user approval per artifact |

---

## Recommended first agent template

### **Option A — Review Assistant Agent** (SELECTED)

| Criterion | Fit |
|-----------|-----|
| Text-only | Yes |
| Low external risk | Yes — no auto external send in base demo |
| Reuses review-loop | Direct lineage |
| Teaches critic ≠ truth | Core lesson |
| Easy evaluation | In smoke + trace examples |

**Why not B (Task Triage) first:** good second template; routing semantics add teaching load.  
**Why not C (Safe Content Draft):** higher publish risk narrative; better after Review Assistant mastered.

---

## v0.1 success criteria

1. A new team member can **fill** Review Assistant template from blanks using curriculum RU/EN.
2. Template lists **required gates** with trace event names.
3. Template acceptance uses evaluation checklist (manual smoke).
4. No new runtime module in repo without user approval.

---

## Phase 3.1+ (preview only — not committed)

- Task Triage template
- Safe Content Draft template
- Optional kit folder structure with generated stubs (user-approved)

See [PROTOTYPE_TO_FACTORY_GAP_ANALYSIS.md](PROTOTYPE_TO_FACTORY_GAP_ANALYSIS.md).
