# Review Assistant Thin — Phase 3.1 + 3.2 Mock LLM

Minimal local implementation of frozen **Review Assistant Agent v0.1** with **mock LLM boundary** (no real API).

---

## What this does

- Accepts a task (scenario-driven)
- **Mock LLM path (Phase 3.2):** parse → safety → draft (unverified)
- **Legacy path:** simple local draft (no LLM)
- Runs advisory critique (simulated)
- Runs verification (mandatory)
- Requires mock human approval per scenario
- Delivers only when verification passed **and** approval granted
- Prints human-readable trace

**Warning:** mock LLM only — **no OpenAI, no external API, no API keys.**

---

## How to run

### Original scenarios (Phase 3.1)

```powershell
cd C:\Dima\Projects\CURSOR\AGENT

python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario happy
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario missing_approval
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario critic_uncertain
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario bad_draft
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario unsafe_publish_attempt
```

### Mock LLM scenarios (Phase 3.2)

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_valid_draft
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_malformed_output
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_timeout
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_uncertain
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_unsafe_output
```

---

## Scenarios

| Scenario | PASS looks like |
|----------|-----------------|
| `happy` | `delivered=True`, `task_completed`, `approval_granted` |
| `missing_approval` | `delivered=False`, `approval_timeout`, `task_failed` |
| `critic_uncertain` | `escalation_triggered`, no delivery |
| `bad_draft` | `verification_failed`, `task_failed` |
| `unsafe_publish_attempt` | `unsafe_action_blocked`, `task_failed` |
| `llm_valid_draft` | `llm_parse_passed`, approval, `delivered=True` |
| `llm_malformed_output` | `llm_parse_failed`, no approval |
| `llm_timeout` | `llm_timeout`, `escalation_triggered` |
| `llm_uncertain` | `llm_uncertain`, no delivery |
| `llm_unsafe_output` | `llm_unsafe_output`, `unsafe_action_blocked` |

---

## Evaluation

```powershell
python evaluation/scripts/check_review_assistant_thin.py      # PASS=5
python evaluation/scripts/check_review_assistant_llm_mock.py  # PASS=5
```

---

## What it does NOT do

- Real LLM / OpenAI / external API
- Auto-publish
- Provider framework / model router
- Telegram / FastAPI / database
- Persistent memory
- Agent factory or reusable runtime

See [llm_boundary.md](llm_boundary.md)

---

## References

| Doc | Path |
|-----|------|
| Frozen template | `agent-builder-kit/templates/review-assistant-agent/` |
| Phase 3.1 plan | `governance/phase-3-1-plan/` |
| Reference prototype (read-only) | `prototypes/review-loop-agent/` |

---

## Files

| File | Purpose |
|------|---------|
| [minimal_demo.py](minimal_demo.py) | Entry script |
| [contracts.md](contracts.md) | I/O and states |
| [behavior.md](behavior.md) | Behavior summary |
| [trace_examples.md](trace_examples.md) | Expected traces |
| [evaluation.md](evaluation.md) | How to evaluate |
| [failure_modes.md](failure_modes.md) | Known failures |
| [governance.md](governance.md) | Scope rules |
| [rollback.md](rollback.md) | Rollback steps |
| [llm_boundary.md](llm_boundary.md) | Mock LLM boundary (Phase 3.2) |
| [freeze/](freeze/README.md) | **v0.2 freeze** (v0.1 history preserved) |

## Status

**FROZEN v0.2** — mock LLM boundary. Eval: thin PASS=5 + LLM mock PASS=5 + smoke PASS=12 + trace PASS=6. See [freeze/V0_2_FREEZE_RECORD.md](freeze/V0_2_FREEZE_RECORD.md).
