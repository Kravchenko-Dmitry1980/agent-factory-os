# Escalation Trace Template

Copy and fill when automation stops and human operator must decide.

```
TRACE id=<trace-id> workflow=<agent-name> scenario=<scenario-name>
────────────────────────────────────────────────────────
[<time>] task_started         actor=<orchestrator>  task_id=<id>
[<time>] verification_failed  actor=critic          advisory=true verdict=uncertain reason=<reason>
[<time>] escalation_triggered actor=system          reason=<why-escalated>
[<time>] approval_requested   actor=supervisor      required=true
[<time>] verification_passed|approval_denied  actor=supervisor  decision=<approve|deny>
[<time>] task_completed|task_failed  actor=system  outcome=<final>
────────────────────────────────────────────────────────
OUTCOME status=<completed|rejected|held>
GOVERNANCE gates_passed=<n> gates_failed=<m> escalated=yes
```

## When to use

- Critic uncertain
- Policy conflict
- Repeated verification failure
- Operator override needed

## Fail-closed default

Until supervisor decides: **no publish**, **no external action**.
