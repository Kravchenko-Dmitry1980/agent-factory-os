# Anti-Platform Rules

Phase 2.2 must not become an integration platform.

## Forbidden

1. **`AdapterRegistry.register()`**
2. **`IntegrationEngine.run_pipeline()`**
3. **Plugin manifest files**
4. **Shared retry/escalation middleware hiding policy**
5. **Universal HTTP client with implicit auth**
6. **Docker Compose for adapter stack**
7. **Extracting `integrations-real/shared/` beyond path helpers**

## Allowed

1. Per-adapter `minimal-demo.py`
2. Per-adapter SQLite schema (not shared ORM)
3. Copy-paste of 10-line audit append
4. Environment variable for credentials

## Test

> Could this ship as `pip install agent-integrations`?

If yes — stop and delete abstractions.
