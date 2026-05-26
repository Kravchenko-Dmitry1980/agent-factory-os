# Change Lock — Task Triage Agent Specs v0.1

**Date:** 2026-05-26  
**Freeze:** task-triage-agent-specs-v0.1  
**Status:** ACTIVE

---

## After Freeze — Required for Any Spec Change

1. [change-proposal.md](../change-proposal.md) with reason and scope
2. Scope review
3. Safety gate review
4. No-execution impact review
5. No-orchestrator impact review
6. Provider / memory policy review
7. Evaluation impact review
8. Rollback plan
9. Explicit human approval

---

## Frozen Semantic Content

Changes to these files require full change lock process:

- All files listed in [SPEC_FREEZE_RECORD.md](SPEC_FREEZE_RECORD.md)
- Decision enum in [contract.md](../contract.md) / [outputs.md](../outputs.md)
- Safety gate definitions in [safety-gates.md](../safety-gates.md)
- Boundary policies: no-execution, no-orchestrator, provider, memory

---

## Allowed Without Full Proposal

| Change | Condition |
|--------|-----------|
| Navigation links | No semantic change |
| Sign-off metadata | Append-only in sign-off/ |
| Typo fixes | No meaning change — note in governance |
| Cross-links to new governance docs | Navigation only |

---

## Forbidden Without New Phase

| Change | Reason |
|--------|--------|
| Adding code | Phase 3.6-Impl + GO/NO-GO |
| Adding provider calls | Separate provider phase |
| Adding memory / persistence | Separate memory phase |
| Adding routing / delegation | Violates no-orchestrator |
| Adding execution capability | Violates no-execution |
| Adding task queue | PM platform drift |
| Adding runtime / factory behavior | Scope violation |
| Modifying frozen decisions (Review Assistant line) | Protected |
| Changing final decision set | Contract break — major version |
| Removing human approval requirement | Governance erosion |
| Importing external templates | Scope violation |

---

## Version Bump Rules

| Change type | Version |
|-------------|---------|
| Typo / navigation | v0.1 (note in sign-off) |
| Clarification, no behavior change | v0.1.x patch |
| New eval cases (synthetic) | v0.1.x patch |
| Contract enum change | v0.2+ — full review |
| Implementation addition | New artifact — not spec version |

---

## Unlock Procedure

To unfreeze or major revision:

1. Governance review with FAIL or drift report
2. [ROLLBACK_RECORD.md](ROLLBACK_RECORD.md) if reverting
3. New freeze cycle after approval

Governance: [PHASE_3_5_FREEZE_TASK_TRIAGE_AGENT_SPECS_V0_1_REVIEW.md](../../../../governance/PHASE_3_5_FREEZE_TASK_TRIAGE_AGENT_SPECS_V0_1_REVIEW.md)
