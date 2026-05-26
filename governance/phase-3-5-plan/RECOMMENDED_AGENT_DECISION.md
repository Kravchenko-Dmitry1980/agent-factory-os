# Recommended Agent Decision — Phase 3.5

**Date:** 2026-05-26  
**Decision status:** **PLAN_ONLY**

---

## Recommended second text agent template

# Task Triage Agent

---

## Rationale

| Factor | Detail |
|--------|--------|
| Complements Review Assistant | Triage before work; Review during/after draft |
| Classifies work safely | Type, risk, missing info, next step — no execution |
| Project leadership utility | Helps decide plan vs impl vs review vs defer |
| Text-only default | No tools, no provider, no files by default |
| Synthetic evaluation | Task strings + expected TRIAGED/ESCALATE/BLOCKED decisions |
| Reuses proven pattern | Template → eval → thin (later) → freeze discipline |

---

## Critical boundary

**Task Triage Agent must not execute tasks.**

It only recommends:

| Output | Meaning |
|--------|---------|
| Task type | planning, implementation, review, … |
| Risk level | low, medium, high, critical |
| Missing information | What is unclear before work starts |
| Suggested next step | Advisory action for human |
| Human approval requirement | yes/no + reason |
| Defer / escalate | Whether task should wait or escalate |
| Final triage decision | TRIAGED, NEEDS_CLARIFICATION, ESCALATE, BLOCKED, REJECT_UNSAFE |

Triage output is **advisory**. Human decides what happens next.

---

## Rejected alternatives

| Candidate | Reason |
|-----------|--------|
| Safe Content Draft Agent | Duplicates Review Assistant |
| Meeting Summary Review Agent | Domain pipeline too early |
| Research Note Agent | RAG/knowledge graph pull too early |

---

## Implementation timing

**Do not implement in Phase 3.5-Plan.**

Future Phase 3.5-Impl should start with **specs only** under `agent-builder-kit/templates/task-triage-agent/` — no code.

See [SECOND_TEMPLATE_IMPLEMENTATION_OPTIONS.md](SECOND_TEMPLATE_IMPLEMENTATION_OPTIONS.md).

---

## Non-negotiable policies

1. [TASK_TRIAGE_AGENT_NO_EXECUTION_POLICY.md](TASK_TRIAGE_AGENT_NO_EXECUTION_POLICY.md)
2. [TASK_TRIAGE_AGENT_NO_ORCHESTRATOR_POLICY.md](TASK_TRIAGE_AGENT_NO_ORCHESTRATOR_POLICY.md)
3. [TASK_TRIAGE_AGENT_HUMAN_APPROVAL_POLICY.md](TASK_TRIAGE_AGENT_HUMAN_APPROVAL_POLICY.md)

If any future design violates these → **NO_GO** for implementation.

---

## GO/NO-GO for next phase

See [PHASE_3_5_GO_NO_GO.md](PHASE_3_5_GO_NO_GO.md) — expected **CONDITIONAL_GO_FOR_SPECS_ONLY**.
