# Real Provider Rollback Plan

**Phase 3.3-Plan** — future rollback for real provider implementation.

---

## Rollback target

Return to **review-assistant-thin-v0.2** mock-only baseline.

Preserve v0.2 freeze history. Do not modify frozen Agent Builder Kit spec body.

---

## Rollback triggers

| Trigger | Severity |
|---------|----------|
| Real provider call happens **by default** (mock not default) | Critical |
| Key appears in logs or trace | Critical |
| Key appears in repo | Critical |
| Provider framework forming (registry, router) | Critical |
| Provider output bypasses verification | Critical |
| Provider output bypasses approval | Critical |
| Timeout creates hallucinated fallback draft | Critical |
| Baseline checks FAIL | High |
| Cost or quota runaway | High |
| Sensitive data sent without approval | Critical |
| Real mode enabled in CI unintentionally | High |

---

## Rollback steps

1. **Stop** — disable real provider immediately (remove env var locally)
2. **Revert** provider code in `minimal_demo.py` and related docs (impl phase only)
3. **Keep** mock v0.2 path intact
4. **Rotate** API key if any leakage suspected
5. **Re-run** baselines:

   ```powershell
   cd C:\Dima\Projects\CURSOR\AGENT
   python evaluation/scripts/check_review_assistant_thin.py
   python evaluation/scripts/check_review_assistant_llm_mock.py
   python evaluation/scripts/run_demo_smoke_checks.py
   python evaluation/scripts/check_expected_text_traces.py
   ```

   Expected: PASS=5, PASS=5, PASS=12, PASS=6

6. **Remove** any real-provider eval script if it cannot be made opt-in safe
7. **Document** incident in governance (rollback note)
8. **Restore** active change lock to v0.2: `freeze/V0_2_CHANGE_LOCK.md`
9. **Do not** delete v0.2 freeze records

---

## Git

```powershell
git revert <provider-impl-commits>
# optional: remain on tag review-assistant-thin-v0.2
```

---

## Preserve on rollback

- review-assistant-thin-v0.2 freeze folder
- Phase 3.3-plan docs (this folder)
- Mock LLM eval scripts
- No changes to protected folders unless accidentally touched — revert those too

---

## Post-rollback state

- Mock default
- No network in default demo path
- Real provider requires new approval + new impl phase

---

## References

- v0.2 rollback: `prototypes-derived/review-assistant-thin/freeze/V0_2_ROLLBACK_RECORD.md`
- Phase 3.2: [../phase-3-2-plan/ROLLBACK_AND_FREEZE_PLAN.md](../phase-3-2-plan/ROLLBACK_AND_FREEZE_PLAN.md)
