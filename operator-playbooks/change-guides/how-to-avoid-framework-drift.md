# How to Avoid Framework Drift

Framework drift = demos become a platform nobody can audit.

---

## Warning signs

- "Let's extract common engine"
- "One CLI to run all demos"
- Shared base class for all workflows
- Plugin registry for adapters
- pytest suite replacing human trace review

---

## Rules

1. **One demo = one lesson** — keep runnable alone
2. **No universal orchestrator** — compose in docs, not runtime
3. **Documentation over automation** — Phase 2.6 adds guides, not runners
4. **Evaluation stays small** — three scripts max unless new phase

---

## Docs

- `prototypes/governance/prototype-boundaries.md`
- `integrations-real/governance/anti-platform-rules.md`
- `evolution/governance/anti-platform-evolution.md`
- [../governance/no-platform-drift.md](../governance/no-platform-drift.md)

---

## If AI suggests framework

Say no. Link [../start-here/what-not-to-touch.md](../start-here/what-not-to-touch.md).

[../safety-guides/why-platform-drift-is-dangerous.md](../safety-guides/why-platform-drift-is-dangerous.md)
