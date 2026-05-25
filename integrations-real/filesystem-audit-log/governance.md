# Filesystem Audit Log — Governance

| Principle | Implementation |
|-----------|----------------|
| Append-only | `append()` only public mutator |
| Timestamped | UTC ISO on every event |
| Immutable records | no update/delete |
| Failure records | explicit failure action types |
| Escalation records | `action=escalated` |
| Lineage | `parent_id` chain |

## Alignment

- `agent-os/doctrine/` trace-first thinking
- `governance/PROMOTION_LOG.md` provenance style
