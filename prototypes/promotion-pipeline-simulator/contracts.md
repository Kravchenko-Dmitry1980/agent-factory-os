# Promotion Pipeline — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `source_path` | string | yes |
| `artifact_type` | pattern/glossary/anti-pattern | yes |
| `scores` | value, maturity, fit, risk (1-5) | yes |
| `provenance` | origin corpus, extraction date | yes |

## Outputs

| Field | Type | When |
|-------|------|------|
| `decision` | PROMOTE_NOW / PROMOTE_LATER / RESEARCH_ONLY / REJECT | terminal |
| `rejection_reason` | string | if rejected |
| `audit_trail` | list | always |
| `target_path` | string | if promoted |

## Verification Points

- Provenance complete
- No stage skipping (research → review → governance)
- Dedup check against agent-os index (mock)

## Failure States

| State | Meaning |
|-------|---------|
| `MISSING_PROVENANCE` | Reject |
| `HIGH_RISK` | PROMOTE_LATER or REJECT |
| `DUPLICATE` | REJECT with reason |

## Escalation Points

- PROMOTE_LATER → governance backlog
- REJECT → log reason, no silent drop
