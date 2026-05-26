# Agent Builder Kit v0.1 — кратко (RU)

---

## Что это

**Agent Builder Kit v0.1** — набор Markdown-спецификаций, шаблонов и чеклистов для **проектирования** безопасных AI-агентов.

Мы **не строим** агентов. Мы описываем, **как безопасный шаблон агента должен выглядеть на бумаге**.

---

## Что это НЕ

- не **фабрика** агентов
- не **генератор** кода или файлов
- не **runtime**
- не production-платформа
- не цифровой двойник
- не CV builder
- не RAG-платформа
- не MCP runtime
- не автономная система

---

## Что можно делать

- описывать агента (цель, входы, выходы)
- описывать workflow
- задавать **safety gates** (fail-closed, verification, approval)
- задавать **границы памяти**
- задавать **evaluation checklist**
- описывать **expected traces**
- проверять **anti-patterns**
- использовать эталонный шаблон **Review Assistant Agent**

---

## Что нельзя делать

- писать код без **отдельного разрешения**
- делать генератор шаблонов
- делать агентную фабрику
- делать production bot
- делать CV / digital twin / RAG / MCP
- импортировать шаблоны из внешних репозиториев без governance review

---

## Первый шаблон: Review Assistant Agent

Агент помогает **подготовить черновик** и оформить его для проверки человеком.

**Обязательно:**

- человек проверяет итог
- без одобрения — нет публикации
- критик (critique) — совет, не истина

**Запрещено:**

- автопубликация
- замена человека-рецензента
- обход approval gate

Подробнее: [templates/review-assistant-agent/README.md](templates/review-assistant-agent/README.md)

---

## Как пользоваться

1. Прочитайте [PHASE_3_WARNING_RU.md](../PHASE_3_WARNING_RU.md)
2. Откройте [template-specs/agent-template-spec.md](template-specs/agent-template-spec.md)
3. Изучите [safety-gates/](safety-gates/README.md)
4. Посмотрите [templates/review-assistant-agent/](templates/review-assistant-agent/)
5. Пройдите [evaluation-checklists/phase-3-template-review-checklist.md](evaluation-checklists/phase-3-template-review-checklist.md)

---

## Связь с Phase 2

| Область | Где в репо |
|---------|------------|
| Прототип | `prototypes/review-loop-agent/` |
| Сценарии eval | `evaluation/scenarios/review-loop-scenarios.md` |
| События trace | `observability/event-taxonomy/canonical-events.md` |
| Governance | `governance/PHASE_3_START_CONDITIONS.md` |

---

## Версия

**v0.1** — только спеки. Без runtime. Без фабрики.
