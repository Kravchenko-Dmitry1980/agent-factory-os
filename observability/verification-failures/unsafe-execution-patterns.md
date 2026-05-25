# Unsafe Execution Patterns

Patterns where action **almost** or **does** run without proper verification.

| Pattern | Trace signature | Gate |
|---------|-----------------|------|
| Publish after critic only | No `approval_requested` | Human HITL |
| Click before visual verify | `proposed_click` before `visual_verify` | GUI loop order |
| External send without approval | No `approval_requested` | fail-closed-external-action |
| Writeback without verify | No `verification_passed` before write | bounded-memory |
| Promote without scan | Jump to integrate | governed-promotion |

## Observable Block (Good)

```
unsafe_action_blocked  actor=gate  reason=deny-by-default
OUTCOME status=denied
```

## Repository Demos

- `prototypes/fail-closed-external-action/`
- `prototypes/integrations/gui-safe-action-workflow/`
