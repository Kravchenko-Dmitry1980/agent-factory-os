# Fail-Closed Gate

**Question:** Did unsafe action still block when approval/verification missing?

---

## Checks

- [ ] `no-approval` scenario: execute denied
- [ ] `uncertain` scenario: execute denied
- [ ] `rejected` scenario: execute denied
- [ ] Timeout path: deny, not approve
- [ ] Bypass attempt: blocked

## Commands

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/fail-closed-external-action/minimal-demo.py --scenario uncertain
python prototypes/fail-closed-external-action/minimal-demo.py --scenario rejected
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

## Pass

- No external/mock execute on deny paths
- Deny reason in output or audit

## Fail

- Default allow
- Execute despite missing approval
- Timeout → proceed

## Regression priority

**Critical** — rollback immediately if fail.
