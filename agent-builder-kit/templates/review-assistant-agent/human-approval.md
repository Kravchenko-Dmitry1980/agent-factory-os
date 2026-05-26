# Review Assistant Agent — Human Approval

## Approval Required Before

- Final delivery to user
- Any external publish/send action
- Persistent memory writeback (disabled in v0.1)

## Not Required For

- Internal draft generation (output marked unverified)
- Advisory critique

## Approval States

| State | Behavior |
|-------|----------|
| pending | Wait for human; block delivery |
| approved | Proceed to output |
| denied | Terminal fail; document reason |
| timeout | Deny-by-default → `approval_timeout` |

## Rejection Path

```
approval_requested → approval_denied → task_failed
```

Human may provide revision feedback. New task = new `task_started`.

Reference scenario: Bad Draft Rejected — `evaluation/scenarios/review-loop-scenarios.md`

## Timeout Path

No response within policy window → `approval_timeout` → `task_failed`. **No auto-approve.**

## Escalation Path

Critic uncertain or policy conflict → `escalation_triggered` → supervisor review → approve/deny.

## No Auto-Publish

Explicit forbidden behavior. Bypass attempt → `unsafe_action_blocked`.

Reference: Bypass Attempt Blocked scenario.

## Trace Requirements

Every happy path must include:

```
approval_requested actor=human required=true
verification_passed actor=human decision=approve
```

Every reject path must include `approval_denied` with reason.

See [expected-traces.md](expected-traces.md)

## Rule

**No approval = no risky action.**

Reference: [human-approval-spec.md](../../template-specs/human-approval-spec.md)
