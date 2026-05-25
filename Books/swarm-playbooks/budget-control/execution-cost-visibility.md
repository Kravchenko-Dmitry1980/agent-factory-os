---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Execution Cost Visibility

## Definition

Operators can **see** cost and token usage at task and run granularity in the UI, not only in provider billing portal.

## Operational Context

- Dashboard shows spend per прогон and per задача
- Этап 9: «как мне читать стоимость»

## Why It Works

- Builds intuition for multi-agent cost multiplication
- Supports decisions on model choice and swarm size
- Enables post-hoc optimization of prompts and roster

## Production Extensions (not in playbooks)

- Cost attribution by project/tenant
- Export to billing/analytics
- Anomaly detection on spikes

## Failure Modes

- Incomplete token capture on streaming
- Hidden tool/API costs excluded
- Stale prices → wrong USD estimate

## Sources

- `source/ai-agents-from-scratch.ru.md` — этап 9
- `source/swarm-ai-agents-prompts.ru.md` — Prompt 4

## Promotion Potential

**SAFE FUTURE PROMOTION** — observability pattern; pair with trace records in canonical layer.
