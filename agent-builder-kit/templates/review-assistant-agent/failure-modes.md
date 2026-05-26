# Review Assistant Agent — Failure Modes

| Failure | Symptom | Guard | Trace signal |
|---------|---------|-------|--------------|
| Hallucinated draft | False facts in output | Verification + human review | `verification_failed` or human deny |
| Weak critique | Critic misses errors | Human is final authority | critic pass + `approval_denied` |
| Critic as truth | Auto-delivery on critic pass | Advisory flag; human gate | missing `approval_requested` |
| Missing approval | Delivery without human | Fail-closed | `unsafe_action_blocked` |
| Silent publish | No audit on delivery | Required trace events | gap before `task_completed` |
| Unbounded revision loop | Infinite draft/critic cycles | Escalation + cap | repeated events, no terminal |
| Unclear output | User cannot review draft | Format verification | `verification_failed` |
| Hidden memory writeback | Profile grows silently | memory-boundary v0.1 off | `memory_write_rejected` |

## Operator Response

1. Read trace — identify last gate event
2. If `approval_denied` — accept terminal fail or restart with new input
3. If `verification_failed` + uncertain — escalate, do not auto-proceed
4. If bypass suspected — check for `unsafe_action_blocked`

## Prototype Reference

`prototypes/review-loop-agent/failure-modes.md` (reference only)
