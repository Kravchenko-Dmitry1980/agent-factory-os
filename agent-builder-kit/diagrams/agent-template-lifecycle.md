# Agent Template Lifecycle

```mermaid
stateDiagram-v2
  [*] --> draft
  draft --> review: sections complete
  review --> evaluation: checklists pass
  evaluation --> accepted: evaluation-gate pass
  accepted --> frozen: lead sign-off
  frozen --> changed: change proposal approved
  changed --> review: re-review required
  review --> evaluation
  evaluation --> accepted
  accepted --> frozen
```

## Notes

- **frozen** — no direct edits
- **changed** — only through [change-proposal-spec.md](../template-specs/change-proposal-spec.md)
- Rollback gate applies on every change from frozen

Reference: [template-lifecycle.md](../template-governance/template-lifecycle.md)
