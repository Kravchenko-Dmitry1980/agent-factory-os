# Integration Boundaries

## In Scope (Phase 2.1)

- Linear composed workflows in single `minimal-demo.py` files
- Explicit scenario flags for failure cases
- Reuse of `prototypes/shared/` audit and gates only
- Mermaid diagrams per workflow

## Out of Scope

- Framework extraction from Phase 2.0 demos
- Cross-workflow import of demo modules
- Durable queue, real GUI, real external APIs
- Production deployment artifacts

## Stop Signals

| Signal | Action |
|--------|--------|
| `integrations/shared/` > 2 files | Freeze and review |
| Base class shared across workflows | Remove it |
| Workflow config files (YAML/JSON driving steps) | Remove it |
| Generic `Step` protocol | Remove it |
| Event bus between steps | Remove it |

## Promotion

Workflow insights → governance review → doctrine/pattern docs.

Workflow **code** stays in `prototypes/integrations/` permanently.
