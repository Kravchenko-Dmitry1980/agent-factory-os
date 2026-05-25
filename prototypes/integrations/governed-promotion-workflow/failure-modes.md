# Governed Promotion — Failure Modes

## Orchestration Drift

Multi-stage pipeline becomes ETL platform. **Mitigation:** linear functions, no engine.

## Queue Failure

N/A.

## Escalation Failure

PROMOTE_LATER items lost. **Mitigation:** audit backlog entry.

## Verification Bypass

Skip anti-pattern scan. **Scenario:** governance-bypass denied.

## Retry Storms

Re-submit rejected artifact unchanged. **Mitigation:** rejection reason stored.

## Memory Corruption

Provenance metadata drift. **Mitigation:** required fields check.

## Approval Bypass

Direct integrate without governance. **Mitigation:** ordered stages in run().

## Hidden Autonomy

Auto-promote on high value. **Mitigation:** scan + risk in matrix.

## Specific Cases

- **Missing provenance** — reject at review
- **Dangerous topology** — "universal multi-agent", "self-improving" flags
- **Unsupported claims** — "guaranteed", "100% autonomous"
- **Research leakage** — "TODO promote", "unreviewed" in content
