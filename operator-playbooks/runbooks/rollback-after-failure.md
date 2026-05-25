# Rollback After Failure

## Purpose

Restore known-good governance when a change breaks behavior or gates.

## When to Use

- Smoke checks FAIL after your change
- Approval gate missing from trace
- Retry ceiling silently increased
- Mentor says stop

## Commands

### Git rollback (if change committed)

```powershell
git status
git diff
git checkout -- path/to/file.py
# or
git revert HEAD
```

### Re-verify after rollback

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
```

### Preserve notes

Write what failed in local notes — optional `evaluation/reports/` or change proposal failure section.

## Expected Result

- Smoke returns to PASS
- Trace gate chain restored
- Audit explains decisions again

## Common Failures

| Situation | Action |
|-----------|--------|
| Rollback but still FAIL | Failure predates your change — see troubleshooting |
| Partial rollback | Rollback all touched files in shared modules |
| No git | Restore files from last known good copy |

## What to Do If Rollback Doesn't Help

1. [../troubleshooting/common-errors.md](../troubleshooting/common-errors.md)
2. Compare with `evolution/examples/rollback-success.md`
3. Ask for help — do not stack patches

## What NOT to Do

- Add retries to "fix" verification failures
- Remove escalation to make demo pass
- Disable smoke check entries instead of fixing behavior

Deep dive: `evolution/rollback-thinking/rollback-strategies.md`

Guide: [../change-guides/how-to-decide-rollback.md](../change-guides/how-to-decide-rollback.md)
