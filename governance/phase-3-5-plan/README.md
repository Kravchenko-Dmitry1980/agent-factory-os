# Phase 3.5-Plan — Second Text Agent Template

**Date:** 2026-05-26  
**Status:** planning-only — **no implementation**, **no template creation**, **no code**

---

## What this phase is

Planning the **second safe text-only agent template** after Review Assistant.

We evaluate candidate agents, recommend **Task Triage Agent**, define scope/contracts/safety gates/evaluation/trace plans, and set preconditions for a future **specs-only** implementation phase.

**This is a plan for a template — not the second agent itself.**

---

## What this phase is not

| Not in scope | Reason |
|--------------|--------|
| Implementation | Separate Phase 3.5-Impl with explicit user approval |
| Template under `agent-builder-kit/templates/` | Specs created only in future impl |
| Thin implementation | Follow Review Assistant discipline: specs first |
| Runtime / factory / generator | Forbidden by Phase 3 scope lock |
| Orchestrator / router / task queue | Task Triage must stay advisory |
| Project management platform | Drift risk — explicitly blocked |
| Multi-agent system | Out of scope |
| RAG / MCP / CV / digital twin | Out of scope |
| Operator Console | Backlog only |
| Provider calls | No LM Studio, OpenAI, or cloud |

---

## Current baseline (unchanged)

| Frozen artifact | Role |
|-----------------|------|
| review-assistant-thin-v0.1 | Original thin |
| review-assistant-thin-v0.2 | Mock LLM boundary |
| review-assistant-thin-v0.3 | Real local provider boundary |
| provider-safety-harness-v0.1 | Synthetic provider-output safety |

Known safe chain:

```text
template → thin implementation → mock LLM → real local provider → safety harness → freeze
```

---

## Reading order

| # | Document |
|---|----------|
| 1 | [PHASE_3_5_SECOND_TEXT_AGENT_PLAN.md](PHASE_3_5_SECOND_TEXT_AGENT_PLAN.md) |
| 2 | [SECOND_AGENT_CANDIDATE_REVIEW.md](SECOND_AGENT_CANDIDATE_REVIEW.md) |
| 3 | [RECOMMENDED_AGENT_DECISION.md](RECOMMENDED_AGENT_DECISION.md) |
| 4 | [TASK_TRIAGE_AGENT_CONCEPT.md](TASK_TRIAGE_AGENT_CONCEPT.md) |
| 5 | [TASK_TRIAGE_AGENT_SCOPE.md](TASK_TRIAGE_AGENT_SCOPE.md) |
| 6 | [TASK_TRIAGE_AGENT_CONTRACT.md](TASK_TRIAGE_AGENT_CONTRACT.md) |
| 7 | [TASK_TRIAGE_AGENT_WORKFLOW.md](TASK_TRIAGE_AGENT_WORKFLOW.md) |
| 8 | [TASK_TRIAGE_AGENT_SAFETY_GATES.md](TASK_TRIAGE_AGENT_SAFETY_GATES.md) |
| 9 | [TASK_TRIAGE_AGENT_EVALUATION_PLAN.md](TASK_TRIAGE_AGENT_EVALUATION_PLAN.md) |
| 10 | [PHASE_3_5_GO_NO_GO.md](PHASE_3_5_GO_NO_GO.md) |
| 11 | [FINAL_PHASE_3_5_PLAN_REPORT.md](FINAL_PHASE_3_5_PLAN_REPORT.md) |

Supporting: trace plan, failure modes, anti-patterns, provider/memory/approval policies, no-orchestrator/no-execution policies, implementation options, preconditions, rollback, diagrams.

---

## How to decide if specs can be created later

All must be true:

1. User message: **"Start Phase 3.5-Impl Task Triage Agent specs only."**
2. [PRECONDITIONS_FOR_3_5_IMPL.md](PRECONDITIONS_FOR_3_5_IMPL.md) satisfied
3. [PHASE_3_5_GO_NO_GO.md](PHASE_3_5_GO_NO_GO.md) → CONDITIONAL_GO_FOR_SPECS_ONLY
4. `review-assistant-thin-v0.3` and `provider-safety-harness-v0.1` committed/tagged
5. All baseline evaluation checks still PASS
6. No-orchestrator and no-execution policies approved

Until then: **plan only.**

---

## Prior art

- [../phase-3-2-plan/README.md](../phase-3-2-plan/README.md) — LLM adapter vs second template
- [../phase-3-4-plan/README.md](../phase-3-4-plan/README.md) — provider safety harness plan
- [../../agent-builder-kit/templates/review-assistant-agent/README.md](../../agent-builder-kit/templates/review-assistant-agent/README.md) — first template pattern
