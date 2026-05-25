# LLM Verification — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `prompt` | string | yes |
| `timeout_seconds` | int | default 20 |

## Outputs

| Field | Type | When |
|-------|------|------|
| `raw_response` | string | after LLM |
| `verification` | pass/fail/uncertain | after verify |
| `decision` | accept/reject/escalate | terminal |

## Verification

- JSON schema when structured output requested
- Confidence heuristics (mock/real)
- LLM output never auto-trusted

## Approval Boundaries

- Accept requires verification pass
- Uncertain → escalate, not accept

## Escalation

- Timeout, malformed, uncertain → escalate

## Failure States

| State | Action |
|-------|--------|
| TIMEOUT | reject + escalate |
| MALFORMED | reject |
| UNCERTAIN | escalate |
| VERIFY_FAIL | reject |
