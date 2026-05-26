# Evaluation Scope — Phase 3.4

**Purpose:** Define what a future minimal provider safety harness may evaluate.  
**Status:** Plan only — no harness exists yet.

---

## In scope

| Item | Notes |
|------|-------|
| Review Assistant Thin only | Single agent, v0.3 baseline |
| Local provider boundary only | OpenAI-compatible local endpoint; mock default |
| Synthetic test prompts only | No real client/project/medical data |
| Prompt injection safety cases | Harmless synthetic shapes; see taxonomy |
| Malformed output cases | Empty, wrong shape, oversized |
| Approval bypass cases | Fake approval, impersonation |
| Unsafe instruction cases | Command/tool suggestions as text |
| Trace event verification | Required families present |
| No-secret logging checks | Grep-style inspection of traces |
| Regression against baselines | thin v0.1, mock v0.2, provider v0.3 |

---

## Out of scope

| Item | Reason |
|------|--------|
| Second agent | Phase 3 scope lock |
| Multi-provider comparison | No ranking framework |
| Benchmark leaderboard | [NO_BENCHMARK_POLICY.md](NO_BENCHMARK_POLICY.md) |
| RAG evaluation | Not in thin demo |
| MCP evaluation | Not in thin demo |
| CV agent evaluation | Separate future track |
| Digital twin evaluation | Not in scope |
| Production QA | No production deployment |
| Domain correctness | Not safety boundary testing |
| Medical/legal advice quality | Forbidden domain claims |
| Cloud provider evaluation | Local-only for Phase 3.4 |
| RU provider integration | Deferred backlog |
| Operator Console | Deferred backlog |
| Automated red-team corpus | [NO_RED_TEAM_PLATFORM_POLICY.md](NO_RED_TEAM_PLATFORM_POLICY.md) |

---

## Evaluation question (one sentence)

> Does the v0.3 safety chain **fail closed** when provider output is unsafe, injected, malformed, or wrong?

Not: *How smart is the model?*

---

## Baseline scripts (must remain passing)

Future harness must not break existing checks:

```powershell
python evaluation/scripts/check_review_assistant_thin.py           # PASS=5
python evaluation/scripts/check_review_assistant_llm_mock.py       # PASS=5
python evaluation/scripts/check_review_assistant_provider_real.py # PASS=2 (contract)
python evaluation/scripts/run_demo_smoke_checks.py                 # PASS=12
python evaluation/scripts/check_expected_text_traces.py          # PASS=6
```

Live provider scenarios in future harness: **opt-in flag only**, skip if env missing (NOT_RUN, not FAIL).

---

## Relationship to Phase 3.3

| Phase 3.3 | Phase 3.4 |
|-----------|-----------|
| Connect one real provider | Evaluate provider **output safety** |
| Boundary contract | Injection/malformed/bypass cases |
| Live check (manual) | Repeatable synthetic safety checks (future) |
| v0.3 freeze | Harness v0.1 freeze (future) |
