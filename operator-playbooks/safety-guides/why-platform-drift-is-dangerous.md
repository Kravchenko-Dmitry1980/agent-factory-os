# Why Platform Drift Is Dangerous

**Platform drift** = educational demos slowly become an undeployable "product" with hidden coupling and weakened gates.

---

## How it starts (innocently)

- "Let's share one orchestrator"
- "Let's add a CLI for all demos"
- "+1 retry while we debug"
- "Skip human for internal calls"

---

## How it ends

- Nobody knows which gate still runs
- Tests green while governance dead
- New person must learn framework + domain

---

## This repo's stance

Stay a **laboratory**. Prototypes teach; they don't ship.

---

## Prevention

- [../change-guides/how-to-avoid-framework-drift.md](../change-guides/how-to-avoid-framework-drift.md)
- [../governance/no-platform-drift.md](../governance/no-platform-drift.md)
- `evolution/drift-detection/early-warning-signals.md`

---

## Example narrative

`evolution/examples/unsafe-shared-runtime.md`
