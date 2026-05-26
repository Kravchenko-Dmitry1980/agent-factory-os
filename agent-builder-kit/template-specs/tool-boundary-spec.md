# Tool Boundary Spec

Defines how agent templates declare and constrain tool use.

---

## Allowed Tools

Document explicitly per template:

| Category | Example | Default in v0.1 Review Assistant |
|----------|---------|----------------------------------|
| Read-only text | parse, summarize | yes (conceptual) |
| Draft generation | LLM draft | yes (advisory) |
| External publish | API, email, git push | **no** without approval |
| Shell | arbitrary commands | **forbidden** |
| Filesystem write | unrestricted write | **forbidden** |

---

## Forbidden Tools

Always forbidden without explicit governance exception:

- unrestricted shell (`bash -c`, `rm -rf`, etc.)
- unrestricted filesystem read/write
- production database write
- payment / billing APIs
- credential access
- autonomous web browsing with write actions

---

## Tool Permissions

Each tool entry must specify:

| Field | Description |
|-------|-------------|
| Tool name | Identifier |
| Permission level | read / propose / write |
| Approval required | yes/no |
| Fail-closed on error | yes/no |
| Audit event | canonical event name |

---

## Tool Risks

| Risk | Mitigation |
|------|------------|
| Data exfiltration | No unrestricted network |
| Destructive action | No shell; approval for writes |
| Credential leak | No secret tools in template |
| Silent side effect | Every tool call → trace event |

---

## Approval Before Tool Action

| Action type | Approval |
|-------------|----------|
| Read public context | no |
| Generate draft | no (marked unverified) |
| Publish / send / delete | **yes, human** |
| Write to memory | **yes, separate gate** |
| External API mutation | **yes, human** |

**Rule:** No production write without explicit human gate.

---

## Unsafe Tool Behavior

Block and emit `unsafe_action_blocked` when:

- tool invoked outside allowlist
- tool invoked after verification failure
- tool invoked without required approval
- bypass path attempted

---

## Tool Failure Handling

| Failure | Response |
|---------|----------|
| Timeout | fail-closed; optional bounded retry |
| Malformed response | `llm_malformed_output`; stop |
| Permission denied | `unsafe_action_blocked`; escalate if repeated |
| Partial success | treat as failure unless verified |

---

## Related

- [safety-gates/tool-use-gate.md](../safety-gates/tool-use-gate.md)
- [human-approval-spec.md](human-approval-spec.md)
- `agent-os/08_patterns/verification-before-writeback.md`
