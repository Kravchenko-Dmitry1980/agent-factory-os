# Workflow Log Examples

Mapped to [../examples/](../examples/) trace files.

| Workflow | Log focus |
|----------|-----------|
| Review queue | critic advisory + human approve |
| Escalation | uncertainty → retry → escalate |
| GUI safe action | visual verify before execute |
| Promotion | scan flags → governance_rejection |
| LLM verify | untrusted raw + format-only accept |

## Minimal Set per Run

1. `task_started`
2. At least one verification event
3. Terminal `OUTCOME` or canonical equivalent
4. If external action: `approval_requested` or block event

## Noise to Drop

- Token counts (unless debugging cost — separate note)
- Full prompt/response bodies in production-style logs
- Per-tool DEBUG in happy path

Demos may print audit dumps for education — document as **demo verbosity**, not target production style.
