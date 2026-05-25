# Scenario: Fail-Closed Action

## What It Teaches

External/high-risk actions need verification + approval. **Missing approval = deny.**

## What Can Go Wrong

- Default allow
- Timeout → proceed
- Execute on rejected approval

## Correct Safe Behavior

- `no-approval` → execute denied
- `rejected` → execute denied
- `approved` → full gate chain in audit

## Files to Run

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario approved
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/fail-closed-external-action/minimal-demo.py --scenario rejected
python integrations-real/telegram-review-gate/minimal-demo.py
```

## Traces to Inspect

- `observability/examples/failed-review-trace.txt` (approval pattern)

## Evaluation Checks

- `evaluation/scenarios/fail-closed-action-scenarios.md`
- Smoke: `fail-closed no-approval`

## Deep Docs

- [../safety-guides/why-fail-closed-matters.md](../safety-guides/why-fail-closed-matters.md)
- [../safety-guides/why-approval-is-required.md](../safety-guides/why-approval-is-required.md)
