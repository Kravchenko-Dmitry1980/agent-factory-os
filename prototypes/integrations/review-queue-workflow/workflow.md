# Review Queue — Workflow

## Stages

1. **Enqueue** — task enters FIFO queue with id
2. **Dequeue / draft** — worker produces draft (mock)
3. **Critique** — advisory verdict (pass / fail / uncertain)
4. **Rework loop** — bounded retries on critic fail
5. **Human review** — mandatory approval gate
6. **Publish** — fail-closed; requires approval
7. **Escalation** — on retry exhaustion or uncertain + no human

## Queue Integrity

Queue corruption scenario simulates duplicate dequeue / missing task — workflow stops with audit, no silent continue.

## Non-Goals

- Durable queue persistence
- Multi-worker parallelism
- Generic orchestration engine
