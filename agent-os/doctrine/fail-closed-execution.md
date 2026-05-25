# Fail-closed Execution Doctrine

Default to **safe non-completion** until explicitly resolved.

---

## Core Thesis

Production agent harnesses optimize for **correct halt or retry**, not apparent progress. Fail-closed execution spans tool defaults, loop termination, writeback rejection, and external action denial.

---

## Two Complementary Patterns (Do Not Merge)

### Fail-closed defaults — tool layer

[[fail-closed-defaults]]

- New tools: serial, write-assumed, hook on parse failure
- Parse failure in batch → serial path
- Forgotten unsafe flags → slower but safe

**Scope:** tool metadata, concurrency classification, permission-adjacent defaults.

### Fail-closed agent loop — lifecycle layer

[[fail-closed-agent-loop]]

- Verification fail → block terminal state
- Permission deny → non-success path
- Ambiguous done → retry, escalate, halt — **not** success default
- Pairs with [[verification-before-writeback]]

**Scope:** loop termination, side effects, GUI outcomes.

Doctrine **disambiguates** these; semantic audit flagged merge confusion as drift risk.

---

## Consolidated Behaviors

| Event | Fail-closed response |
|-------|---------------------|
| Tool parse failure | Serial/safe batch |
| Verification fail | Loop continues or halts |
| Writeback without verify | Reject payload |
| External action without approval | Deny tool |
| GUI unverified click | No progress credit |
| Ambiguous terminal | Withhold success ([[withholding-errors]]) |

---

## Review Gates & Escalation

Fail-closed does not mean infinite stall:

- Retry **within budget** ([[infinite-retry-loops]] inverse)
- Escalate to human when automated resolution exhausted
- Circuit breaker on repeated GUI C outcomes

Review gates (operational reference) are **human fail-closed** on release — no publish until approve event.

---

## GUI Verification Requirements

[[visual-verification]] + [[fail-closed-agent-loop]]:

- Transport success ≠ task progress
- [[unverified-gui-clicks]] is primary anti-pattern
- [[brittle-gui-automation]] compounds fail-open risk

---

## Production Tradeoff

Over-aggressive fail-closed without retry budget frustrates users. Under-aggressive ships wrong clicks and bad memory. Tune per modality and risk tier.

---

## Sources

- `agent-os/08_patterns/fail-closed-defaults.md`
- `agent-os/08_patterns/fail-closed-agent-loop.md`
- `agent-os/09_antipatterns/unverified-gui-clicks.md`
- `governance/SEMANTIC_LINKING_AUDIT.md`

See also: [canonical-principles.md](canonical-principles.md) § Principle 3
