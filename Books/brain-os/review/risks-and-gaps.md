# Risks and Gaps

## Missing Specifications

| Gap | Impact | Source evidence |
|-----|--------|-----------------|
| **OpenAPI spec** | No codegen, no contract tests | Backlog J.§1; MD §22 |
| **Evaluator contract** | quality_score не verifiable | evaluation/run response only |
| **Governance for adaptation** | Policy drift, unsafe learning | v0.3 roadmap only |
| **Replay model** | Twin reproducibility impossible | Metric named, no design |
| **Memory writeback rules** | Pollution / conflict | Event exists, rules absent |
| **Idempotency details** | Duplicate side effects | NFR claim only |
| **Safety escalation matrix** | Inconsistent human gates | Partial (medical/hr in pseudocode) |
| **Benchmark strategy** | A/B routing unevaluated | v0.3 mention only |

## Architectural Risks (from source)

1. Router без правил
2. Memory overfetch
3. Policy+reasoning black box
4. Trace not first-class
5. No idempotency

## Operational Gaps

- AuthN/AuthZ для brain-api
- Multi-tenant isolation beyond tenant_id field
- Plane failure modes (CAIM down → ?)
- Cost accounting per plane

## Recommendation

Treat Brain OS as **design draft v0.1** — valuable for patterns, not for implementation fork without gap closure.
