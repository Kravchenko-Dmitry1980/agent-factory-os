# Lesson: Critic Is Not Truth

## What is this?

A **critic** reviews quality — like an editor. It gives advice. It is **not** a verifier that guarantees facts.

## Why does it matter?

Critics can pass text with wrong facts that **sound** professional. If critic pass → auto publish, humans never catch errors.

## What can go wrong?

- Wiring critic PASS to publish
- Treating "verdict: pass" as verification_passed (final)

## How do we check it?

Trace must show human step for external publish. Read failed-review example.

`observability/examples/failed-review-trace.txt` — critic passed, human denied.

## Which demo shows it?

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
```

Module: [../modules/module-02-why-ai-systems-fail.md](../modules/module-02-why-ai-systems-fail.md)
