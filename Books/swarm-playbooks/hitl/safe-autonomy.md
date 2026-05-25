---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Safe Autonomy

## Definition

Autonomy is **bounded** by: progressive rollout stage, tool allowlists, critic rework caps, budget limits, and mandatory human gates for external effects.

## Autonomy Levels (operational model)

| Level | Description | Playbook stage |
|-------|-------------|----------------|
| L0 | Human does all external actions | Этап 5 MVP |
| L1 | Agent drafts; human approves all visible output | Этап 5–6 |
| L2 | Multi-agent internal; human review queue | Prompt 3 |
| L3 | Closed loop drafts; human approves publish | Prompt 4 |
| L4 | Platform features (Telegram, multi-project) | Prompt 5 — **highest risk if boundaries slip** |

## Rules

1. **Never** L4 before L2 stable on fixtures
2. External tools require L1+ with explicit approval event
3. Critic does not increase autonomy level — only filters drafts
4. Solo `/task` mode stays at L1 unless review wired

## Anti-patterns

- [unbounded-agent-autonomy.md](../anti-patterns/unbounded-agent-autonomy.md)
- [premature-agent-swarm.md](../anti-patterns/premature-agent-swarm.md)

## Sources

- `source/ai-agents-from-scratch.ru.md` — этапы 2, 9
- `source/swarm-ai-agents-prompts.ru.md` — progressive prompts

## Promotion Potential

**SAFE FUTURE PROMOTION** — as maturity model; pair with policy engine in canonical layer.
