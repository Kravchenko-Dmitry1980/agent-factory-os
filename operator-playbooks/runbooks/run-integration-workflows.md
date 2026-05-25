# Run Integration Workflows

## Purpose

Run composed mock workflows under `prototypes/integrations/` — multi-step governance stories.

## When to Use

- After changing integration workflow code
- Teaching queue + review + escalation together
- Before touching real adapters

## Commands

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario happy
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
python prototypes/integrations/bounded-memory-review-workflow/minimal-demo.py --scenario happy
python prototypes/integrations/gui-safe-action-workflow/minimal-demo.py --scenario mismatch
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py --scenario missing-provenance
```

## Expected Result

- Workflow narrative in stdout
- Audit dump with gate events
- Deny/escalate scenarios stop before unsafe action

## Common Failures

| Symptom | Likely cause |
|---------|--------------|
| Import error from `prototypes.shared` | Broken shared module — high impact |
| Scenario not in choices | Typo in `--scenario` flag |

## What to Do If It Fails

1. Run single prototype equivalent first ([run-prototypes.md](run-prototypes.md))
2. If shared import fails — treat as high-risk; see [perform-safe-change.md](perform-safe-change.md)
3. [../troubleshooting/demo-does-not-run.md](../troubleshooting/demo-does-not-run.md)

## What NOT to Do

- Do not extract integrations into orchestration platform
- Do not disable gates to make demo "prettier"

Reference: [../../prototypes/integrations/README.md](../../prototypes/integrations/README.md)
