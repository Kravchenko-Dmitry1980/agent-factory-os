# Что ещё mock / lab

**Дата:** 2026-05-26

Hands-on показал **real loop**, но многие части системы **намеренно упрощены** для лаборатории.

---

## Всё ещё mock или lab-only

| Область | Почему это mock/lab |
|---------|---------------------|
| **Human approval** | Симулируется сценарием (grant/timeout/deny), не живой человек в runtime |
| **Interactive approval** | Нет «нажми Y/N» в процессе — всё predetermined |
| **User input** | Нет режима «введи свой текст задачи» |
| **UI** | Только терминал, нет web/chat |
| **Database** | Нет сохранения сессий, истории, пользователей |
| **Memory** | Bounded task context в demo, не persistent memory |
| **Workflow execution** | Нет реальных CI, webhooks, ticket systems |
| **External publishing** | Delivery — флаг/print, не отправка в Slack/email/web |
| **Task queue** | Нет очереди задач |
| **Task Triage** | Только frozen specs, zero code |
| **Operator Console** | Backlog, не реализован |
| **Mock LLM** | Deterministic fake responses, не OpenAI cloud |
| **Provider (default)** | Без `--real-provider` — mock/rules; live только explicit |
| **Critic** | Advisory simulation, не отдельная production-модель |
| **Quality eval** | PASS/FAIL scripts, не benchmark leaderboard |

---

## Что это значит на практике

Оператор **видит правильное поведение gates**, но:

- не может **свободно** задать задачу;
- не **одобряет** черновик в реальном времени;
- не получает **красивый отчёт** — только raw trace;
- не **сохраняет** прогон для команды.

Это **ожидаемо** для текущей фазы Phase 3.x lab.

---

## Mock vs real — простая таблица

| Элемент | Mock/Lab | Real (hands-on) |
|---------|----------|-----------------|
| Agent loop logic | — | yes (CLI) |
| Trace printing | — | yes |
| Scenario outcomes | predetermined | yes, but fixed scenarios |
| LLM (default path) | mock adapter | — |
| LLM (explicit) | — | LM Studio local HTTP |
| Human approval | scenario sim | — |
| Delivery | boolean flag | yes (not external publish) |
| Safety harness | synthetic local | yes (script, not live model) |

---

## Не путать

**«LM Studio реально ответил»** ≠ **«продукт с AI готов»**.

Ответ provider — **сырой input** для gates. Система не доверяет ему автоматически.

См. [WHAT_IS_REAL_NOW_RU.md](WHAT_IS_REAL_NOW_RU.md), [WHY_IT_DOES_NOT_FEEL_LIKE_PRODUCT_RU.md](WHY_IT_DOES_NOT_FEEL_LIKE_PRODUCT_RU.md).
