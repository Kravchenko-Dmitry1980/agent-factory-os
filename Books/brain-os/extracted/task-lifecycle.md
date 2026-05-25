# Task Lifecycle

## Definition

receive → classify → route → memory → policy → reasoning → evaluate → trace → writeback → adapt.

## Source Extract

FSM: RECEIVED → CLASSIFIED → ROUTED → MEMORY_READY → EXECUTING → EVALUATING → COMPLETED; FAILED, ESCALATED, FALLBACK_EXECUTED.

## Why It Matters

Единый lifecycle для observability и idempotency.

## Architecture Implications

Каждая стадия → event; trace связывает стадии.

## Production Implications

Human escalation до COMPLETED на high-risk.

## Risks

adapt без governance.

## Maturity

production-relevant

## Related Concepts

- [[trace-model]]
- [[event-schema]]

## Provenance

| Field | Value |
|-------|-------|
| source_file | `source/Brain OS MD.docx` |
| source_section | §4 Жизненный цикл |
| extraction_reason | Согласовано в обоих docs |
| confidence_level | high |
