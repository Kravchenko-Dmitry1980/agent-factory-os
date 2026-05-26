# Task Triage Agent Template

**Second reference agent template for Agent Builder Kit v0.1.**

Markdown-only specification. No runtime. No code.

---

## Template name

**Task Triage Agent**

## Status

| Field | Value |
|-------|-------|
| Version | **task-triage-agent-specs-v0.1** |
| Freeze status | **FROZEN_WITH_NOTES** |
| Sign-off | **SIGNED_OFF_WITH_NOTES** |
| Implementation | **NOT_STARTED** |
| Code | **NONE** |
| Runtime | **NONE** |

## Purpose

Classify incoming text tasks, detect risk, identify missing information, and recommend a safe next step.

## Current phase

**Phase 3.5-Freeze complete** — specification freeze only.

No implementation. No thin demo. No provider calls.

**This is only a specification freeze. No implementation exists.**

---

## What this template is

- text-only advisory agent
- task classifier
- risk detector
- missing-info detector
- next-step recommender
- human-approval recommender

---

## What this template is not

- executor
- orchestrator
- router
- task queue
- PM platform
- tool user
- provider caller
- automation engine

---

## Reading order

1. [agent-card.md](agent-card.md)
2. [purpose.md](purpose.md)
3. [non-purpose.md](non-purpose.md)
4. [contract.md](contract.md)
5. [inputs.md](inputs.md)
6. [outputs.md](outputs.md)
7. [workflow.md](workflow.md)
8. [safety-gates.md](safety-gates.md)
9. [no-execution-boundary.md](no-execution-boundary.md)
10. [no-orchestrator-boundary.md](no-orchestrator-boundary.md)
11. [human-approval.md](human-approval.md)
12. [provider-policy.md](provider-policy.md)
13. [memory-policy.md](memory-policy.md)
14. [evaluation.md](evaluation.md)
15. [expected-traces.md](expected-traces.md)
16. [failure-modes.md](failure-modes.md)
17. [anti-patterns.md](anti-patterns.md)
18. [acceptance-criteria.md](acceptance-criteria.md)
19. [change-proposal.md](change-proposal.md)
20. [implementation-notes.md](implementation-notes.md)
21. [sign-off/README.md](sign-off/README.md)

---

## Files

| File | Content |
|------|---------|
| [agent-card.md](agent-card.md) | Identity, inputs, outputs, forbidden capabilities |
| [purpose.md](purpose.md) | What the agent does |
| [non-purpose.md](non-purpose.md) | What the agent must not do |
| [inputs.md](inputs.md) | Accepted input fields |
| [outputs.md](outputs.md) | Output fields and allowed values |
| [contract.md](contract.md) | Input/output/decision contract |
| [workflow.md](workflow.md) | Standard triage flow |
| [safety-gates.md](safety-gates.md) | Required safety gates |
| [no-execution-boundary.md](no-execution-boundary.md) | No execution policy |
| [no-orchestrator-boundary.md](no-orchestrator-boundary.md) | No orchestrator policy |
| [human-approval.md](human-approval.md) | HITL policy |
| [provider-policy.md](provider-policy.md) | No provider by default |
| [memory-policy.md](memory-policy.md) | No persistent memory by default |
| [evaluation.md](evaluation.md) | Future synthetic evaluation groups |
| [expected-traces.md](expected-traces.md) | Required trace events |
| [failure-modes.md](failure-modes.md) | Known failure modes |
| [anti-patterns.md](anti-patterns.md) | Blocked patterns |
| [change-proposal.md](change-proposal.md) | How to propose changes |
| [acceptance-criteria.md](acceptance-criteria.md) | Acceptance gate checklist |
| [implementation-notes.md](implementation-notes.md) | Future implementation path |
| [sign-off/](sign-off/README.md) | Freeze and sign-off bundle (v0.1) |

---

## Based on (reference only)

- [governance/phase-3-5-plan/](../../../governance/phase-3-5-plan/README.md)
- [templates/review-assistant-agent/](../review-assistant-agent/README.md) — first reference template
- [evaluation/scripts/check_review_assistant_provider_safety.py](../../../evaluation/scripts/check_review_assistant_provider_safety.py) — baseline discipline

**Doctrine:** advisory-only, fail-closed, governance-before-autonomy, no execution, no orchestration

---

## Version

**v0.1** — `task-triage-agent-specs-v0.1` — frozen 2026-05-26

## Freeze (2026-05-26)

**FROZEN_WITH_NOTES** · **SIGNED_OFF_WITH_NOTES** — see [sign-off/](sign-off/README.md) · [sign-off/SPEC_FREEZE_RECORD.md](sign-off/SPEC_FREEZE_RECORD.md)

Implementation: **NOT_STARTED**. This freeze does **not** permit code.

Governance: [governance/PHASE_3_5_FREEZE_TASK_TRIAGE_AGENT_SPECS_V0_1_REVIEW.md](../../../governance/PHASE_3_5_FREEZE_TASK_TRIAGE_AGENT_SPECS_V0_1_REVIEW.md) · [governance/PHASE_3_5_TASK_TRIAGE_AGENT_SPECS_REVIEW.md](../../../governance/PHASE_3_5_TASK_TRIAGE_AGENT_SPECS_REVIEW.md)
