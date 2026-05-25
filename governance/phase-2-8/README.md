# Phase 2.8 — Phase 3 Readiness Audit

**Дата:** 2026-05-25  
**Статус:** аудит готовности — **не** реализация Phase 3

---

## Что это

Phase 2.8 — финальный gate перед **Agent Builder Kit** (Phase 3). Мы проверяем, можно ли безопасно начать **спецификации шаблонов v0.1**, а не «фабрику агентов» или production.

---

## Зачем существует

После Phase 2.0–2.7-RU репозиторий содержит:

- прототипы и workflow
- реальные адаптеры (local-first)
- observability, evolution, evaluation
- operator-playbooks и curriculum (EN + RU)

Нужно явное решение: **GO / CONDITIONAL GO / NO-GO** — с рисками, freeze и минимальным scope.

---

## Как читать пакет

| Порядок | Документ | Зачем |
|---------|----------|-------|
| 1 | [PHASE_2_8_READINESS_AUDIT.md](PHASE_2_8_READINESS_AUDIT.md) | Полный аудит, оценки 1–10, вердикт |
| 2 | [PHASE_3_GO_NO_GO.md](PHASE_3_GO_NO_GO.md) | Явное решение и условия |
| 3 | [PHASE_3_MINIMAL_SCOPE.md](PHASE_3_MINIMAL_SCOPE.md) | Agent Builder Kit v0.1 — только это |
| 4 | [PHASE_3_FREEZE_POLICY.md](PHASE_3_FREEZE_POLICY.md) | Что заморожено до Phase 3 |
| 5 | [FINAL_PHASE_2_8_REPORT.md](FINAL_PHASE_2_8_REPORT.md) | Итог для руководителя |

### Углубление по темам

| Тема | Документ |
|------|----------|
| Завершение Phase 2.x | [PHASE_2_COMPLETION_REVIEW.md](PHASE_2_COMPLETION_REVIEW.md) |
| Критерии входа | [PHASE_3_ENTRY_CRITERIA.md](PHASE_3_ENTRY_CRITERIA.md) |
| Риски | [PHASE_3_RISK_REGISTER.md](PHASE_3_RISK_REGISTER.md) |
| Запреты | [PHASE_3_DO_NOT_BUILD_LIST.md](PHASE_3_DO_NOT_BUILD_LIST.md) |
| Фундамент | [PHASE_3_FOUNDATION_MAP.md](PHASE_3_FOUNDATION_MAP.md) |
| RU curriculum | [RUSSIAN_CURRICULUM_READINESS.md](RUSSIAN_CURRICULUM_READINESS.md) |
| Операторы | [OPERATOR_READINESS_REVIEW.md](OPERATOR_READINESS_REVIEW.md) |
| Evaluation | [EVALUATION_READINESS_REVIEW.md](EVALUATION_READINESS_REVIEW.md) |
| Gap prototypes → kit | [PROTOTYPE_TO_FACTORY_GAP_ANALYSIS.md](PROTOTYPE_TO_FACTORY_GAP_ANALYSIS.md) |
| Lab vs Builder vs Factory | [AGENT_FACTORY_VS_LEARNING_LAB.md](AGENT_FACTORY_VS_LEARNING_LAB.md) |
| Digital twin | [DIGITAL_TWIN_DEFER_DECISION.md](DIGITAL_TWIN_DEFER_DECISION.md) |
| CV agent | [CV_AGENT_FUTURE_DECISION.md](CV_AGENT_FUTURE_DECISION.md) |
| Диаграммы | [diagrams/](diagrams/) |

---

## Ожидаемое решение

По итогам аудита 2026-05-25:

**CONDITIONAL GO** — Phase 3 planning и Agent Builder Kit **v0.1 specs** разрешены при выполнении условий из [PHASE_3_GO_NO_GO.md](PHASE_3_GO_NO_GO.md).

Полный NO-GO на «фабрику», digital twin builder, CV builder, runtime, RAG, MCP.

---

## Связь с curriculum

- EN: `curriculum/methodology/phase-3-entry-criteria.md`
- RU: `curriculum/ru/methodology/phase-3-entry-criteria.md`
- Gate policy: `curriculum/governance/phase-3-gate-policy.md`

Phase 2.8 **не заменяет** эти документы — дополняет governance-аудитом репозитория.
