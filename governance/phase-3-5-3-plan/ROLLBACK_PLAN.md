# Rollback Plan — Free-Form CLI

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

Applies to **future** Phase 3.5.3-Impl artifact.

---

## Rollback triggers

| Trigger | Severity |
|---------|----------|
| Free-form CLI changes demo_runner without approval | critical |
| Provider called by default | critical |
| Secrets saved in transcript | critical |
| Unsafe input delivered | critical |
| Approval bypassed | critical |
| Script grows into runtime/framework | high |
| Baseline checks fail | high |
| Protected folders changed | critical |
| Multi-turn chat / memory added without phase | high |

---

## Rollback actions

1. Remove or revert `demos/review-assistant-freeform/free_form_cli.py`
2. Remove freeform docs / freeze folder if created
3. **Keep** demo-runner-v0.1 unchanged
4. **Keep** Review Assistant Thin v0.3
5. **Keep** provider safety harness v0.1
6. Rerun baselines:

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
python demos/review-assistant-runner/demo_runner.py --list
```

7. Document rollback in governance review
8. Remove navigation links to freeform if added

---

## Post-rollback operator path

- **Scenarios:** Demo Runner v0.1
- **Direct demo:** `minimal_demo.py --scenario <name>`
- **Hands-on:** `demos/review-assistant-hands-on/`

Free-form CLI is optional UX layer — lab works without it.

---

## Partial rollback

If only Mode 2 is problematic: disable Mode 2 in script (requires new impl/freeze phase), keep Mode 1 mock path.

Full removal preferred if gates fail critically.
