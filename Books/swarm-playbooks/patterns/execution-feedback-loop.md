# Execution Feedback Loop

---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Definition

Closed loop where execution outputs, critic verdicts, human rework comments, and test batch results **feed back** into subsequent planning and agent behavior.

## Operational Context

- «На доработку» с комментарием → re-execution
- Test factory: `tests:batch` through critic → pass-rate per agent
- Approved publish → auto draft in content plan (closed loop)
- Idea inbox → one-click convert to run

## Why It Works

- System improves from operator corrections, not only prompt edits
- Test scenarios catch regressions when prompts/models change
- Links operational approval to downstream artifacts

## Architecture Implications

- Persist rework comments on task/run
- Test scenarios as fixtures table (`test_scenarios`, `test_runs`)
- Content pipeline: approval event triggers draft creation
- Activity log as audit trail for feedback attribution

## Human-in-the-loop Implications

- Human comment is **first-class input** to orchestrator replan
- Human defines/regenerates test scenarios
- Feedback loop must not auto-promote to production memory without governance

## Failure Modes

- Feedback only in chat history — lost context
- Test pass-rate gaming via weak scenarios
- Auto draft creation without human intent
- No attribution: which comment fixed which failure

## Related Anti-patterns

- [critic-as-fake-verification.md](../anti-patterns/critic-as-fake-verification.md)
- [prompt-chain-fragility.md](../anti-patterns/prompt-chain-fragility.md)

## Production Constraints

- Structured feedback schema (not free text only)
- Evaluation separate from critique in canonical systems
- Rate limit on rework loops

## Sources

- `source/swarm-ai-agents-prompts.ru.md` — Prompts 3–5 (rework, tests, content loop)

## Promotion Potential

**RESEARCH ONLY** — valuable ops loop; canonical promotion needs verification-before-writeback and trace records.
