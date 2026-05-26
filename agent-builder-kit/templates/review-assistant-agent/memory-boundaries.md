# Review Assistant Agent — Memory Boundaries

v0.1 memory rules for Review Assistant.

## Allowed

| Memory type | Scope | Retention |
|-------------|-------|-----------|
| Current task context | single task | until terminal |
| Draft artifact | single task | until terminal or archive with approval |
| Audit trace | required | per observability policy |

## Forbidden

- Long-term user memory **by default**
- Automatic profile mutation
- Hidden writeback to persistent store
- Cross-session preference learning without approval
- Unbounded conversation history

## Read Rules

- Read task input and bounded context only
- Do not infer secrets from historical sessions (none stored in v0.1)

## Write Rules

- Write audit events (required)
- No persistent user profile writes
- Optional future memory → **separate governance approval** + memory-boundary gate

## Limits

| Limit | v0.1 default |
|-------|--------------|
| Task context | template-defined cap (document in implementation phase) |
| Long-term store | disabled |
| Reset | on task terminal |

## Drift Risks

| Risk | Mitigation |
|------|------------|
| Silent profile growth | no auto writeback |
| Review assistant remembers "user style" silently | forbidden in v0.1 |
| Memory becomes hidden autonomy | all writes traced |

## Event

Failed persistent write → `memory_write_rejected`

Reference: [memory-boundary-spec.md](../../template-specs/memory-boundary-spec.md)
