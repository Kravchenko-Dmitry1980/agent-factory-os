# Doctrine Map

Relationships between principles, lifecycle, anti-patterns, governance, graph layer, and operational reference tier.

```mermaid
flowchart TB
    subgraph doctrine [Doctrine Layer Phase 1.4]
        SP[system-positioning]
        AW[architecture-worldview]
        CP[canonical-principles]
        OL[operational-lifecycle]
        VF[verification-first]
        GA[governance-before-autonomy]
        BM[bounded-memory]
        FC[fail-closed-execution]
        PF[provenance-first]
        APF[anti-pattern-families]
        EP[execution-philosophy]
    end

    subgraph curated [Curated 00-09]
        P08[08_patterns]
        P09[09_antipatterns]
        P02[02_memory]
        P01[01_agent-runtime]
        P04[04_multi-agent]
    end

    subgraph graph [Graph Layer 1.3]
        CL[concept-clusters]
        PV[provenance-graph]
        CVR[canonical-vs-research-map]
    end

    subgraph gov [Governance]
        PS[PROMOTION_STRATEGY]
        PL[PROMOTION_LOG]
        CD[CANONICAL_DIRECTION]
    end

    subgraph ops [Operational Reference]
        SW[Books/swarm-playbooks]
    end

    SP --> CP
    AW --> CP
    CP --> VF
    CP --> GA
    CP --> BM
    CP --> FC
    CP --> PF
    VF --> FC
    VF --> BM
    GA --> OL
    VF --> OL
    OL --> APF
    EP --> OL

    CP --> P08
    CP --> P09
    VF --> P01
    BM --> P02
    GA --> P04
    APF --> P09

    PF --> PV
    PF --> CVR
    PF --> PS
    PS --> PL
    CD --> SP

    CL --> curated
    OL -. reference .-> SW
    SW -. non-canonical .-> PF

    style SW fill:#fef3c7
    style doctrine fill:#dbeafe
    style gov fill:#dcfce7
```

---

## Principle → Lifecycle Stage

| Principle | Primary lifecycle stages |
|-----------|-------------------------|
| Verification-first | execution, verification, writeback |
| Governance-before-autonomy | routing, planning, approval |
| Fail-closed | execution, verification |
| Bounded memory | writeback |
| Provenance-first | goal (source selection), promotion (meta) |
| Human escalation | review, escalation, approval |
| Modality-unified | execution |
| Research isolation | goal, routing |

---

## Principle → Cluster

| Principle | Semantic cluster |
|-----------|------------------|
| Verification-first | verification |
| Bounded memory | memory-governance |
| Governance-before-autonomy | orchestration + promotion-governance |
| Modality-unified | gui-modality + agent-runtime |

Indexes: [cluster-navigation](../graph/navigation/cluster-navigation.md)

---

## Anti-pattern Family → Principle

| Family | Principles violated |
|--------|---------------------|
| Verification failures | Verification-first, Fail-closed |
| Memory failures | Bounded memory, Verification-first |
| Governance failures | Provenance-first, Promotion discipline |
| Orchestration failures | Governance-before-autonomy |
| Autonomy failures | Governance-before-autonomy |
| Taxonomy failures | Research isolation, Anti-pattern adjacency |

---

## Layer Boundaries

| From | To | Allowed |
|------|-----|---------|
| doctrine | curated | wikilink + synthesis |
| doctrine | governance | path reference |
| doctrine | swarm-playbooks | path reference only |
| curated | research | path + (research) label |
| swarm | curated | **forbidden** without promotion |

---

## Sources

- [doctrine/README.md](README.md)
- [graph/concept-clusters.md](../graph/concept-clusters.md)
- [governance/CONSOLIDATION_CANDIDATES.md](../../governance/CONSOLIDATION_CANDIDATES.md)
