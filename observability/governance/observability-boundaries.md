# Observability Boundaries

## In Scope (Phase 2.3)

- Conceptual event taxonomy
- Text trace formats and examples
- Failure intelligence documentation
- Human-readable log principles
- Mermaid diagrams for learning

## Out of Scope

- Prometheus, Grafana, Datadog
- OpenTelemetry SDK / collectors
- Distributed tracing (Jaeger, Tempo)
- Metrics databases
- Log aggregation platforms
- Runtime auto-instrumentation framework

## Allowed Connection to Code

- Read `integrations-real/.data/**/*.jsonl` manually
- Map demo audit actions to canonical events (docs only)
- Do **not** add instrumentation middleware to demos in this phase

## Stop Signals

| Signal | Action |
|--------|--------|
| `observability/collector.py` | Remove |
| Dashboard JSON/YAML | Remove |
| Metric registry class | Remove |
| Trace SDK wrapper | Remove |
