# Review Gate

---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Definition

Dedicated checkpoint in the pipeline where completed work **pauses** in status «awaiting review» until a human (or authorized role) renders a verdict.

## Operational Context

- Run completes all tasks + critic rounds → status «на твоей проверке»
- Dashboard route `/review` — per-result approve / rework
- Distinct from critic loop (automated) and from plan approval (pre-execution)

## Why It Works

- Separates **generation** from **release**
- Gives operator batch review UX instead of interrupting each micro-step
- Enables comment-driven rework without restarting entire run

## Architecture Implications

- Terminal automated states must transition to `pending_human_review`, not `completed`
- `completed` reserved for post-human-approval
- Rework triggers partial re-execution (task-level), not full run by default
- Notification events when review queue non-empty

## Human-in-the-loop Implications

- Human sees **aggregated summary** (Стратег пишет сводку) plus per-task artifacts
- Rework comment is structured input to orchestrator
- Approve may trigger downstream automation (e.g. draft → content plan)

## Failure Modes

- Review queue grows unbounded — operator overload
- Summary misrepresents task outputs — approval on wrong premise
- Approve without reading — governance theater
- Rework loop without max iterations

## Related Anti-patterns

- [automation-without-review.md](../anti-patterns/automation-without-review.md)
- [critic-as-fake-verification.md](../anti-patterns/critic-as-fake-verification.md)

## Production Constraints

- SLA for review queue depth
- Version pinning: review applies to specific artifact revision
- Separation of duties: creator agent ≠ approver (in team settings)

## Sources

- `source/swarm-ai-agents-prompts.ru.md` — Prompt 3 (логика статусов, `/review`)

## Promotion Potential

**SAFE FUTURE PROMOTION** — maps to evaluation-before-writeback + human gate; requires trace/contract layer.
