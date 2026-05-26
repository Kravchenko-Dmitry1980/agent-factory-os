# Failure Trace Template

Copy and fill for rejection / hard-fail scenarios.

```
TRACE id=<trace-id> workflow=<agent-name> scenario=<scenario-name>
────────────────────────────────────────────────────────
[<time>] task_started         actor=<orchestrator>  task_id=<id>
[<time>] verification_passed|verification_failed  actor=critic  advisory=true verdict=<pass|fail|uncertain>
[<time>] approval_requested   actor=human           required=true
[<time>] approval_denied       actor=human           reason=<reason>
[<time>] task_failed           actor=system          reason=<terminal-reason>
────────────────────────────────────────────────────────
OUTCOME status=rejected
GOVERNANCE gates_passed=<n> gates_failed=<m> escalated=no
```

## Variant: verification failure (no approval reached)

```
[<time>] task_started
[<time>] verification_failed  actor=<gate>  reason=<reason>
[<time>] task_failed          actor=system  reason=verification_failed
OUTCOME status=failed
```

Reference: `observability/examples/failed-review-trace.txt`

Note: critic may pass — human still catches error. **critic ≠ truth.**
