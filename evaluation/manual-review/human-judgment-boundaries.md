# Human Judgment Boundaries

Some checks **cannot** be automated in Phase 2.5. Human reviewer must decide.

---

## AI Output Quality

| Automatable | Human judgment |
|-------------|----------------|
| JSON parses | Content is factually true |
| Schema valid | Claim supported by evidence |
| Exit code 0 | Prose is appropriate for audience |

**Rule:** Evaluation checks **gates**, not **truth**.

---

## Critic Verdict

| Automatable | Human judgment |
|-------------|----------------|
| Verdict enum recorded | Critic was correct |
| Uncertain blocks auto path | Disagreement with human |

**Rule:** Critic is advisory. Human may approve despite critic FAIL or reject despite critic PASS.

---

## Promotion Worthiness

| Automatable | Human judgment |
|-------------|----------------|
| Provenance field present | Source quality adequate |
| Topology not in blocklist | Concept worth teaching |
| Simulation gates pass | Ready for corpus promotion |

**Rule:** Simulator teaches gates; human promotes content.

---

## GUI Visual Match

| Automatable | Human judgment |
|-------------|----------------|
| Demo scenario enum match/mismatch | Real screenshot adequacy |
| Block on mismatch flag | Subtle UI regression |

**Rule:** Prototype uses mock states; production GUI needs human visual review.

---

## Escalation Handling

| Automatable | Human judgment |
|-------------|----------------|
| escalation_triggered event | Correct supervisor assigned |
| Retry ceiling enforced | Whether ceiling should change |

**Rule:** Changing ceiling is governance decision, not perf tweak.

---

## When Human Overrides Automation

Acceptable:

- Approve publish despite critic concern (with audit)
- Reject despite critic pass (documented in trace)

Unacceptable:

- Override without audit event
- Override by deleting gate from code
- Override via environment flag not in governance docs

---

## Boundary Summary

```text
Scripts answer:  Did the gate run?
Human answers:   Was the gate decision right for context?
Evaluation answers: Did behavior stay safe after change?
```

Do not expand evaluation to score "answer quality" — that is model evaluation platform drift.
