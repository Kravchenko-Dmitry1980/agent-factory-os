# Trace Does Not Match

## Symptom

Demo audit looks different from `observability/examples/*.txt`.

## This May Be OK

- Different demo (review-loop vs review-queue-workflow)
- Demo uses JSON audit; example uses canonical event names
- Timestamps differ

## Map using canonical events

Read: `observability/event-taxonomy/canonical-events.md`

Example mapping:

| Demo audit action | Canonical event |
|-------------------|-----------------|
| bypass_attempt | unsafe path blocked |
| timeout_denied | approval_timeout |

## This Is NOT OK

- Missing approval step on publish path
- Fewer events after your code change
- Generic "error" instead of gate name

**Action:** [../runbooks/rollback-after-failure.md](../runbooks/rollback-after-failure.md)

## Compare guide

`evaluation/trace-comparison/trace-diff-checklist.md`

`evaluation/trace-comparison/good-trace-vs-bad-trace.md`
