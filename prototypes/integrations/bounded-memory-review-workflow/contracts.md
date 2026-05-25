# Bounded Memory Review — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `curated_snapshot` | string | session start |
| `candidate_entry` | string | after execution |
| `verified` | bool | for writeback |

## Outputs

| Field | Type | When |
|-------|------|------|
| `critique_verdict` | pass/fail/uncertain | after critique |
| `write_accepted` | bool | terminal |
| `snapshot_unchanged` | bool | always true mid-session |

## Verification Points

- Critique before writeback consideration
- Verification pass required
- Size ceiling check

## Escalation Points

- Uncertain verification → human review (mock: block)

## Approval Boundaries

- Writeback requires verified=True AND critique != uncertain

## Failure States

| State | Trigger |
|-------|---------|
| `UNVERIFIED` | verified=False |
| `UNCERTAIN` | critique or verify uncertain |
| `OVERFLOW` | exceeds MAX_MEMORY_CHARS |
| `CRITIQUE_FAIL` | critic rejects entry |
