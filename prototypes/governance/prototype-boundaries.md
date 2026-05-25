# Prototype Boundaries

## What Prototypes ARE

- Executable teaching aids
- Contract sketches with runnable gates
- Failure-mode catalogs with one happy path + one fail path
- Evidence that governance principles fit in small code

## What Prototypes ARE NOT

| Forbidden evolution | Why |
|---------------------|-----|
| Production platform | Ops burden hides governance lesson |
| Orchestration runtime | Becomes framework maintenance |
| Agent swarm | Autonomy scope explodes |
| LangGraph / CrewAI stack | Teaches vendor API, not boundaries |
| RAG / vector pipeline | Infra distraction |
| Graph DB / ontology runtime | Wrong phase |
| MCP server | Protocol ≠ governance |
| Digital twin runtime | Identity scope unbounded |
| Self-improving agents | Violates verification-before-writeback |
| Cloud deployment | Not the learning goal |

## Stop Signals (Runtime Drift)

Stop and refactor if you observe:

1. **Abstract base classes** for "Agent" appearing across prototypes
2. **Plugin registry** or **dependency injection container**
3. **More than 3 shared modules** in `shared/`
4. **Async event bus** between prototype components
5. **Configuration YAML** driving behavior instead of readable code
6. **Test suite larger than demo code**

## Allowed Extensions (Still Prototype)

- One additional scenario in `minimal-demo.py`
- New `failure-modes.md` section from incident review
- Diagram update in `diagrams/`
- Cross-link to new `agent-os/` pattern after promotion

## Promotion Path

Prototype → doctrine insight → governance review → `agent-os/` pattern.

**Never:** prototype → production repo copy.

See `governance/PROMOTION_STRATEGY.md` and `promotion-pipeline-simulator/`.
