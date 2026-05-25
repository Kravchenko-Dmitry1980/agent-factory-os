# Exercise: Block Unsafe Action

## Purpose

See fail-closed deny when approval missing or rejected.

## Time

15 minutes

## Steps

1. Read [../lessons/lesson-fail-closed.md](../lessons/lesson-fail-closed.md)
2. Run:

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/fail-closed-external-action/minimal-demo.py --scenario rejected
python prototypes/fail-closed-external-action/minimal-demo.py --scenario approved
```

3. Compare Execute line and audit across three runs

## Expected Result

no-approval + rejected: denied. approved: mock execute after gates.

## What To Observe

- Deny message explicit
- Approved still shows verification + approval in audit

## Questions

1. Default when approval missing?
2. Difference rejected vs no-approval?

## Pass Criteria

States deny-by-default; describes approved gate chain.

## Fail Criteria

Thinks no-approval executes; cannot read audit.
