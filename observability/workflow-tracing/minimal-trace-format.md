# Minimal Trace Format

Text-first, human-readable, no OpenTelemetry.

```
TRACE id=<short-id> workflow=<name> scenario=<optional>
────────────────────────────────────────────────────────
[HH:MM:SS] EVENT          actor=<who>  <key details>
...
────────────────────────────────────────────────────────
OUTCOME status=<completed|escalated|denied|failed>
GOVERNANCE gates_passed=<n> gates_failed=<n> escalated=<yes|no>
```

## Field Rules

| Field | Required | Notes |
|-------|----------|-------|
| `TRACE id` | yes | Correlate with audit file |
| `workflow` | yes | e.g. review-queue |
| `EVENT` | yes | Use [canonical events](../event-taxonomy/canonical-events.md) |
| `actor` | yes | executor, critic, human, gate, supervisor |
| `OUTCOME` | yes | Terminal state explicit |

## Size Limit

Target **≤ 25 lines** per trace example. If longer — split stages or summarize retries.

## Example Snippet

```
[19:56:59] task_started      actor=queue      task_id=cb81c378
[19:56:59] verification_passed actor=critic    verdict=pass (advisory)
[19:56:59] approval_requested  actor=human      required=true
[19:56:59] task_completed      actor=publisher  published=true
OUTCOME status=completed
```

See [../examples/](../examples/) for full traces.
