# Premature Agent Swarm

---
classification: non-promotable
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Statement

Building a multi-agent «swarm» (especially fixed N-agent topology like «8 agents») **before** a single-agent MVP proves value on real task fixtures.

## Symptoms

- Eight chat personas before one end-to-end run works
- Coordination overhead exceeds task complexity
- Debugging failures requires tracing across many prompts
- Cost scales linearly with agent count without quality gain

## Why It Fails

- Multi-agent systems multiply failure modes (handoffs, context loss, duplicate work)
- «Рой» branding encourages role inflation unrelated to task decomposition
- Operators cannot tell which agent caused regression

## Corrective Pattern

- [progressive-autonomy.md](../patterns/progressive-autonomy.md)
- [staged-agent-evolution.md](../patterns/staged-agent-evolution.md)

## Sources

- `source/ai-agents-from-scratch.ru.md` — «Сразу строить рой из 8 агентов» в частых ошибках
- `source/swarm-ai-agents-prompts.ru.md` — Prompt 2 adds 7 agents after Prompt 1 (tutorial order OK; as **architecture default** — anti-pattern)

## Promotion Potential

**NEVER PROMOTE** as default architecture — only as instructional caution.
