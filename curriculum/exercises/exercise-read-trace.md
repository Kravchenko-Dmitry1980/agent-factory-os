# Exercise: Read Trace

## Purpose

Read a trace and explain the story — who decided what.

## Time

25 minutes

## Steps

1. Read `observability/workflow-tracing/minimal-trace-format.md`
2. Study two traces:
   - `observability/examples/successful-review-trace.txt`
   - `observability/examples/failed-review-trace.txt`
3. Answer in writing:
   - First event? Last event?
   - Where is human gate?
   - OUTCOME status?

4. Optional: run matching demo and compare audit wording

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
```

## Expected Result

Written narrative (5–8 sentences) per trace.

## What To Observe

- advisory critic on happy trace
- human deny on failed trace despite critic pass

## Questions

1. Why is failed trace valuable for training?
2. What would bad trace look like?

See `evaluation/trace-comparison/good-trace-vs-bad-trace.md`

## Pass Criteria

Correct event order; explains human deny case; defines trace in own words.

## Fail Criteria

Only describes OUTCOME; misses approval_requested.
