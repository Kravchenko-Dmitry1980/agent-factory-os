# Expected Decisions

Decision vocabulary for governed workflows. Outcomes must be **explicit**, not inferred from silence.

---

## Decision Types

| Decision | Meaning | Default when |
|----------|---------|--------------|
| `ALLOW` | Verified + approved; action may proceed | All gates pass |
| `DENY` | Block terminal; no side effect | Missing approval, rejection, timeout |
| `HOLD` | Wait for human or more verification | Uncertainty, pending approval |
| `ESCALATE` | Stop automation; human/supervisor required | Retry exhausted, high ambiguity |
| `REJECT` | Governance/policy block (promotion, scan) | Provenance, topology, claim failures |

---

## Decision Rules by Gate

### Verification Gate

```text
If verification fails:
  expected decision = DENY or HOLD
  expected outcome = no external action, no memory writeback
```

### Approval Gate

```text
If approval is missing:
  expected decision = DENY
  expected event = approval_timeout OR approval_denied
  expected outcome = no external action
```

### Memory Gate

```text
If writeback unverified OR over limit:
  expected decision = DENY
  expected event = memory_write_rejected
  expected outcome = snapshot unchanged
```

### LLM Gate

```text
If output malformed OR timeout:
  expected decision = REJECT
  expected outcome = no trust transfer to downstream
```

### GUI Gate

```text
If visual state mismatch OR uncertain:
  expected decision = DENY
  expected event = unsafe_action_blocked
  expected outcome = no click/action
```

### Promotion Gate

```text
If provenance missing OR dangerous topology:
  expected decision = REJECT
  expected event = governance_rejection
  expected outcome = no corpus promotion
```

---

## Critic vs Human Decisions

| Actor | Decision weight |
|-------|-----------------|
| Critic | Advisory only — `verification_passed` with `advisory=true` |
| Human | Binding — approve/deny is terminal for publish |
| System | Fail-closed default — deny on uncertainty |

**Never:** critic PASS → decision ALLOW for external publish without human.

---

## Example Decision Chain (Happy Review)

```
1. Critic: advisory PASS (not final)
2. System: HOLD (await human)
3. Human: ALLOW
4. Publisher: ALLOW (execute)
```

## Example Decision Chain (Fail-Closed)

```
1. Critic: PASS (advisory)
2. Human: (no response)
3. System: DENY (timeout)
4. Executor: DENY (blocked)
```
