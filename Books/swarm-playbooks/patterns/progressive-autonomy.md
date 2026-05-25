# Progressive Autonomy

---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Definition

Постепенное расширение автономии системы: от одного агента с human-in-the-loop к multi-agent orchestration **только когда** single-agent path исчерпан.

## Operational Context

- Этап 5: один агент MVP
- Этап 7: swarm «только если одной роли мало»
- Совет новичку: «начни с одного»

## Why It Works

- Один работающий агент > десять сломанных
- Раннее обнаружение ошибок в scope/prompt/tools
- Снижает coordination overhead и cost до proof of value

## Architecture Implications

- Explicit capability flags: `single_agent_mode` vs `orchestrated_mode`
- Metrics gate: promote to swarm when single-agent failure modes repeat
- Same task envelope should work in both modes (future contract work)

## Human-in-the-loop Implications

- Early stages: human approves **everything** visible
- Later stages: human approves external + high-risk; internal drafts automated
- Autonomy expansion is **operator decision**, not default

## Failure Modes

- Premature swarm before MVP validated
- Never expanding — under-automation of stable subtasks
- Adding agents for «cool factor» not functional decomposition

## Related Anti-patterns

- [premature-agent-swarm.md](../anti-patterns/premature-agent-swarm.md)
- [tutorial-driven-architecture.md](../anti-patterns/tutorial-driven-architecture.md)

## Production Constraints

- Feature flags per tenant/project for orchestration depth
- Cost ceiling lower in single-agent mode
- Documented criteria for «ready for orchestration»

## Sources

- `source/ai-agents-from-scratch.ru.md` — этапы 2, 5, 7; «частые ошибки»
- `source/swarm-ai-agents-prompts.ru.md` — Prompt 1 (один Стратег) before Prompt 2 (8 agents)

## Promotion Potential

**SAFE FUTURE PROMOTION** — strong alignment with staged rollout; map to Agent-OS progressive skill disclosure pattern.
