# Template Lifecycle

## Stages

```
draft
  → review
  → evaluation
  → accepted
  → frozen
  → changed only through proposal
```

## Stage Definitions

| Stage | Meaning | Exit criteria |
|-------|---------|---------------|
| **draft** | Author writing spec | All required sections started |
| **review** | Peer/governance review | Checklists pass |
| **evaluation** | Scenarios and traces verified | evaluation-gate pass |
| **accepted** | Approved for use as reference | Sign-off recorded |
| **frozen** | No direct edits | Version locked |
| **changed** | Only via change proposal | rollback-gate pass |

## Phase 3.0 Status

Review Assistant Agent v0.1 target: **accepted** (pending review) → **frozen** after `PHASE_3_0_BUILDER_KIT_REVIEW.md` PASS.

## Diagram

See [diagrams/agent-template-lifecycle.md](../diagrams/agent-template-lifecycle.md)
