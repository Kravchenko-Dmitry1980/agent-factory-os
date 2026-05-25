# Scenario: GUI Safe Action

## What It Teaches

Click only after visual verification. Mismatch and uncertainty **block** action.

## What Can Go Wrong

- Click on wrong screen
- "Looks fine" without verify step
- Uncertain UI → best-guess click

## Correct Safe Behavior

- `happy` → verify then act (mock)
- `outcome-b` → mismatch block
- `outcome-c` → uncertainty block

## Files to Run

```powershell
python prototypes/gui-verification-loop/minimal-demo.py --scenario happy
python prototypes/gui-verification-loop/minimal-demo.py --scenario outcome-b
python prototypes/gui-verification-loop/minimal-demo.py --scenario outcome-c
python prototypes/integrations/gui-safe-action-workflow/minimal-demo.py --scenario mismatch
```

## Traces to Inspect

- `observability/examples/unsafe-gui-action-trace.txt`

## Evaluation Checks

- `evaluation/scenarios/gui-verification-scenarios.md`
- Smoke: `gui outcome-b mismatch`

## Deep Docs

- `agent-os/01_agent-runtime/visual-grounding.md`
- `agent-os/09_antipatterns/unverified-gui-clicks.md`
