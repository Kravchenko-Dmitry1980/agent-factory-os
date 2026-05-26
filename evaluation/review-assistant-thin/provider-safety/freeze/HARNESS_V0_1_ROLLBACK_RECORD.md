# Harness v0.1 Rollback Record — Provider Safety Harness

**Version:** v0.1  
**Status:** FROZEN  
**Recorded:** 2026-05-26

---

## Rollback target

Remove or revert harness artifacts. **Keep** Review Assistant Thin v0.3 and all prior evaluation baselines.

### Remove or revert

| Artifact | Action |
|----------|--------|
| `evaluation/scripts/check_review_assistant_provider_safety.py` | Delete |
| `evaluation/review-assistant-thin/provider-safety/` | Delete or revert to pre-Phase-3.4 state |
| Navigation updates in evaluation/governance README | Revert if needed |
| `governance/PHASE_3_4_*` reviews | Archive or mark superseded |

### Keep unchanged

| Artifact | Reason |
|----------|--------|
| `review-assistant-thin-v0.3` | Implementation baseline |
| `prototypes-derived/review-assistant-thin/minimal_demo.py` | Agent behavior |
| Thin / mock / real provider contract checks | Pre-harness baselines |
| Frozen Agent Builder Kit specs | Protected |
| Smoke and trace checks | Phase 2.5 baseline |

---

## Rollback triggers

| Trigger | Action |
|---------|--------|
| Harness becomes a framework (plugins, registry, factory) | Rollback |
| New provider calls appear in harness default path | Rollback |
| Benchmark / leaderboard appears | Rollback |
| pytest / CI appears for harness | Rollback or separate phase |
| Secrets used in cases or traces | Rollback |
| Real private/client/medical data used | Rollback |
| Baseline checks regress | Fix or rollback |
| Agent behavior changes for harness | Rollback agent change |
| Protected folders modified | Rollback |

---

## Rollback steps

1. Remove `evaluation/scripts/check_review_assistant_provider_safety.py`
2. Remove or revert `evaluation/review-assistant-thin/provider-safety/` (including freeze docs)
3. Revert navigation in:
   - `evaluation/README.md`
   - `evaluation/review-assistant-thin/README.md`
   - `governance/README.md`
4. Re-run baseline checks:

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

5. Document rollback in governance (new review note with date and reason)
6. Confirm `review-assistant-thin-v0.3` remains active frozen baseline

---

## Post-rollback state

System returns to pre-Phase-3.4 evaluation surface:

- Review Assistant Thin v0.3 frozen
- Phase 3.1–3.3 eval scripts only
- No provider safety harness

---

## Related

- Pre-freeze rollback notes: [../rollback.md](../rollback.md)
- Plan rollback: [ROLLBACK_AND_FREEZE_PLAN.md](../../../../governance/phase-3-4-plan/ROLLBACK_AND_FREEZE_PLAN.md)
