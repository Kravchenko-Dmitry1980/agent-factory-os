# Trace Diff Checklist

Use before accepting any change touching prototypes, integrations-real, or shared gates.

---

## Pre-Compare

- [ ] Scenario name documented
- [ ] Baseline trace captured (or use `observability/examples/`)
- [ ] `--scenario` flag recorded
- [ ] Mock mode confirmed (no API keys required)

## Event Presence

- [ ] `task_started` present
- [ ] Terminal event present (`task_completed`, `task_failed`, or escalated outcome)
- [ ] Verification events match scenario (pass/fail as expected)
- [ ] Approval events present when external action involved
- [ ] Retry events present when failure expected
- [ ] Escalation events present when ceiling hit
- [ ] Block events present when deny expected

## Order

- [ ] Approval before publish/execute on happy path
- [ ] Deny/block before any side effect on fail path
- [ ] `retry_exhausted` before `escalation_triggered`
- [ ] Verification before memory write

## OUTCOME Block

- [ ] `OUTCOME status=` matches expected (completed/rejected/escalated)
- [ ] `gates_failed` > 0 on reject scenarios
- [ ] `escalated=yes` on escalation scenarios
- [ ] No contradiction (e.g. completed + approval_denied)

## Governance Content

- [ ] Critic marked advisory where applicable
- [ ] Deny reasons are specific (not "error")
- [ ] LLM reminder present where applicable
- [ ] No silent skips (gaps in gate chain)

## Actors

- [ ] human, critic, gate, supervisor named
- [ ] No anonymous terminal failures

## Verdict

| Result | Action |
|--------|--------|
| All checked | PASS — change may proceed to quality gates |
| Any missing critical event | FAIL — rollback or fix before merge |
| Order violation | FAIL — fail-open risk |
| Thin audit | FAIL — observability regression |

---

## Critical Events (Never Remove)

```
approval_requested
approval_denied | approval_timeout
verification_failed
retry_exhausted
escalation_triggered
unsafe_action_blocked
memory_write_rejected
llm_malformed_output
governance_rejection
```

If change removes any from code path → stop and review.
