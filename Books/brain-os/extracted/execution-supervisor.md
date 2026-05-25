# Execution Supervisor

## Definition

Контроль latency, token_budget, cost, fallback, retry при исполнении plan.

## Source Extract

Brain OS MD §11: latency, token_budget, cost, fallback, retry.

## Why It Matters

Enforcement budgets после routing.

## Architecture Implications

Между EXECUTING и EVALUATING; FALLBACK_TRIGGERED.

## Production Implications

fallback_rate metric.

## Risks

Retry/idempotency не детализированы.

## Maturity

production-relevant

## Related Concepts

- [[fallback-supervision]]

## Provenance

| Field | Value |
|-------|-------|
| source_file | `source/Brain OS MD.docx` |
| source_section | §11 Execution Supervisor |
| extraction_reason | Назначение сервиса |
| confidence_level | medium |
