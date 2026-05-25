---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Critique Limitations

## Mandatory Statements

1. **Critique cannot replace governance.** Policy, approvals, audit, and contracts live outside critic prompts.
2. **Critique cannot guarantee truthfulness.** Another LLM cannot reliably detect all hallucinations in sibling LLM output.
3. **Critique cannot replace human review** for external-facing or high-stakes artifacts.
4. **Critique pass-rate is not quality SLA.** Test factory metrics measure critic agreement, not ground truth.

## Known Failure Modes

| Failure | Example |
|---------|---------|
| Shared model bias | Critic accepts plausible fiction |
| No source grounding | Invented citations pass |
| Verbosity bias | Longer answer rated «better» |
| False negatives | Over-aggressive rework wastes cost |
| Gaming | Executor learns critic prompt patterns |

## Safe Use

- Pre-filter for **obvious** issues (format, missing sections, contradictions with brief)
- Bounded rework only
- Always pair with human review gate
- Log verdicts for later eval of critic accuracy

## Never Use As

- Compliance sign-off
- Medical/legal/financial verification
- Substitute for fact-check tools or RAG with citations
- Auto-publish trigger alone

## Sources

- `source/ai-agents-from-scratch.ru.md` — «ИИ может ошибаться и выдумывать»
- `source/swarm-ai-agents-prompts.ru.md` — critic role oversell in Prompt 2–3

## Promotion Potential

**SAFE FUTURE PROMOTION** — limitations doc should accompany any critic pattern promoted to Agent-OS.
