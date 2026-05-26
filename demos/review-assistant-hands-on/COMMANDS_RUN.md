# Commands Run — Hands-on Demo

**Дата:** 2026-05-26  
**Shell:** PowerShell  
**CWD:** `C:\Dima\Projects\CURSOR\AGENT`

Все команды ниже — **фактически выполненные оператором** вручную.

---

## Подготовка

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
```

---

## Original scenarios (Review Assistant Thin v0.1 path)

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario happy
```

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario missing_approval
```

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario critic_uncertain
```

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario bad_draft
```

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario unsafe_publish_attempt
```

---

## Mock LLM scenarios (Review Assistant Thin v0.2 path)

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_valid_draft
```

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_malformed_output
```

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_unsafe_output
```

---

## Real local provider scenario (Review Assistant Thin v0.3 path)

**Предупреждение:** не запускать `--real-provider`, если LM Studio не запущен локально и если цель — не synthetic-only тест. Real provider шлёт HTTP-запрос на локальный сервер.

```powershell
$env:RA_LLM_BASE_URL = "http://127.0.0.1:1234"
$env:RA_LLM_MODEL = "qwen2.5-7b-instruct-1m"
```

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario real_provider_synthetic --real-provider
```

**Наблюдаемый вывод (оператор):**

- `Mode: real provider enabled`
- `decision=DELIVERED`
- `delivered=True`
- Trace: provider_request_prepared → provider_response_received → provider_parse_passed → verification_passed → approval_granted → task_completed

---

## Автоматические проверки (для справки, не часть hands-on)

Эти скрипты **не заменяют** ручной walkthrough, но подтверждают baseline:

```powershell
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

**Cursor в Phase 3.5.1 не вызывал** `--real-provider` и не обращался к LM Studio.

---

## Что **не** запускалось в этом hands-on

- Task Triage (нет implementation)
- Provider safety harness в интерактивном режиме (только eval script при CI/check)
- LM Studio live check от Cursor
