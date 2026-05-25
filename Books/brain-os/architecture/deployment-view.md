# Deployment View

```
[API Gateway]
    ├── brain-api
    │     ├── task-classifier
    │     ├── cognitive-router
    │     ├── policy-engine
    │     ├── reasoning-orchestrator
    │     ├── execution-supervisor
    │     ├── evaluation-engine
    │     ├── safety-service
    │     └── trace-service
    ├── memory-orchestrator (+ stores + vector index)
    ├── sandbox-service
    ├── agent-service
    └── event-bus
```

## Reference Stack (рекомендация автора)

FastAPI + Redis + Postgres + Qdrant — **interpretation**, не часть immutable source.

## Maturity

promising

## Provenance

`source/Brain OS.docx` C.§1; `source/Brain OS MD.docx` §22
