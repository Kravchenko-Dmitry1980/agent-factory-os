# Module 09 — Observability and Traces

## Goal

Read traces — ordered events that explain **why** a decision happened.

## Simple Explanation

A **trace** is a human-readable log: who did what, in what order, with what outcome. If you cannot read the trace, you cannot audit the system.

## Key Ideas

- Canonical events (task_started, approval_denied, etc.)
- OUTCOME and GOVERNANCE summary blocks
- Good trace vs bad trace (missing gates)
- critic != truth visible in trace

## Files to Read

- `observability/README.md`
- `observability/event-taxonomy/canonical-events.md`
- `evaluation/trace-comparison/good-trace-vs-bad-trace.md`
- [../lessons/lesson-audit-lineage.md](../lessons/lesson-audit-lineage.md)

## Commands to Run

Read all six files in `observability/examples/` (no runner).

Compare after:

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
```

## Exercise

[../exercises/exercise-read-trace.md](../exercises/exercise-read-trace.md)

## Common Mistakes

- Trusting exit code only
- Generic "error" without gate name
- Metrics without story

## Checkpoint Questions

1. What events appear in successful-review trace?
2. What makes failed-review trace teachable?
3. Define trace in your own words.

## Expected Outcome

Student walks through one example trace event-by-event aloud.
