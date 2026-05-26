# Trace Explanation Mapping (RU)

**Дата:** 2026-05-26  
**Статус:** PLAN_ONLY

Таблица для будущего Demo Runner: событие TRACE → русское объяснение → смысл для безопасности.

Источник событий: hands-on [TRACE_EXPLANATION_RU.md](../../demos/review-assistant-hands-on/TRACE_EXPLANATION_RU.md), frozen thin v0.3.

---

## Mapping table

| Trace Event | Russian Explanation | Safety Meaning |
|-------------|---------------------|----------------|
| `task_started` | Задача принята, цикл агента начался | Normal start |
| `draft_created` | Черновик создан | Output advisory until verified |
| `critique_completed` | Критик завершил (результат advisory) | Critic ≠ truth |
| `verification_passed` | Проверки черновика пройдены | Gate passed |
| `verification_failed` | Черновик не прошёл проверку | Fail-closed — no delivery |
| `approval_requested` | Запрошено human approval | HITL gate active |
| `approval_granted` | Approval получен | Required for legitimate DELIVERED |
| `approval_timeout` | Approval не получен в срок | Deny by default |
| `approval_denied` | Approval явно отклонён | Human blocked delivery |
| `unsafe_action_blocked` | Опасное действие заблокировано | Self-protection worked |
| `escalation_triggered` | Эскалация из-за неопределённости/риска | No auto-delivery on uncertainty |
| `task_completed` | Цикл успешно завершён | Terminal success state |
| `task_failed` | Цикл остановлен без delivery | Fail-closed terminal |
| `llm_request_started` | Запрос к mock LLM начат | LLM path — not default truth |
| `llm_response_received` | Ответ mock LLM получен | Unverified content |
| `llm_parse_passed` | Ответ LLM разобран в форму | Parse ≠ trust |
| `llm_parse_failed` | Ответ LLM malformed | Rejected at boundary |
| `llm_unsafe_output` | LLM вернул unsafe content | Blocked before delivery |
| `provider_request_prepared` | Запрос к local provider подготовлен | Explicit provider path |
| `provider_request_started` | HTTP-запрос к LM Studio отправлен | Network — operator chose this |
| `provider_response_received` | Ответ provider получен | Raw model output |
| `provider_parse_passed` | Ответ provider разобран | Parse ≠ trust; still unverified |

---

## Key events by scenario (runner priority)

Runner shows **subset** — not every line, only safety-relevant:

| Scenario | Priority events |
|----------|-----------------|
| happy | task_started, verification_passed, approval_granted, task_completed |
| missing_approval | approval_requested, approval_timeout, task_failed |
| critic_uncertain | critique_completed, escalation_triggered, task_failed |
| bad_draft | verification_failed, task_failed |
| unsafe_publish_attempt | unsafe_action_blocked, task_failed |
| llm_valid_draft | llm_parse_passed, draft_created, approval_granted |
| llm_malformed_output | llm_parse_failed, task_failed |
| llm_unsafe_output | llm_unsafe_output, unsafe_action_blocked |
| real_provider_synthetic | provider_parse_passed, verification_passed, approval_granted |

---

## Interpretation rules for runner

| Rule | Action |
|------|--------|
| DELIVERED without `approval_granted` in trace | Summary WARNING — inconsistent |
| `unsafe_action_blocked` present | Emphasize in СТАТУС БЕЗОПАСНОСТИ |
| `source=llm_unverified` or `provider_unverified` | Mention in ЧТО ПРОИЗОШЛО |
| Unknown event in trace | Show raw name + «см. документацию» |

---

## Flow diagram

See [diagrams/trace-to-summary-flow.md](diagrams/trace-to-summary-flow.md).
