# Phase Alignment Review

**Дата:** 2026-05-25  
**Method:** Compare planned phases vs repository evidence

---

## Phase 0 — Git Baseline + Source Policy

| Planned | Status | Evidence |
|---------|--------|----------|
| `git init` | ✅ Done | Repo exists |
| `.gitignore` | ✅ Done | Phase 0.1 |
| `sources.md` two corpora | ✅ Done | Claude + Harness |
| Root README update | ✅ Done | |
| Initial commit | ⚠️ **Partial** | BASELINE_STATUS said none; git log now shows commits (e.g. Hermes/MobileAgent research) |
| Freeze Claude source | ✅ Policy documented | |

**Correct:** source policy, gitignore  
**Missing:** full baseline snapshot commit at Phase 0 boundary; corpora policy not updated for brain-os/experiments  
**Premature:** none  
**Should have happened earlier:** initial commit after agent-os skeleton stable

---

## Phase 1 — Knowledge OS Bootstrap

| Planned | Status | Evidence |
|---------|--------|----------|
| Initial commit baseline | ⚠️ Partial | Commits exist but not framed as Phase 1 deliverable |
| Harness catalog stubs in 10_research | ❌ Not done | 6 chapter stubs missing |
| PDF QA Harness | ❌ Pending | conversion_report Next Steps |
| Continue extraction ch9,12–14,16–18 | ❌ Not done | extraction-plan ⬜ |
| No taxonomy reorg | ✅ Respected | |

**Correct:** extraction partial from Claude; template + indexes  
**Missing:** Harness integration path; extraction wave 1  
**Premature:** experiments + brain-os before Harness catalog — **acceptable** if isolated (they were)  
**Should NOT happen yet:** auto-promotion from experiments (correctly deferred)

---

## Phase 1.1 — Promotion Review (Experiments)

| Planned | Status | Evidence |
|---------|--------|----------|
| Read hermes + mobile sandboxes | ✅ | 36+36 review MD each |
| Score 65 candidates | ✅ | PROMOTION_REVIEW.md |
| No agent-os changes | ✅ | |
| PROMOTION_REVIEW.md deliverable | ✅ | Root file |
| Recommend 13_gui-agents LATER | ✅ | |

**Correct:** entire phase executed per boundaries  
**Missing:** governance/ folder (addressed by this audit)  
**Premature:** none in 1.1

---

## Brain OS Ingestion (parallel track)

| Planned (implicit) | Status | Evidence |
|--------------------|--------|----------|
| Books/brain-os/ only | ✅ | 67 MD, source docx |
| No agent-os promotion | ✅ | |
| Critical review | ✅ | review/ folder |
| sources.md entry | ❌ Not done | Policy gap |

**Correct:** isolation, maturity labels, promotion-candidates as recommendations only  
**Premature:** would be promoting Brain OS planes as canonical — **avoided**  
**Missing:** register in governance corpora inventory (this audit)

---

## Phase Alignment Summary

| Phase | Alignment | Grade |
|-------|-----------|-------|
| 0 | Good policy, weak git milestone | B |
| 1 | Incomplete bootstrap | C+ |
| 1.1 | Strong | A |
| Brain OS | Strong isolation | A- |

---

## What Should Have Happened Earlier

1. Initial git commit at end of Phase 0
2. Harness `10_research/` stubs before third corpus
3. `sources.md` extended with **research corpus registry** (experiments, brain-os)
4. `extraction_status` on atomic notes

## What Should NOT Happen Yet

1. `13_gui-agents/` section creation
2. Brain OS / Hermes runtime patterns as canonical without scoring gate
3. Merging Books/brain-os into agent-os/10_research bodies
4. OpenAPI / implementation backlog from Brain OS as Agent-OS contracts
5. RAG embedding pipeline before link + provenance discipline

---

## Up

- [NEXT_PHASE_ROADMAP.md](NEXT_PHASE_ROADMAP.md)
- [FULL_SYSTEM_AUDIT.md](FULL_SYSTEM_AUDIT.md)
