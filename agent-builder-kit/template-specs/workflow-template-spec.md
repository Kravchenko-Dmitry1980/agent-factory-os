# Workflow Template Spec

Standard safe workflow for agent templates.

---

## Standard Flow

```
input
  → validation
  → planning
  → draft / action proposal
  → verification
  → critique (optional)
  → human review
  → approval / rejection
  → output
  → audit / trace
  → optional writeback (gated)
```

---

## Stage Definitions

| Stage | Purpose | Fail-closed |
|-------|---------|-------------|
| **input** | Accept task and constraints | Reject malformed input |
| **validation** | Schema, scope, policy check | Block out-of-scope requests |
| **planning** | Decompose task (advisory) | No external actions |
| **draft / action proposal** | Produce candidate output | Mark as unverified |
| **verification** | Gate on facts, policy, format | Block on failure |
| **critique** | Optional advisory review | Never replaces verification |
| **human review** | HITL decision | Required for risky outputs |
| **approval / rejection** | Explicit terminal decision | Deny-by-default |
| **output** | Deliver approved result only | No delivery on reject |
| **audit / trace** | Record canonical events | Required, not optional |
| **optional writeback** | Persist to memory/system | Requires separate approval gate |

---

## Critical Rules

### Critique is optional and never replaces verification

- Critic output is **advisory**
- Critic pass ≠ verified truth
- Critic uncertain → fail-closed or escalate to human
- See `Books/swarm-playbooks/anti-patterns/critic-as-fake-verification.md`

### Human approval is required for risky outputs

- Publish, send, delete, pay, external API write → human gate
- No approval = no risky action
- Timeout → deny-by-default (`approval_timeout`)

### Verification before progress

- Every gate must emit `verification_passed` or `verification_failed`
- Failed verification stops forward progress unless human overrides with audit

---

## Workflow Variants

| Variant | When | Extra gates |
|---------|------|-------------|
| Read-only assistant | No external writes | verification only |
| Review assistant | Draft + human publish | approval + verification |
| Tool-using agent | External actions | tool-use gate + approval |

Phase 3.0 supports **Review Assistant** variant only.

---

## Related

- [human-approval-spec.md](human-approval-spec.md)
- [observability-trace-spec.md](observability-trace-spec.md)
- [diagrams/review-assistant-workflow.md](../diagrams/review-assistant-workflow.md)
