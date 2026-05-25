# Human-in-the-Loop Approval

---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Definition

Обязательная точка, где **человек явно подтверждает или отклоняет** результат или действие агента перед продолжением pipeline или внешним эффектом.

## Operational Context

- Публикация контента, отправка клиенту, оплата — «всё, что уходит наружу»
- Страница «На проверке» с кнопками «Одобрить» / «На доработку»
- Крупный прогон: статус «ждёт одобрения плана» до запуска исполнения

## Why It Works

- Снижает liability и reputational risk
- Строит доверие оператора к системе на ранних этапах
- Компенсирует ненадёжность LLM-output без блокировки автomation draft stage

## Architecture Implications

- State machine must include explicit `awaiting_human_approval` (or equivalent)
- UI/API endpoints: approve, reject-with-comment, request-rework
- Audit: who approved, when, which version of artifact
- External action tools must be **disabled or gated** until approval event

## Human-in-the-loop Implications

- Human is **decision authority**, not optional reviewer
- Rework comment becomes input to next execution cycle
- On startup, default posture: **human confirms external actions**

## Failure Modes

- Approval UI bypassed via direct API/tool call
- «Approve all» fatigue — rubber-stamping
- Stale artifacts approved after underlying data changed
- Missing comment on rework → agent repeats same error

## Related Anti-patterns

- [unbounded-agent-autonomy.md](../anti-patterns/unbounded-agent-autonomy.md)
- [automation-without-review.md](../anti-patterns/automation-without-review.md)
- [critic-as-fake-verification.md](../anti-patterns/critic-as-fake-verification.md)

## Production Constraints

- RBAC: not every user may approve external actions
- Idempotent approval handler (double-click safe)
- Timeout / escalation if human unavailable
- Immutable record of approved artifact hash

## Sources

- `source/ai-agents-from-scratch.ru.md` — этап 9 (подтверждение «наружу»)
- `source/swarm-ai-agents-prompts.ru.md` — Prompt 3 (страница «На проверке»), Prompt 4 (одобрение → черновик)

## Promotion Potential

**SAFE FUTURE PROMOTION** — aligns with Agent-OS `human-escalation-gate` and `verification-before-writeback` themes; needs contract formalization before canonical merge.
