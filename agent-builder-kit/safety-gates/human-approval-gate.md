# Human Approval Gate

## Purpose

Ensure a **human** explicitly approves risky outputs before delivery or external action.

## When Required

Publish, send, delete, pay, production write, final user-facing delivery.

## Pass Condition

- `approval_requested` before risky action
- `verification_passed actor=human decision=approve` OR documented override path
- Approval fingerprint in trace

## Fail Condition

- Publish without `approval_requested`
- Auto-approve on timeout
- Critic pass substitutes for human approval

## Example

```
approval_requested actor=human required=true
verification_passed actor=human decision=approve
task_completed actor=publisher published=true
```

Reference: `observability/examples/successful-review-trace.txt`

## Related Anti-patterns

- Missing approval
- Critic treated as truth
- Hidden autonomy
