# Phase 3.5.2-Impl — Demo Runner Implementation Review

**Date:** 2026-05-26  
**Phase:** 3.5.2-Impl — Minimal Demo Runner  
**Verdict:** **PASS_WITH_NOTES**

---

## Executive Verdict

**PASS_WITH_NOTES**

Demo Runner improves operator UX as a stdlib-only CLI wrapper. It is **not** product UI, **not** runtime, and **not** a change to Review Assistant logic.

Reason for PASS_WITH_NOTES (not full PASS): runner is intentionally minimal — fixed menu, subprocess-only, no session history, no free-form input. Scope is correct but UX remains CLI-lab level.

---

## Pre-flight Results

Run from `C:\Dima\Projects\CURSOR\AGENT` before implementation (no real provider):

| Script | Expected | Actual |
|--------|----------|--------|
| `check_review_assistant_provider_safety.py` | PASS=16 FAIL=0 | PASS=16 FAIL=0 |
| `check_review_assistant_thin.py` | PASS=5 FAIL=0 | PASS=5 FAIL=0 |
| `check_review_assistant_llm_mock.py` | PASS=5 FAIL=0 | PASS=5 FAIL=0 |
| `check_review_assistant_real_provider_contract.py` | PASS=2 FAIL=0 | PASS=2 FAIL=0 |
| `run_demo_smoke_checks.py` | PASS=12 FAIL=0 | PASS=12 FAIL=0 |
| `check_expected_text_traces.py` | PASS=6 FAIL=0 | PASS=6 FAIL=0 |

**Pre-flight:** PASS — implementation proceeded.

---

## Files Created

| Path | Purpose |
|------|---------|
| `demos/review-assistant-runner/demo_runner.py` | Single stdlib CLI wrapper |
| `demos/review-assistant-runner/README.md` | English overview |
| `demos/review-assistant-runner/USAGE_RU.md` | Russian step-by-step usage |
| `demos/review-assistant-runner/SCENARIO_GUIDE_RU.md` | All 15 menu items |
| `demos/review-assistant-runner/TRACE_SUMMARY_MAPPING_RU.md` | TRACE event mapping |
| `demos/review-assistant-runner/TRANSCRIPT_POLICY_RU.md` | Transcript and secret policy |
| `demos/review-assistant-runner/ROLLBACK.md` | Rollback instructions |

---

## Files Updated (navigation only)

| Path | Change |
|------|--------|
| `governance/README.md` | Added impl review + runner link |
| `START_HERE_RU.md` | Demo Runner commands |
| `operator-playbooks/ru/README.md` | USAGE_RU link |
| `demos/review-assistant-hands-on/README.md` | Next step → runner |

---

## Runner Behavior

| Requirement | Status |
|-------------|--------|
| Russian scenario menu (15 items) | OK |
| Subprocess to existing commands | OK |
| Parse FINAL decision + delivered | OK |
| Parse TRACE events | OK |
| Russian summary blocks | OK |
| Real provider warning + confirmation | OK |
| No real provider by default | OK |
| Transcript only with `--save-transcript` | OK |
| `--list`, `--scenario`, `--debug` | OK |
| Repo root detection | OK |
| Stdlib only | OK |
| No project module imports | OK |

**Note:** UTF-8 stdout reconfigure added for Windows console (cp1251 emoji crash on `--list`).

---

## Validation Results (post-impl)

| Command | Expected | Actual |
|---------|----------|--------|
| `demo_runner.py --list` | Lists 15 items | OK |
| `--scenario happy` | DELIVERED + Russian summary | OK |
| `--scenario missing_approval` | BLOCKED + Russian summary | OK |
| `--scenario unsafe_publish_attempt` | FAILED + Russian summary | OK |
| `--scenario provider_safety_harness` | PASS=16 FAIL=0 | OK |

Baseline re-check after impl:

| Script | Result |
|--------|--------|
| provider_safety | PASS=16 FAIL=0 |
| thin | PASS=5 FAIL=0 |
| mock_llm | PASS=5 FAIL=0 |
| real_provider_contract | PASS=2 FAIL=0 |
| smoke | PASS=12 FAIL=0 |
| text_traces | PASS=6 FAIL=0 |

Real provider scenario **not** run in automated validation.

---

## Scope Compliance

| Rule | Compliant |
|------|-----------|
| One Python script only | yes |
| Stdlib only | yes |
| No agent logic change | yes — `minimal_demo.py` untouched |
| No provider call by default | yes |
| No runtime/factory | yes |
| No UI/web app | yes |
| No protected folder changes | yes |
| No new dependencies | yes |
| No evaluation script changes | yes |
| No frozen spec changes | yes |

---

## Remaining Gaps

- Not product UI
- No interactive free-form task input
- No real human approval UI
- No saved sessions / history browser
- No Operator Console
- No dynamic scenario registry (by design)
- Windows console may need UTF-8 terminal for best Cyrillic display (reconfigure mitigates)

---

## Weakest Area

Operator experience is still **terminal CLI** — readable Russian summary helps, but no guided onboarding flow beyond markdown docs. Risk: operators may treat runner as «the product» despite disclaimers.

---

## Next Recommended Phase

**Phase 3.5.2-Freeze — Freeze Demo Runner v0.1**

After freeze, optional paths:

- Phase 3.5.3-Plan — Interactive Free-Form CLI
- Phase 3.6-Plan — Task Triage Thin Implementation Plan

---

## Real Provider Default Behavior

- Not in default path
- Requires menu item 9 or `--scenario real_provider_synthetic`
- Requires explicit `yes` confirmation
- Requires `RA_LLM_BASE_URL` in environment
- Cancel message: «Real provider scenario cancelled»

---

## Transcript Behavior

- Default: **no save**
- `--save-transcript`: saves to `demos/review-assistant-runner/transcripts/`
- No env vars, no API keys, no RA_LLM_BASE_URL value in transcript

---

## Agent Logic Changed?

**No.**

---

## Provider Call by Default?

**No.**

---

## New Dependency?

**No** — Python stdlib only.

---

## Runtime/Factory/UI Drift?

**No.**

---

## Protected Folders Changed?

**No** — only `demos/review-assistant-runner/` created + navigation markdown updates.
