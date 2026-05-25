# Task Envelope Contract

## Purpose

Reference contract for inbound task (not OpenAPI).

## Schema (extract)

```json
{
  "task_id": "tsk_123",
  "tenant_id": "org_1",
  "product_context": "digital_twin",
  "user_id": "usr_42",
  "agent_id": "agt_007",
  "scenario_id": "scn_12",
  "input": { "text": "...", "attachments": [] },
  "constraints": {
    "latency_ms": 8000,
    "token_budget": 12000,
    "cost_budget_usd": 0.08,
    "safety_level": "high"
  },
  "metadata": { "locale": "ru", "channel": "web" }
}
```

## Invariants

- task_id уникален per tenant (idempotency anchor)
- constraints обязательны для supervisor

## Maturity

production-relevant

## Provenance

`source/Brain OS.docx` B.§1 TaskEnvelope
