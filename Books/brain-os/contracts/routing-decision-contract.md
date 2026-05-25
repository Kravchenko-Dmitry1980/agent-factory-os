# Routing Decision Contract

## Schema

```json
{
  "task_id": "tsk_123",
  "task_type": "simulation",
  "complexity": "high",
  "novelty": "medium",
  "risk": "high",
  "mode": "hybrid",
  "selected_planes": ["caim", "mirrormind", "vgp2"],
  "reasoning_depth": 3,
  "memory_profile": "profile+episodic+reflection",
  "fallback_mode": "memory_augmented",
  "human_escalation_required": false
}
```

## Persistence

NFR: routing decision persisted = 100%

## Maturity

production-relevant

## Provenance

`source/Brain OS.docx` B.§1 RoutingDecision
