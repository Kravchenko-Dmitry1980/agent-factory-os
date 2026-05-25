# System State After Phase 1.3

**Snapshot date:** 2026-05-25  
**Purpose:** Current repository inventory for governance and Phase 1.4 planning

---

## Layer File Counts (markdown)

| Layer | Path | MD files (approx.) |
|-------|------|-------------------:|
| Curated + catalog | `agent-os/` | **177** |
| Semantic graph | `agent-os/graph/` | **25** |
| Patterns | `agent-os/08_patterns/` | 12 (10 concepts + index) |
| Anti-patterns | `agent-os/09_antipatterns/` | 11 (10 concepts + index) |
| Glossary pointers | `agent-os/11_glossary/` | 13 |
| Diagrams | `agent-os/12_diagrams/` | 7 |
| Governance | `governance/` | **22** (+ 7 new from 1.3R = **29** after this audit) |
| Canonical source | `Books/claude/` | 18 |
| Harness source | `Books/agents/` | 6 chapters + pipeline artifacts |
| Brain OS research | `Books/brain-os/` | ~67 |
| Swarm operational | `Books/swarm-playbooks/` | **51** |
| Hermes sandbox | `experiments/hermes-agent-review/` | ~36 review MD (excl. upstream) |
| MobileAgent sandbox | `experiments/mobile-agent-review/` | ~39 review MD (excl. upstream) |

---

## Corpora Registry

| Corpus | Tier | In sources.md? | Curated promotions |
|--------|------|:--------------:|-------------------|
| `Books/claude/` | T0 Canonical source | ✅ | Via extraction |
| `Books/agents/` | T0 Canonical source | ✅ | Planned |
| `Books/brain-os/` | T1 Research | ✅ | 2 stripped patterns (writeback, memory-aware) |
| `experiments/hermes-agent-review/` | T1 Research sandbox | ✅ | 16 notes |
| `experiments/mobile-agent-review/` | T1 Research sandbox | ✅ | 6 notes |
| `Books/swarm-playbooks/` | **T1 Operational** | ❌ | **0** (by design) |

---

## Phase 1.2 Promoted Concepts (22)

### Memory (`02_memory/`)
- frozen-memory-snapshot, memory-char-limits, profile-isolation, memory-provider-boundaries

### Multi-agent (`04_multi-agent/`)
- kanban-vs-delegate, subagent-tool-restrictions, durable-task-coordination

### GUI (`01_agent-runtime/`, `00_foundations/`)
- gui-agent-loop, visual-grounding, visual-verification

### Patterns (`08_patterns/`)
- progressive-skill-disclosure, memory-aware-execution, verification-before-writeback, fail-closed-agent-loop

### Anti-patterns (`09_antipatterns/`)
- unverified-gui-clicks, brittle-gui-automation, mid-session-memory-injection, unbounded-memory-growth, recursive-self-improvement

### Diagrams (`12_diagrams/`)
- gui-agent-loop, memory-governance, promotion-pipeline

---

## Graph Layer Structure

```
agent-os/graph/
├── README.md
├── concept-clusters.md
├── semantic-linking-rules.md
├── provenance-graph.md
├── canonical-vs-research-map.md
├── future-rag-readiness.md
├── cluster-indexes/     (5)
├── concept-maps/        (5)
├── navigation/          (2)
└── diagrams/            (7)
```

---

## Semantic Clusters

| ID | Hub |
|----|-----|
| verification | `graph/cluster-indexes/verification-cluster.md` |
| memory-governance | `graph/cluster-indexes/memory-governance-cluster.md` |
| orchestration | `graph/cluster-indexes/orchestration-cluster.md` |
| gui-modality | `graph/cluster-indexes/gui-modality-cluster.md` |
| promotion-governance | `graph/cluster-indexes/promotion-governance-cluster.md` |

---

## Pre-existing Curated Spine (Claude-derived)

- **Foundations:** harness, query loop, verification, golden path
- **Runtime:** tool-runtime, concurrency, error recovery, terminal states
- **Harness:** permissions, hooks, execution feedback/verification
- **Multi-agent:** subagents, swarms, coordination, task SM
- **MCP:** protocol, transports, orchestration (partial)
- **Digital twins:** 6 thin notes (identity, personas, skill-graphs)
- **Patterns:** 6 Claude patterns + 4 Phase 1.2
- **Anti-patterns:** 5 Claude + 5 Phase 1.2

---

## Research-Only (must not traverse as canonical)

- Brain OS planes, adaptation-service, trace-first (uncurated), human-escalation-gate (uncurated)
- Hermes gateway, provider matrix, Honcho
- MobileAgent OCR, weights, ADB scripts
- Swarm «8-agent default topology», critic-as-verification, tutorial stack

---

## Governance Documents (key)

| Doc | Role |
|-----|------|
| PROMOTION_REVIEW.md | Phase 1.1 scored candidates |
| PROMOTION_LOG.md | Phase 1.2 audit trail |
| PROMOTION_STRATEGY.md | Pipeline policy |
| SEMANTIC_LINKING_AUDIT.md | Phase 1.3 link audit |
| SEMANTIC_DRIFT_ANALYSIS.md | Phase 1.3 drift |
| REAUDIT_2026_05_25.md | This re-audit |
| PHASE_1_4_READINESS.md | Go/no-go |

---

## Recommended Entry Points

| Audience | Start |
|----------|-------|
| New architect | `agent-os/README.md` → `00_foundations/golden-path.md` |
| Cluster traversal | `agent-os/graph/navigation/cluster-navigation.md` |
| Promotion audit | `governance/PROMOTION_LOG.md` → `agent-os/graph/provenance-graph.md` |
| Operational patterns (non-canonical) | `Books/swarm-playbooks/README.md` |
| Governance reviewer | `governance/REAUDIT_2026_05_25.md` |
| Phase 1.4 planner | `governance/CONSOLIDATION_CANDIDATES.md` |

---

## Up

- [REAUDIT_2026_05_25.md](REAUDIT_2026_05_25.md)
- [agent-os/graph/README.md](../agent-os/graph/README.md)
