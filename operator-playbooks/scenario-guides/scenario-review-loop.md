# Scenario: Review Loop

## What It Teaches

Draft → critic (advisory) → human review → publish. **Critic is not truth.**

## What Can Go Wrong

- Critic pass treated as approval
- Bypass publish without human
- Uncertain critic auto-publishes

## Correct Safe Behavior

- Human gate before external publish
- Bypass blocked
- Uncertainty fails closed

## Files to Run

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python prototypes/review-loop-agent/minimal-demo.py --scenario uncertain-critic
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
```

## Traces to Inspect

- `observability/examples/successful-review-trace.txt`
- `observability/examples/failed-review-trace.txt`

## Evaluation Checks

- `evaluation/scenarios/review-loop-scenarios.md`
- Smoke: `review-loop happy`, `review-loop bypass blocked`

## Deep Docs

- `prototypes/review-loop-agent/README.md`
- `evaluation/scenario-guides` → [../safety-guides/why-critic-is-not-truth.md](../safety-guides/why-critic-is-not-truth.md)
