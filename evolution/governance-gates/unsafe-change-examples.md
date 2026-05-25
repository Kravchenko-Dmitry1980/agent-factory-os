# Unsafe Change Examples

| Change | Gate violated | Example file |
|--------|---------------|--------------|
| Remove human review on publish | Approval | review-loop demo |
| `MAX_RETRIES = 99` | Escalation | queue demos |
| Skip anti-pattern scan | Promotion | governed-promotion |
| Auto-execute on critic pass | Verification | review-queue |
| Delete audit append | Observability | filesystem-audit-log |
| Extract `WorkflowEngine` | Platform | integrations/shared |

Full narratives in [../examples/](../examples/).

## Pattern

Each example includes: intent → drift → symptom → rollback → lesson.
