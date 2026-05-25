# Policy Engine (VGP2)

## Definition

Strategy selection и decomposition до reasoning: policy_id, strategy, subgoals.

## Source Extract

decompose_compare_score; subgoals: analyze actors, enumerate options, simulate outcomes, score utility.

## Why It Matters

Policy-before-reasoning.

## Architecture Implications

ExecutionPlan step policy_selection.

## Production Implications

policies.version для audit.

## Risks

Policy-reasoning coupling → black box.

## Maturity

promising

## Related Concepts

- [[reasoning-orchestrator]]
- [[policy-plane]]

## Provenance

| Field | Value |
|-------|-------|
| source_file | `source/Brain OS.docx` |
| source_section | D. §5 policy/select |
| extraction_reason | API contract |
| confidence_level | medium |
