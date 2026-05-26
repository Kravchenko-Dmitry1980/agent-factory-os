# Preconditions for Phase 3.2 Implementation

**Phase 3.2-Plan does NOT start implementation.** These gates apply to future **Phase 3.2-Impl** (mock LLM adapter).

---

## Required before any Phase 3.2 code

| # | Precondition | Verification |
|---|--------------|--------------|
| P1 | User explicitly approves LLM adapter implementation | Message e.g. «Start Phase 3.2 mock LLM adapter for Review Assistant.» |
| P2 | Review Assistant thin check | `check_review_assistant_thin.py` → PASS=5 FAIL=0 |
| P3 | Phase 2 smoke | PASS=12 FAIL=0 |
| P4 | Phase 2 trace | PASS=6 FAIL=0 |
| P5 | No pending semantic changes to frozen specs | git diff clean on template + thin impl freeze files |
| P6 | Mock-first approach approved | Default mode = mock; no network |
| P7 | No external API by default approved | Real provider requires separate P8 |
| P8 | **No OpenAI/API call without explicit approval** | Separate user message for real mode |
| P9 | Rollback plan accepted | [ROLLBACK_AND_FREEZE_PLAN.md](ROLLBACK_AND_FREEZE_PLAN.md) |
| P10 | Evaluation scenarios selected | [LLM_EVALUATION_PLAN.md](LLM_EVALUATION_PLAN.md) mock set |
| P11 | Security review acknowledged | [LLM_SECURITY_REVIEW.md](LLM_SECURITY_REVIEW.md) |
| P12 | NO_RUNTIME_NO_FACTORY policy accepted | [NO_RUNTIME_NO_FACTORY_POLICY.md](NO_RUNTIME_NO_FACTORY_POLICY.md) |

---

## Forbidden without new phase approval

- Real OpenAI/API calls (P8)
- Second agent template
- Modify `prototypes-derived/review-assistant-thin/minimal_demo.py` without change proposal
- Modify existing `evaluation/scripts/*` (add new script only with approval)
- New pip dependency for mock mode
- RAG, MCP, multi-agent

---

## Allowed future paths (after P1–P12)

**Plan only — do not create until Impl prompt:**

```text
prototypes-derived/review-assistant-llm-mock/
  README.md
  llm_adapter_mock.py
  minimal_demo_with_llm.py   # or extend via new entry — not edit frozen thin v0.1
```

Exact path chosen at kickoff. Must not create `runtime/`, `factory/`, `adapters/registry`.

---

## Current status (2026-05-26)

| Precondition | Met |
|--------------|-----|
| P2–P4 | yes (baseline at 3.1.1) |
| P1, P6–P12 impl gates | **not met** — plan only |
| Phase 3.2-Plan complete | yes after this folder |

**Verdict:** NOT READY for code. READY for LLM adapter **planning**.

---

## Pre-flight commands (impl start day)

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```
