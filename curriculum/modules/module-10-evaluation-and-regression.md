# Module 10 — Evaluation and Regression

## Goal

Check that behavior **stayed safe** after learning or after a change.

## Simple Explanation

**Evaluation** here is local behavioral checking: run demos, compare traces, use smoke scripts — not CI, not model leaderboard.

## Key Ideas

- Scenarios define expected behavior
- Smoke PASS ≠ full proof; human trace compare still matters
- Regression matrix maps change → re-checks
- No new automation in curriculum phase

## Files to Read

- `evaluation/README.md`
- `evaluation/regression-matrix/regression-matrix.md`
- [../lessons/lesson-regression.md](../lessons/lesson-regression.md)

## Commands to Run

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
python evaluation/scripts/summarize_evaluation_status.py
```

## Exercise

[../exercises/exercise-run-evaluation.md](../exercises/exercise-run-evaluation.md)

## Common Mistakes

- "It still runs" as only test
- Weakening smoke to get green
- Building pytest platform

## Checkpoint Questions

1. What three evaluation scripts exist?
2. What does smoke FAIL suggest?
3. Evaluation vs CI — difference?

## Expected Outcome

Student runs smoke and explains one PASS and one fail-path check.
