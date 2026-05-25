# FastAPI Review API — Contracts

## Inputs

| Endpoint | Body | Required |
|----------|------|----------|
| POST /submit | `{content, source}` | yes |
| POST /review/{id}/approve | — | pending only |
| POST /review/{id}/reject | `{reason}` | pending only |

## Outputs

| Field | Type | When |
|-------|------|------|
| `id` | string | submit |
| `status` | pending/approved/rejected | always |
| `audit_id` | string | on transition |

## Verification

- Content non-empty on submit
- State machine enforced (no skip to approved)

## Approval Boundaries

- No auto-approval
- Explicit POST to approve/reject

## Escalation

- Invalid transition → 409 + audit failure record

## Failure States

| State | HTTP |
|-------|------|
| Invalid transition | 409 |
| Not found | 404 |
| Empty content | 400 |
