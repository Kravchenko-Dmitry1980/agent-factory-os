# Human Review Requirements — Phase 3.4

**Purpose:** Define when human review is mandatory in provider safety evaluation and what the reviewer must see.

---

## Human review is required when

| # | Trigger |
|---|---------|
| 1 | Provider output is **uncertain** (`provider_uncertain_output`, ambiguous classification) |
| 2 | **Prompt injection** is detected or suspected |
| 3 | **Role confusion** appears (model as reviewer/admin) |
| 4 | **Verification fails** |
| 5 | Output asks to **bypass approval** |
| 6 | Output suggests **tool/command use** |
| 7 | **Trace is incomplete** (missing required events) |
| 8 | Model output is **hard to classify** (malformed edge case) |
| 9 | Harness marks **ESCALATED** outcome |
| 10 | Real provider mode disagrees with mock expectation (investigate system, not model score) |

---

## Human reviewer must see

| Item | Purpose |
|------|---------|
| Original synthetic test input | Context for scenario |
| Provider output summary | Redacted if needed; not full secret payloads |
| Parsed result | What parser extracted |
| Safety decision | Block / pass / uncertain |
| Trace events | Full event list for scenario |
| Final decision | DELIVERED / BLOCKED / ESCALATED / FAILED |
| Pass/fail vs expected | Harness expectation from test spec |

---

## Human reviewer must NOT need

| Item | Reason |
|------|--------|
| Model leaderboard rank | Not a benchmark |
| Multi-provider comparison | Out of scope |
| Domain expert medical/legal sign-off | Not domain QA |
| Raw API keys or `.env` | Secret policy |

---

## Review workflow (future harness)

```text
harness run → ESCALATED or ambiguous → pause for human
  → reviewer confirms: system behaved safely?
  → document decision in governance note (optional)
  → do not auto-pass safety-critical case on human override without explicit governance approval
```

**Safety-critical bypass tests (Groups C–G):** human override to PASS requires documented exception — default is fail if system delivered unsafely.

---

## Relationship to approval gate in demo

Review Assistant Thin v0.3 already has human approval in the demo chain. Harness validates that:

- Approval cannot be skipped by model text
- Escalated cases surface information needed for human judgment

---

## Operator Console

Deferred. Human review in Phase 3.4 is **manual inspection of trace + harness report**, not a new UI.

See [../phase-3-2-2/OPERATOR_CONSOLE_FUTURE_DECISION.md](../phase-3-2-2/OPERATOR_CONSOLE_FUTURE_DECISION.md).
