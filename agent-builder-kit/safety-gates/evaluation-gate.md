# Evaluation Gate

## Purpose

Block template acceptance until evaluation scenarios and pass/fail criteria are defined and reviewed.

## When Required

Before template status moves to **accepted**.

## Pass Condition

- Happy, fail, approval-missing, verification-fail scenarios documented
- Expected traces defined
- Checklists completed (template-acceptance, safety-regression)
- References to `evaluation/scenarios/` where applicable

## Fail Condition

- No scenarios
- Scenarios without pass/fail criteria
- No trace expectations
- Benchmark-only eval without behavioral checks

## Example

Review Assistant includes five scenarios in `evaluation.md` mapped to `review-loop-scenarios.md`.

## Related Anti-patterns

- Missing evaluation
- Missing audit
- Template copied without provenance
