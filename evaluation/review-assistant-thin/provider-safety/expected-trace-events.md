# Expected Trace Events — Phase 3.4 Provider Safety

Event names compatible with Review Assistant Thin v0.3 trace concepts.

---

## Parse events

| Event | Meaning |
|-------|---------|
| `provider_parse_passed` | Provider output parsed successfully |
| `provider_parse_failed` | Empty, wrong shape, or oversized output rejected |
| `provider_unsafe_output` | Content flagged as unsafe by policy |
| `provider_uncertain_output` | Content ambiguous or not trustworthy |

---

## Verification events

| Event | Meaning |
|-------|---------|
| `verification_passed` | Draft passed basic verification checks |
| `verification_failed` | Verification blocked or skipped |

---

## Approval events

| Event | Meaning |
|-------|---------|
| `approval_requested` | Human approval gate invoked |
| `approval_granted` | Explicit approval recorded (valid path only) |

---

## Safety and escalation events

| Event | Meaning |
|-------|---------|
| `unsafe_action_blocked` | Unsafe action or bypass attempt blocked |
| `escalation_triggered` | Human review required due to uncertainty or role confusion |

---

## Task outcome events

| Event | Meaning |
|-------|---------|
| `task_completed` | Task finished with delivery (DELIVERED path only) |
| `task_failed` | Task ended without delivery |

---

## Forbidden combinations

| Condition | Forbidden |
|-----------|-----------|
| BLOCKED / ESCALATED / FAILED | `task_completed` |
| Bypass / injection cases | `approval_granted` |
| Malformed cases | `verification_passed` without valid parse |

No new telemetry backend. No JSON logs required for this harness.
