# Event Envelope Contract

## Envelope

```json
{
  "event_id": "evt_001",
  "event_type": "TASK_CLASSIFIED",
  "event_version": "1.0",
  "occurred_at": "2026-03-17T20:10:11Z",
  "tenant_id": "org_1",
  "task_id": "tsk_123",
  "trace_id": "trc_333",
  "producer": "task-classifier",
  "payload": {}
}
```

## Event Catalog (partial)

TASK_RECEIVED, TASK_CLASSIFIED, ROUTING_DECIDED, MEMORY_RETRIEVAL_STARTED/COMPLETED, POLICY_SELECTED, REASONING_*, EVALUATION_*, TRACE_WRITTEN, MEMORY_WRITEBACK_COMPLETED, SAFETY_CHECK_COMPLETED, HUMAN_ESCALATION_REQUESTED, TASK_COMPLETED/FAILED, FALLBACK_TRIGGERED

## Maturity

reusable-pattern

## Provenance

`source/Brain OS.docx` F.§1–2
