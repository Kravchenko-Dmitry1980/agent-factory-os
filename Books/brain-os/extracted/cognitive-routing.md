# Cognitive Routing

## Definition

Rule-based выбор execution mode и planes по classification: task_type, complexity, risk, memory_need, novelty.

## Source Extract

choose_mode pseudocode: high-risk medical/hr → hybrid; low complexity + low memory → fast_reflex; high memory → memory_augmented; high complexity + novelty → deep_cognitive; simulation/strategy → multi_agent_deliberation; default hybrid.

## Why It Matters

Снижает cost reasoning на простых задачах без implicit prompt routing.

## Architecture Implications

task-classifier → cognitive-router → RoutingDecision (persist 100%).

## Production Implications

Persisted routing + fallback_mode + audit on high-risk.

## Risks

Router без rules → недетерминированность.

## Maturity

reusable-pattern

## Related Concepts

- [[execution-mode]]
- [[policy-engine]]
- [[deterministic-cognitive-routing]]

## Provenance

| Field | Value |
|-------|-------|
| source_file | `source/Brain OS.docx` |
| source_section | C. §2 Decision routing logic |
| extraction_reason | Ключевой алгоритм |
| confidence_level | high |
