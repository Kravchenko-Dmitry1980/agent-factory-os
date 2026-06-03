# TRACE → русское резюме (Demo Runner)

**Phase 3.5.2** — mapping событий TRACE для operator summary.

Источник событий: frozen thin v0.3, hands-on [TRACE_EXPLANATION_RU.md](../review-assistant-hands-on/TRACE_EXPLANATION_RU.md).

---

## Таблица событий

| Trace Event | Русское объяснение | Смысл для безопасности |
|-------------|-------------------|------------------------|
| `task_started` | задача запущена | Normal start |
| `draft_created` | создан черновик | Output advisory until verified |
| `critique_completed` | критик дал advisory-оценку | Critic ≠ truth |
| `verification_passed` | проверка пройдена | Gate passed |
| `verification_failed` | проверка не пройдена | Fail-closed — no delivery |
| `approval_requested` | запрошено подтверждение человека | HITL gate active |
| `approval_granted` | подтверждение получено | Required for legitimate DELIVERED |
| `approval_timeout` | подтверждение не получено вовремя | Deny by default |
| `approval_denied` | подтверждение отклонено | Human blocked delivery |
| `unsafe_action_blocked` | опасное действие заблокировано | Self-protection worked |
| `escalation_triggered` | случай передан на эскалацию | No auto-delivery on uncertainty |
| `task_completed` | задача завершена успешно | Terminal success state |
| `task_failed` | задача завершена безопасной ошибкой | Fail-closed terminal |
| `llm_request_started` | начат mock LLM запрос | LLM path — not default truth |
| `llm_response_received` | получен mock LLM ответ | Unverified content |
| `llm_parse_passed` | LLM ответ разобран | Parse ≠ trust |
| `llm_parse_failed` | LLM ответ не удалось разобрать | Rejected at boundary |
| `llm_unsafe_output` | LLM ответ признан опасным | Blocked before delivery |
| `provider_request_prepared` | подготовлен запрос к локальному провайдеру | Explicit provider path |
| `provider_request_started` | запрос к локальному провайдеру отправлен | Network — operator chose this |
| `provider_response_received` | ответ локального провайдера получен | Raw model output |
| `provider_parse_passed` | ответ локального провайдера разобран | Parse ≠ trust; still unverified |

---

## Приоритетные события по сценарию

| Сценарий | Ключевые события |
|----------|------------------|
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

## Правила интерпретации

| Условие | Действие runner |
|---------|-----------------|
| DELIVERED без `approval_granted` | Статус WARNING |
| `unsafe_action_blocked` present | Статус FAILED или BLOCKED |
| `source=llm_unverified` / `provider_unverified` | Упомянуть в «Что произошло» |
| Unknown event | Raw name + «см. документацию» |

---

## Decision → русское объяснение

| Decision | Объяснение |
|----------|------------|
| DELIVERED | Результат доставлен после проверки и approval |
| BLOCKED | Доставка заблокирована без обязательных условий |
| ESCALATED | Эскалация из-за неопределённости или риска |
| FAILED | Безопасная ошибка — delivery не произошёл |
