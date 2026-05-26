# Phase 3.5.1 — Hands-on Demo Report — Governance Review

**Date:** 2026-05-26  
**Phase:** 3.5.1 — Hands-on Demo Report (documentation only)  
**Baseline:** review-assistant-thin-v0.3 (frozen), provider-safety-harness-v0.1 (frozen), task-triage-agent-specs-v0.1 (frozen)

---

## Executive Verdict

**PASS_WITH_NOTES**

Manual hands-on demo confirmed working lab behavior across original, mock LLM, and real local provider layers. UX/product layer is still missing — expected for current phase. No code, no behavior change, no provider call by Cursor.

---

## What Was Recorded

| Category | Detail |
|----------|--------|
| Operator | Dmitry — manual PowerShell runs |
| Demo target | `prototypes-derived/review-assistant-thin/minimal_demo.py` |
| Original scenarios | 5 (happy, missing_approval, critic_uncertain, bad_draft, unsafe_publish_attempt) |
| Mock LLM scenarios | 3 (llm_valid_draft, llm_malformed_output, llm_unsafe_output) |
| Real provider scenario | 1 (real_provider_synthetic + `--real-provider`) |
| Documentation package | `demos/review-assistant-hands-on/` — 11 Markdown files |

---

## Manual Commands

Recorded in [COMMANDS_RUN.md](../demos/review-assistant-hands-on/COMMANDS_RUN.md).

All commands use frozen `minimal_demo.py` — **not modified** in this phase.

---

## Scenario Results

| Layer | Scenarios | Outcome |
|-------|-----------|---------|
| Original | 5 | All match expected decisions (DELIVERED / BLOCKED / ESCALATED / FAILED) |
| Mock LLM | 3 | All match expected (DELIVERED / FAILED) |
| Real provider | 1 | DELIVERED with provider trace chain (operator manual) |

Full table: [SCENARIO_RESULTS.md](../demos/review-assistant-hands-on/SCENARIO_RESULTS.md).

---

## Real Provider Result (Operator Manual)

| Field | Value |
|-------|-------|
| Env | `RA_LLM_BASE_URL=http://127.0.0.1:1234`, `RA_LLM_MODEL=qwen2.5-7b-instruct-1m` |
| Flag | `--real-provider` |
| Decision | DELIVERED |
| delivered | True |
| Key principle | provider output = unverified until parse → verification → approval |

**Cursor did not run this command.** Recorded from operator observation only.

---

## What This Proves

| Principle | Evidence |
|-----------|----------|
| Controlled agent loop exists | CLI runs, trace visible |
| Approval mandatory | missing_approval → BLOCKED |
| Verification blocks bad draft | bad_draft → FAILED |
| Critic not truth | critic_uncertain → ESCALATED |
| Unsafe blocked | unsafe_publish_attempt, llm_unsafe_output |
| LLM output not truth | llm_unverified + gates |
| Provider output not truth | provider_unverified + gates |
| Mock default preserved | Original + mock work without --real-provider |
| Real provider explicit only | Requires env + flag |
| Lab is tangible | Operator hands-on confirmation |

---

## What This Does Not Prove

| Claim | Why not |
|-------|---------|
| Production ready | Lab prototype only |
| Model quality | Single synthetic live run |
| Live prompt injection resistance | Harness is synthetic local |
| Product UX | No UI, no free-form input |
| Task Triage works | Specs only, no impl |
| Interactive HITL | Approval scenario-simulated |

---

## Files Created

| Path |
|------|
| `demos/review-assistant-hands-on/README.md` |
| `demos/review-assistant-hands-on/HANDS_ON_DEMO_REPORT_RU.md` |
| `demos/review-assistant-hands-on/COMMANDS_RUN.md` |
| `demos/review-assistant-hands-on/SCENARIO_RESULTS.md` |
| `demos/review-assistant-hands-on/TRACE_EXPLANATION_RU.md` |
| `demos/review-assistant-hands-on/WHAT_IS_REAL_NOW_RU.md` |
| `demos/review-assistant-hands-on/WHAT_IS_STILL_MOCK_RU.md` |
| `demos/review-assistant-hands-on/WHY_IT_DOES_NOT_FEEL_LIKE_PRODUCT_RU.md` |
| `demos/review-assistant-hands-on/UX_GAPS_RU.md` |
| `demos/review-assistant-hands-on/NEXT_PRACTICAL_STEPS_RU.md` |
| `demos/review-assistant-hands-on/DEMO_SUMMARY_FOR_DMITRY_RU.md` |
| `governance/PHASE_3_5_1_HANDS_ON_DEMO_REPORT_REVIEW.md` |

---

## Files Updated

| Path | Change |
|------|--------|
| `governance/README.md` | Phase 3.5.1 review link |
| `START_HERE_RU.md` | Hands-on demo navigation |
| `operator-playbooks/ru/README.md` | Link to hands-on demo |

---

## Scope Compliance

| Check | Result |
|-------|--------|
| No code | **PASS** — Markdown only |
| No behavior change | **PASS** — minimal_demo.py untouched |
| No provider call by Cursor | **PASS** |
| No runtime / factory | **PASS** |
| No UI | **PASS** |
| No protected folder changes | **PASS** |
| No new scenarios | **PASS** |
| No eval script changes | **PASS** |
| Honest reporting | **PASS** — no production overclaim |

---

## Baseline Validation (Cursor, no-network)

Optional verification run 2026-05-26:

| Script | Result |
|--------|--------|
| check_review_assistant_provider_safety.py | PASS=16 FAIL=0 |
| check_review_assistant_thin.py | PASS=5 FAIL=0 |
| check_review_assistant_llm_mock.py | PASS=5 FAIL=0 |
| check_review_assistant_real_provider_contract.py | PASS=2 FAIL=0 |
| run_demo_smoke_checks.py | PASS=12 FAIL=0 |
| check_expected_text_traces.py | PASS=6 FAIL=0 |

**Not run:** `minimal_demo.py --scenario real_provider_synthetic --real-provider`

---

## Remaining Gaps

| Gap | Notes |
|-----|-------|
| No Demo Runner | Recommended next plan |
| No Interactive CLI | After Demo Runner |
| No product UX | Expected |
| Task Triage impl | Phase 3.6-Plan |
| Operator Console | Backlog |

---

## Recommended Next Step

**Phase 3.5.2-Plan — Demo Runner / Operator-Friendly CLI Output**

Plan only. Wrapper + Russian summary. No agent logic change.

See [NEXT_PRACTICAL_STEPS_RU.md](../demos/review-assistant-hands-on/NEXT_PRACTICAL_STEPS_RU.md).

---

## Related

- [PHASE_3_5_FREEZE_TASK_TRIAGE_AGENT_SPECS_V0_1_REVIEW.md](PHASE_3_5_FREEZE_TASK_TRIAGE_AGENT_SPECS_V0_1_REVIEW.md)
- [prototypes-derived/review-assistant-thin/README.md](../prototypes-derived/review-assistant-thin/README.md)
- [PHASE_3_3_LIVE_PROVIDER_CHECK_REVIEW.md](PHASE_3_3_LIVE_PROVIDER_CHECK_REVIEW.md)
