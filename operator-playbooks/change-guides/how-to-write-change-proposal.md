# How to Write Change Proposal

Use template: `evolution/change-proposals/change-template.md`

---

## Minimum Fields

| Field | Question to answer |
|-------|-------------------|
| What changes | Files and behavior |
| Why | Problem being solved |
| Which gate moves | Approval? Retry? Verification? |
| Risk | low / medium / high |
| Rollback | How to revert in 5 minutes |
| Evaluation | Which scenarios to re-run |

---

## Risk Guide

| High risk | Examples |
|-----------|----------|
| Yes | shared/gates.py, retry limits, approval logic, new shared runtime |
| Medium | Single demo behavior, adapter mock path |
| Low | operator-playbooks docs only |

---

## Submit

- Save in `evolution/change-proposals/` or link in PR description
- Human review before merge on high-risk

Examples: `evolution/change-proposals/high-risk-changes.md`, `low-risk-changes.md`
