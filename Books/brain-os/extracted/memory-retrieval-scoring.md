# Memory Retrieval Scoring

## Definition

score = Σ w_i * factor_i для recency, relevance, importance, identity, goal.

## Source Extract

Формула с w_recency, w_relevance, w_importance, w_identity, w_goal. Пример top_k=20.

## Why It Matters

Предсказуемее pure vector search.

## Architecture Implications

Weights configurable per tenant.

## Production Implications

Caps на hits; metric memory_hit_rate.

## Risks

Числовые w_* не заданы в source.

## Maturity

reusable-pattern

## Related Concepts

- [[memory-orchestration]]

## Provenance

| Field | Value |
|-------|-------|
| source_file | `source/Brain OS.docx` |
| source_section | C. §4 Retrieval policy |
| extraction_reason | Единственная формула scoring |
| confidence_level | high |
