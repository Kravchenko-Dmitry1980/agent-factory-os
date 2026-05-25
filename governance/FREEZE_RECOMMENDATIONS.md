# Freeze Recommendations — Before Phase 1.4

**Effective:** Phase 1.4 entry through Phase 1.4 exit  
**Authority:** Governance re-audit 2026-05-25

---

## Freeze (do not change without explicit user approval)

| Zone | Rule |
|------|------|
| Taxonomy `00–12` | No new sections; no renumbering |
| `13_gui-agents/` | **Forbidden** |
| New corpora | No new `Books/*` research imports |
| New experiments sandboxes | No new `experiments/*` without governance review |
| Promotion batch | **No Phase 1.4 promotions** — PROMOTE_LATER stays queued |
| `agent-os/` concept bodies | No rewrites of existing curated definitions |
| RAG / embeddings / vector DB | **Forbidden** |
| Ontology engine / graph DB | **Forbidden** |
| Runtime code | Hermes, MobileAgent, swarm stack, MCP servers |
| Digital twin system design | Replay, curator automation, adaptation-service |
| Swarm → agent-os copy | Verbatim or unscored promotion **forbidden** |

---

## Allow (Phase 1.4 permitted work)

| Activity | Location |
|----------|----------|
| Governance doctrine documents | `governance/` |
| Consolidation maps / family indexes | `governance/` |
| Non-destructive governance addenda | Existing governance MD (append sections) |
| Architecture principles synthesis | `governance/ARCHITECTURE_DOCTRINE.md` (new) |
| Lifecycle synthesis | `governance/OPERATIONAL_LIFECYCLE.md` (new) |
| System positioning | `governance/SYSTEM_POSITIONING.md` |
| Anti-pattern family map | `governance/ANTIPATTERN_FAMILIES.md` |
| Governance index / navigation | `governance/README.md` or index |
| Staleness refresh | Per GOVERNANCE_STALENESS_REPORT priorities |
| Diagrams (Mermaid) | `governance/diagrams/` |

---

## Require user approval before

| Action | Why |
|--------|-----|
| Any new **canonical principle** note in `agent-os/00–09/` | Changes curated layer |
| Any promotion from `Books/swarm-playbooks/` | Operational → canonical gate |
| Any migration research → curated | PROMOTION_STRATEGY pipeline |
| Edit `agent-os/10_research/sources.md` | Curated catalog policy |
| Architecture doctrine that **contradicts** PROMOTION_LOG entries | Canonical drift |
| Creating `13_gui-agents/` or new taxonomy section | Taxonomy explosion |
| Merging fail-closed-defaults + fail-closed-agent-loop into one file | Concept boundary change |
| Unfreezing PROMOTE_LATER batch (curator, kanban-orchestration, etc.) | Post-1.4 phase gate |

---

## Phase 1.4 Exit Criteria (suggested)

1. Doctrine documents exist and cross-link to clusters (no duplicate definitions).
2. SYSTEM_POSITIONING published in governance.
3. ANTIPATTERN_FAMILIES map covers all 10 curated anti-patterns.
4. swarm-playbooks registered in sources policy (if approved).
5. Stale P1 governance docs have addenda or successor references.
6. No freeze violations in git diff.

---

## Up

- [PHASE_1_4_READINESS.md](PHASE_1_4_READINESS.md)
- [CONSOLIDATION_CANDIDATES.md](CONSOLIDATION_CANDIDATES.md)
