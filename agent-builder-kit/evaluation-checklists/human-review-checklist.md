# Human Review Checklist

Use when auditing HITL policy in a template.

## Policy

- [ ] Risky actions list complete
- [ ] Deny-by-default stated
- [ ] Timeout → `approval_timeout`, not auto-approve
- [ ] Rejection path documented
- [ ] Escalation path documented

## Trace evidence

- [ ] `approval_requested` in happy path
- [ ] `approval_denied` in reject scenario
- [ ] Human actor identifiable
- [ ] No publish after deny

## Operator clarity

- [ ] Reviewer knows what they approve (artifact id/hash)
- [ ] Rejection reason captured
- [ ] Re-submit flow documented

## Anti-patterns

- [ ] Critic not final judge
- [ ] No auto-publish
- [ ] No hidden approval skip

Reference: [human-approval-spec.md](../template-specs/human-approval-spec.md)
