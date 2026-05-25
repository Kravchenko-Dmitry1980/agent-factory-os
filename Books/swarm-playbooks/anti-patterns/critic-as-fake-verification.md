# Critic as Fake Verification

---
classification: non-promotable
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Statement

Treating an LLM **critic agent** as a verification system that guarantees factual correctness, eliminates hallucinations, or replaces governance gates.

## Symptoms

- «Критик проверяет на выдумки» → operator skips human review
- Test batch pass-rate reported as «quality score»
- Critic verdict stored as `verified: true` without ground truth
- No separation between critique, evaluation, and verification

## Why It Fails

- Critic is another LLM — subject to same hallucination class
- No grounding contract (sources, tools, deterministic checks)
- Adversarial failure: executor and critic share model biases
- Creates **false confidence** and liability exposure

## Corrective Pattern

- [critique-vs-verification.md](../critique/critique-vs-verification.md)
- [critique-limitations.md](../critique/critique-limitations.md)
- [human-in-the-loop-approval.md](../patterns/human-in-the-loop-approval.md)

## Sources

- `source/ai-agents-from-scratch.ru.md` — этапы 7, 9
- `source/swarm-ai-agents-prompts.ru.md` — Prompt 3, 5 (test factory via critic)

## Promotion Potential

**NEVER PROMOTE** — mandatory anti-pattern in canonical layer.
