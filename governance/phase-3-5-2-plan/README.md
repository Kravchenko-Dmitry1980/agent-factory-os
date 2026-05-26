# Phase 3.5.2-Plan — Demo Runner / Operator-Friendly CLI Output

**Date:** 2026-05-26  
**Status:** planning-only — **no code**, **no runner**, **no behavior change**

---

## What this phase is

Planning a **future operator-friendly CLI Demo Runner** for Review Assistant Thin v0.3.

The runner will wrap existing `minimal_demo.py` and eval scripts — menu, Russian summaries, trace explanations — **without changing agent logic**.

---

## Why this phase exists

Phase 3.5.1 hands-on demo proved the system **works**, but the operator experience is still too technical:

- long commands to memorize
- raw TRACE to interpret manually
- no Russian result summary
- no scenario menu

This plan defines how to make the **existing** lab prototype easier to touch.

---

## What this phase is not

| Not in scope | Reason |
|--------------|--------|
| Code / `demo_runner.py` | Phase 3.5.2-Impl only |
| Runner implementation | Explicit user approval required |
| New agent / scenarios | Wrapper only |
| UI / web app | Out of scope |
| Runtime / factory | Forbidden |
| Scenario framework / plugins | Forbidden |
| Provider calls by Cursor | Forbidden |
| Modifying `minimal_demo.py` | No agent logic change |

---

## Current baseline (unchanged)

| Artifact | Role |
|----------|------|
| review-assistant-thin-v0.3 | Working CLI demo |
| provider-safety-harness-v0.1 | Synthetic safety eval |
| task-triage-agent-specs-v0.1 | Second agent specs (not run) |
| demos/review-assistant-hands-on/ | Phase 3.5.1 operator report |

---

## Reading order

| # | Document |
|---|----------|
| 1 | [PHASE_3_5_2_DEMO_RUNNER_PLAN.md](PHASE_3_5_2_DEMO_RUNNER_PLAN.md) |
| 2 | [OPERATOR_PROBLEM_STATEMENT_RU.md](OPERATOR_PROBLEM_STATEMENT_RU.md) |
| 3 | [DEMO_RUNNER_SCOPE.md](DEMO_RUNNER_SCOPE.md) |
| 4 | [DEMO_RUNNER_NON_GOALS.md](DEMO_RUNNER_NON_GOALS.md) |
| 5 | [SCENARIO_MENU_PLAN.md](SCENARIO_MENU_PLAN.md) |
| 6 | [OPERATOR_OUTPUT_FORMAT_RU.md](OPERATOR_OUTPUT_FORMAT_RU.md) |
| 7 | [TRACE_EXPLANATION_MAPPING_RU.md](TRACE_EXPLANATION_MAPPING_RU.md) |
| 8 | [TRANSCRIPT_SAVE_PLAN.md](TRANSCRIPT_SAVE_PLAN.md) |
| 9 | [REAL_PROVIDER_WARNING_POLICY.md](REAL_PROVIDER_WARNING_POLICY.md) |
| 10 | [NO_AGENT_LOGIC_CHANGE_POLICY.md](NO_AGENT_LOGIC_CHANGE_POLICY.md) |
| 11 | [NO_RUNTIME_NO_FACTORY_POLICY.md](NO_RUNTIME_NO_FACTORY_POLICY.md) |
| 12 | [IMPLEMENTATION_OPTIONS.md](IMPLEMENTATION_OPTIONS.md) |
| 13 | [RECOMMENDED_IMPLEMENTATION_PATH.md](RECOMMENDED_IMPLEMENTATION_PATH.md) |
| 14 | [EVALUATION_PLAN.md](EVALUATION_PLAN.md) |
| 15 | [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md) |
| 16 | [ROLLBACK_PLAN.md](ROLLBACK_PLAN.md) |
| 17 | [PRECONDITIONS_FOR_3_5_2_IMPL.md](PRECONDITIONS_FOR_3_5_2_IMPL.md) |
| 18 | [PHASE_3_5_2_GO_NO_GO.md](PHASE_3_5_2_GO_NO_GO.md) |
| 19 | [diagrams/](diagrams/demo-runner-boundary.md) |
| 20 | [FINAL_PHASE_3_5_2_PLAN_REPORT.md](FINAL_PHASE_3_5_2_PLAN_REPORT.md) |

---

## Expected outcome

**CONDITIONAL_GO_FOR_IMPLEMENTATION** — one stdlib script at `demos/review-assistant-runner/demo_runner.py` **after** explicit Phase 3.5.2-Impl approval.

Governance review: [../PHASE_3_5_2_DEMO_RUNNER_PLAN_REVIEW.md](../PHASE_3_5_2_DEMO_RUNNER_PLAN_REVIEW.md)

Related: [demos/review-assistant-hands-on/](../../demos/review-assistant-hands-on/README.md)
