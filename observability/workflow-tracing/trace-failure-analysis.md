# Trace Failure Analysis

## Five Questions (Postmortem)

1. **Which gate was supposed to stop this?**
2. **Did that gate emit an event?**
3. **Was escalation correct or missing?**
4. **Did autonomy continue after deny?**
5. **Can we replay lineage without the model?**

## Failure Signatures

| Signature | Likely cause |
|-----------|--------------|
| `task_completed` without `verification_passed` | Verification bypass |
| Many `retry_triggered`, no `escalation_triggered` | Retry storm bug |
| `approval_timeout` then `task_completed` | Fail-closed broken |
| `llm_malformed_output` then `task_completed` | LLM trusted as truth |
| `memory_write_rejected` missing but store grew | Silent writeback |

## Cascade Reading

Read bottom-up from terminal event:

```
escalation_triggered
  ← retry_exhausted
    ← verification_failed (×3)
      ← task_started
```

## Action

Fix **gate or event naming** in workflow — not add Grafana panel.
