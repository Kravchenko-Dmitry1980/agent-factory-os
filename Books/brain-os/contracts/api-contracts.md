# API Contracts (Reference)

Архитектурные reference endpoints — **не production OpenAPI**.

| Method | Path | Role |
|--------|------|------|
| POST | /v1/tasks/execute | End-to-end pipeline |
| POST | /v1/tasks/classify | Classification only |
| POST | /v1/routing/decide | Routing decision |
| POST | /v1/memory/retrieve | Memory hits |
| POST | /v1/policy/select | Policy/strategy |
| POST | /v1/reasoning/run | Reasoning execution |
| POST | /v1/evaluation/run | Quality gate |
| GET | /v1/traces/{trace_id} | Trace retrieval |

## Response Shape (execute)

status, mode, result.summary, quality.score, decision_trace_ref / trace_id

## Gap

Auth, pagination, errors, versioning — **missing**

## Maturity

promising

## Provenance

`source/Brain OS.docx` D; `source/Brain OS MD.docx` §6
