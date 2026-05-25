# Bounded Memory — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `entry` | string | for write |
| `verified` | bool | for write |
| `source` | string | for write |
| `keys` | list[str] | for context load |

## Outputs

| Field | Type | When |
|-------|------|------|
| `snapshot` | string | session start |
| `durable_size` | int | after write |
| `write_accepted` | bool | after write attempt |
| `context_loaded` | string | after explicit load |

## Verification Points

1. Pre-write: `verified == True`
2. Pre-write: projected size ≤ `MAX_MEMORY_CHARS`
3. Post-write: durable store consistent with audit

## Failure States

| State | Meaning |
|-------|---------|
| `WRITE_REJECTED_UNVERIFIED` | No verification flag |
| `WRITE_REJECTED_OVERFLOW` | Exceeds char budget |
| `SNAPSHOT_STALE` | Expected — snapshot != durable until next session |

## Escalation Points

- Repeated overflow → operator must prune durable store
- Verification failures → human review of proposed memory
