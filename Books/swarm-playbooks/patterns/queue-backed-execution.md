# Queue-Backed Execution

---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Definition

Фоновая очередь выполняет agent tasks **последовательно или с controlled concurrency**, не блокируя UI/API, с возможностью **recovery** незавершённых задач после restart.

## Operational Context

- «Очередь задач, чтобы тяжёлая работа шла в фоне и интерфейс не зависал»
- `queue.ts` — задачи по одной; при restart backend подхватывает incomplete tasks

## Why It Works

- Long LLM calls don't block dashboard
- Operator sees progress while work continues
- Crash resilience for multi-step runs

## Architecture Implications

- Task states: `queued`, `running`, `completed`, `failed`, `waiting_rework`
- Persistent queue store (DB table `tasks`, not in-memory only)
- Worker idempotency: re-processing same task must be safe
- Backpressure when queue depth exceeds threshold

## Human-in-the-loop Implications

- Human monitors progress via runs UI, not blocking session
- Notifications (events/Telegram) when queue drains to review state

## Failure Modes

- In-memory queue — lost on crash (playbook avoids via DB)
- No dead-letter for permanently failing tasks
- Single-threaded queue — throughput bottleneck at scale
- Duplicate execution on recovery without idempotency keys

## Related Anti-patterns

- [orchestration-without-contracts.md](../anti-patterns/orchestration-without-contracts.md)
- [unbounded-agent-autonomy.md](../anti-patterns/unbounded-agent-autonomy.md)

## Production Constraints

- Configurable concurrency with rate limits per model/provider
- Visibility: queue depth, oldest task age
- Poison message handling
- Graceful shutdown: finish or re-queue in-flight tasks

## Sources

- `source/ai-agents-from-scratch.ru.md` — этап 7
- `source/swarm-ai-agents-prompts.ru.md` — Prompt 3 (`queue.ts`)

## Promotion Potential

**SAFE FUTURE PROMOTION** — operational pattern; canonical layer needs durable task coordination contract (cf. Agent-OS `durable-task-coordination`).
