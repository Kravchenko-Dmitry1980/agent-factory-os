# Promotion Pipeline — Failure Modes

## Hallucination

Promoted note contains unverified claims from research. **Mitigation:** review stage + provenance required.

## Retry Loops

Re-submit same artifact after reject without changes. **Mitigation:** rejection reason stored; re-submit flagged.

## Missing Verification

Skip governance stage. **Mitigation:** pipeline enforces ordered stages.

## Memory Drift

Canonical doc diverges from source without trace. **Mitigation:** provenance metadata on every record.

## Unsafe Autonomy

Auto-promote on high value score alone. **Mitigation:** decision matrix uses risk + maturity.

## Missing Escalation

PROMOTE_LATER items vanish. **Mitigation:** audit + backlog status.

## Governance Bypass

Direct copy experiment → agent-os. **Mitigation:** simulator rejects without governance stage pass.
