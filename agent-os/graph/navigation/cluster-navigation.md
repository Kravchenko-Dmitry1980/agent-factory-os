# Cluster Navigation

Entry point for semantic traversal by architecture cluster (Phase 1.3).

---

## Clusters

| Cluster | Start here | Golden path |
|---------|------------|-------------|
| **Verification** | [verification-cluster](../cluster-indexes/verification-cluster.md) | [[verification]] → [[visual-verification]] → [[fail-closed-agent-loop]] |
| **Memory governance** | [memory-governance-cluster](../cluster-indexes/memory-governance-cluster.md) | [[memory-taxonomy]] → [[frozen-memory-snapshot]] → [[memory-char-limits]] |
| **Orchestration** | [orchestration-cluster](../cluster-indexes/orchestration-cluster.md) | [[subagents]] → [[kanban-vs-delegate]] → [[durable-task-coordination]] |
| **GUI modality** | [gui-modality-cluster](../cluster-indexes/gui-modality-cluster.md) | [[query-loop]] ∥ [[gui-agent-loop]] → [[visual-verification]] |
| **Promotion governance** | [promotion-governance-cluster](../cluster-indexes/promotion-governance-cluster.md) | [provenance-graph](../provenance-graph.md) → [canonical-vs-research-map](../canonical-vs-research-map.md) |

---

## Cross-cluster bridges

1. [[verification-before-writeback]] — verification × memory-governance
2. [[fail-closed-agent-loop]] — verification × orchestration
3. [[memory-aware-execution]] — memory-governance × orchestration routing

---

## By failure mode

| Symptom | Start |
|---------|-------|
| Agent declares done too early | [[fail-closed-agent-loop]] |
| Memory bloat / cache cost | [memory-governance cluster](../cluster-indexes/memory-governance-cluster.md) |
| Wrong multi-agent primitive | [[kanban-vs-delegate]] |
| GUI clicks don't stick | [[unverified-gui-clicks]] |
| Research leaked into prod docs | [canonical-vs-research-map](../canonical-vs-research-map.md) |

---

## Up

- [graph/README.md](../README.md)
- [semantic-traversal.md](semantic-traversal.md)
