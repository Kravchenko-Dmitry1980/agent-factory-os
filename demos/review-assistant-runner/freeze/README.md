# Demo Runner v0.1 — Freeze Index

**Date:** 2026-05-26  
**Status:** FROZEN_WITH_NOTES

---

## What this folder is

Freeze records for **Review Assistant Demo Runner v0.1** (`demo-runner-v0.1`).

This folder documents the frozen baseline. It does **not** change runner behavior.

---

## Frozen artifact

| Field | Value |
|-------|-------|
| **Script** | `demos/review-assistant-runner/demo_runner.py` |
| **Version** | `demo-runner-v0.1` |
| **Status** | **FROZEN_WITH_NOTES** |

---

## What v0.1 includes

- Russian scenario menu (15 fixed items)
- Direct scenario run (`--scenario`)
- Interactive menu
- List mode (`--list`)
- FINAL decision parsing
- Delivered status parsing
- TRACE event extraction
- Russian operator summary
- Safety status (OK / BLOCKED / ESCALATED / FAILED / WARNING)
- Validation script menu items (Group 4)
- Explicit real provider warning + confirmation
- Optional transcript saving (`--save-transcript` only)

---

## What v0.1 does not include

- Product UI
- Web app
- Operator Console
- Free-form task input
- Real human approval UI
- Saved session browser
- Agent logic changes
- Runtime / factory
- Provider calls by default
- Dynamic scenario registry
- External dependencies

---

## Freeze documents

| File | Purpose |
|------|---------|
| [DEMO_RUNNER_V0_1_FREEZE_RECORD.md](DEMO_RUNNER_V0_1_FREEZE_RECORD.md) | Official freeze record |
| [DEMO_RUNNER_V0_1_MANIFEST.md](DEMO_RUNNER_V0_1_MANIFEST.md) | File manifest |
| [DEMO_RUNNER_V0_1_MENU_BASELINE.md](DEMO_RUNNER_V0_1_MENU_BASELINE.md) | 15-item menu baseline |
| [DEMO_RUNNER_V0_1_COMMAND_BASELINE.md](DEMO_RUNNER_V0_1_COMMAND_BASELINE.md) | Supported commands |
| [DEMO_RUNNER_V0_1_VALIDATION_RECORD.md](DEMO_RUNNER_V0_1_VALIDATION_RECORD.md) | Validation results |
| [DEMO_RUNNER_V0_1_REAL_PROVIDER_POLICY.md](DEMO_RUNNER_V0_1_REAL_PROVIDER_POLICY.md) | Real provider policy |
| [DEMO_RUNNER_V0_1_TRANSCRIPT_POLICY.md](DEMO_RUNNER_V0_1_TRANSCRIPT_POLICY.md) | Transcript policy |
| [DEMO_RUNNER_V0_1_LIMITATIONS.md](DEMO_RUNNER_V0_1_LIMITATIONS.md) | Known limitations |
| [DEMO_RUNNER_V0_1_CHANGE_LOCK.md](DEMO_RUNNER_V0_1_CHANGE_LOCK.md) | Change lock rules |
| [DEMO_RUNNER_V0_1_ROLLBACK_RECORD.md](DEMO_RUNNER_V0_1_ROLLBACK_RECORD.md) | Rollback record |

---

## Governance

[governance/PHASE_3_5_2_FREEZE_DEMO_RUNNER_V0_1_REVIEW.md](../../../governance/PHASE_3_5_2_FREEZE_DEMO_RUNNER_V0_1_REVIEW.md)

---

## Important note

Demo Runner is **not** product UI and **not** runtime. It is a stdlib CLI wrapper around existing Review Assistant demo commands.
