# High-Risk Changes

Require explicit human review + rollback plan before implementation.

| Change type | Why high risk |
|-------------|---------------|
| **Introducing autonomy** | Hidden execution paths |
| **Changing approval boundaries** | External harm |
| **Integrating new adapter** | Real I/O + trust boundaries |
| **Changing escalation policy** | Silent stall or runaway retry |
| **Adding memory writeback** | Durable pollution |
| **Removing verification step** | Fail-open |
| **Increasing retry without ceiling review** | Storm + cost |
| **Shared runtime extraction** | Platform drift |

## Mandatory

- Fill [change-template.md](change-template.md) completely
- [governance-gates/gate-checklists.md](../governance-gates/gate-checklists.md) all items
- Update or add [observability/examples/](../../observability/examples/) trace if workflow visible

## Default Answer

**Defer** until bounded prototype proves gate still holds.
