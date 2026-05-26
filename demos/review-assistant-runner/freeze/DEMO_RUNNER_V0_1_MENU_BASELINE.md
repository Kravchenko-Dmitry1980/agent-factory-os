# Demo Runner v0.1 — Menu Baseline

**Version:** demo-runner-v0.1  
**Date:** 2026-05-26  
**Status:** FROZEN

Fixed 15-item menu. No dynamic registry. No plugins.

**Rule:** No menu item may be added without change proposal, validation, and explicit approval.

---

## Menu table

| ID | Group | Scenario/Check | Russian Title | Requires Real Provider? | Type |
|----|-------|----------------|---------------|-------------------------|------|
| 1 | Basic Review Assistant | `happy` | Нормальный сценарий | no | demo |
| 2 | Basic Review Assistant | `missing_approval` | Нет approval | no | demo |
| 3 | Basic Review Assistant | `critic_uncertain` | Критик не уверен | no | demo |
| 4 | Basic Review Assistant | `bad_draft` | Плохой черновик | no | demo |
| 5 | Basic Review Assistant | `unsafe_publish_attempt` | Опасная попытка публикации | no | demo |
| 6 | Mock LLM | `llm_valid_draft` | Mock LLM — хороший ответ | no | demo |
| 7 | Mock LLM | `llm_malformed_output` | Mock LLM — сломанный ответ | no | demo |
| 8 | Mock LLM | `llm_unsafe_output` | Mock LLM — опасный ответ | no | demo |
| 9 | Real Local Provider | `real_provider_synthetic` | Real provider — LM Studio (synthetic) | **yes** | demo |
| 10 | Baseline Checks | `provider_safety_harness` | Provider safety harness (16 cases) | no | validation |
| 11 | Baseline Checks | `thin_baseline` | Thin baseline (5 cases) | no | validation |
| 12 | Baseline Checks | `mock_llm_baseline` | Mock LLM baseline (5 cases) | no | validation |
| 13 | Baseline Checks | `real_provider_contract_no_network` | Real provider contract (no-network) | no | validation |
| 14 | Baseline Checks | `smoke_checks` | Smoke checks (12 cases) | no | validation |
| 15 | Baseline Checks | `text_trace_checks` | Text trace examples (6 cases) | no | validation |

---

## Group summary

| Group | Items | Count |
|-------|-------|-------|
| Basic Review Assistant | 1–5 | 5 |
| Mock LLM | 6–8 | 3 |
| Real Local Provider | 9 | 1 |
| Baseline Checks | 10–15 | 6 |
| **Total** | | **15** |

---

## Expected decisions (demo items)

| Key | Expected decision |
|-----|-------------------|
| happy | DELIVERED |
| missing_approval | BLOCKED |
| critic_uncertain | ESCALATED |
| bad_draft | FAILED |
| unsafe_publish_attempt | FAILED |
| llm_valid_draft | DELIVERED |
| llm_malformed_output | FAILED |
| llm_unsafe_output | FAILED |
| real_provider_synthetic | DELIVERED (manual live only) |

---

## Change rule

Adding, removing, or renaming menu items requires:

1. Change proposal
2. Menu baseline update
3. Validation run
4. Governance review
5. Explicit approval

This is **not** allowed as drive-by edits to frozen v0.1.
