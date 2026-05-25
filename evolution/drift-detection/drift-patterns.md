# Drift Patterns

| Drift | Symptom | Repository example zone |
|-------|---------|-------------------------|
| **Framework** | BaseWorkflow, registry | `integrations/shared/` growth |
| **Telemetry** | Metrics before readable logs | new collector.py |
| **Orchestration** | YAML pipelines | workflow config files |
| **Autonomy** | Auto-approve internal | external-action demo |
| **Verification** | Skip verify on happy path | GUI/LLM adapters |
| **Memory** | Silent durable writes | bounded-memory demos |
| **Platform** | pip-installable package | evolution of shared libs |

## Phase History Watch

| Phase | Drift risk |
|-------|------------|
| 2.0 | Prototype → framework |
| 2.1 | Integration → orchestrator |
| 2.2 | Adapter → platform SDK |
| 2.3 | Observability → monitoring stack |
| 2.4 | Evolution → CI/CD (forbidden) |

## Response

Stop feature work → rollback → document in [examples/](../examples/).
