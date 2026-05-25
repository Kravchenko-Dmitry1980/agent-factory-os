# Real Integration Boundaries

## In Scope

- Single-process local adapters
- Optional real API calls (Telegram, OpenAI, HTTP)
- SQLite or JSON file persistence
- Append-only filesystem audit
- Mock mode without credentials

## Out of Scope

- Cloud deployment
- Distributed queues (Redis, Kafka, Celery)
- Microservices
- Universal adapter framework
- MCP runtime
- Production auth platform

## Stop Signals

| Signal | Action |
|--------|--------|
| Adapter imports another adapter's core logic | Refactor to duplicate or stop |
| Shared `BaseAdapter` class | Delete |
| Config-driven adapter discovery | Delete |
| Multi-tenant API | Out of scope |

## Data Locality

All persistent state under `integrations-real/.data/`. No remote DB.
