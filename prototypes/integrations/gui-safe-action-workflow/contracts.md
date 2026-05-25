# GUI Safe Action — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `screen_id` | mock id | yes |
| `action` | click descriptor | yes |
| `approval` | bool \| null | for high-risk |

## Outputs

| Field | Type | When |
|-------|------|------|
| `outcome` | A/B/C | after verify |
| `executed` | bool | terminal |
| `denial_reason` | string | if rejected |

## Verification Points

- Visual A/B/C before execution
- Approval for `risk=high` actions

## Escalation Points

- Repeated C outcomes → circuit breaker (2 strikes)

## Approval Boundaries

- High-risk: payment, delete, send — require explicit True
- Low-risk: navigate — still logged, verify required

## Failure States

| State | Meaning |
|-------|---------|
| `MISMATCH` | Outcome B |
| `NO_CHANGE` | Outcome C |
| `UNCERTAIN` | Cannot determine state |
| `NO_APPROVAL` | Deny-by-default |
