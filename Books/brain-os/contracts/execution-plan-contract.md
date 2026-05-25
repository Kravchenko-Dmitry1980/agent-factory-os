# Execution Plan Contract

## Schema

```json
{
  "task_id": "tsk_123",
  "plan_id": "pln_888",
  "steps": [
    { "step_id": "s1", "type": "memory_retrieval", "service": "memory-orchestrator" },
    { "step_id": "s2", "type": "policy_selection", "service": "policy-engine" },
    { "step_id": "s3", "type": "multi_agent_reasoning", "service": "reasoning-orchestrator" },
    { "step_id": "s4", "type": "evaluation", "service": "evaluation-engine" }
  ]
}
```

## Gap

step failure / retry semantics не описаны

## Maturity

promising

## Provenance

`source/Brain OS.docx` B.§1 ExecutionPlan
