# Service Topology

## Logical Services

brain-api, task-classifier, cognitive-router, memory-orchestrator, policy-engine, reasoning-orchestrator, execution-supervisor, evaluation-engine, trace-service, safety-service, adaptation-service, event-bus

## Deployment Grouping

- **API Gateway** → brain-api subtree
- **memory-orchestrator** → profile/episodic/semantic stores + vector index
- **sandbox-service**, **agent-service** (product-adjacent)
- **event-bus** — cross-cutting

## Maturity

reusable-pattern

## Provenance

`source/Brain OS.docx` A.§4, C.§1 Deployment view
