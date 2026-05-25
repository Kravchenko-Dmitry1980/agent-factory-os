# Product Layer Integration

## Product Contexts

`product_context`: digital_twin, sandbox, recruiter, bs-evolve (из примеров TaskEnvelope)

## Integration Contract

Product отправляет TaskEnvelope в brain-api; получает result + quality + decision_trace_ref.

## Digital Twin Link

agent_id, scenario_id, digital_twin_id в ER model связывают product entities с tasks/traces.

## Gaps

- Нет product-specific permission matrix
- Нет sandbox event sync spec

## Maturity

promising

## Provenance

`source/Brain OS.docx` A.§3, E. ER model
