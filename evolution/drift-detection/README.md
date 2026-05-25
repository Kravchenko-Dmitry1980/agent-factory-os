# Drift Detection

Detect architecture and governance erosion early.

## Drift Types

| Type | See |
|------|-----|
| Framework drift | [drift-patterns.md](drift-patterns.md) |
| Telemetry drift | observability platform creep |
| Orchestration drift | workflow engine extraction |
| Autonomy drift | silent auto-execute |
| Verification drift | critic = truth |
| Memory drift | unbounded writeback |
| Platform drift | universal adapters |

## Files

- [drift-patterns.md](drift-patterns.md)
- [early-warning-signals.md](early-warning-signals.md)
- [hidden-drift-analysis.md](hidden-drift-analysis.md)
- [drift-prevention.md](drift-prevention.md)

## Cadence

Review drift signals when touching `prototypes/`, `integrations-real/`, or `shared/`.

Cross-check [governance/ARCHITECTURAL_DRIFT_REPORT.md](../../governance/ARCHITECTURAL_DRIFT_REPORT.md) if present.
