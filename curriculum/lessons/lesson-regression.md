# Lesson: Regression

## What is this?

**Regression** = something that worked safely **stopped** working safely after a change.

## Why does it matter?

AI/gate regressions are often silent — demo still exits 0 while approval disappeared.

## What can go wrong?

- Fewer audit events with same flow
- Fail-path demo now "succeeds"
- Retry ceiling raised without review

## How do we check it?

Before/after smoke + trace compare. See regression matrix.

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
```

`evaluation/trace-comparison/trace-regression-examples.md`

## Which demo shows it?

Any demo after a change — compare to baseline. Escalation trace is canonical regression teaching example.

Exercise: [../exercises/exercise-run-evaluation.md](../exercises/exercise-run-evaluation.md)
