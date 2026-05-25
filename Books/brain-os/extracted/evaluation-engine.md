# Evaluation Engine

## Definition

Post-reasoning quality gate: faithfulness, consistency, goal_alignment → pass.

## Source Extract

POST /v1/evaluation/run; quality_score, pass; NFR: evaluation обязательна.

## Why It Matters

Gate перед writeback.

## Architecture Implications

Plan step evaluation; EVALUATION_COMPLETED event.

## Production Implications

quality_pass_rate SLA.

## Risks

Нет evaluator contract.

## Maturity

promising

## Related Concepts

- [[trace-model]]

## Provenance

| Field | Value |
|-------|-------|
| source_file | `source/Brain OS.docx` |
| source_section | D. §7 evaluation/run |
| extraction_reason | API без evaluator spec |
| confidence_level | medium |
