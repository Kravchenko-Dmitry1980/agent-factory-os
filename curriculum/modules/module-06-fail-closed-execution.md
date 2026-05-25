# Module 06 — Fail-Closed Execution

## Goal

When uncertain, **deny** — do not proceed by default.

## Simple Explanation

**Fail-closed** = absence of proof of safety is treated as unsafe. Missing approval, failed verification, ambiguous GUI → stop.

## Key Ideas

- Deny-by-default
- Uncertainty is not permission
- Fail-open is hidden autonomy
- External systems are untrusted input

## Files to Read

- `agent-os/doctrine/fail-closed-execution.md`
- `agent-os/08_patterns/fail-closed-defaults.md`
- [../lessons/lesson-fail-closed.md](../lessons/lesson-fail-closed.md)

## Commands to Run

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario uncertain
python prototypes/fail-closed-external-action/minimal-demo.py --scenario rejected
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

## Exercise

[../exercises/exercise-block-unsafe-action.md](../exercises/exercise-block-unsafe-action.md)

## Common Mistakes

- Default allow on timeout
- Best-effort proceed on GUI uncertain
- Catch-all exception that continues workflow

## Checkpoint Questions

1. Define fail-closed in one sentence.
2. Give fail-open example.
3. Which demo shows bypass blocked?

## Expected Outcome

Student contrasts fail-closed vs fail-open with repo examples.
