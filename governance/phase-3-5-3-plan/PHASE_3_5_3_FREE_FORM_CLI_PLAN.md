# Phase 3.5.3 — Interactive Free-Form CLI — Master Plan

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Goal

Plan a **minimal future interactive free-form CLI** that lets an operator type a custom task and run it through a safe Review Assistant-like flow with visible gates and Russian explanation.

**Not implemented in this phase.**

---

## Why now

The lab now has a stable operator stack:

| Layer | Status |
|-------|--------|
| Review Assistant Thin v0.3 | Frozen, working |
| Real local provider boundary | Frozen, explicit flag |
| Provider safety harness v0.1 | Frozen, 16 cases |
| Demo Runner v0.1 | Frozen, scenario menu + RU summary |
| Hands-on report (3.5.1) | Operator validation record |

**Gap:** interaction is still **scenario-based only**. Operator cannot type «свою задачу».

Next practical touchability step: **controlled free-form input** — planned here, built later.

---

## What should improve (future impl)

| Improvement | Constraint |
|-------------|------------|
| Operator types custom task text | Single task per run |
| System explains result in Russian | Same style as Demo Runner |
| Safety gates remain visible | verification, approval, unsafe block |
| No external action | No publish, no file write, no API side effects |
| Provider not called by default | Mock/default first |
| Approval explicit or simulated | Default deny; yes required for delivery |

---

## What must not happen

| Forbidden | Reason |
|-----------|--------|
| Runtime / factory | Platform drift |
| Production chat | Not a product |
| Hidden provider call | Operator must choose + confirm |
| Execution (publish, files, APIs) | Demo boundary |
| Memory writeback | No persistence layer |
| Task routing / orchestrator | Out of scope |
| UI platform | Terminal CLI only |
| Modify frozen demo-runner-v0.1 | Separate script preferred |
| Modify minimal_demo.py | No agent logic change in this track |

---

## Planned future artifact

| Field | Value |
|-------|-------|
| Path | `demos/review-assistant-freeform/free_form_cli.py` |
| Type | One stdlib script |
| Depends on | Review Assistant patterns, not frozen runner code |
| Entry | Separate from Demo Runner menu |

See [RECOMMENDED_IMPLEMENTATION_PATH.md](RECOMMENDED_IMPLEMENTATION_PATH.md).

---

## Document map

| Topic | Document |
|-------|----------|
| Operator need (RU) | [OPERATOR_NEED_RU.md](OPERATOR_NEED_RU.md) |
| Scope | [FREE_FORM_CLI_SCOPE.md](FREE_FORM_CLI_SCOPE.md) |
| Non-goals | [FREE_FORM_CLI_NON_GOALS.md](FREE_FORM_CLI_NON_GOALS.md) |
| Interaction flow | [INTERACTION_FLOW_RU.md](INTERACTION_FLOW_RU.md) |
| Input policy | [INPUT_POLICY.md](INPUT_POLICY.md) |
| Output format | [OUTPUT_FORMAT_RU.md](OUTPUT_FORMAT_RU.md) |
| Approval | [APPROVAL_MODEL_PLAN.md](APPROVAL_MODEL_PLAN.md) |
| Provider modes | [PROVIDER_MODE_POLICY.md](PROVIDER_MODE_POLICY.md) |
| Safety gates | [SAFETY_GATES_PLAN.md](SAFETY_GATES_PLAN.md) |
| GO/NO-GO | [PHASE_3_5_3_GO_NO_GO.md](PHASE_3_5_3_GO_NO_GO.md) |

---

## Phase sequence

```text
Phase 3.5.3-Plan   ← this document (planning only)
Phase 3.5.3-Impl   ← future, after explicit approval
Phase 3.5.3-Freeze ← future, after impl validation
```

Demo Runner v0.1 remains frozen and unchanged unless separate change proposal.
