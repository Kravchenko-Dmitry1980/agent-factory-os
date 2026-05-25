# Acceptance Criteria

## Functional

1. Задача классифицируется
2. Режим выбирается **детерминированно** по policy/rules
3. Память извлекается по профилю
4. Reasoning по execution plan
5. Trace пишется **всегда**
6. Результат проходит evaluation
7. High-risk → возможна human escalation

## NFR

| Metric | Target |
|--------|--------|
| p95 latency (memory_augmented) | ≤ 8s |
| trace completeness | ≥ 99% |
| routing decision persisted | 100% |
| idempotency | повторный task_id без дублей side effects |
| auditability | high-risk tasks |

## Maturity

production-relevant

## Provenance

`source/Brain OS.docx` B.§3
