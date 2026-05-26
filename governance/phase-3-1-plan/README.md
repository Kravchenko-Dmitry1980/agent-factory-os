# Phase 3.1-Plan — Thin Implementation Plan

**Status:** Planning only — **no code**, **no implementation folder**.

---

## What Phase 3.1-Plan is

A **Markdown-only** plan for a future **thin** implementation of the frozen **Review Assistant Agent v0.1**. It answers where code may live, what behavior is allowed, how to evaluate, and how to rollback — without writing any implementation.

---

## Why it exists

Phase 3.0 created specs. Phase 3.0-Freeze locked Review Assistant v0.1. Before any Python or runtime work, the repository needs an explicit **implementation plan** so Phase 3.1 cannot drift into factory, platform, or second-agent scope.

---

## Why no code is created

Phase 3.1-Plan is **planning**, not **implementation**. Creating code or folders now would violate:

- [PHASE_3_1_PRECONDITIONS.md](../PHASE_3_1_PRECONDITIONS.md) (P1, P5, H1–H5 not met)
- [NO_RUNTIME_DECISION.md](NO_RUNTIME_DECISION.md)
- Frozen template [CHANGE_LOCK.md](../../agent-builder-kit/templates/review-assistant-agent/sign-off/CHANGE_LOCK.md)

---

## Documents that matter most

| Order | Document | Purpose |
|-------|----------|---------|
| 1 | [PHASE_3_1_THIN_IMPLEMENTATION_PLAN.md](PHASE_3_1_THIN_IMPLEMENTATION_PLAN.md) | Master plan |
| 2 | [IMPLEMENTATION_SCOPE.md](IMPLEMENTATION_SCOPE.md) | Allowed / forbidden behavior |
| 3 | [FILE_BOUNDARY_PLAN.md](FILE_BOUNDARY_PLAN.md) | Where code may live |
| 4 | [BEHAVIOR_CONTRACT.md](BEHAVIOR_CONTRACT.md) | States, I/O, gates |
| 5 | [EVALUATION_PLAN.md](EVALUATION_PLAN.md) | What to test after impl |
| 6 | [ROLLBACK_PLAN.md](ROLLBACK_PLAN.md) | How to revert safely |
| 7 | [PHASE_3_1_GO_NO_GO.md](PHASE_3_1_GO_NO_GO.md) | Implementation readiness |
| 8 | [FINAL_PHASE_3_1_PLAN_REPORT.md](FINAL_PHASE_3_1_PLAN_REPORT.md) | Summary report |

Supporting: [HUMAN_APPROVAL_PLAN.md](HUMAN_APPROVAL_PLAN.md), [TRACE_PLAN.md](TRACE_PLAN.md), [ACCEPTANCE_PLAN.md](ACCEPTANCE_PLAN.md), [RISK_REVIEW.md](RISK_REVIEW.md), [PRE_IMPLEMENTATION_CHECKLIST.md](PRE_IMPLEMENTATION_CHECKLIST.md), [POST_IMPLEMENTATION_CHECKLIST.md](POST_IMPLEMENTATION_CHECKLIST.md), [diagrams/](diagrams/)

---

## How to decide if Phase 3.1 implementation can start

All must be true:

1. User message: **«Start Phase 3.1 thin implementation of Review Assistant.»**
2. [PRE_IMPLEMENTATION_CHECKLIST.md](PRE_IMPLEMENTATION_CHECKLIST.md) complete
3. [PHASE_3_1_GO_NO_GO.md](PHASE_3_1_GO_NO_GO.md) = GO or CONDITIONAL_GO with conditions met
4. Human lead sign-off acknowledged
5. H1–H5 assessments (see [PHASE_3_1_PRECONDITIONS.md](../PHASE_3_1_PRECONDITIONS.md))
6. Smoke PASS=12, trace PASS=6 re-run on start day

**Current plan verdict:** CONDITIONAL_GO_FOR_IMPLEMENTATION — plan ready; human gates pending.

---

## Related governance

| Doc | Link |
|-----|------|
| Phase 3.0 kit review | [PHASE_3_0_BUILDER_KIT_REVIEW.md](../PHASE_3_0_BUILDER_KIT_REVIEW.md) |
| Freeze review | [PHASE_3_0_FREEZE_REVIEW_ASSISTANT.md](../PHASE_3_0_FREEZE_REVIEW_ASSISTANT.md) |
| Preconditions | [PHASE_3_1_PRECONDITIONS.md](../PHASE_3_1_PRECONDITIONS.md) |
| Frozen template | [review-assistant-agent/sign-off/](../../agent-builder-kit/templates/review-assistant-agent/sign-off/README.md) |

---

## Diagrams

- [thin-implementation-boundary.md](diagrams/thin-implementation-boundary.md)
- [review-assistant-flow.md](diagrams/review-assistant-flow.md)
- [evaluation-loop.md](diagrams/evaluation-loop.md)
- [rollback-flow.md](diagrams/rollback-flow.md)
- [no-runtime-boundary.md](diagrams/no-runtime-boundary.md)
