# Repository Evolution Map

**Дата:** 2026-05-25  
**Purpose:** Narrative map of how AGENT repository evolved and where it is heading

---

## Timeline

| Period | State | Key artifacts |
|--------|-------|---------------|
| **Genesis** | Claude book → Agent-OS skeleton | `Books/claude/`, `agent-os/00–12`, template |
| **Phase 0.1** | Git + dual source policy | `.gitignore`, `sources.md`, `BASELINE_STATUS.md`, Harness PDF pipeline |
| **Phase 0 audit** | Inventory frozen | `CURRENT_STATE_AUDIT.md` |
| **Research expansion** | Isolated sandboxes | `experiments/hermes-agent-review/`, `experiments/mobile-agent-review/` |
| **Promotion analysis** | Scored candidates | `PROMOTION_REVIEW.md` (65 items) |
| **Third corpus** | Author draft KB | `Books/brain-os/` (67 MD, not canonical) |
| **Governance audit** | This folder | `governance/*` |
| **Next** | Curated promotion gate | Phase 1.2 pending user approval |

---

## Layer Evolution

```
Phase 1          Phase 1.1         Phase 1.2 (planned)
────────         ─────────         ───────────────────
Books/claude     experiments/      agent-os/00-09
Books/agents     PROMOTION_REVIEW  (PROMOTE_NOW only)
agent-os/        Books/brain-os/   sources.md research tier
(partial)        governance/       Harness catalog stubs
```

---

## Corpus Evolution

| Corpus | Introduced | Role evolution |
|--------|------------|----------------|
| Claude | Day 0 | Primary canonical — **unchanged** |
| Harness | Phase 0.1 | Secondary canonical — **catalog incomplete** |
| Hermes | Experiments | Memory/orchestration research — **stable** |
| MobileAgent | Experiments | GUI modality research — **stable** |
| Brain OS | Post-1.1 | Control-plane draft — **isolated correctly** |

---

## Agent-OS Maturity Evolution

| Dimension | Then (audit 2026-05-21) | Now |
|-----------|-------------------------|-----|
| Atomic notes | ~85 partial | ~85 (unchanged curated) |
| Antipatterns | 5 | 5 |
| Patterns | 7 | 7 |
| Research stubs | 18 Claude | 18 Claude |
| GUI coverage | 0 | 0 curated (sandbox only) |
| Governance docs | 2 root | 2 root + governance/ |

**Curated layer intentionally frozen** during research — correct discipline.

---

## Identity Evolution (project direction)

| Direction | Evidence | Verdict |
|-----------|----------|---------|
| Architecture OS | agent-os taxonomy, patterns | **Primary** |
| Research library | Books/, experiments/ | **Strong secondary** |
| Agent framework | No runtime code | **Not current** |
| Digital twin platform | 06 section + research | **Aspirational** |
| Ontology system | Implicit only | **Future** |
| Cognitive runtime | Brain OS doc tone | **Rejected as repo goal** |
| Chaos | Multi-corpus | **Avoided** if governance enforced |

---

## File Count Reference (approx.)

| Area | MD files |
|------|----------|
| agent-os | 122 |
| Books/claude | 18 |
| Books/agents | 12 |
| Books/brain-os | 67 |
| experiments/hermes (review docs only) | ~36 (+ upstream clone) |
| experiments/mobile (review docs only) | ~36 (+ upstream clone) |
| governance | 12 + 7 diagrams |

---

## Evolution Diagram

See [diagrams/repository-evolution.md](diagrams/repository-evolution.md)

## Corpus Diagram

See [diagrams/corpus-relationships.md](diagrams/corpus-relationships.md)

## Future Direction

See [diagrams/future-architecture-direction.md](diagrams/future-architecture-direction.md)

---

## Up

- [FULL_SYSTEM_AUDIT.md](FULL_SYSTEM_AUDIT.md)
- [NEXT_PHASE_ROADMAP.md](NEXT_PHASE_ROADMAP.md)
