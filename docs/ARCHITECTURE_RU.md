# Архитектура Agent Factory OS (кратко)

## Позиционирование

Agent Factory OS — **governance-first** система для проектирования и эволюции AI-агентов. Это не production SaaS и не автономный рой агентов.

## Слои

```text
┌─────────────────────────────────────────────────────────┐
│  Оператор: CLI demos, playbooks, curriculum (RU/EN)   │
├─────────────────────────────────────────────────────────┤
│  Governance: фазы, freeze, reviews, change proposals    │
├─────────────────────────────────────────────────────────┤
│  Templates: agent-builder-kit (контракты, safety gates) │
├─────────────────────────────────────────────────────────┤
│  Thin impl: prototypes-derived (Review Assistant thin)  │
├─────────────────────────────────────────────────────────┤
│  Evaluation: no-network harnesses, smoke, text traces   │
├─────────────────────────────────────────────────────────┤
│  Provider boundary: mock (default) │ real (opt-in)    │
└─────────────────────────────────────────────────────────┘
```

## Принципы

1. **Выход провайдера ≠ истина** — классификация и политики до доставки.
2. **Human approval обязателен** для сценариев публикации/доставки.
3. **Fail closed** — без approval, без конфига, при unsafe — блокировка.
4. **TRACE человекочитаемый** — оператор видит цепочку решений.
5. **Изменения через governance** — freeze перед расширением поведения.

## Review Assistant (рабочая линия)

- Шаблон и thin: `prototypes-derived/review-assistant-thin/`
- Demo Runner: `demos/review-assistant-runner/demo_runner.py`
- Harness: `evaluation/review-assistant-thin/provider-safety/`

## Границы

- Нет оркестратора «фабрики» в runtime по умолчанию
- Нет сетевых вызовов в baseline-проверках
- Память и writeback — только с политикой и одобрением (см. templates)

## Дальше

- [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) (EN)
- [../governance/README.md](../governance/README.md)
