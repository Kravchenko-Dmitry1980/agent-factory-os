# Provenance-first Doctrine

Lineage is architecture for a **multi-corpus** repository.

---

## Core Thesis

When sources multiply — Claude harness, agent surveys, Brain OS, experiments, operational playbooks — **without provenance discipline**, curated truth decays: hype patterns become canonical, duplicate definitions proliferate, and research wikilinks masquerade as production guidance.

Provenance-first means: every curated claim knows its **tier, promotion path, and trust boundary**.

---

## Consolidated Provenance Model

### Source lineage

| Tier | Paths | Rule |
|------|-------|------|
| T0 Frozen | `Books/claude/`, `Books/agents/` PDF | Cite; do not mutate |
| T1 Research | `Books/brain-os/`, `experiments/`, `Books/swarm-playbooks/` | Score before promote; path reference in doctrine |
| T2 Curated | `agent-os/00–09/` | Primary wikilink targets |
| T3 Catalog | `agent-os/10_research/` | Links and extraction plans only |

From [governance/GOVERNANCE_GAPS.md](../../governance/GOVERNANCE_GAPS.md).

### Promotion lineage

```
Research → Extraction → Scoring → Review → Governance → Curated → Validation
```

Logged in [PROMOTION_LOG.md](../../governance/PROMOTION_LOG.md). **No stage skipping.**

### Provenance graph

[provenance-graph](../graph/provenance-graph.md) — docs-layer navigation of promotion decisions and source adjacency. **Not** a graph database product.

### Canonical vs research

[canonical-vs-research-map](../graph/canonical-vs-research-map.md):

- Prefer canonical wikilinks
- Research → plain path + `(research)` label
- Rejected → drift docs only, no wikilink

---

## Source Trustworthiness & Conflict Resolution

Priority on conflict ([governance/PROMOTION_STRATEGY.md](../../governance/PROMOTION_STRATEGY.md)):

1. `Books/claude/` — wins harness/runtime
2. `Books/agents/` — survey framing
3. `experiments/hermes-agent-review/` — memory, orchestration
4. `experiments/mobile-agent-review/` — GUI modality
5. `Books/brain-os/` — control-plane **ideas** only; strip plane branding

Swarm-playbooks: operational reference; `canonical_status: non-canonical`.

---

## Why Provenance Matters

1. **Prevents false production readiness** — research ideas look implemented when linked incorrectly.
2. **Enables audit** — who promoted what, when, under which score.
3. **Contains drift** — NR2/NR3 Phase 1.4 risks (swarm leakage, 8-agent topology).
4. **Supports future RAG** — atomic notes + lineage without building RAG in Phase 1.4 ([future-rag-readiness](../graph/future-rag-readiness.md) — readiness only).

---

## Why Hype Repos Are Dangerous

Repositories optimized for engagement often ship:

- personality-centric multi-agent topology as default
- critic-as-verification claims
- tutorial stacks as “architecture”
- missing contracts, trace, idempotency

Agent-OS **isolates** these in research/operational tiers. Doctrine cites; does not elevate.

---

## Why Source Separation Matters

- `experiments/` outside taxonomy — maintain isolation
- Brain OS JSON contracts — normalize before any curated import
- Silent merge from comparison tables → **forbidden** ([governance/ARCHITECTURAL_DRIFT_REPORT.md](../../governance/ARCHITECTURAL_DRIFT_REPORT.md))

---

## Sources

- `agent-os/graph/provenance-graph.md`
- `agent-os/graph/canonical-vs-research-map.md`
- `governance/PROMOTION_STRATEGY.md`
- `governance/CANONICAL_DIRECTION.md`
- `Books/swarm-playbooks/governance/corpus-positioning.md`

See also: [diagrams/provenance-lineage.md](diagrams/provenance-lineage.md)
