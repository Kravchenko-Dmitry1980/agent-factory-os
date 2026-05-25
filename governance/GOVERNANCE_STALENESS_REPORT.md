# Governance Staleness Report

**Date:** 2026-05-25  
**Compare baseline:** Pre–Phase 1.2 governance audit (2026-05-25 morning) vs repository after Phase 1.2, 1.3, SWARM-EXTRACTION

---

| File | Still valid? | Stale parts | Required update | Priority |
|------|--------------|-------------|-----------------|----------|
| [FULL_SYSTEM_AUDIT.md](FULL_SYSTEM_AUDIT.md) | **Partial** | File counts (~122 agent-os); antipattern count (5); no graph layer; no swarm corpus; GUI gap statement | Addendum section «Post 1.3» or pointer to REAUDIT | P2 |
| [ARCHITECTURE_HEALTH_REPORT.md](ARCHITECTURE_HEALTH_REPORT.md) | **Partial** | All domain scores pre-1.2; GUI 3/10; antipattern 5/10; promotion «not executed» | Re-score table from REAUDIT §3 or replace with delta | **P1** |
| [TAXONOMY_REVIEW.md](TAXONOMY_REVIEW.md) | **Partial** | 02_memory «no char limits»; 09 «5 entries»; 12 «3 diagrams»; 11 «5 stubs» | Update section load table counts | P2 |
| [CANONICAL_DIRECTION.md](CANONICAL_DIRECTION.md) | **Partial** | «~85 notes»; Phase 1.2 listed as future; GUI «modality not canonical»; Phase 1.3 = PROMOTE_LATER | Mark 1.2 complete; GUI partial canonical; 1.3 = graph | **P1** |
| [NEXT_PHASE_ROADMAP.md](NEXT_PHASE_ROADMAP.md) | **Stale** | Entire phase sequence wrong for 1.3/1.4; «1.2 requires approval»; 1.4 = link linter | Rewrite phases 1.4+ or add PHASE_1_4_READINESS as authority | **P1** |
| [RISK_REGISTER.md](RISK_REGISTER.md) | **Partial** | R7 sources stale (fixed); R18 antipattern (fixed); R20 wikilinks (partial fix); no swarm risks | Use UPDATED_RISK_REGISTER_DELTA; add NR1–NR6 | P2 |
| [KNOWLEDGE_GRAPH_DIRECTION.md](KNOWLEDGE_GRAPH_DIRECTION.md) | **Mostly valid** | Phase 1.3 marked complete ✅ | Minor: add swarm as operational corpus input | P3 |
| [PROMOTION_STRATEGY.md](PROMOTION_STRATEGY.md) | **Valid** | Batch 1 executed; log pointer exists | Add «Batch 1 complete»; freeze Batch 2 until 1.4 gate | P3 |
| [PHASE_ALIGNMENT_REVIEW.md](PHASE_ALIGNMENT_REVIEW.md) | **Stale** | Pre-1.2 alignment | Add 1.3R alignment note | P2 |
| [GOVERNANCE_GAPS.md](GOVERNANCE_GAPS.md) | **Partial** | G1 partially closed; G8 antipattern improved; G10 graph standards now exist; G20 link linter open | Mark G1/G8/G10 progress; add G21 swarm registry | P2 |
| [ARCHITECTURAL_DRIFT_REPORT.md](ARCHITECTURAL_DRIFT_REPORT.md) | **Partial** | No swarm; no graph layer assessment | Add drift vectors: operational corpus, doctrine gap | P3 |
| [REPOSITORY_EVOLUTION_MAP.md](REPOSITORY_EVOLUTION_MAP.md) | **Stale** | Ends before 1.2/1.3/swarm | Extend timeline | P2 |
| [PROMOTION_LOG.md](PROMOTION_LOG.md) | **Current** | — | None until next promotion batch | — |
| [SEMANTIC_LINKING_AUDIT.md](SEMANTIC_LINKING_AUDIT.md) | **Current** | Pre-1.3R only | Refresh after 1.4 if doctrine adds links | P3 |
| [SEMANTIC_DRIFT_ANALYSIS.md](SEMANTIC_DRIFT_ANALYSIS.md) | **Current** | — | Monitor Phase 1.4 doctrine inflation | P3 |
| [CURRENT_STATE_AUDIT.md](../CURRENT_STATE_AUDIT.md) (root) | **Stale** | 2026-05-21; 153 MD; no git commits narrative may differ | Superseded by SYSTEM_STATE_AFTER_1_3 for navigation | P2 |
| [PROMOTION_REVIEW.md](../PROMOTION_REVIEW.md) | **Valid as snapshot** | Phase 1.1 only; PROMOTE_LATER not executed | Keep immutable; new reviews for swarm | P3 |
| `agent-os/10_research/sources.md` | **Partial** | Missing `Books/swarm-playbooks/` tier | Add operational corpus section | **P1** |

---

## Summary

| Category | Count |
|----------|------:|
| Current | 3 |
| Mostly valid | 2 |
| Partially stale | 10 |
| Stale | 3 |

**Highest priority updates (before/during Phase 1.4):**

1. `NEXT_PHASE_ROADMAP.md` — phase definition alignment  
2. `CANONICAL_DIRECTION.md` — canonical inventory counts  
3. `ARCHITECTURE_HEALTH_REPORT.md` — re-scores  
4. `agent-os/10_research/sources.md` — swarm-playbooks tier (**requires user approval** for agent-os edit)

---

## Up

- [REAUDIT_2026_05_25.md](REAUDIT_2026_05_25.md)
- [UPDATED_RISK_REGISTER_DELTA.md](UPDATED_RISK_REGISTER_DELTA.md)
