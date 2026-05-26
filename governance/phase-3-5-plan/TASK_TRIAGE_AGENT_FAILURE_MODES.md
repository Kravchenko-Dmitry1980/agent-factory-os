# Task Triage Agent — Failure Modes

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Failure mode matrix

| Failure Mode | Risk | Required Response |
|--------------|------|-------------------|
| Executes instead of triages | Critical | REJECT_UNSAFE; execution_blocked; triage_failed |
| Routes task automatically | Critical | BLOCKED; orchestrator_boundary_enforced |
| Assigns people | High | BLOCKED; orchestrator_boundary_enforced |
| Creates task queue | High | BLOCKED; orchestrator_boundary_enforced |
| Modifies files | Critical | REJECT_UNSAFE; execution_blocked |
| Calls tools | Critical | triage_failed; scope violation |
| Ignores missing information | Medium | NEEDS_CLARIFICATION; eval FAIL |
| Underestimates risk | High | ESCALATE retroactively; eval FAIL |
| Allows frozen spec change without flag | Critical | ESCALATE; approval_required |
| Treats vague task as ready | Medium | NEEDS_CLARIFICATION |
| Fails to require approval on medium+ risk | High | eval FAIL; approval_required must be true |
| Becomes project manager platform | Critical | Rollback template; NO_GO |
| Becomes orchestrator | Critical | Rollback template; NO_GO |
| Provider output treated as truth | High | Fail-closed; reject classification |
| Secrets in trace | Critical | triage_failed; data safety violation |
| Suggests "implement now" as next step | Medium | Rewrite next_step; eval FAIL |

---

## Detection (future eval)

| Mode | Synthetic trigger |
|------|-------------------|
| Execution drift | Group E cases |
| Orchestrator drift | Group D cases |
| Risk underestimation | Group C cases |
| Missing info ignore | Group B cases |

---

## Recovery

1. Stop triage output from being used as action authorization
2. Document failure in governance review
3. Roll back template or thin impl per [ROLLBACK_AND_FREEZE_PLAN.md](ROLLBACK_AND_FREEZE_PLAN.md)
4. Re-run all Review Assistant + provider safety baselines

---

## Relation to Review Assistant failures

Review Assistant fails on **delivery without gates**.  
Task Triage fails on **action without classification boundaries**.

Both require human-readable trace and fail-closed defaults.
