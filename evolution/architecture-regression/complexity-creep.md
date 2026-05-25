# Complexity Creep

Complexity grows invisibly when problems are patched forward.

## Signals

| Metric | Creep |
|--------|-------|
| Lines per `minimal-demo.py` | > 350 |
| Files in `shared/` | > 2 per phase |
| Scenarios per demo | > 6 without split |
| Indirection layers | Engine between steps |
| Cross-imports | Demos import demos |

## Law

Complexity should grow in **documentation**, not **runtime abstraction**.

## Response

Delete abstraction, duplicate logic, restore linear flow.

## Reference Budget

[prototypes/integrations/governance/workflow-complexity-limits.md](../../prototypes/integrations/governance/workflow-complexity-limits.md)
