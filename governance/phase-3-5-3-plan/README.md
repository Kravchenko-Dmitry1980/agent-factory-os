# Phase 3.5.3-Plan — Interactive Free-Form CLI

**Date:** 2026-05-26  
**Status:** planning-only — **no code**, **no free-form CLI**, **no behavior change**

---

## What this phase is

Planning a **future interactive free-form CLI** for Review Assistant Thin.

The operator will type custom task text and see a controlled Review Assistant-like flow with safety gates, Russian summary, and trace — **without external action**.

---

## Why this phase exists

**Demo Runner v0.1** (`demo-runner-v0.1`, FROZEN_WITH_NOTES) made predefined scenarios touchable:

- Russian menu
- direct `--scenario` run
- TRACE explanation
- safety status

But the operator **still cannot enter arbitrary task text**. The system feels like a test suite, not a touchable agent.

This plan defines how to add **controlled free-form input** without platform drift.

---

## What this phase is not

| Not in scope | Reason |
|--------------|--------|
| Code / `free_form_cli.py` | Phase 3.5.3-Impl only |
| Implementation | Explicit user approval required |
| Chat product / ChatGPT clone | Out of scope |
| Runtime / factory / orchestrator | Forbidden |
| Provider framework / router | Forbidden |
| Web UI / Operator Console | Forbidden |
| Task execution / publishing | Forbidden |
| Memory / database / sessions | Forbidden |
| Modifying `demo_runner.py` | Frozen v0.1 |
| Modifying `minimal_demo.py` | No agent logic change |

---

## Current baseline (unchanged)

| Artifact | Role |
|----------|------|
| review-assistant-thin-v0.3 | Working CLI demo (frozen scenarios) |
| provider-safety-harness-v0.1 | Synthetic safety eval |
| task-triage-agent-specs-v0.1 | Second agent specs (not run) |
| demo-runner-v0.1 | Scenario menu wrapper (frozen) |
| demos/review-assistant-hands-on/ | Phase 3.5.1 operator report |

---

## Reading order

| # | Document |
|---|----------|
| 1 | [PHASE_3_5_3_FREE_FORM_CLI_PLAN.md](PHASE_3_5_3_FREE_FORM_CLI_PLAN.md) |
| 2 | [OPERATOR_NEED_RU.md](OPERATOR_NEED_RU.md) |
| 3 | [FREE_FORM_CLI_SCOPE.md](FREE_FORM_CLI_SCOPE.md) |
| 4 | [FREE_FORM_CLI_NON_GOALS.md](FREE_FORM_CLI_NON_GOALS.md) |
| 5 | [INTERACTION_FLOW_RU.md](INTERACTION_FLOW_RU.md) |
| 6 | [INPUT_POLICY.md](INPUT_POLICY.md) |
| 7 | [OUTPUT_FORMAT_RU.md](OUTPUT_FORMAT_RU.md) |
| 8 | [APPROVAL_MODEL_PLAN.md](APPROVAL_MODEL_PLAN.md) |
| 9 | [PROVIDER_MODE_POLICY.md](PROVIDER_MODE_POLICY.md) |
| 10 | [SAFETY_GATES_PLAN.md](SAFETY_GATES_PLAN.md) |
| 11 | [TRACE_PLAN.md](TRACE_PLAN.md) |
| 12 | [TRANSCRIPT_POLICY.md](TRANSCRIPT_POLICY.md) |
| 13 | [EVALUATION_PLAN.md](EVALUATION_PLAN.md) |
| 14 | [IMPLEMENTATION_OPTIONS.md](IMPLEMENTATION_OPTIONS.md) |
| 15 | [RECOMMENDED_IMPLEMENTATION_PATH.md](RECOMMENDED_IMPLEMENTATION_PATH.md) |
| 16 | [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md) |
| 17 | [ROLLBACK_PLAN.md](ROLLBACK_PLAN.md) |
| 18 | [PRECONDITIONS_FOR_3_5_3_IMPL.md](PRECONDITIONS_FOR_3_5_3_IMPL.md) |
| 19 | [PHASE_3_5_3_GO_NO_GO.md](PHASE_3_5_3_GO_NO_GO.md) |
| 20 | [diagrams/](diagrams/free-form-cli-boundary.md) |
| 21 | [FINAL_PHASE_3_5_3_PLAN_REPORT.md](FINAL_PHASE_3_5_3_PLAN_REPORT.md) |

---

## Expected outcome

**CONDITIONAL_GO_FOR_IMPLEMENTATION** — separate stdlib script at `demos/review-assistant-freeform/free_form_cli.py` **after** explicit Phase 3.5.3-Impl approval.

Governance review: [../PHASE_3_5_3_FREE_FORM_CLI_PLAN_REVIEW.md](../PHASE_3_5_3_FREE_FORM_CLI_PLAN_REVIEW.md)

Related: [../../demos/review-assistant-runner/freeze/README.md](../../demos/review-assistant-runner/freeze/README.md)
