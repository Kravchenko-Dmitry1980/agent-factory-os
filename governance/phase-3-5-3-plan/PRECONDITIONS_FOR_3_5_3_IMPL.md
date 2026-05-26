# Preconditions for Phase 3.5.3-Impl

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

Implementation must **not** start until all preconditions met.

---

## Required before implementation

| # | Precondition | Status (2026-05-26) |
|---|--------------|----------------------|
| 1 | User explicitly says: **«Start Phase 3.5.3-Impl — Minimal Interactive Free-Form CLI.»** | pending |
| 2 | demo-runner-v0.1 committed/tagged | recommended (see freeze review) |
| 3 | Phase 3.5.3-Plan approved | this package |
| 4 | Input policy accepted | [INPUT_POLICY.md](INPUT_POLICY.md) |
| 5 | Approval model accepted | [APPROVAL_MODEL_PLAN.md](APPROVAL_MODEL_PLAN.md) — Option A |
| 6 | Provider mode policy accepted | [PROVIDER_MODE_POLICY.md](PROVIDER_MODE_POLICY.md) |
| 7 | Transcript policy accepted | [TRANSCRIPT_POLICY.md](TRANSCRIPT_POLICY.md) |
| 8 | Rollback plan accepted | [ROLLBACK_PLAN.md](ROLLBACK_PLAN.md) |
| 9 | Baseline checks pass | verify at impl start |

---

## Implementation constraints (repeat)

- One stdlib script
- No dependencies
- No provider by default
- No runtime / factory
- No agent logic change (`minimal_demo.py` untouched)
- No demo_runner.py change (separate script path)
- No memory / database

---

## Baseline verification command (at impl start)

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

Expected: 16/5/5/2/12/6 PASS — same as current frozen baseline.

---

## GO reference

[PHASE_3_5_3_GO_NO_GO.md](PHASE_3_5_3_GO_NO_GO.md) — **CONDITIONAL_GO_FOR_IMPLEMENTATION**
