# Предупреждение перед Phase 3

**Прочитайте до любого промпта «начни Phase 3».**

Phase 2.8 дала решение: **CONDITIONAL GO** — можно планировать kit, **нельзя** строить фабрику и runtime без явного одобрения.

---

## Phase 3 — это НЕ

| Нельзя называть Phase 3 | Почему |
|------------------------|--------|
| Полная фабрика агентов | Нет registry, ops, production eval |
| Фабрика цифровых двойников | Нет replay, versioned identity |
| CV agent builder | Нет evidence layer |
| Production-платформа | Репо — Learning Lab |
| RAG-платформа | Freeze |
| MCP runtime | Freeze |
| LangGraph / workflow engine | Platform drift |
| SaaS / dashboard | Productization |

---

## Phase 3 начинается с

# Agent Builder Kit v0.1

**Только:**

- markdown **спецификации**
- **шаблоны** (templates) — как документы
- **чеклисты** безопасности
- чеклист evaluation для шаблона
- **один** эталонный шаблон: **Review Assistant Agent**

Код, генераторы, общий runtime — **по умолчанию запрещены**.

Источник: [governance/phase-2-8/PHASE_3_MINIMAL_SCOPE.md](governance/phase-2-8/PHASE_3_MINIMAL_SCOPE.md)

---

## Запрещено в Phase 3.0

- agent **swarm** / рой
- digital twin **builder**
- CV **builder**
- RAG
- MCP **runtime**
- production **FastAPI** backend
- production **Telegram** bot
- **code generator** по умолчанию
- **shared runtime** (`prototypes/shared/` → framework)
- **framework extraction**

Полный список: [governance/phase-2-8/PHASE_3_DO_NOT_BUILD_LIST.md](governance/phase-2-8/PHASE_3_DO_NOT_BUILD_LIST.md)

---

## Почему так жёстко

Если начать шире, проект **схлопнется в хаос**:

- gates станут невидимыми
- критик и LLM снова станут «истиной»
- демо назовут MVP
- evaluation пропустят

Phase 3.0 = **один безопасный шаблон на бумаге**, опирающийся на `review-loop-agent`.

---

## Что нужно перед стартом Phase 3

[governance/PHASE_3_START_CONDITIONS.md](governance/PHASE_3_START_CONDITIONS.md)

Кратко:

1. Подтверждение пользователя: Phase 3 = **только specs**
2. Подписи mentor / lead / architect (assessments) — для **implementation**
3. Smoke + trace PASS
4. Freeze policy принята

---

## Если вам обещали «фабрику за неделю»

Это **не** этот репозиторий на Phase 3.0.  
Сначала Builder Kit v0.1 — потом (может быть) Factory — намного позже.

См. [governance/phase-2-8/AGENT_FACTORY_VS_LEARNING_LAB.md](governance/phase-2-8/AGENT_FACTORY_VS_LEARNING_LAB.md)
