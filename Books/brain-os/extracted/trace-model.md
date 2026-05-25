# Trace Model

## Definition

TraceRecord first-class: trace_id, metrics, status, events; completeness ≥99%.

## Source Extract

Trace всегда; GET /v1/traces/{id}; decision_trace_ref in result.

## Why It Matters

Audit для twin/HR/medical/Test Machine.

## Architecture Implications

trace-service; traces UNIQUE per task.

## Production Implications

trace_completeness SLA.

## Risks

GET trace — event names без full payloads.

## Maturity

production-relevant

## Related Concepts

- [[trace-first]]
- [[event-schema]]

## Provenance

| Field | Value |
|-------|-------|
| source_file | `source/Brain OS.docx` |
| source_section | B. TraceRecord + D/F traces/events |
| extraction_reason | Сквозная модель |
| confidence_level | high |
