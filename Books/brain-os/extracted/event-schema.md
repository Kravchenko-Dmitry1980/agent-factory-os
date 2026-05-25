# Event Schema

## Definition

Envelope: event_id, type, version, occurred_at, tenant, task, trace, producer, payload.

## Source Extract

20+ event types incl. FALLBACK_TRIGGERED, HUMAN_ESCALATION_REQUESTED, MEMORY_WRITEBACK_COMPLETED.

## Why It Matters

Decoupling + future replay (если будет).

## Architecture Implications

event-bus + event_logs table.

## Production Implications

event_version for evolution.

## Risks

Replay model отсутствует.

## Maturity

reusable-pattern

## Related Concepts

- [[trace-model]]
- [[task-lifecycle]]

## Provenance

| Field | Value |
|-------|-------|
| source_file | `source/Brain OS.docx` |
| source_section | F. Event schema |
| extraction_reason | Полный список |
| confidence_level | high |
