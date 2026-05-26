# Trace Plan — Free-Form CLI

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Required trace events (future impl)

| Event | When |
|-------|------|
| `input_received` | Task text accepted (sanitized detail in trace) |
| `input_validated` | Passed input gate |
| `input_rejected` | Failed input gate |
| `mode_selected` | mock/default or local_provider |
| `draft_created` | Mock draft ready |
| `llm_request_started` | Mock LLM path (if used) |
| `llm_response_received` | Mock response |
| `llm_parse_passed` / `llm_parse_failed` | Parse boundary |
| `provider_request_prepared` | Mode 2 only |
| `provider_request_started` | Mode 2 only |
| `provider_response_received` | Mode 2 only |
| `provider_parse_passed` / failed | Mode 2 only |
| `critique_completed` | If critique step included |
| `verification_passed` / `verification_failed` | Verification gate |
| `approval_requested` | Before approval prompt |
| `approval_granted` / `approval_denied` | After prompt |
| `unsafe_action_blocked` | Unsafe detected |
| `escalation_triggered` | Uncertainty path |
| `task_completed` / `task_failed` | Terminal |

Subset shown in operator summary; full list in raw TRACE block.

---

## Trace properties

| Property | Requirement |
|----------|-------------|
| Human-readable | yes |
| Telemetry backend | **no** |
| Secrets in trace | **no** |
| Raw provider config | **no** (no RA_LLM_BASE_URL value) |
| Full private task dump in logs | avoid; preview only |
| Format | `- event: key=value` lines under `TRACE` header (thin demo style) |

---

## Russian mapping

Reuse spirit of Demo Runner v0.1 / [phase-3-5-2-plan/TRACE_EXPLANATION_MAPPING_RU.md](../phase-3-5-2-plan/TRACE_EXPLANATION_MAPPING_RU.md).

Add for free-form:

| Event | RU short |
|-------|----------|
| `input_received` | задача принята |
| `input_validated` | ввод прошёл проверку |
| `input_rejected` | ввод отклонён |
| `mode_selected` | режим выбран |

---

## Parse failure

If trace parse fails in future wrapper tests → show raw output + WARNING in summary (same as Demo Runner behavior).

---

## No persistence

Trace exists in stdout (and optional transcript) only. No DB, no session file.
