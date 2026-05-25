# Governed Promotion — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `source_path` | string | yes |
| `provenance.origin` | string | yes |
| `content` | string | yes |
| `scores` | value/maturity/fit/risk | yes |

## Outputs

| Field | Type | When |
|-------|------|------|
| `decision` | enum | terminal |
| `scan_flags` | list | after anti-pattern scan |
| `rejection_reason` | string | if rejected |

## Verification Points

- Provenance non-empty
- Anti-pattern scan before governance
- Governance before simulated integrate

## Escalation Points

- PROMOTE_LATER → backlog (audit only)

## Approval Boundaries

- PROMOTE_NOW requires scan pass + governance pass
- Bypass attempt → reject

## Failure States

| State | Trigger |
|-------|---------|
| `MISSING_PROVENANCE` | Empty origin |
| `DANGEROUS_TOPOLOGY` | Scan flag |
| `UNSUPPORTED_CLAIMS` | Scan flag |
| `RESEARCH_LEAKAGE` | Non-canonical language in content |
| `GOVERNANCE_BYPASS` | Skip scan attempt |
