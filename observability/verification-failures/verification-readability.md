# Verification Readability

## Good Log Line

```
[19:56:59] verification_failed actor=verifier reason=GUI outcome B (wrong_screen) expected=settings_saved actual=profile
```

## Bad Log Line

```
[19:56:59] verify ok=false code=12
```

## Checklist

- [ ] Named gate (visual, schema, policy)
- [ ] Expected vs actual when applicable
- [ ] Advisory flag for critic
- [ ] Link to next event (retry vs escalate vs deny)
- [ ] No opaque error codes without prose

## Trace Tie-In

Every `verification_failed` should be followed within 3 lines by:

- `retry_triggered`, OR
- `escalation_triggered`, OR
- `unsafe_action_blocked`

Otherwise reader cannot predict system behavior.
