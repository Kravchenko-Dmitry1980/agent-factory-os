# Workshop: 2-Hour Practical

## Audience

New developers or interns day 1.

## Duration

2 hours

## Goal

Run core safety demos; read fail trace; introduce evaluation.

## Agenda

| Block | Content |
|-------|---------|
| 0:00–0:30 | workshop-30-min-intro content |
| 0:30–1:00 | fail-closed + bounded memory demos |
| 1:00–1:20 | failed-review + escalation traces |
| 1:20–1:40 | [../lessons/lesson-fail-closed.md](../lessons/lesson-fail-closed.md) discussion |
| 1:40–2:00 | [../assessments/beginner-assessment.md](../assessments/beginner-assessment.md) Q&A |

## Files to Open

- observability/examples/failed-review-trace.txt
- observability/examples/escalation-trace.txt

## Commands to Run

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
python evaluation/scripts/check_expected_text_traces.py
```

## Discussion Questions

1. fail-closed in one sentence?
2. Why memory limit?
3. What happens at max retries?

## Expected Learning Outcome

Participant completes two exercises from `exercises/` as homework.
