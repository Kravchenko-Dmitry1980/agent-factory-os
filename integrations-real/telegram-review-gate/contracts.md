# Telegram Review Gate — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `action_type` | string | yes |
| `payload` | dict | yes |
| `timeout_seconds` | int | default 5 (mock) |

## Outputs

| Field | Type | When |
|-------|------|------|
| `fingerprint` | string | on request |
| `approved` | bool \| null | terminal |
| `continued` | bool | terminal |

## Verification

- Fingerprint matches pending request before continue

## Approval Boundaries

- Explicit `/approve <fp>` or mock flag
- Timeout → deny (fail-closed)

## Escalation

- Deny + audit `escalated` when timeout with high-risk action

## Failure States

| State | Meaning |
|-------|---------|
| `TIMEOUT_DENIED` | No response in window |
| `INVALID_APPROVAL` | Fingerprint mismatch |
| `NETWORK_FAIL` | Telegram API error |
| `REJECTED` | Explicit reject |
