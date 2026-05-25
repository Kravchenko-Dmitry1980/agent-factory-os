# Reasoning Orchestrator

## Definition

Запуск reasoning: single-pass, reflection, multi-agent, recursive synthesis.

## Source Extract

Roles: Analyst, Critic, Strategist, Synthesizer. Stop: max_rounds, confidence, disagreement, budget→fallback.

## Why It Matters

Central cognition invocation with budgets.

## Architecture Implications

Inputs: policy_id, memory_context, reasoning_agents, budgets.

## Production Implications

Typed stop criteria required.

## Risks

Universal 4-role template — weak-abstraction.

## Maturity

promising

## Related Concepts

- [[evaluation-engine]]
- [[cognition-plane]]

## Provenance

| Field | Value |
|-------|-------|
| source_file | `source/Brain OS.docx` |
| source_section | C. §5 Multi-agent template |
| extraction_reason | Template + stops |
| confidence_level | medium |
