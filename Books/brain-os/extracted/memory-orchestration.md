# Memory Orchestration

## Definition

Делегирование памяти memory-orchestrator / CAIM; Brain OS не хранит память напрямую.

## Source Extract

Classes: profile, working, episodic, semantic, reflection, scenario. POST /v1/memory/retrieve с memory_profile и top_k.

## Why It Matters

Explicit Memory Plane boundary.

## Architecture Implications

memory-orchestrator → stores + vector index.

## Production Implications

memory_profile must match task.

## Risks

Writeback rules не формализованы.

## Maturity

production-relevant

## Related Concepts

- [[memory-retrieval-scoring]]
- [[memory-plane]]

## Provenance

| Field | Value |
|-------|-------|
| source_file | `source/Brain OS.docx` |
| source_section | C. §4 Memory orchestration |
| extraction_reason | Полная модель |
| confidence_level | high |
