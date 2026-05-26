# Provider Safety Harness — Phase 3.4

**Status:** **FROZEN_WITH_NOTES** — [provider-safety-harness-v0.1](freeze/README.md) (2026-05-26)

**Small local safety-boundary check** for Review Assistant Thin v0.3 provider-output handling.

---

## What this checks

Whether synthetic provider-like output that is malformed, unsafe, injection-like, approval-bypassing, verification-bypassing, command-suggesting, secret-requesting, role-confusing, overconfident, or irrelevant still maps to safe system decisions:

- **BLOCKED**
- **ESCALATED**
- **FAILED**

Only a clean neutral synthetic draft may map to **DELIVERED**, and only after parse, verification, and approval gates.

---

## Why it exists

Phase 3.4 adds a fixed local harness to verify the safety chain:

```text
provider output → parse → safety check → verification → human approval → delivery or block
```

This is a **safety-boundary harness**, not a model intelligence test.

---

## Why this is NOT a benchmark

- No scores
- No ranking
- No leaderboard
- No model comparison
- No provider quality assessment

See [no-benchmark-note.md](no-benchmark-note.md).

---

## Why this is NOT a red-team platform

- Controlled synthetic cases only
- No exploit library
- No harmful command corpus
- No real data exfiltration attempts

See [no-red-team-note.md](no-red-team-note.md).

---

## How to run

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_provider_safety.py
```

Expected:

```text
Summary: PASS=16 FAIL=0
```

No network. No API keys. No LM Studio. No cloud providers.

---

## Files

| File | Purpose |
|------|---------|
| [provider-safety-cases.md](provider-safety-cases.md) | All 16 synthetic cases by group |
| [expected-decisions.md](expected-decisions.md) | DELIVERED / BLOCKED / ESCALATED / FAILED rules |
| [expected-trace-events.md](expected-trace-events.md) | Allowed trace events |
| [harness-limitations.md](harness-limitations.md) | What this does not prove |
| [no-benchmark-note.md](no-benchmark-note.md) | No scoring policy |
| [no-red-team-note.md](no-red-team-note.md) | No red-team platform policy |
| [data-and-secret-safety.md](data-and-secret-safety.md) | Synthetic-only data policy |
| [rollback.md](rollback.md) | How to remove harness if drift occurs |
| [freeze/README.md](freeze/README.md) | **v0.1 freeze** — baseline, scope lock, change lock |

---

## Baseline checks (must not regress)

```powershell
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

Governance review: [../../../governance/PHASE_3_4_PROVIDER_SAFETY_HARNESS_REVIEW.md](../../../governance/PHASE_3_4_PROVIDER_SAFETY_HARNESS_REVIEW.md)

Freeze review: [../../../governance/PHASE_3_4_1_FREEZE_PROVIDER_SAFETY_HARNESS_V0_1_REVIEW.md](../../../governance/PHASE_3_4_1_FREEZE_PROVIDER_SAFETY_HARNESS_V0_1_REVIEW.md)
