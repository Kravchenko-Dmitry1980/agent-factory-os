# Execution Modes

## Definition

Режимы: fast_reflex, memory_augmented, deep_cognitive, multi_agent_deliberation, simulation_mode, hybrid.

## Source Extract

Mode задаёт reasoning_depth, memory_profile, selected_planes, fallback_mode в RoutingDecision.

## Why It Matters

Явная типизация вместо неявного prompt tuning.

## Architecture Implications

RoutingDecision.mode drives ExecutionPlan steps.

## Production Implications

SLA per mode; обязательный fallback.

## Risks

simulation_mode vs hybrid слабо разведены в v0.1.

## Maturity

production-relevant

## Related Concepts

- [[cognitive-routing]]
- [[execution-supervisor]]

## Provenance

| Field | Value |
|-------|-------|
| source_file | `source/Brain OS.docx` |
| source_section | B. §2 Режимы выполнения |
| extraction_reason | Канонический список |
| confidence_level | high |
