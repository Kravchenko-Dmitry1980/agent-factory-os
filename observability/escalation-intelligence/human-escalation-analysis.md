# Human Escalation Analysis

## When Humans Must Appear

| Situation | Human role |
|-----------|------------|
| External publish | Approve content |
| High-risk GUI action | Approve click |
| Uncertain verification | Judge evidence |
| Promotion governance | Policy decision |
| Post-retry-exhaustion | Unblock or cancel |

## What Human Should See

1. **What automation tried** (last N events)
2. **Why it stopped** (plain language)
3. **Fingerprint / task id** for approval
4. **What happens on timeout** (deny-by-default)

## Telegram Adapter Example

Human receives: action type + fingerprint + `/approve` or `/reject`.

Trace must show:

```
approval_requested → (wait) → approval_timeout | approved
```

## Anti-Pattern

Human sees only final error string with no lineage — escalation intelligence lost.
