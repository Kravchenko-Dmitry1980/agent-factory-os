# Preconditions for Phase 3.5.2-Impl

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

Implementation must **not** start until all preconditions are met.

---

## Required before code

| # | Precondition | Status (plan phase) |
|---|--------------|----------------------|
| 1 | User explicitly says: **«Start Phase 3.5.2-Impl minimal demo runner.»** | Pending |
| 2 | Current baseline committed (thin v0.3, harness, triage specs, hands-on report) | Operator responsibility |
| 3 | Hands-on report exists | **Met** — demos/review-assistant-hands-on/ |
| 4 | Demo runner plan approved | **Met** — this package |
| 5 | No-agent-logic-change policy accepted | Documented |
| 6 | No-runtime/factory policy accepted | Documented |
| 7 | Real provider warning policy accepted | Documented |
| 8 | Baseline checks PASS | Met 2026-05-26 (optional verify at impl) |
| 9 | GO/NO-GO = CONDITIONAL_GO_FOR_IMPLEMENTATION | See GO_NO_GO doc |
| 10 | Scope: one stdlib script only | Documented |

---

## Implementation constraints (repeat)

| Constraint | Detail |
|------------|--------|
| One script | `demo_runner.py` |
| Stdlib only | No pip install |
| Fixed menu | SCENARIO_MENU_PLAN |
| No behavior change | subprocess wrapper only |
| No provider default | Confirm + env |

---

## Pre-impl verification commands

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

All must PASS before and after impl.

---

## Explicit user phrase (gate)

Implementation authorized only when user message includes intent equivalent to:

> Start Phase 3.5.2-Impl — Minimal Demo Runner

Plan phase (now) does **not** satisfy this gate.

---

## Related

- [PHASE_3_5_2_GO_NO_GO.md](PHASE_3_5_2_GO_NO_GO.md)
- [RECOMMENDED_IMPLEMENTATION_PATH.md](RECOMMENDED_IMPLEMENTATION_PATH.md)
