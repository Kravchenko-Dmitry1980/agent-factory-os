# Scenario Menu Plan

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

Future `demo_runner.py` fixed menu. Menu IDs are **planning identifiers** — not implemented yet.

---

## Group 1 — Basic Review Assistant (original v0.1)

| Menu ID | Scenario | Russian Title | Safe by Default? | Requires LM Studio? |
|---------|----------|---------------|------------------|---------------------|
| 1.1 | `happy` | Нормальный успешный сценарий | yes | no |
| 1.2 | `missing_approval` | Нет approval — доставка заблокирована | yes | no |
| 1.3 | `critic_uncertain` | Критик не уверен — эскалация | yes | no |
| 1.4 | `bad_draft` | Плохой черновик — verification failed | yes | no |
| 1.5 | `unsafe_publish_attempt` | Опасная попытка публикации | yes | no |

**Command template:**

```text
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario {name}
```

---

## Group 2 — Mock LLM (v0.2)

| Menu ID | Scenario | Russian Title | Safe by Default? | Requires LM Studio? |
|---------|----------|---------------|------------------|---------------------|
| 2.1 | `llm_valid_draft` | Mock LLM — хороший ответ (unverified) | yes | no |
| 2.2 | `llm_malformed_output` | Mock LLM — сломанный ответ | yes | no |
| 2.3 | `llm_unsafe_output` | Mock LLM — опасный ответ | yes | no |

---

## Group 3 — Real Local Provider (v0.3)

| Menu ID | Scenario | Russian Title | Safe by Default? | Requires LM Studio? |
|---------|----------|---------------|------------------|---------------------|
| 3.1 | `real_provider_synthetic` | Real provider — LM Studio (synthetic) | **no** | **yes** |

**Requires:**

- `--real-provider` flag (passed by runner only after confirmation)
- Env: `RA_LLM_BASE_URL`, `RA_LLM_MODEL`
- Operator confirmation per [REAL_PROVIDER_WARNING_POLICY.md](REAL_PROVIDER_WARNING_POLICY.md)

**Default menu behavior:** show warning, default answer **no**.

---

## Group 4 — Validation Scripts (baseline checks)

| Menu ID | Script | Russian Title | Safe by Default? | Requires LM Studio? |
|---------|--------|---------------|------------------|---------------------|
| 4.1 | `check_review_assistant_provider_safety.py` | Provider safety harness (16 cases) | yes | no |
| 4.2 | `check_review_assistant_thin.py` | Thin baseline (5 cases) | yes | no |
| 4.3 | `check_review_assistant_llm_mock.py` | Mock LLM baseline (5 cases) | yes | no |
| 4.4 | `check_review_assistant_real_provider_contract.py` | Real provider contract (no-network) | yes | no |
| 4.5 | `run_demo_smoke_checks.py` | Smoke checks (12 cases) | yes | no |
| 4.6 | `check_expected_text_traces.py` | Text trace examples (6 cases) | yes | no |

**Command template:**

```text
python evaluation/scripts/{script_name}
```

Group 4 items print eval PASS/FAIL summary — runner adds Russian intro only.

---

## Future menu layout (conceptual)

```text
Review Assistant Demo Runner
============================

[1] Базовые сценарии Review Assistant
  1.1 happy
  1.2 missing_approval
  ...

[2] Mock LLM
  2.1 llm_valid_draft
  ...

[3] Real provider (⚠ требует LM Studio)
  3.1 real_provider_synthetic

[4] Проверки baseline (no network)
  4.1 provider safety harness
  ...

[0] Выход

Выберите пункт:
```

---

## Menu rules

| Rule | Detail |
|------|--------|
| Fixed list | No dynamic discovery of scenarios |
| No new scenarios | Only frozen names from thin v0.3 |
| Real provider last in group 3 | Visually separated with warning |
| Eval scripts optional section | Clearly labeled “не agent demo” |

---

## What each item should display (after run)

Per scenario: link to “what it proves” from [OPERATOR_OUTPUT_FORMAT_RU.md](OPERATOR_OUTPUT_FORMAT_RU.md) and hands-on [SCENARIO_RESULTS.md](../../demos/review-assistant-hands-on/SCENARIO_RESULTS.md).
