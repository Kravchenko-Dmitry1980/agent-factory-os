# Implementation Manifest — Review Assistant Thin v0.3

Inventory of implementation, evaluation, and governance files at v0.3 freeze.

---

## Implementation files

| File | Purpose | Changed in v0.3? | Frozen? |
|------|---------|------------------|---------|
| README.md | Entry docs, run commands, scope | yes (real provider nav) | yes |
| minimal_demo.py | **Only executable** — 13 scenarios, mock LLM + real provider boundary | yes | yes |
| contracts.md | I/O, states, events incl. provider contracts | yes | yes |
| behavior.md | Flow and rules incl. real provider path | yes | yes |
| trace_examples.md | Expected trace shapes incl. provider | yes | yes |
| evaluation.md | Manual eval steps incl. provider | yes | yes |
| failure_modes.md | Known failure guards incl. provider | yes | yes |
| governance.md | Scope lock, provider policy | yes | yes |
| rollback.md | Revert procedure incl. provider rollback | yes | yes |
| llm_boundary.md | Mock LLM boundary docs (Phase 3.2) | no | yes |
| real_provider_boundary.md | Real local provider boundary (Phase 3.3) | **new** | yes |

---

## Evaluation support files

| File | Purpose | Changed in v0.3? | Frozen? |
|------|---------|------------------|---------|
| evaluation/review-assistant-thin/real-provider-scenario-checklist.md | Real provider manual checklist | **new** | no (eval metadata) |
| evaluation/review-assistant-thin/real-provider-expected-events.md | Provider event substrings | **new** | no (eval metadata) |
| evaluation/review-assistant-thin/real-provider-hardening-notes.md | Provider scope limits | **new** | no (eval metadata) |
| evaluation/review-assistant-thin/live-provider-checklist.md | LiveCheck eval checklist | **new** (LiveCheck) | no (eval metadata) |
| evaluation/scripts/check_review_assistant_real_provider_contract.py | No-network + optional live contract check | **new** | no (eval script) |

---

## Unchanged evaluation (v0.1 / v0.2 preserved)

| File | Purpose | Changed in v0.3? | Frozen? |
|------|---------|------------------|---------|
| evaluation/review-assistant-thin/scenario-checklist.md | Original 5-scenario checklist | no | no |
| evaluation/review-assistant-thin/expected-events.md | Original event substrings | no | no |
| evaluation/review-assistant-thin/hardening-notes.md | Original scope limits | no | no |
| evaluation/review-assistant-thin/llm-scenario-checklist.md | LLM mock checklist | no | no |
| evaluation/review-assistant-thin/llm-expected-events.md | LLM event substrings | no | no |
| evaluation/review-assistant-thin/llm-hardening-notes.md | LLM scope limits | no | no |
| evaluation/scripts/check_review_assistant_thin.py | Original thin check | no | no |
| evaluation/scripts/check_review_assistant_llm_mock.py | LLM mock check | no | no |
| evaluation/scripts/run_demo_smoke_checks.py | Phase 2 smoke | no | no |
| evaluation/scripts/check_expected_text_traces.py | Trace examples check | no | no |

---

## Governance records (Phase 3.3 + LiveCheck)

| File | Purpose | Changed in v0.3? | Frozen? |
|------|---------|------------------|---------|
| governance/PHASE_3_3_REAL_PROVIDER_BOUNDARY_REVIEW.md | Phase 3.3 impl review | **new** | no |
| governance/PHASE_3_3_LIVE_PROVIDER_CHECK_REVIEW.md | LiveCheck review | **new** | no |
| governance/phase-3-3-livecheck/FINAL_PHASE_3_3_LIVECHECK_REPORT.md | LiveCheck final report | **new** | no |
| governance/phase-3-3-livecheck/ | LiveCheck doc set (11 files) | **new** | no |

---

## Freeze metadata (this folder)

| File | Purpose | Changed in v0.3? | Frozen? |
|------|---------|------------------|---------|
| freeze/README.md | Freeze index (v0.1 + v0.2 + v0.3 history) | yes | no |
| freeze/V0_3_FREEZE_RECORD.md | v0.3 freeze record | **new** | no |
| freeze/V0_3_IMPLEMENTATION_MANIFEST.md | This file | **new** | no |
| freeze/V0_3_REAL_PROVIDER_BOUNDARY_BASELINE.md | Real provider baseline | **new** | no |
| freeze/V0_3_SCENARIO_BASELINE.md | 13 scenario baselines | **new** | no |
| freeze/V0_3_VALIDATION_RECORD.md | Validation results | **new** | no |
| freeze/V0_3_LIVE_PROVIDER_RECORD.md | LM Studio live record | **new** | no |
| freeze/V0_3_CHANGE_LOCK.md | v0.3 change policy (active) | **new** | no |
| freeze/V0_3_ROLLBACK_RECORD.md | v0.3 rollback steps | **new** | no |
| freeze/V0_2_* | v0.2 history | no | no (historical) |
| freeze/IMPLEMENTATION_* , SCENARIO_BASELINE, CHANGE_LOCK, ROLLBACK | v0.1 history | no | no (historical) |

---

## Executable summary

- **One file:** `minimal_demo.py`
- **Scenarios:** 13 (5 original + 5 LLM mock + 3 real provider contract)
- **Dependencies:** none (Python stdlib)
- **Hidden state:** none
- **Network:** none by default; localhost only with `--real-provider` + env
- **Memory persistence:** none
- **Cloud LLM API:** none by default

## Template link

Implements (does not replace): `agent-builder-kit/templates/review-assistant-agent/` v0.1 frozen spec.

## Reference (read-only)

`prototypes/review-loop-agent/` — patterns only; not imported at runtime.
