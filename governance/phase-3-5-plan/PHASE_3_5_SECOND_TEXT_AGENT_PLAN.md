# Phase 3.5 — Second Text Agent Template — Master Plan

**Date:** 2026-05-26  
**Status:** PLAN_ONLY — no implementation

---

## Goal

Plan the **second safe text-only agent template** after Review Assistant Agent Template v0.1.

The plan must decide:

- Which second template is most useful
- Which candidate is safest
- Which candidate has lowest factory/runtime drift risk
- What the template must include
- What safety gates are required
- What evaluation must exist before implementation
- What remains forbidden
- Whether Phase 3.5-Impl creates **specs only** or also thin implementation (recommendation: specs only first)

---

## Why now

Review Assistant line is complete and frozen:

| Layer | Artifact |
|-------|----------|
| Template | Review Assistant Agent Template v0.1 |
| Thin impl | review-assistant-thin-v0.1 → v0.3 |
| Mock LLM | v0.2 boundary |
| Real provider | v0.3 local OpenAI-compatible boundary |
| Safety harness | provider-safety-harness-v0.1 |
| Live validation | LM Studio (Phase 3.3-LiveCheck) |

We have a proven pattern:

```text
template → thin → mock → real provider → safety harness → freeze
```

A second template can reuse this discipline without repeating Review Assistant's domain.

---

## Why not immediately build

Second agent introduces high drift risk:

| Risk | Consequence |
|------|-------------|
| Template sprawl | Unmaintained partial specs |
| Factory illusion | "Two agents = platform" mindset |
| Runtime drift | Hidden orchestration code |
| Orchestration drift | Task Triage becomes router |
| Evaluation surface growth | Unbounded test matrix |
| PM platform drift | Tickets, queues, assignments |

Planning first constrains scope before any Markdown template or code exists.

---

## Expected direction

**Recommend Task Triage Agent** as second template candidate — **plan only**, no implementation.

Task Triage classifies incoming work and recommends safe next steps. It does **not** execute, route, or delegate.

See [RECOMMENDED_AGENT_DECISION.md](RECOMMENDED_AGENT_DECISION.md).

---

## Relationship to Review Assistant

| Agent | Role | Output |
|-------|------|--------|
| **Review Assistant** | Draft + verify + approve before delivery | DELIVERED / BLOCKED / … |
| **Task Triage Agent** | Classify task + assess risk + recommend next step | TRIAGED / ESCALATE / BLOCKED / … |

Complementary, not duplicate:

- Triage happens **before** implementation or review work is assigned
- Review Assistant handles **content** after a task is scoped
- Triage never produces deliverable content for external send

---

## Phase deliverables (this plan)

| Deliverable | Document |
|-------------|----------|
| Candidate comparison | [SECOND_AGENT_CANDIDATE_REVIEW.md](SECOND_AGENT_CANDIDATE_REVIEW.md) |
| Recommendation | [RECOMMENDED_AGENT_DECISION.md](RECOMMENDED_AGENT_DECISION.md) |
| Concept + scope + contract | TASK_TRIAGE_AGENT_*.md |
| Safety + policies | SAFETY_GATES, NO_ORCHESTRATOR, NO_EXECUTION, etc. |
| Future evaluation | [TASK_TRIAGE_AGENT_EVALUATION_PLAN.md](TASK_TRIAGE_AGENT_EVALUATION_PLAN.md) |
| Impl options | [SECOND_TEMPLATE_IMPLEMENTATION_OPTIONS.md](SECOND_TEMPLATE_IMPLEMENTATION_OPTIONS.md) |
| Gates + rollback | PRECONDITIONS, ROLLBACK, GO/NO-GO |
| Diagrams | [diagrams/](diagrams/) |

---

## Hard boundaries (unchanged)

**Forbidden in Phase 3.5-Plan and future impl without new phase:**

- Runtime, factory, generator
- Provider framework
- Orchestrator, router, task queue
- Multi-agent control
- RAG, MCP, CV, digital twin
- Operator Console
- Default provider calls
- Persistent memory / task backlog
- Modifying frozen Review Assistant or provider safety harness

---

## Recommended next phase (after plan approval)

**Phase 3.5-Impl — Task Triage Agent specs only**

Create `agent-builder-kit/templates/task-triage-agent/` Markdown specs following Review Assistant template structure. **No Python. No thin demo.**

User must explicitly say:

> Start Phase 3.5-Impl Task Triage Agent specs only.

Plus [PRECONDITIONS_FOR_3_5_IMPL.md](PRECONDITIONS_FOR_3_5_IMPL.md).

---

## Success criteria for this plan

- [x] Second agent candidates compared
- [x] Task Triage Agent recommended with boundaries
- [x] Scope, contract, workflow defined
- [x] Safety gates and anti-patterns documented
- [x] Evaluation and trace plans sketched
- [x] Provider/memory/approval policies defined
- [x] No-orchestrator and no-execution policies explicit
- [x] Impl options compared (specs-only recommended)
- [x] Preconditions and rollback documented
- [x] GO/NO-GO recorded
- [x] No code, no template, no protected folder changes
