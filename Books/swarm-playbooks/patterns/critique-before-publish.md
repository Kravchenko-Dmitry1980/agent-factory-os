# Critique Before Publish

---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Definition

Automated **critique pass** (dedicated critic agent or role) runs on task outputs **before** human review and **before** any publish/external action — with bounded rework rounds.

## Operational Context

- Критик проверяет результаты на ошибки и «выдумки»
- До 2 кругов автодоработки по вердикту Критика
- Плохо → задача на доработку; хорошо → human review queue

## Why It Works

- Filters obvious quality issues before human attention
- Reduces reviewer fatigue and rubber-stamping
- Structured rework loop cheaper than full human rewrite

## Architecture Implications

- Critic is **separate role** from executors (conflict of interest reduction)
- Store critic verdict on task record
- Cap rework iterations (playbook: 2)
- Critic must not have publish/external tools

## Human-in-the-loop Implications

- Critique **precedes** human review, does not replace it
- Human still required for external release
- Human may override critic false negatives/positives

## Failure Modes

- Treating critic pass as truth — see critique-limitations
- Critic and executor share same context bias
- Uncapped rework → cost explosion
- Critic approves hallucinations confidently

## Related Anti-patterns

- [critic-as-fake-verification.md](../anti-patterns/critic-as-fake-verification.md)
- [automation-without-review.md](../anti-patterns/automation-without-review.md)

## Production Constraints

- Critic ≠ verification system — supplemental only
- Log critic reasoning for audit
- Separate model/temperature optional for diversity
- Metrics: critic-human disagreement rate

## Sources

- `source/ai-agents-from-scratch.ru.md` — этапы 7, 9
- `source/swarm-ai-agents-prompts.ru.md` — Prompt 3 (orchestrator critic rounds)

## Promotion Potential

**RESEARCH ONLY** — useful UX pattern; promotion requires explicit critique-vs-verification boundary (mandatory in this corpus).
