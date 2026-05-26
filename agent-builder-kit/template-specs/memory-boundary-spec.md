# Memory Boundary Spec

Defines what agent templates may store, read, and write.

---

## What Memory Is Allowed

| Type | Default | Notes |
|------|---------|-------|
| Task context | yes | Current session only |
| Draft artifacts | yes | Until task terminal |
| Approval decisions | yes | Audit trail |
| User preferences (explicit) | optional | Requires separate approval to enable |

---

## What Memory Is Forbidden

- infinite / unbounded conversation history
- automatic personality mutation
- uncontrolled self-learning memory
- hidden writeback to long-term store
- cross-user memory without isolation
- credential or secret storage in agent memory

---

## When Memory Can Be Read

- During active task processing
- During human review (full audit context)
- During evaluation replay (test scenarios)

**Not allowed:** read long-term memory to infer secrets or bypass approval.

---

## When Memory Can Be Written

| Write type | Approval |
|------------|----------|
| Task-scoped draft | no (ephemeral) |
| Audit log entry | automatic (required) |
| Long-term user profile | **human approval required** |
| Cross-session preference | **human approval required** |

Emit `memory_write_rejected` when writeback fails verification or exceeds limits.

---

## Who Approves Memory Writeback

- **Human operator** for any persistent store
- **Governance review** for new memory categories
- No automatic writeback on task completion

---

## Memory Size Limits

| Limit | Default |
|-------|---------|
| Task context tokens | template-defined cap |
| Retention after task | purge or archive per policy |
| Long-term store | disabled in v0.1 Review Assistant |

---

## Memory Reset Policy

- Task terminal → clear task context (unless explicitly archived with approval)
- Template version change → evaluate memory compatibility
- User request → reset allowed with audit

---

## Memory Drift Risks

| Risk | Guard |
|------|-------|
| Silent profile growth | no auto writeback |
| Stale context | task-scoped only |
| Conflicting preferences | human resolves |
| Memory as hidden autonomy | trace all writes |

---

## Explicitly Rejected

- **Infinite memory** — must have caps and reset
- **Automatic personality mutation** — forbidden
- **Uncontrolled self-learning memory** — forbidden without governance + eval harness

---

## Related

- [safety-gates/memory-boundary-gate.md](../safety-gates/memory-boundary-gate.md)
- `observability/event-taxonomy/canonical-events.md` (`memory_write_rejected`)
- [templates/review-assistant-agent/memory-boundaries.md](../templates/review-assistant-agent/memory-boundaries.md)
