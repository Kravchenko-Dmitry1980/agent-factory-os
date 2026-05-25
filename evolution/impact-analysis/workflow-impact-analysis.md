# Workflow Impact Analysis

## Dimensions

| Dimension | Questions |
|-----------|-----------|
| **Stage order** | Did any step move before verification? |
| **Terminal states** | New success path without audit? |
| **HITL** | Human still mandatory where required? |
| **Fail-closed** | Uncertain still denies? |
| **Cross-workflow** | Does integration import create coupling? |

## Trace Test

Compare traces before/after using [observability/workflow-tracing/](../../observability/workflow-tracing/minimal-trace-format.md).

Missing events = impact.

## Repository Zones

| Zone | Impact sensitivity |
|------|-------------------|
| `prototypes/integrations/` | High — composed gates |
| `integrations-real/` | High — real I/O |
| `prototypes/shared/` | Medium — shared gates |
| `observability/` | Low — docs |
| `evolution/` | Low — docs |

## Red Flag

One workflow change forces edits in 3+ unrelated demos — hidden coupling.
