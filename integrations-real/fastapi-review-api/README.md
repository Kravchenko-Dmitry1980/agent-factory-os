# FastAPI Review API

Minimal governed HTTP API: submit → pending → approve/reject → immutable audit.

## Run

```powershell
python integrations-real/fastapi-review-api/minimal-demo.py
python integrations-real/fastapi-review-api/minimal-demo.py --scenario invalid-transition

# Optional: start server locally
python integrations-real/fastapi-review-api/minimal-demo.py --serve
```

SQLite storage. No auth platform. No DB cluster.
