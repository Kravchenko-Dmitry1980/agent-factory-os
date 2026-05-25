# Filesystem Audit Log — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `actor` | string | yes |
| `action` | string | yes |
| `detail` | dict | optional |
| `parent_id` | string | for lineage |

## Outputs

| Field | Type | When |
|-------|------|------|
| `event_id` | string | each append |
| `lineage_chain` | list | query |

## Verification

- Append-only API (no update/delete methods)
- Timestamp UTC ISO

## Approval Boundaries

- `approval` events require `fingerprint` field

## Escalation

- `escalation` action type recorded explicitly

## Failure States

| State | Meaning |
|-------|---------|
| APPEND_FAIL | IO error |
| CORRUPT_LINE | Skip on read, audit warning |
| TAMPER_ATTEMPT | Update rejected |
