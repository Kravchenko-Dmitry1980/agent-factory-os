# Automation Without Review

---
classification: non-promotable
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Statement

Shipping agent outputs to users, customers, or public channels **without** a dedicated human review gate (relying only on executor self-check or critic).

## Symptoms

- Run status jumps to `completed` skipping `pending_human_review`
- Publish webhooks wired directly to task completion
- «Слепо доверять результату» operator behavior
- No `/review` equivalent in custom forks

## Why It Fails

- LLM errors are inevitable — review is liability control
- Critic false positives/negatives — see critic-as-fake-verification
- Brand and legal risk on automated content

## Corrective Pattern

- [review-gate.md](../patterns/review-gate.md)
- [human-in-the-loop-approval.md](../patterns/human-in-the-loop-approval.md)

## Sources

- `source/ai-agents-from-scratch.ru.md` — частые ошибки, этап 9
- `source/swarm-ai-agents-prompts.ru.md` — Prompt 3 review flow (positive example)

## Promotion Potential

**NEVER PROMOTE** bypass paths — review gate is SAFE promotion candidate.
