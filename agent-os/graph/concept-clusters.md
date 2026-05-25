# Concept Clusters

Canonical semantic clusters for Agent-OS curated layer. Clusters cross-cut taxonomy folders (`00–12`); they do not replace section numbering.

---

## 1. Verification Cluster

**Theme:** Trust before termination and before durable writeback.

| Node | Layer | Path |
|------|-------|------|
| [[visual-verification]] | curated | `00_foundations/` |
| [[verification-before-writeback]] | curated | `08_patterns/` |
| [[fail-closed-agent-loop]] | curated | `08_patterns/` |
| [[verification]] | curated | `00_foundations/` |
| [[execution-feedback]] | curated | `03_harness-engineering/` |
| [[execution-verification]] | curated | `03_harness-engineering/` |
| trace-first-architecture | **research** | `Books/brain-os/patterns/` — not curated |
| human-escalation-gate | **research** | `Books/brain-os/patterns/` — not curated |

**Index:** [verification-cluster](cluster-indexes/verification-cluster.md)  
**Map:** [verification-map](concept-maps/verification-map.md)

---

## 2. Memory Governance Cluster

**Theme:** Bounded, scoped, injection-safe memory.

| Node | Layer | Path |
|------|-------|------|
| [[frozen-memory-snapshot]] | curated | `02_memory/` |
| [[memory-char-limits]] | curated | `02_memory/` |
| [[profile-isolation]] | curated | `02_memory/` |
| [[memory-provider-boundaries]] | curated | `02_memory/` |
| [[memory-aware-execution]] | curated | `08_patterns/` |
| [[unbounded-memory-growth]] | curated | `09_antipatterns/` |
| [[mid-session-memory-injection]] | curated | `09_antipatterns/` |
| [[memory-taxonomy]] | curated | `02_memory/` |
| [[prompt-cache-as-constraint]] | curated | `08_patterns/` |

**Index:** [memory-governance-cluster](cluster-indexes/memory-governance-cluster.md)  
**Map:** [memory-governance-map](concept-maps/memory-governance-map.md)

---

## 3. Orchestration Cluster

**Theme:** Multi-agent primitive choice, durable coordination, delegation safety.

| Node | Layer | Path |
|------|-------|------|
| [[kanban-vs-delegate]] | curated | `04_multi-agent/` |
| [[durable-task-coordination]] | curated | `04_multi-agent/` |
| [[subagent-tool-restrictions]] | curated | `04_multi-agent/` |
| [[subagents]] | curated | `04_multi-agent/` |
| [[fail-closed-agent-loop]] | curated | `08_patterns/` |
| [[task-state-machine]] | curated | `04_multi-agent/` |
| [[infinite-retry-loops]] | curated | `09_antipatterns/` |
| human-escalation-gate | **research** | `Books/brain-os/patterns/` — escalation adjacency |

**Index:** [orchestration-cluster](cluster-indexes/orchestration-cluster.md)  
**Map:** [orchestration-map](concept-maps/orchestration-map.md)

---

## 4. GUI Modality Cluster

**Theme:** Embodied observe–act–verify loop (modality extension, not separate taxonomy).

| Node | Layer | Path |
|------|-------|------|
| [[gui-agent-loop]] | curated | `01_agent-runtime/` |
| [[visual-grounding]] | curated | `01_agent-runtime/` |
| [[visual-verification]] | curated | `00_foundations/` |
| [[unverified-gui-clicks]] | curated | `09_antipatterns/` |
| [[brittle-gui-automation]] | curated | `09_antipatterns/` |
| [[query-loop]] | curated | `01_agent-runtime/` — code golden path parallel |

**Index:** [gui-modality-cluster](cluster-indexes/gui-modality-cluster.md)  
**Map:** [gui-modality-map](concept-maps/gui-modality-map.md)

---

## 5. Promotion Governance Cluster

**Theme:** Research → curated discipline and audit trail.

| Node | Layer | Path |
|------|-------|------|
| promotion-pipeline | curated diagram | `12_diagrams/promotion-pipeline.md` |
| [provenance-graph](provenance-graph.md) | graph layer | `graph/` |
| [canonical-vs-research-map](canonical-vs-research-map.md) | graph layer | `graph/` |
| [semantic-linking-rules](semantic-linking-rules.md) | graph layer | `graph/` |
| `PROMOTION_REVIEW.md` | governance | repo root |
| `governance/PROMOTION_LOG.md` | governance | `governance/` |
| `governance/PROMOTION_STRATEGY.md` | governance | `governance/` |
| Anti-pattern governance | curated | `09_antipatterns/` + fix patterns in `08_patterns/` |

**Index:** [promotion-governance-cluster](cluster-indexes/promotion-governance-cluster.md)  
**Map:** [promotion-governance-map](concept-maps/promotion-governance-map.md)

---

## Cross-Cluster Bridges

| Bridge | Clusters connected |
|--------|-------------------|
| [[fail-closed-agent-loop]] | verification ↔ orchestration |
| [[verification-before-writeback]] | verification ↔ memory-governance |
| [[visual-verification]] | verification ↔ gui-modality |
| [[memory-aware-execution]] | memory-governance ↔ orchestration (routing) |

## Up

- [graph/README.md](README.md)
- [semantic-linking-rules.md](semantic-linking-rules.md)
