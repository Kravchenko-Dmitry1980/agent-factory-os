# Lesson: Fail-Closed

## What is this?

**Fail-closed** means: if the system is not sure it is safe, it **stops** — it does not guess.

## Why does it matter?

Fail-open systems look fast until they publish wrong content, click the wrong button, or send the wrong email. Fail-closed trades false stops for fewer disasters.

## What can go wrong?

- Timeout treated as approval
- "Low risk" exceptions without audit
- Parser error → default allow

## How do we check it?

Run deny scenarios; trace must show block/deny events.

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
```

## Which demo shows it?

- `prototypes/fail-closed-external-action/` — no-approval, rejected, uncertain
- `prototypes/review-loop-agent/` — bypass-attempt

Doctrine: `agent-os/doctrine/fail-closed-execution.md`
