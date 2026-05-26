# Rollback Record — Review Assistant Thin v0.2

**Recorded:** 2026-05-26

---

## Rollback target

Return to **v0.1 thin implementation** (5 scenarios, no LLM boundary) **or** remove v0.2 LLM additions while preserving v0.1 behavior.

Historical v0.1 rollback: [ROLLBACK_RECORD.md](ROLLBACK_RECORD.md)

---

## Rollback triggers

| Trigger | Action |
|---------|--------|
| LLM mock check fails after change | Stop; revert LLM changes |
| Original thin scenarios regress | Stop; revert to v0.1 baseline |
| Provider framework appears | Remove; document in governance |
| Runtime / factory drift appears | Remove; document in governance |
| Real API added without approval | Immediate revert; security review |
| Unsafe LLM output delivered | Immediate revert; incident note |
| Approval bypass appears | Immediate revert |

---

## Rollback steps

1. **Stop** further changes
2. **Revert** v0.2 LLM additions in `prototypes-derived/review-assistant-thin/`:
   - Remove or revert mock LLM functions and `llm_*` scenarios from `minimal_demo.py`
   - Remove or revert `llm_boundary.md` and LLM sections in docs
   - Optionally remove `evaluation/scripts/check_review_assistant_llm_mock.py` and LLM eval docs
3. **Keep** frozen Agent Builder Kit specs **unchanged**
4. **Do not** modify protected folders: `prototypes/`, `integrations-real/`, `observability/examples/`, `Books/`, `experiments/`
5. **Re-run** baselines:

   ```powershell
   cd C:\Dima\Projects\CURSOR\AGENT
   python evaluation/scripts/check_review_assistant_thin.py
   python evaluation/scripts/run_demo_smoke_checks.py
   python evaluation/scripts/check_expected_text_traces.py
   ```

   Expected after rollback to v0.1: thin PASS=5, smoke PASS=12, trace PASS=6. LLM mock check N/A or removed.

6. **Document** rollback in governance (e.g. new rollback note or update [PHASE_3_2_1_FREEZE_MOCK_LLM_V0_2_REVIEW.md](../../../governance/PHASE_3_2_1_FREEZE_MOCK_LLM_V0_2_REVIEW.md))
7. **Restore** active change lock to [CHANGE_LOCK.md](CHANGE_LOCK.md) if fully reverted to v0.1

---

## Git

```powershell
git revert <commits>
# optional: git checkout review-assistant-thin-v0.1  (if tagged)
# optional: git tag review-assistant-thin-v0.1
```

---

## Preserve on rollback

- Frozen template v0.1 spec (Agent Builder Kit)
- v0.1 freeze history in `freeze/` (IMPLEMENTATION_FREEZE_RECORD.md, etc.)
- Phase 3.1 / 3.2 plan and review docs
- Phase 2 prototypes and harness

---

## Pre-freeze tags

| Tag | Meaning |
|-----|---------|
| `review-assistant-thin-v0.1` | Original thin baseline |
| `review-assistant-thin-v0.2` | Thin + mock LLM baseline (recommended at freeze commit) |
