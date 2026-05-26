# Preconditions for Phase 3.5-Impl — Task Triage Agent

**Date:** 2026-05-26  
**Target:** Specs-only template creation (Option A)

---

## Before any implementation/template creation

All must be true:

| # | Precondition | Status (plan date) |
|---|--------------|-------------------|
| 1 | User explicitly says: **"Start Phase 3.5-Impl Task Triage Agent specs only."** | Pending |
| 2 | `provider-safety-harness-v0.1` committed/tagged | Pending user git action |
| 3 | `review-assistant-thin-v0.3` committed/tagged | Pending user git action |
| 4 | No pending uncommitted freeze docs for Phase 3.4.1 | Verify before impl |
| 5 | Task Triage scope approved (this plan) | ✅ Phase 3.5-Plan |
| 6 | No-orchestrator policy approved | ✅ Documented |
| 7 | No-execution policy approved | ✅ Documented |
| 8 | Evaluation plan approved (future) | ✅ Documented |
| 9 | Rollback plan approved | ✅ Documented |
| 10 | [PHASE_3_5_GO_NO_GO.md](PHASE_3_5_GO_NO_GO.md) → CONDITIONAL_GO_FOR_SPECS_ONLY | ✅ Expected |
| 11 | All baseline eval scripts PASS | Re-run at impl start |

---

## Baseline commands (must PASS at impl start)

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

Expected: PASS=16,5,5,2,12,6 — FAIL=0 each.

---

## Implementation phase rules (Phase 3.5-Impl)

| Rule | Value |
|------|-------|
| Create template dir | `agent-builder-kit/templates/task-triage-agent/` |
| Create code | **Forbidden** |
| Create thin demo | **Forbidden** |
| Create eval script | **Forbidden** |
| Modify Review Assistant | **Forbidden** |
| Modify provider safety harness | **Forbidden** |
| Provider calls | **Forbidden** |
| Runtime/factory | **Forbidden** |

---

## After specs created

1. Template review (governance)
2. Sign-off checklist (mirror Review Assistant)
3. Freeze `task-triage-agent-v0.1` before any thin impl plan
4. Only then plan Phase 3.6 thin implementation (separate)

---

## User messages that do NOT start impl

- "Plan task triage" → planning only (this phase)
- "Build task triage agent" → too vague — reject until specs-only prompt
- "Implement task triage with code" → violates preconditions
