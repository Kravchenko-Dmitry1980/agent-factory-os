# Demo Runner v0.1 — Validation Record

**Date:** 2026-05-26  
**Environment:** `C:\Dima\Projects\CURSOR\AGENT`  
**Real provider:** not run (no LM Studio call)

---

## Runner validation

| Check | Expected | Actual | Pass? |
|-------|----------|--------|-------|
| `demo_runner.py --list` | 15 menu items in 4 groups | 15 items: Basic (5), Mock LLM (3), Real Provider (1), Baseline (6) | **yes** |
| `--scenario happy` | DELIVERED, RU summary, safety OK | `decision=DELIVERED delivered=True`, Russian summary, `Статус безопасности: OK` | **yes** |
| `--scenario missing_approval` | BLOCKED, RU summary | `decision=BLOCKED delivered=False`, Russian summary, `Статус безопасности: BLOCKED` | **yes** |
| `--scenario unsafe_publish_attempt` | FAILED, RU summary | `decision=FAILED delivered=False`, Russian summary, `Статус безопасности: FAILED` | **yes** |
| `--scenario provider_safety_harness` | PASS=16 FAIL=0 | `Summary: PASS=16 FAIL=0`, runner `PASS: 16 FAIL: 0` | **yes** |

---

## Manual validation (Phase 3.5.2-Impl, recorded at freeze)

Observed by operator before freeze (not re-run in this document as automated proof):

| Mode | Observation |
|------|-------------|
| Interactive menu | Menu appears; item 1 runs `happy`; item 7 runs `llm_malformed_output`; exit works |
| `--list` | 15 grouped items |
| Direct `--scenario` | Russian summary + TRACE explanations |

---

## Baseline validation (no-network)

Run during Phase 3.5.2-Freeze pre-flight on 2026-05-26:

| Script | Expected | Actual | Pass? |
|--------|----------|--------|-------|
| `check_review_assistant_provider_safety.py` | PASS=16 FAIL=0 | PASS=16 FAIL=0 | **yes** |
| `check_review_assistant_thin.py` | PASS=5 FAIL=0 | PASS=5 FAIL=0 | **yes** |
| `check_review_assistant_llm_mock.py` | PASS=5 FAIL=0 | PASS=5 FAIL=0 | **yes** |
| `check_review_assistant_real_provider_contract.py` | PASS=2 FAIL=0 | PASS=2 FAIL=0 | **yes** |
| `run_demo_smoke_checks.py` | PASS=12 FAIL=0 | PASS=12 FAIL=0 | **yes** |
| `check_expected_text_traces.py` | PASS=6 FAIL=0 | PASS=6 FAIL=0 | **yes** |

---

## Not validated in freeze phase

| Item | Reason |
|------|--------|
| `real_provider_synthetic` live run | Requires LM Studio; excluded by policy |
| Transcript file content audit | Optional feature; policy documented separately |

---

## Overall freeze validation verdict

**PASS** — all required runner and baseline checks passed on 2026-05-26.

Agent logic unchanged. No provider call during validation.
