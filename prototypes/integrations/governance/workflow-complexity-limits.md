# Workflow Complexity Limits

## Size Limits

| Metric | Limit |
|--------|-------|
| `minimal-demo.py` lines | ~350 max |
| Shared modules in `integrations/shared/` | 1 utility file |
| Steps per workflow | ≤ 8 visible stages |
| Scenarios per demo | ≤ 6 CLI flags |
| External dependencies | stdlib + `prototypes/shared/` |

## Complexity Budget

Each workflow may add **at most one** new concept beyond Phase 2.0:

| Workflow | New concept |
|----------|-------------|
| review-queue | queue + review chaining |
| gui-safe-action | verify then approve chain |
| governed-promotion | anti-pattern scan stage |
| bounded-memory-review | writeback after critique |
| escalation | uncertainty routing |

## Readability Test

A reader must trace the full workflow in one file without jumping to 3+ modules.

## Time Budget

Target: **< 45 minutes** to read workflow.md + minimal-demo.py + failure-modes.md.
