# Change Management & Safe Evolution (Phase 2.4)

**Status:** Governance-aware change discipline — not deployment engineering.

---

## Why AI Systems Decay Over Time

Governed workflows **rot** without malice:

- Retry limits creep upward "temporarily"
- Critic pass becomes implicit approval
- Mock adapters gain "real" shortcuts
- Shared helpers become accidental frameworks
- Observability becomes metrics without story

Each change alone looks small. Together they **erase gates**.

---

## Why Uncontrolled Evolution Is Dangerous

| Change | Hidden effect |
|--------|---------------|
| +1 retry | Masks verification bugs |
| Skip human on "low risk" | Autonomy leak |
| Merge shared module | Platform drift |
| Faster LLM path | Verification skipped |
| Remove escalation log | Invisible failures |

AI systems fail by **accumulation**, not single bugs.

---

## Why Governance Matters During Change

Doctrine and gates are not "v1 constraints" — they are **invariants**.

Every modification must answer:

- Which gate moves?
- Who can still stop unsafe action?
- What event proves the gate ran?

See [governance-gates/](governance-gates/).

---

## Why Rollback Thinking Is Critical

Forward fixes under pressure add complexity. **Rollback** restores known-good governance:

- Revert retry increase before debugging root cause
- Disable new adapter path before incident spreads
- Preserve audit lineage through reversal

See [rollback-thinking/](rollback-thinking/).

---

## Why Architecture Drift Is Invisible at First

Drift whispers before it shouts:

- "Just one base class"
- "Just extract to shared/"
- "Just auto-approve internal actions"

Early signals in [drift-detection/early-warning-signals.md](drift-detection/early-warning-signals.md).

---

## Structure

| Module | Purpose |
|--------|---------|
| [change-proposals/](change-proposals/) | Structured change thinking |
| [impact-analysis/](impact-analysis/) | Hidden side effects |
| [rollback-thinking/](rollback-thinking/) | Safe reversal |
| [drift-detection/](drift-detection/) | Architecture & governance drift |
| [governance-gates/](governance-gates/) | Modification boundaries |
| [safe-rollouts/](safe-rollouts/) | Incremental discipline (conceptual) |
| [anti-fragile-patterns/](anti-fragile-patterns/) | Survive mistakes |
| [architecture-regression/](architecture-regression/) | Slow decay |
| [examples/](examples/) | Change scenarios |
| [diagrams/](diagrams/) | Mermaid views |
| [governance/](governance/) | Boundaries |

---

## Relation to Repository

```
Phases 2.0–2.2  → runnable governed workflows
Phase 2.3       → how to see failures
Phase 2.4       → how to change without breaking governance
governance/     → promotion & policy (existing)
agent-os/       → doctrine (existing)
```

---

## Navigation

1. [change-proposals/change-template.md](change-proposals/change-template.md)
2. [governance-gates/gate-checklists.md](governance-gates/gate-checklists.md)
3. [examples/](examples/)
4. [governance/anti-platform-evolution.md](governance/anti-platform-evolution.md)
