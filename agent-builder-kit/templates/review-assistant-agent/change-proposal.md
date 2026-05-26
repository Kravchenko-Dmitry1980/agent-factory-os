# Review Assistant Agent — Change Proposal

Template-specific change proposal. Fill when modifying v0.1+.

Reference: [change-proposal-spec.md](../../template-specs/change-proposal-spec.md)

---

## Proposal ID

`RA-CP-<number>`

## What changes?

_Describe sections/files affected._

## Why?

_Incident, eval gap, or clarity improvement._

## What can break?

- Evaluation scenarios: _list_
- Operator playbooks referencing Review Assistant
- Curriculum modules citing workflow

## Which safety gate is affected?

- [ ] fail-closed
- [ ] verification
- [ ] human approval
- [ ] escalation
- [ ] evaluation
- [ ] memory-boundary (if enabled later)
- [ ] tool-use (if tools added)

## Which trace should be compared?

Before: `expected-traces.md` scenario ___  
After: _new trace draft_

## Which evaluation check must run?

- [ ] safety-regression-checklist.md
- [ ] All five scenarios in evaluation.md
- [ ] trace-review-checklist.md

## Rollback plan

Restore `templates/review-assistant-agent/` at git tag `review-assistant-v0.1` (or prior commit). Rerun evaluation checklists.

## Who approves?

| Role | Name | Date |
|------|------|------|
| Author | | |
| Lead | | |

---

## v0.1 Note

Initial version — no changes until frozen. First change requires unfreeze per [template-freeze-policy.md](../../template-governance/template-freeze-policy.md).
