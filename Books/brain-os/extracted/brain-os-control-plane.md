# Brain OS Control Plane

## Definition

Управляющий слой между Product Layer и cognitive planes, оркестрирующий classification, routing, memory, policy, reasoning, supervision, evaluation, trace, safety, adaptation.

## Source Extract

Brain OS — control plane: classifier/router/policy/trace/eval. Внутри: task classification, cognitive routing, memory control, policy selection, reasoning orchestration, execution supervision, evaluation, safety, adaptation. Вне: UI, LLM providers, vector DB, sandbox renderer, MCP/API.

## Why It Matters

Отделяет orchestration от product и моделей; единая точка traceability и cost control.

## Architecture Implications

Product → brain-api → pipeline сервисов → planes (CAIM, MirrorMind, System-1.5, VGP2) → LLM.

## Production Implications

Чёткие границы ответственности; иначе control plane = god-service.

## Risks

Раздувание scope; дублирование product layer.

## Maturity

production-relevant

## Related Concepts

- [[control-plane]]
- [[cognitive-router]]
- [[task-lifecycle]]

## Provenance

| Field | Value |
|-------|-------|
| source_file | `source/Brain OS.docx` |
| source_section | A. Система §1–2 |
| extraction_reason | Центральная архитектурная рамка |
| confidence_level | high |
