---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Source Analysis — Swarm Playbooks

Анализ двух operational playbook-корпусов перед controlled extraction.

## Sources

1. **ai-agents-from-scratch.ru.md** — универсальный 11-этапный гайд для non-programmers
2. **swarm-ai-agents-prompts.ru.md** — промты для конкретного «Роя из 8 агентов» (соцсети)

---

## Operational Strengths

### Процесс и дисциплина

- **Пошаговая верификация** — «не идём дальше, пока не работает» на каждом этапе
- **MVP-first** — явный совет начать с одного агента (этап 5), swarm только при необходимости (этап 7)
- **ЗАДАЧА.md / вход-выход-критерии** — формализация задачи до кода
- **3–5 проверочных примеров** — regression fixtures для качества

### HITL и безопасность

- «Где обязательно решает человек» — вопрос на этапе 1
- Подтверждение человеком для **внешних действий** (публикация, отправка клиенту)
- Статус «на твоей проверке» / страница «На проверке» с approve/rework
- Крупный прогон ждёт **одобрения плана** перед исполнением

### Orchestration lifecycle

- Цель → план (Стратег) → декомпозиция задач → очередь → исполнение → Критик → сводка → human review
- **До 2 кругов автодоработки** по вердикту Критика
- **Зависимости между задачами** — task graph, не flat list
- **Queue recovery** — незавершённые задачи подхватываются после restart

### Budget & observability

- Поля стоимости/токенов на run и task
- Опциональный бюджет на прогон
- Activity log, events feed, notification counter

### Operational wisdom (explicit in sources)

- «Слепо доверять результату» — анти-паттерн; нужен Критик + человек
- «Сразу строить рой из 8 агентов» — анти-паттерн
- Секреты только в `.env`

---

## Architectural Weaknesses

### Нет контрактов и governance

- Нет task envelope, trace record, routing decision contracts
- Статусы run/task описаны словами, не как state machine с idempotency
- Нет provenance на решения агентов
- Нет policy plane — только system prompts

### Personality-centric design

- «Характер агента = 80% качества» — oversimplification
- 8 ролей с «живыми личностями» в seed.sql — branding, не architecture
- Оркестратор = «Стратег» с дружелюбным тоном, не control plane

### Critic overclaim

- Критик «проверяет на ошибки и галлюцинации» — без formal verification
- Test factory через Критика — pass-rate ≠ ground truth
- Нет разделения critique / verification / evaluation

### Framework coupling

- Claude Agent SDK, Next.js, Express, PostgreSQL — tutorial stack, не abstract pattern
- MCP tools привязаны к конкретному прогону — нет reusable tool contract
- CLAUDE.md как «память» — session hint, не memory governance

### Scale & production gaps

- Нет multi-tenant isolation model (projects добавлены поздно)
- Нет rate limiting, dead-letter queue, saga/compensation
- Backup = pg dump 14 days — minimal DR
- Telegram long-polling — не production messaging pattern

---

## Reusable Concepts (extracted → patterns/)

| Concept | Source | Value |
|---------|--------|-------|
| Progressive autonomy (1 agent → swarm) | 1.md этапы 5–7 | High |
| Human approval before external action | 1.md этап 9, 2.md Prompt 3–4 | High |
| Review gate («На проверке») | 2.md Prompt 3 | High |
| Plan approval for large runs | 2.md Prompt 3 | High |
| Queue-backed background execution | 1.md этап 7, 2.md queue.ts | High |
| Critic loop with bounded retries | 2.md Prompt 3 | Medium (with limits) |
| Budget per run | 2.md Prompt 4 | Medium |
| Task dependencies | 2.md Prompt 4 | Medium |
| Closed content loop (approve → draft) | 2.md Prompt 4 | Domain-specific |
| waiting_question escalation | 2.md Prompt 4 | Medium |

---

## Dangerous Misconceptions

| Misconception | Risk | Mitigation in corpus |
|---------------|------|----------------------|
| «8-agent swarm» as default architecture | Complexity explosion, coordination cost | anti-pattern: premature-agent-swarm |
| Critic solves hallucinations | False confidence, liability | critique-limitations, critic-as-fake-verification |
| System prompt = governance | Policy bypass, no audit | orchestration-without-contracts |
| Personality = quality | Inconsistent behavior | personality-over-architecture |
| Prompt chain = reliable system | Fragile, untestable | prompt-chain-fragility |
| Full autonomy after critic | External harm | unbounded-agent-autonomy, approval-before-external-action |
| Tutorial stack = architecture | Lock-in, non-transferable | tutorial-driven-architecture |

---

## Governance Gaps (vs Agent-OS)

| Agent-OS capability | Present in playbooks? |
|---------------------|----------------------|
| Trace-first architecture | Partial (activity_log only) |
| Verification before writeback | Conflated with critic |
| Memory taxonomy / frozen snapshot | CLAUDE.md + knowledge_chunks ad hoc |
| Anti-patterns catalog | Implicit in «частые ошибки» |
| Promotion pipeline | Absent |
| Semantic graph / provenance | Absent |
| Fail-closed defaults | Partial (human confirm for external) |
| Subagent tool restrictions | Not addressed |

---

## Production-Readiness Limitations

- **Instructional tier only** — assumes single owner, local machine
- **No contract testing** — quality = eyeball + critic LLM
- **No idempotency keys** on runs/tasks
- **No formal escalation SLA** — waiting_question without timeout policy spec
- **Cost tracking** — accounting, not enforcement (budget optional)
- **Security** — SWARM_PASSWORD optional; no RBAC

---

## Classification Summary

| Content type | Examples | Action |
|--------------|----------|--------|
| reusable-pattern | HITL gates, queue, lifecycle, budget visibility | Extract to patterns/ |
| beginner-tutorial | VSCode install, npm run dev, seed.sql prompts | Keep in source/ only |
| operational-guidance | «маленькими шагами», git rollback | Reference in review |
| non-promotable | 8-agent topology, personality prompts, critic-as-truth | anti-patterns + NEVER PROMOTE |

---

## Conclusion

Источники **ценны операционно** (lifecycle, HITL, staged complexity, queue, review UX) и **слабы архитектурно** (нет контрактов, trace, verification, governance).  
Корпус `Books/swarm-playbooks/` изолирует reusable operational wisdom без contamination canonical layer.
