# Review Assistant Demo Runner

**Phase 3.5.2** — minimal stdlib-only CLI wrapper for Review Assistant Thin.

---

## Freeze status

| Field | Value |
|-------|-------|
| **Version** | `demo-runner-v0.1` |
| **Status** | **FROZEN_WITH_NOTES** |
| **Scope** | Operator-friendly CLI wrapper |
| **Implementation** | One stdlib script (`demo_runner.py`) |
| **Product UI** | no |
| **Runtime / factory** | no |

Freeze records: [freeze/README.md](freeze/README.md)

Governance: [../../governance/PHASE_3_5_2_FREEZE_DEMO_RUNNER_V0_1_REVIEW.md](../../governance/PHASE_3_5_2_FREEZE_DEMO_RUNNER_V0_1_REVIEW.md)

---

## What it is

- Russian scenario menu for operators
- Runs **existing** `minimal_demo.py` scenarios via subprocess
- Runs **existing** evaluation scripts via subprocess
- Parses FINAL decision and TRACE events from stdout
- Prints Russian summary: what happened, what it proves, safety status
- Warns before real provider scenario (never by default)

---

## What it is NOT

- Not product UI or Operator Console
- Not runtime, factory, or orchestrator
- Not agent logic change — `minimal_demo.py` is untouched
- Not a plugin system or dynamic scenario registry
- Not default network/provider calls

---

## Requirements

- Python 3.12+ (stdlib only)
- Run from repository root: `C:\Dima\Projects\CURSOR\AGENT`

---

## Interactive menu

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python demos/review-assistant-runner/demo_runner.py
```

---

## Direct scenario run

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario happy
python demos/review-assistant-runner/demo_runner.py --scenario missing_approval
python demos/review-assistant-runner/demo_runner.py --list
```

---

## Save transcript (explicit flag only)

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario happy --save-transcript
```

Transcripts go to `demos/review-assistant-runner/transcripts/`. See [TRANSCRIPT_POLICY_RU.md](TRANSCRIPT_POLICY_RU.md).

**Default:** no transcript saved.

---

## Real provider warning

Scenario `real_provider_synthetic` requires:

1. Explicit menu selection
2. Operator confirmation (`yes`)
3. `RA_LLM_BASE_URL` in environment

Without confirmation or env — **no provider call**.

See [USAGE_RU.md](USAGE_RU.md) and [SCENARIO_GUIDE_RU.md](SCENARIO_GUIDE_RU.md).

---

## Documentation

| File | Purpose |
|------|---------|
| [USAGE_RU.md](USAGE_RU.md) | Step-by-step Russian usage |
| [SCENARIO_GUIDE_RU.md](SCENARIO_GUIDE_RU.md) | All 15 menu items |
| [TRACE_SUMMARY_MAPPING_RU.md](TRACE_SUMMARY_MAPPING_RU.md) | TRACE event mapping |
| [TRANSCRIPT_POLICY_RU.md](TRANSCRIPT_POLICY_RU.md) | Transcript and secret safety |
| [ROLLBACK.md](ROLLBACK.md) | How to remove runner |
| [freeze/README.md](freeze/README.md) | **v0.1 freeze records** (FROZEN_WITH_NOTES) |

---

## Related

- [../review-assistant-hands-on/README.md](../review-assistant-hands-on/README.md) — Phase 3.5.1 hands-on report
- [../../prototypes-derived/review-assistant-thin/README.md](../../prototypes-derived/review-assistant-thin/README.md) — thin demo
- [../../governance/PHASE_3_5_2_DEMO_RUNNER_IMPL_REVIEW.md](../../governance/PHASE_3_5_2_DEMO_RUNNER_IMPL_REVIEW.md) — impl review
- [../../governance/PHASE_3_5_2_FREEZE_DEMO_RUNNER_V0_1_REVIEW.md](../../governance/PHASE_3_5_2_FREEZE_DEMO_RUNNER_V0_1_REVIEW.md) — **freeze v0.1**
