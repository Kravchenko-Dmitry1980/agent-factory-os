---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Promotion Candidates Review

Classification of every extracted concept. **No promotions executed in this phase.**

---

## SAFE FUTURE PROMOTION

Candidates aligned with Agent-OS themes; need contract/trace formalization before merge.

| Concept | Location | Notes |
|---------|----------|-------|
| Human-in-the-loop approval | `patterns/human-in-the-loop-approval.md` | Aligns with human-escalation-gate |
| Progressive autonomy | `patterns/progressive-autonomy.md` | MVP-first rollout |
| Review gate | `patterns/review-gate.md` | Pre-release checkpoint |
| Orchestration lifecycle (skeleton) | `lifecycle/orchestration-lifecycle.md` | Map to task lifecycle contracts |
| Queue-backed execution | `patterns/queue-backed-execution.md` | Aligns with durable-task-coordination |
| Approval before external action | `patterns/approval-before-external-action.md` | Fail-closed external tools |
| Safe autonomy levels | `hitl/safe-autonomy.md` | Maturity model |
| Human approval boundaries | `hitl/human-approval-boundaries.md` | Policy input |
| Execution cost visibility | `budget-control/execution-cost-visibility.md` | Observability |
| Critique limitations | `critique/critique-limitations.md` | Must accompany any critic promotion |
| Staged agent evolution | `patterns/staged-agent-evolution.md` | Onboarding maturity |

---

## RESEARCH ONLY

Useful operationally; insufficient rigor or wrong abstraction level for direct canonical merge.

| Concept | Location | Blocker |
|---------|----------|---------|
| Critique before publish | `patterns/critique-before-publish.md` | Needs verification boundary |
| Execution feedback loop | `patterns/execution-feedback-loop.md` | Needs eval/writeback governance |
| Budget-aware orchestration | `budget-control/budget-aware-orchestration.md` | Enforcement semantics undefined |
| Retry cost awareness | `budget-control/retry-cost-awareness.md` | Needs retry policy contracts |
| Critic loop | `critique/critic-loop.md` | LLM-only QA |
| Plan approval for large runs | `lifecycle/` phase 2 | Size threshold heuristic |
| Task dependencies in queue | Prompt 4 extraction | No DAG contract |
| Closed content loop | Prompt 4 | Domain-specific (content factory) |
| waiting_question escalation | `hitl/escalation-to-human.md` | No SLA/timeout spec |
| Test factory via critic | Prompt 5 | Pass-rate ≠ truth |

---

## NEVER PROMOTE

**Mandatory section — these must not enter canonical layer as architecture.**

| Concept | Reason |
|---------|--------|
| **«8-agent swarm» as default architecture** | Fixed role topology; premature complexity |
| **Personality-centric orchestration** | Prompt flavor ≠ responsibilities/contracts |
| **Critic solves hallucinations** | False verification claim |
| **Prompt-only governance** | No policy plane, no audit |
| **Orchestration without contracts** | Fragile, untestable handoffs |
| **Autonomy without approval boundaries** | External harm risk |
| Tutorial stack as architecture | Next.js/Express/seed.sql coupling |
| CLAUDE.md as system memory governance | Session hint, not memory plane |
| «Хороший промпт = 80% качества» | Oversimplification |
| Brand/project profile injection as policy | Context stuffing ≠ policy engine |
| Telegram long-polling as integration pattern | Not production messaging |
| 8 named personas in seed.sql | Branding artifact |
| Test pass-rate as quality SLA | Critic circularity |
| Solo `/task` bypass without review policy | Unbounded autonomy path |
| Knowledge chunks in system prompt | RAG shortcut without retrieval scoring |

---

## Per-Pattern Classification

| File | Classification |
|------|----------------|
| human-in-the-loop-approval.md | reusable-pattern → SAFE |
| progressive-autonomy.md | reusable-pattern → SAFE |
| review-gate.md | reusable-pattern → SAFE |
| orchestration-lifecycle.md (pattern) | reusable-pattern → SAFE |
| queue-backed-execution.md | reusable-pattern → SAFE |
| critique-before-publish.md | reusable-pattern → RESEARCH |
| staged-agent-evolution.md | reusable-pattern → SAFE |
| execution-feedback-loop.md | reusable-pattern → RESEARCH |
| approval-before-external-action.md | reusable-pattern → SAFE |

## Per-Anti-pattern Classification

All `anti-patterns/*.md` → **non-promotable** (warnings stay in operational corpus; some *inverse lessons* SAFE as anti-pattern entries in Agent-OS already exist separately).

---

## Source Material Classification

| Source content | Classification |
|----------------|----------------|
| Этапы 0, 4 install/setup | beginner-tutorial |
| Промты 0–1 framework scaffold | beginner-tutorial |
| Этап 1 ЗАДАЧА.md questions | operational-guidance |
| Этап 9 quality/budget | reusable-pattern (extracted) |
| Prompt 3 run orchestration | reusable-pattern (extracted) |
| Prompt 2 eight personas | non-promotable |
| Prompt 5 multi-project platform | operational-guidance (partial) |

---

## Next Step (out of scope for this phase)

Formal promotion review in `governance/PROMOTION_LOG.md` — **not executed here**.
