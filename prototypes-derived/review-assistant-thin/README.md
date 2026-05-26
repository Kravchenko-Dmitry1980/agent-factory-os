# Review Assistant Thin — Phase 3.1 + 3.2 Mock + 3.3 Real Provider (opt-in)

Minimal local implementation of frozen **Review Assistant Agent v0.1** with **mock LLM boundary** (default) and **optional real local provider** (Phase 3.3).

---

## What this does

- Accepts a task (scenario-driven)
- **Mock LLM path (Phase 3.2, default):** parse → safety → draft (unverified)
- **Real provider path (Phase 3.3, opt-in):** local OpenAI-compatible endpoint with `--real-provider`
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

**Default:** mock only — no network. **Real:** `--real-provider` + `RA_LLM_BASE_URL`. Do **not** send sensitive data.

---

### Real provider contract (Phase 3.3 — no network by default)

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario real_provider_forbidden_without_flag
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario real_provider_missing_config --real-provider
```

Optional live (local endpoint required):

```powershell
$env:RA_LLM_BASE_URL = "http://127.0.0.1:1234"
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario real_provider_synthetic --real-provider
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
| `real_provider_forbidden_without_flag` | `provider_disabled`, no network |
| `real_provider_missing_config` | `provider_config_missing`, no network |
| `real_provider_synthetic` | live path with `--real-provider` only |

---

## Evaluation

```powershell
python evaluation/scripts/check_review_assistant_thin.py      # PASS=5
python evaluation/scripts/check_review_assistant_llm_mock.py  # PASS=5
python evaluation/scripts/check_review_assistant_real_provider_contract.py  # PASS=2
```

---

## What it does NOT do (by default)

- OpenAI cloud by default / Anthropic / RU providers
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
| [real_provider_boundary.md](real_provider_boundary.md) | Real provider boundary (Phase 3.3) |
| [freeze/](freeze/README.md) | **v0.2 freeze** (v0.1 history preserved) |

## Status

**v0.2 frozen mock** + **Phase 3.3 real provider contract** (opt-in). Eval: thin PASS=5 + mock PASS=5 + contract PASS=2 + smoke PASS=12 + trace PASS=6.
