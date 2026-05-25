# Local Queue Worker

Durable local task queue with retry ceiling and recovery.

## Run

```powershell
python integrations-real/local-queue-worker/minimal-demo.py
python integrations-real/local-queue-worker/minimal-demo.py --scenario retry-exhaustion
python integrations-real/local-queue-worker/minimal-demo.py --scenario recovery
```

SQLite only. No Redis/Celery/Kafka.
