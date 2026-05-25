# Governance Over Speed

Speed is not a governance exception.

## Common Pressures

| Pressure | Wrong response | Right response |
|----------|----------------|----------------|
| Demo deadline | Skip HITL | Mock path only |
| "Internal only" | Auto-approve | Same gates |
| Flaky verify | Remove verify | Fix or escalate |
| Too many escalations | Raise retries | Fix root cause |
| Docs boring | Skip failure-modes | Update traces |

## Measure Success

- Gates intact after change
- Failure scenarios still fail closed
- New engineer understands traces

Not: lines shipped per day.

## Alignment

Doctrine: governance before autonomy (`agent-os/doctrine/`).
