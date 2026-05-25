# FastAPI Review API — Governance

| Rule | Implementation |
|------|----------------|
| Explicit states | pending → approved \| rejected |
| Verification before writeback | approve validates pending |
| Immutable audit | append-only audit table |
| Fail-closed | invalid transitions rejected |
| No auto-approval | no background jobs |

States are terminal — no reopen without new submit.
