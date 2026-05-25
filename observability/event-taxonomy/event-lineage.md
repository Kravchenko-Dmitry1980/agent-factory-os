# Event Lineage

Events form **chains**, not isolated log lines.

## Lineage Pattern

```
task_started
  → verification_passed | verification_failed
  → approval_requested (if external/high-risk)
  → approval_denied | approval_timeout | (implicit approve)
  → task_completed | escalation_triggered | task_failed
```

## Parent Links

Use `parent_id` or `correlation_id` in append-only audit (see `integrations-real/filesystem-audit-log/`).

Example:

```
e1 task_started
e2 verification_failed     parent=e1
e3 retry_triggered         parent=e2
e4 retry_exhausted         parent=e3
e5 escalation_triggered    parent=e4
```

## Readable Lineage Question

> Can a human reconstruct the story in 60 seconds from the chain alone?

If no — add events, not metrics.

## Anti-Pattern

Flat logs with identical `INFO` level and no causal links — lineage destroyed.
