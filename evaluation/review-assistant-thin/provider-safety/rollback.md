# Rollback — Phase 3.4 Provider Safety Harness

If the harness causes drift or unwanted scope expansion:

---

## Remove harness artifacts

1. Delete `evaluation/scripts/check_review_assistant_provider_safety.py`
2. Delete `evaluation/review-assistant-thin/provider-safety/` (if no longer needed)
3. Revert navigation updates in:
   - `evaluation/README.md`
   - `evaluation/review-assistant-thin/README.md`
   - `governance/README.md`

---

## Preserve v0.3 baseline

Do **not** modify:

- `prototypes-derived/review-assistant-thin/minimal_demo.py`
- Frozen specs under `agent-builder-kit/templates/review-assistant-agent/`
- Protected folders (`prototypes/`, `integrations-real/`, etc.)

---

## Re-run baseline checks

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

Expected:

- thin: PASS=5 FAIL=0
- mock LLM: PASS=5 FAIL=0
- real provider no-network: PASS=2 FAIL=0
- smoke: PASS=12 FAIL=0
- trace: PASS=6 FAIL=0

---

## Document rollback

Record rollback in a governance review note with reason and date. Keep v0.3 as the active frozen baseline.

See also:

- [governance/phase-3-4-plan/ROLLBACK_AND_FREEZE_PLAN.md](../../../governance/phase-3-4-plan/ROLLBACK_AND_FREEZE_PLAN.md)
