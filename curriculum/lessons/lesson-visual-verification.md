# Lesson: Visual Verification

## What is this?

Before clicking in a GUI, the agent **checks the screen matches** what it expects (layout, labels, state).

## Why does it matter?

Blind clicks cause real damage — wrong form, wrong payment, wrong delete.

## What can go wrong?

- Coordinate-only automation
- Uncertain UI → click anyway
- Screenshot without semantic check

## How do we check it?

Mismatch scenario blocks action; audit shows verification_failed.

```powershell
python prototypes/gui-verification-loop/minimal-demo.py --scenario outcome-b
```

Trace: `observability/examples/unsafe-gui-action-trace.txt`

## Which demo shows it?

- gui-verification-loop
- gui-safe-action-workflow integration

Anti-pattern: `agent-os/09_antipatterns/unverified-gui-clicks.md`
