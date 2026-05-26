# Expected Trace Template

Copy and fill for happy-path scenarios.

```
TRACE id=<trace-id> workflow=<agent-name> scenario=<scenario-name>
────────────────────────────────────────────────────────
[<time>] task_started         actor=<orchestrator>  task_id=<id> goal=<short-goal>
[<time>] task_started         actor=<worker>        action=draft_created
[<time>] verification_passed  actor=<validator>     scope=<what-was-checked>
[<time>] verification_passed  actor=critic          advisory=true facts_verified=false
[<time>] approval_requested   actor=human           required=true
[<time>] verification_passed  actor=human           decision=approve
[<time>] task_completed       actor=<publisher>     delivered=true
────────────────────────────────────────────────────────
OUTCOME status=completed
GOVERNANCE gates_passed=<n> gates_failed=0 escalated=no
```

## Notes

- Critic line optional; if present, `advisory=true`
- Human gate mandatory before delivery for Review Assistant
- Reference: `observability/examples/successful-review-trace.txt`
