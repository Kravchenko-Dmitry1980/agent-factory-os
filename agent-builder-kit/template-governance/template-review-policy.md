# Template Review Policy

## Who Reviews

| Stage | Reviewer |
|-------|----------|
| draft → review | template author + one peer |
| review → evaluation | operator or developer assessor |
| evaluation → accepted | project lead |
| accepted → frozen | governance + lead co-sign |
| frozen → change | change proposal approver |

## Review Inputs

- [template-acceptance-checklist.md](../evaluation-checklists/template-acceptance-checklist.md)
- [phase-3-template-review-checklist.md](../evaluation-checklists/phase-3-template-review-checklist.md)
- [anti-pattern-checklist-spec.md](../template-specs/anti-pattern-checklist-spec.md)

## Review Outputs

- PASS / CONDITIONAL / FAIL
- Gap list with owners
- Trace comparison notes

## Blockers

Any scope violation (runtime, factory, external import, CV/twin) → **FAIL** until removed.

## Timeline

Phase 3.0: review within same phase; no parallel implementation.
