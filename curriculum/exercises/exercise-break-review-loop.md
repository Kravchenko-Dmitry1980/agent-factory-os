# Exercise: Break Review Loop (Observe, Don't Code)

## Purpose

Learn failure modes **documented** in the repo — without modifying code.

## Time

20 minutes

## Steps

1. Read `prototypes/review-loop-agent/failure-modes.md`
2. Run scenarios:

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario uncertain-critic
python prototypes/review-loop-agent/minimal-demo.py --scenario human-overrides-block
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

3. For each: note Published? Block reason? Audit events?

## Expected Result

Each fail scenario stops without unsafe publish.

## What To Observe

- Uncertainty does not auto-publish
- Human can reject
- Bypass denied

## Questions

1. Which scenario shows critic != final authority?
2. What would happen if bypass were allowed?

## Pass Criteria

Matches failure-modes.md; explains one silent failure if gate removed.

## Fail Criteria

Confuses scenarios; cannot explain bypass risk.

**Do not** edit prototype code in this exercise.
