# Bounded Rollout

Limit **blast radius** conceptually.

## Boundaries

| Boundary | Example |
|----------|---------|
| **Workflow** | Only review-queue, not all integrations |
| **Mode** | Mock before `--real` |
| **Scenario** | New `--scenario` before default change |
| **Directory** | One adapter under integrations-real |
| **Audience** | Solo dev machine before any shared env |

## Expansion Criteria

Expand only when:

- Failure scenarios pass
- Trace readable
- Rollback tested once
- Gate checklist green

## Stop

First missing gate event → stop expansion, rollback slice.
