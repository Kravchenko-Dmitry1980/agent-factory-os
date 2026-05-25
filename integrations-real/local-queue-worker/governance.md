# Local Queue Worker — Governance

| Rule | Implementation |
|------|----------------|
| Local persistence | SQLite file in `.data/` |
| Retry ceiling | MAX_RETRIES = 3 |
| Fail-closed stop | No infinite retry |
| Audit events | JSONL + DB status |
| Queue recovery | Reload pending on start |

## Alignment

- `prototypes/queue-orchestration/`
- `integrations-real/governance/local-first-policy.md`
