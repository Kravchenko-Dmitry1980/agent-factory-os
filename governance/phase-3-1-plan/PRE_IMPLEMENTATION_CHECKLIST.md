# Pre-Implementation Checklist — Phase 3.1

Complete **before** creating `prototypes-derived/review-assistant-thin/` or any `.py` impl files.

---

## User and governance gates

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | User explicitly starts Phase 3.1: «Start Phase 3.1 thin implementation of Review Assistant.» | ☐ | P1 |
| 2 | [PHASE_3_1_GO_NO_GO.md](PHASE_3_1_GO_NO_GO.md) allows implementation | ☐ | CONDITIONAL_GO minimum |
| 3 | Human lead sign-off acknowledged | ☐ | P5 — pending as of plan date |
| 4 | H1 Mentor assessment pass | ☐ | |
| 5 | H2 Lead assessment pass | ☐ | |
| 6 | H3 Architect phase-3-readiness pass | ☐ | |
| 7 | H4 PHASE_3_FREEZE_POLICY acknowledged | ☐ | |
| 8 | Review Assistant v0.1 frozen | ☑ | FROZEN_WITH_NOTES 2026-05-26 |

---

## Baseline scripts (run on start day)

| # | Item | Status | Expected |
|---|------|--------|----------|
| 9 | `run_demo_smoke_checks.py` | ☑ ref | PASS=12 FAIL=0 |
| 10 | `check_expected_text_traces.py` | ☑ ref | PASS=6 FAIL=0 |

Re-run items 9–10 immediately before first impl commit.

---

## Plan acceptance

| # | Item | Status |
|---|------|--------|
| 11 | [FILE_BOUNDARY_PLAN.md](FILE_BOUNDARY_PLAN.md) — Option B accepted | ☑ plan |
| 12 | [IMPLEMENTATION_SCOPE.md](IMPLEMENTATION_SCOPE.md) read | ☐ impl team |
| 13 | [BEHAVIOR_CONTRACT.md](BEHAVIOR_CONTRACT.md) read | ☐ impl team |
| 14 | [EVALUATION_PLAN.md](EVALUATION_PLAN.md) accepted | ☐ lead |
| 15 | [ROLLBACK_PLAN.md](ROLLBACK_PLAN.md) accepted | ☐ lead |
| 16 | [NO_RUNTIME_DECISION.md](NO_RUNTIME_DECISION.md) accepted | ☑ plan |
| 17 | [HUMAN_APPROVAL_PLAN.md](HUMAN_APPROVAL_PLAN.md) accepted | ☐ impl team |

---

## Repository hygiene

| # | Item | Status |
|---|------|--------|
| 18 | `git status` reviewed | ☐ |
| 19 | Pre-impl tag planned (`phase-3.1-pre-impl`) | ☐ |
| 20 | Protected folders listed — no edits planned | ☑ |

**Protected:** `prototypes/`, `integrations-real/`, `evaluation/scripts/`, `observability/examples/`, `Books/`, `experiments/`, frozen template body

---

## Ready to implement?

**All boxes must be ☑** except where explicitly waived by lead in writing.

**Current (plan date):** **NOT READY** — items 1, 3–7, 11–20 pending for impl day.
