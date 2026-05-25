# Adapter Complexity Limits

| Metric | Limit |
|--------|-------|
| `minimal-demo.py` | ~350 lines |
| Files per adapter (excl. docs) | ≤ 2 code files preferred |
| External pip deps | fastapi/httpx optional only |
| Network timeout | ≤ 30 seconds |
| Retry ceiling | ≤ 3 (explicit in code) |
| SQLite tables per adapter | ≤ 2 |

## Time Budget

Understand adapter in **< 60 minutes** (README + contracts + demo).

## Realism Budget

Each adapter adds **one** real I/O concern:

| Adapter | Real concern |
|---------|--------------|
| telegram-review-gate | Human async approval + timeout |
| fastapi-review-api | HTTP state machine |
| llm-verification-adapter | Untrusted model output |
| local-queue-worker | Crash recovery |
| filesystem-audit-log | Append-only lineage |

No adapter may solve two real concerns (e.g. queue + LLM in one).
