# Что уже настоящее (real)

**Дата:** 2026-05-26  
**Контекст:** hands-on demo Review Assistant Thin v0.3

---

## Уже real — можно потрогать руками

| Компонент | Что это значит |
|-----------|----------------|
| **Python CLI demo** | `minimal_demo.py` запускается, печатает результат |
| **Scenario engine** | 9+ сценариев с предсказуемым поведением |
| **Trace в терминале** | Видимая история шагов агента |
| **Decision output** | `decision=...`, `delivered=True/False` |
| **Original loop** | draft → critique → verification → approval → delivery/block |
| **Mock LLM boundary** | v0.2: parse, unsafe block, malformed block |
| **Local provider boundary** | v0.3: HTTP к LM Studio при `--real-provider` |
| **LM Studio call** | Оператор получил реальный ответ модели qwen2.5-7b-instruct-1m |
| **Safety harness** | 16 synthetic cases, `check_review_assistant_provider_safety.py` |
| **Eval scripts** | thin, mock, contract, smoke, trace — PASS |
| **Freeze / governance** | v0.1–v0.3, harness v0.1, task-triage specs v0.1 — задокументированы |
| **Fail-closed поведение** | BLOCKED, FAILED, ESCALATED — реально видны в терминале |

---

## Что именно «ожило» после hands-on

До запуска: «Review Assistant» — название в governance.

После запуска:

1. Вводишь команду → видишь **решение**.
2. Читаешь **TRACE** → понимаешь **почему**.
3. Плохой сценарий → **не доставляет** — это не теория, это вывод в PowerShell.
4. LM Studio → **реальный HTTP**, но output всё равно **unverified** до gates.

---

## Честная формулировка

**Это working lab prototype, not production product.**

| Real | Не overclaim |
|------|--------------|
| CLI demo работает | Не «готов к клиентам» |
| Provider boundary работает локально | Не «cloud production LLM» |
| Gates видны в trace | Не «100% безопасность модели» |
| Harness 16 cases | Не red-team platform |

---

## Frozen artifacts, подтверждённые hands-on

```text
review-assistant-thin-v0.1  → original 5 scenarios
review-assistant-thin-v0.2  → + mock LLM scenarios
review-assistant-thin-v0.3  → + real provider (explicit flag)
provider-safety-harness-v0.1 → eval script (no live provider in harness)
task-triage-agent-specs-v0.1 → specs only, not run in this demo
```

---

## Связанные пути

- Demo: `prototypes-derived/review-assistant-thin/minimal_demo.py`
- Eval: `evaluation/scripts/check_review_assistant_*.py`
- Template: `agent-builder-kit/templates/review-assistant-agent/`
