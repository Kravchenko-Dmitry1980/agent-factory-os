# Rollback and Freeze Plan — Task Triage Agent

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## If future Task Triage template drifts

### Rollback triggers

| Trigger | Severity |
|---------|----------|
| Agent executes tasks | Critical |
| Agent routes automatically | Critical |
| Agent becomes orchestrator | Critical |
| Agent creates tasks/tickets | High |
| Agent modifies files | Critical |
| Agent calls tools/providers by default | High |
| Frozen Review Assistant specs changed without approval | Critical |
| Provider safety harness modified for triage without phase | High |
| Evaluation missing for thin impl | High |
| Approval policy missing in template | High |
| pytest/CI added without phase | Medium |
| Benchmark/leaderboard appears | High |
| Real secrets or client data in cases | Critical |

---

## Rollback actions

1. **Remove** Task Triage template draft (`agent-builder-kit/templates/task-triage-agent/` if created)
2. **Remove** any thin impl (`prototypes-derived/task-triage-thin/` if created prematurely)
3. **Remove** any triage eval script if created without approval
4. **Keep unchanged:**
   - Review Assistant line (v0.1–v0.3)
   - provider-safety-harness-v0.1
   - Frozen Agent Builder Kit Review Assistant template
   - All existing evaluation scripts
5. **Re-run baseline checks:**

```powershell
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

6. **Document rollback** in governance review with date and trigger

---

## If future specs succeed

### Freeze sequence (after Phase 3.5-Impl + review)

| Step | Artifact |
|------|----------|
| 1 | Template sign-off complete |
| 2 | Create `task-triage-agent-v0.1` freeze record in template `sign-off/` |
| 3 | Tag `task-triage-agent-v0.1` |
| 4 | **Then** plan thin implementation (Phase 3.6+) — not before |

**Rule:** Freeze template v0.1 **before** any code in `prototypes-derived/`.

---

## Preserve always

| Artifact | Never rollback unless explicit project decision |
|----------|---------------------------------------------------|
| review-assistant-thin-v0.3 | Keep |
| provider-safety-harness-v0.1 | Keep |
| Review Assistant template v0.1 | Keep |
| Phase 3.5-Plan docs | Keep as historical plan |

---

## Related

- Provider harness rollback: [../../evaluation/review-assistant-thin/provider-safety/freeze/HARNESS_V0_1_ROLLBACK_RECORD.md](../../evaluation/review-assistant-thin/provider-safety/freeze/HARNESS_V0_1_ROLLBACK_RECORD.md)
- Review Assistant rollback: [../../prototypes-derived/review-assistant-thin/freeze/V0_3_ROLLBACK_RECORD.md](../../prototypes-derived/review-assistant-thin/freeze/V0_3_ROLLBACK_RECORD.md)
