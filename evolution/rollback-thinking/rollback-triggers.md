# Rollback Triggers

Automatic **human decision** to rollback (no bot required).

| Trigger | Threshold |
|---------|-----------|
| Missing gate event in trace | Any required event absent |
| Auto-approve observed | `approval_requested` skipped |
| Retry storm | retries > ceiling in prod-like test |
| Escalation suppressed | max retries without escalate log |
| New shared/ module | Any Phase 2.x shared growth |
| Real adapter default-on | Mock no longer works offline |
| Governance review reject | PROMOTION / phase review fail |

## Time Triggers

- **30 min** stuck on forward fix during gate regression → rollback
- **Before merge** if checklist incomplete → do not merge

## Post-Rollback Validation

Re-run:

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
```

All failure scenarios must still fail closed.
