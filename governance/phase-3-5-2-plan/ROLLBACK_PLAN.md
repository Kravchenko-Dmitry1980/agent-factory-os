# Rollback Plan — Demo Runner

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Rollback triggers

| Trigger | Severity |
|---------|----------|
| Runner modifies agent behavior | Critical |
| Runner grows into framework (plugins, YAML registry) | High |
| Provider call happens by default | Critical |
| Dependencies added (rich, typer, etc.) | High |
| UI / web layer introduced | High |
| Secrets logged in transcript or summary | Critical |
| Baseline checks fail after runner merge | Critical |
| Protected folders changed without approval | Critical |
| Parse hacks require minimal_demo.py change | Critical |

---

## Rollback actions

1. **Stop** using runner in demos and docs navigation
2. **Remove** `demos/review-assistant-runner/demo_runner.py` (and runner-specific code)
3. **Keep** `demos/review-assistant-hands-on/` — unchanged operator report
4. **Keep** Review Assistant thin v0.3 — frozen
5. **Revert** navigation links to hands-on only
6. **Re-run** baseline checks:

```powershell
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

7. **Document** rollback in governance review (verdict: ROLLED_BACK)

---

## Rollback does not remove

| Keep | Reason |
|------|--------|
| Phase 3.5.2-Plan docs | Historical plan |
| Phase 3.5.1 hands-on report | Still valid manual path |
| minimal_demo.py direct CLI | Primary interface |
| Frozen artifacts v0.1–v0.3 | Independent of runner |

---

## Partial rollback

If only transcript feature fails:

- Disable `--save-transcript`
- Keep menu + summary

If summary parse fails for one scenario:

- Fix mapping table
- Do not change demo output format without thin freeze review

---

## Authority

Rollback requires human acknowledgment. Do not silently delete runner if used in START_HERE navigation — update docs in same commit.
