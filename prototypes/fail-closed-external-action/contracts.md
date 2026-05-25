# Fail-Closed External Action — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `action_type` | string | yes |
| `payload` | dict | yes |
| `risk_level` | low/medium/high | yes |
| `approval` | bool \| null | for gate |

## Outputs

| Field | Type | When |
|-------|------|------|
| `verification` | pass/fail/uncertain | pre-gate |
| `executed` | bool | terminal |
| `denial_reason` | string | if denied |
| `audit_trail` | list | always |

## Verification Points

1. Action schema valid
2. Risk assessment recorded
3. High-risk requires human approval

## Failure States

| State | Meaning |
|-------|---------|
| `DENY_DEFAULT` | No approval provided |
| `DENY_UNCERTAIN` | Verification uncertain |
| `DENY_REJECTED` | Explicit rejection |

## Escalation Points

- High-risk + no approval → queue for human
- Uncertain verification → deny, escalate
