# Anti-pattern Family Review

**Phase:** 1.4  
**Scope:** Family completeness, overlap, missing mitigations, weak adjacency

---

## Family Completeness

| Required family | Covered | Curated AP members |
|-----------------|---------|-------------------|
| Verification failures | ✓ | unverified-gui-clicks, infinite-retry-loops (partial) |
| Memory failures | ✓ | 4 memory APs |
| Governance failures | ✓ | doctrine-level + ops inverse |
| Orchestration failures | ✓ | god-object, recursive-self-improvement, infinite-retry |
| GUI failures | ✓ | brittle-gui, unverified-clicks |
| Tutorial-driven failures | ✓ | ops inverse only (no curated AP file — acceptable) |
| Autonomy failures | ✓ | recursive-self-improvement + ops inverse |
| Taxonomy failures | ✓ | governance-level |

**Completeness: PASS** — all 8 required families present.

---

## Overlap Analysis

| Overlap | Assessment |
|---------|------------|
| infinite-retry-loops in Verification + Orchestration | **Acceptable** — retry spans both verify bypass and orchestration budget |
| recursive-self-improvement in Orchestration + Autonomy | **Acceptable** — autonomy is root cause lens |
| cache-busting in Memory | **Correct** — single primary family |
| critic-as-fake-verify (ops) vs unverified-gui | **Distinct** — LLM vs GUI modality |

No family merge required.

---

## Missing Mitigations

| Family | Gap | Severity |
|--------|-----|----------|
| Tutorial-driven | No curated AP file | Low — ops corpus covers; consider PROMOTE_LATER AP if repeated |
| Governance failures | No atomic AP in 09/ | Low — promotion skip is process failure; documented in doctrine |
| Taxonomy failures | No atomic AP | Low — prevented by governance rules |

**No P0 mitigation gap** — all curated APs have linked patterns in source files.

---

## Weak Adjacency

| AP | Adjacency strength |
|----|-------------------|
| scattered-permission-sync | Linked in fail-closed doctrine; not in family table | Minor — add to Governance family in future index pass (not 1.4 body rewrite) |
| central-orchestrator-god-object | Strong — self-describing-tools inverse |
| memory-as-crutch | Strong — memory-aware-execution |

---

## Swarm Operational APs

8 swarm anti-patterns mapped as **inverse lessons** only — not curated. Correct per freeze.

NEVER PROMOTE list honored in families doc.

---

## Verdict

**PASS** — families complete, overlaps manageable, mitigations present for all curated members.

---

## Up

- [anti-pattern-families.md](../agent-os/doctrine/anti-pattern-families.md)
- [PHASE_1_4_CONSOLIDATION_REPORT.md](PHASE_1_4_CONSOLIDATION_REPORT.md)
