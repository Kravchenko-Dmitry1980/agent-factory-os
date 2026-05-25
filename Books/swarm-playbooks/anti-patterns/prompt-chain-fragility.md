# Prompt Chain Fragility

---
classification: non-promotable
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Statement

System reliability depends on **sequential LLM prompt chains** without structured state, schema validation, retries with bounds, or non-LLM checkpoints.

## Symptoms

- Orchestrator output parsed informally into tasks
- Plan quality varies run-to-run with no validation gate
- Single malformed JSON breaks entire run
- No version pinning on prompt templates

## Why It Fails

- LLM outputs are stochastic — chains amplify variance
- Debugging requires reading long chat logs
- Cannot contract-test intermediate artifacts
- Recovery logic becomes more prompts (meta-fragility)

## Corrective Pattern

- Structured planning output schema + validator
- [queue-backed-execution.md](../patterns/queue-backed-execution.md) with persisted task records
- [orchestration-without-contracts.md](orchestration-without-contracts.md) — inverse lesson

## Sources

- `source/swarm-ai-agents-prompts.ru.md` — orchestrator planning step
- `source/ai-agents-from-scratch.ru.md` — prompt-driven stages

## Promotion Potential

**NEVER PROMOTE** as architecture — prompts are tutorial vehicle only.
