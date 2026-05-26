# LLM Evaluation Plan — Phase 3.2 (Future)

**Applies to:** future mock/real LLM adapter — not Phase 3.2-Plan

---

## Required checks (behavioral)

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | Valid mock draft | Reaches verification; delivery only after human approve |
| 2 | Malformed output | Rejected; no delivery; `llm_parse_failed` or `verification_failed` |
| 3 | Timeout | Escalate or fail-closed; no delivery |
| 4 | Unsafe output | Blocked; trace shows block event |
| 5 | Uncertain output | Escalation; no auto-delivery |
| 6 | Critic pass ≠ final | Critique advisory; human still required on happy path |
| 7 | Human approval | approval_requested before task_completed |
| 8 | Trace completeness | LLM boundary events present |

---

## Baseline regression (must not break)

```powershell
python evaluation/scripts/check_review_assistant_thin.py   # PASS=5
python evaluation/scripts/run_demo_smoke_checks.py         # PASS=12
python evaluation/scripts/check_expected_text_traces.py    # PASS=6
```

---

## Future eval artifacts (when impl approved)

| Artifact | Purpose |
|----------|---------|
| `evaluation/review-assistant-llm/` | Scenario checklist + expected events |
| `evaluation/scripts/check_review_assistant_llm_mock.py` | Optional — **new file only**; do not weaken existing scripts |

---

## Explicitly out of scope

- Model leaderboard / accuracy benchmark
- RAG retrieval eval
- Multi-model comparison
- Production load testing
- BLEU/ROUGE scoring

---

## Acceptance gate

Adapter v0.1 accepted only when:

- All mock failure scenarios pass
- Thin v0.1 scenarios still pass (unchanged impl path or isolated adapter folder)
- Security review checklist complete
- No new deps for mock mode

See [PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md](PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md)
