# Review Queue — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `task_description` | string | yes |
| `scenario` | CLI flag | no |

## Outputs

| Field | Type | When |
|-------|------|------|
| `queue_status` | enum | terminal |
| `published` | bool | terminal |
| `escalated` | bool | if triggered |
| `audit_trail` | list | always |

## Verification Points

- Draft non-empty before critique
- Critic verdict recorded before human review
- Publish only after `human_approved=True`

## Escalation Points

- Retry exhaustion (critic fail × max)
- Uncertain critic + no human override
- Queue corruption detected

## Approval Boundaries

- Human must explicitly approve publish
- Critic pass alone insufficient
- Approval denied → terminal reject, no publish

## Failure States

| State | Trigger |
|-------|---------|
| `CRITIC_DISAGREEMENT` | Human rejects despite critic pass |
| `RETRY_EXHAUSTED` | Max rework reached |
| `APPROVAL_DENIED` | Human reject |
| `ESCALATED` | Supervisor path |
| `QUEUE_CORRUPT` | Invalid queue state |
