# Review Queue Workflow

**Composes:** queue orchestration + review loop + escalation + approval gate.

## Flow

```
task → queue → draft → critique → review → approve/reject → publish
```

## Scenarios

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario critic-disagreement
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario retry-exhaustion
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario escalation
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario queue-corruption
```

## Phase 2.0 Sources

- `prototypes/queue-orchestration/`
- `prototypes/review-loop-agent/`

Composition is **inline** — no imports from those demos.
