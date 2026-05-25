# Scenario: Promotion Pipeline

## What It Teaches

Ideas enter curated corpus only through governance gates — provenance, risk, topology checks.

## What Can Go Wrong

- Promote without source
- Swarm topology without contracts
- Plausible prose as architecture

## Correct Safe Behavior

- `promote` → valid artifact passes simulation
- `reject` → bad provenance/scores blocked
- Integration: `missing-provenance`, `dangerous-topology` rejected

## Files to Run

```powershell
python prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario promote
python prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario reject
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py --scenario missing-provenance
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py --scenario dangerous-topology
```

## Traces to Inspect

- Demo audit (governance_rejection events)

## Evaluation Checks

- `evaluation/scenarios/promotion-pipeline-scenarios.md`
- Smoke: `promotion reject`

## Deep Docs

- `governance/PROMOTION_STRATEGY.md`
- [../operator-checklists/before-promoting-idea.md](../operator-checklists/before-promoting-idea.md)
