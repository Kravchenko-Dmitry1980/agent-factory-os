# Semantic Linking Audit

**Phase:** 1.3  
**Date:** 2026-05-25  
**Scope:** `agent-os/` curated layer post Phase 1.2

---

## Executive Summary

Phase 1.2 added 22 promoted notes with partial wikilinks and inconsistent section structure. Taxonomy indexes list files but **semantic clusters did not exist**. Glossary covers 4 terms only. ~85 pre-existing Claude notes lack cluster tags. **No orphan promoted notes** after index updates; **weak backlinks** on cluster hub concepts (`verification`, `execution-feedback`).

---

## Isolated Notes (pre–Phase 1.3)

| Note | Issue | Remediation |
|------|-------|-------------|
| Phase 1.2 promotions | Related sections non-standard | Phase 1.3 standardized footer |
| `execution-verification.md` | No link to `visual-verification` | Add cluster links |
| `07_projects/*` | No cluster membership | OK — applied layer, out of scope |
| `10_research/chapters/*` | Stubs only | OK — catalog not concepts |
| Brain OS patterns | Outside agent-os | canonical-vs-research-map |

---

## Weakly Linked Notes

| Note | Missing backlinks from |
|------|------------------------|
| [[visual-verification]] | `execution-feedback`, `execution-verification` (fixed Phase 1.3) |
| [[fail-closed-agent-loop]] | `execution-verification`, `terminal-states` |
| [[memory-aware-execution]] | `memory-recall`, `memory-compaction` |
| [[durable-task-coordination]] | `coordination`, `swarms` |
| [[progressive-skill-disclosure]] | `skill-graphs`, ch12 stub |

---

## Duplicated Semantic Zones

| Zone | Locations | Resolution |
|------|-----------|------------|
| Fail-closed | `fail-closed-defaults` vs `fail-closed-agent-loop` | Explicit cross-ref; different layers |
| Verification | `verification`, `execution-verification`, `visual-verification` | Verification cluster map |
| Profile identity | `profile-isolation` vs `persistent-identity` | Cross-ref; memory vs session ID |
| Memory bounds | `memory-char-limits` vs `memory-taxonomy` | Cluster adjacency |
| Provider rule | `memory-provider-boundaries` (merged one-provider) | Single canonical node |

---

## Orphan Concepts (promoted set)

**None** — all 22 Phase 1.2 files appear in section indexes.

**Latent orphans (cluster-required, not curated):**

- trace-first-architecture — research only
- human-escalation-gate — research only

---

## Weak Provenance

| Issue | Count | Fix |
|-------|------:|-----|
| Promoted notes missing Governance References section | 22 | Standardized footer Phase 1.3 |
| Pre-Claude notes lack promotion metadata | ~63 | OK — frozen canonical |
| Brain OS links without `(stripped)` note | 2 patterns | semantic-linking-rules |

---

## Missing Backlinks (sample)

| From | To (missing return link) |
|------|--------------------------|
| `gui-agent-loop` | `query-loop` |
| `verification-before-writeback` | `episodic-memory` |
| `subagent-tool-restrictions` | `permission-modes` |

Phase 1.3 adds bidirectional links where semantically valid (not spam).

---

## Anti-Pattern Gaps (pre–Phase 1.3)

| Promoted anti-pattern | Fix pattern linked? |
|-----------------------|---------------------|
| unverified-gui-clicks | visual-verification ✅ |
| mid-session-memory-injection | frozen-memory-snapshot ✅ |
| unbounded-memory-growth | memory-char-limits ✅ |
| recursive-self-improvement | subagent-tool-restrictions ✅ |
| brittle-gui-automation | visual-grounding ✅ |

**Not yet promoted (PROMOTION_REVIEW backlog):** wrong-orchestration-primitive, multiple-memory-providers, subagent-memory-writes — gap remains by design.

---

## Disconnected Clusters (pre–Phase 1.3)

- GUI modality notes not linked from `golden-path.md`
- Memory governance not linked from `06_digital-twins/index.md`
- Promotion pipeline diagram isolated from graph layer

**Fixed:** `agent-os/graph/` layer + cluster indexes.

---

## Recommendations Applied in Phase 1.3

1. Create `agent-os/graph/` navigation layer
2. Standardize promoted note footers (6 sections)
3. Harden glossary with pointers to promoted concepts
4. Add cluster visibility to section indexes
5. Document research adjacency without false canonical wikilinks

---

## Up

- [SEMANTIC_DRIFT_ANALYSIS.md](SEMANTIC_DRIFT_ANALYSIS.md)
- [KNOWLEDGE_GRAPH_DIRECTION.md](KNOWLEDGE_GRAPH_DIRECTION.md)
- [agent-os/graph/semantic-linking-rules.md](../agent-os/graph/semantic-linking-rules.md)
