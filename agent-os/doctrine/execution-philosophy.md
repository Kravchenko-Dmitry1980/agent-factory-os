# Execution Philosophy

How Agent-OS expects agents and **teams building agents** to execute work — consolidated from curated patterns and governance, not from tutorial hype.

---

## MVP-first

One working path beats ten broken roles. Canonical: prove [[query-loop]] or [[gui-agent-loop]] on real fixtures before multi-agent expansion.

Operational alignment: progressive-autonomy (swarm-playbooks reference).

**Reject:** premature-agent-swarm, tutorial big-bang.

---

## Progressive Autonomy

Expand capability in **discrete stages**:

1. Single agent + bounded tools
2. Verification wired
3. Memory governance applied
4. Multi-agent primitive chosen ([[kanban-vs-delegate]])
5. Durable coordination if needed ([[durable-task-coordination]])
6. Human gates for external effects

[[progressive-skill-disclosure]] — skills load in tiers, not all-at-once context dump.

---

## Bounded Experimentation

- `experiments/` and research corpora stay isolated
- Promote only through scoring pipeline
- Doctrine and Phase 1.4 do not add experiments

Fail fast in research tier; fail closed in curated/production posture.

---

## Review-first Execution

Release-class outcomes pass **human review** after automated verification — not critic alone.

Aligns with [operational-lifecycle.md](operational-lifecycle.md) review and approval stages.

---

## Production Realism

Every curated note includes production implications. Doctrine rejects:

- infinite context
- critic as truth
- prompt-only governance
- unverified writeback
- digital twin claims without replay

---

## No Hype Expansion

Phase boundaries explicit:

- No RAG/embeddings build in doctrine phase
- No ontology runtime
- No orchestration engine product
- No AGI positioning ([system-positioning.md](system-positioning.md))

README “future-ready” = structure, not shipped infra.

---

## No Premature Infrastructure

Graph layer = markdown navigation. Governance = markdown audit trail. Do not mistake documentation depth for deployed platform.

Queue/orchestration patterns describe **choices**, not mandatory stack.

---

## Execution Loop Summary

```
Observe need → Minimal vertical slice → Verify → Govern writes →
Link to canon → Promote only if scored → Scale coordination deliberately
```

---

## Sources

- [execution-philosophy](execution-philosophy.md) inputs from [[progressive-skill-disclosure]], [[kanban-vs-delegate]]
- `governance/FREEZE_RECOMMENDATIONS.md`
- `Books/swarm-playbooks/patterns/staged-agent-evolution.md` (reference)
- [canonical-principles.md](canonical-principles.md)
