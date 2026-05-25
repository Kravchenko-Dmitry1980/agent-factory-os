# Review Loop — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `task_id` | string | yes |
| `task_description` | string | yes |
| `draft` | string | after draft step |

## Outputs

| Field | Type | When |
|-------|------|------|
| `critique_verdict` | `pass \| fail \| uncertain` | after critique |
| `critique_notes` | string | after critique |
| `human_decision` | `approve \| reject \| pending` | after review |
| `published` | bool | terminal |
| `audit_trail` | list | always |

## Verification Points

1. **Post-draft:** draft non-empty
2. **Post-critique:** verdict recorded (critic cannot publish)
3. **Pre-publish:** `human_decision == approve` AND `critique_verdict != uncertain`

## Failure States

| State | Meaning | Next action |
|-------|---------|-------------|
| `BLOCKED_UNCERTAIN` | Critic uncertain | Human must inspect manually |
| `REWORK_EXHAUSTED` | Max rework reached | Escalate, no auto-publish |
| `REJECTED` | Human rejected | Stop, no publish |
| `BYPASS_DENIED` | Publish without approval attempted | Fail-closed deny |

## Escalation Points

- Critic `uncertain` → human review required before any publish
- Rework count ≥ max → human escalation with blocked flag
- Human reject → terminal, log reason
