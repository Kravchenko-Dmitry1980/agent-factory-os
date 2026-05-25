# Brain OS — Knowledge Base

Локальная **source/research** база по архитектурной заготовке Brain OS (Control Plane).

## Что это

**Brain OS** — авторская концепция управляющего слоя (control plane), который координирует:

- классификацию и маршрутизацию задач;
- работу с памятью (CAIM / Memory Plane);
- стратегию (VGP2 / Policy Plane);
- рассуждение (MirrorMind / Cognition Plane);
- оптимизацию вычислений (System-1.5);
- трассировку, оценку качества, безопасность и адаптацию.

Документы описывают **implementation-ready system design**, но это **не production-код** и **не canonical Agent-OS layer**.

## Источники (immutable)

| Файл | Роль |
|------|------|
| `source/Brain OS.docx` | Полная спецификация: контракты, API, ER, events, риски, backlog |
| `source/Brain OS MD.docx` | Formal Architecture Specification v0.1 — сжатый обзор |

**Policy:** файлы в `source/` не редактировать. Все производные материалы — только markdown в остальных папках.

## Сильные идеи (reusable)

- **Control plane** как отдельный слой между Product и cognitive planes
- **Детерминированный cognitive routing** по правилам (не «магический» LLM-router)
- **Execution modes** (fast_reflex … hybrid) с явным fallback
- **Trace-first** — TraceRecord + event schema как first-class
- **Task lifecycle** и state machine (RECEIVED → … → COMPLETED)
- **Memory retrieval scoring** с весами recency/relevance/importance
- **Policy-before-reasoning** — policy-engine до reasoning-orchestrator
- **Evaluation-before-writeback** — quality gate перед записью в память
- **Execution supervisor** — бюджеты latency/token/cost + fallback
- **Human escalation** для high-risk доменов
- **Idempotency** по task_id (заявлено в NFR)

## Спорное / сырое (читать с осторожностью)

- **CAIM / MirrorMind / System-1.5 / VGP2** — сильные названия planes, но **мало контрактов** на границах между ними
- **adaptation-service** — заявлен без governance, replay, rollback
- **evaluation-engine** — метрики названы, **evaluator contract** не формализован
- **Universal multi-agent template** (Analyst/Critic/Strategist/Synthesizer) — шаблон без domain-specific stop criteria
- **Digital twin reproducibility** — цель заявлена, **replay/versioning model** отсутствует
- **OpenAPI** — в backlog «Define OpenAPI spec», в документе только JSON-примеры

## Не является

- ❌ Частью `agent-os/` (curated layer)
- ❌ Заменой `Books/claude/` или `Books/agents/`
- ❌ Production-ready спецификацией без доработки контрактов
- ❌ Runtime-реализацией

## Как читать

1. **`index.md`** — навигация по всем файлам
2. **`architecture/architecture-overview.md`** — контекст и границы
3. **`extracted/`** — атомарные концепты с provenance
4. **`contracts/`** — reference contracts (не OpenAPI)
5. **`patterns/`** и **`anti-patterns/`** — что применять / чего избегать
6. **`review/`** — критический разбор и promotion-candidates (рекомендации only)

## Maturity labels

В заметках используются метки: `production-relevant`, `reusable-pattern`, `promising`, `speculative`, `weak-abstraction`, `branding-only`, `reject`.

## Связь с Agent-OS

Промоция в `agent-os/` **не выполнялась**. См. `review/promotion-candidates.md` для будущих рекомендаций.
