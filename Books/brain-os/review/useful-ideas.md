# Useful Ideas

Жёсткий shortlist — **реально полезно** для engineering knowledge (не hype).

| # | Idea | Why |
|---|------|-----|
| 1 | **Control plane** | Чёткое разделение orchestration / product / planes |
| 2 | **Deterministic routing** | Rule-based choose_mode с persisted RoutingDecision |
| 3 | **Execution modes** | Typed modes + fallback_mode |
| 4 | **Trace-first** | TraceRecord + events + completeness SLA |
| 5 | **Event schema** | Versioned envelope + catalog |
| 6 | **Task lifecycle** | FSM + pipeline steps |
| 7 | **Memory retrieval scoring** | Weighted multi-factor rank (needs numeric weights) |
| 8 | **Fallback supervisor** | Budget enforcement + FALLBACK_TRIGGERED |
| 9 | **Human escalation** | High-risk gate |
| 10 | **Idempotency requirement** | task_id as dedup key (needs spec) |

Все помечены **reusable-pattern** или **production-relevant** в extracted notes.
