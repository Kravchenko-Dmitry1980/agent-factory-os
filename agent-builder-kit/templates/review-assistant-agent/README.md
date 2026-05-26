# Review Assistant Agent Template

**First reference agent template for Agent Builder Kit v0.1.**

Markdown-only specification. No runtime. No code.

---

## Purpose

Review Assistant helps create a **draft** and prepare it for **human review**. It structures critique and verification but does **not** publish automatically.

---

## What it does

- Accept review task (e.g. blog post draft, summary)
- Generate draft
- Optional advisory critique
- Verification checks
- Request human approval
- Deliver only after explicit human approve

---

## What it does NOT do

- Publish automatically
- Claim final truth
- Replace human reviewer
- Bypass approval gates
- Store unbounded user memory
- Execute unrestricted tools

---

## Files

| File | Content |
|------|---------|
| [agent-card.md](agent-card.md) | Identity and policies |
| [workflow.md](workflow.md) | Standard flow |
| [safety-gates.md](safety-gates.md) | Required gates |
| [memory-boundaries.md](memory-boundaries.md) | Memory rules |
| [human-approval.md](human-approval.md) | HITL policy |
| [evaluation.md](evaluation.md) | Scenarios |
| [expected-traces.md](expected-traces.md) | Trace examples |
| [failure-modes.md](failure-modes.md) | Known failures |
| [anti-patterns.md](anti-patterns.md) | Blocked patterns |
| [change-proposal.md](change-proposal.md) | Change template |
| [acceptance-criteria.md](acceptance-criteria.md) | Acceptance gate |

---

## Based on (reference only)

- `prototypes/review-loop-agent/`
- `prototypes/integrations/review-queue-workflow/`
- `evaluation/scenarios/review-loop-scenarios.md`
- `observability/examples/successful-review-trace.txt`
- `observability/examples/failed-review-trace.txt`

**Doctrine:** verification-first, fail-closed, governance-before-autonomy

---

## Version

v0.1 — Phase 3.0 specs only

## Freeze status (2026-05-26)

**FROZEN_WITH_NOTES** — see [sign-off/](sign-off/README.md) · [sign-off/FREEZE_RECORD.md](sign-off/FREEZE_RECORD.md)

Governance: [governance/PHASE_3_0_FREEZE_REVIEW_ASSISTANT.md](../../../governance/PHASE_3_0_FREEZE_REVIEW_ASSISTANT.md) · [governance/PHASE_3_START_CONDITIONS.md](../../../governance/PHASE_3_START_CONDITIONS.md)
