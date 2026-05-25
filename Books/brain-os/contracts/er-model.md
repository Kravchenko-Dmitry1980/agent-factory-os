# ER Model (Reference)

## Core Entities

Tenant, User, AgentProfile, DigitalTwin, Scenario, Task, RoutingDecision, ExecutionPlan, MemoryItem, Policy, ReasoningRun, ToolCall, EvaluationResult, Trace, EventLog, SafetyDecision

## Key Tables (extract)

- **tasks**: tenant_id, digital_twin_id, scenario_id, product_context, input_json, status
- **routing_decisions**: task_id UNIQUE, mode, selected_planes_json, fallback_mode
- **traces**: task_id UNIQUE, mode, latency, tokens, quality_score, status
- **memory_items**: digital_twin_id, memory_type, importance_score, embedding_ref
- **event_logs**: trace_id, task_id, event_type, payload_json

## Gap

FK cascades, indexes, partitioning — не описаны

## Maturity

promising

## Provenance

`source/Brain OS.docx` E
