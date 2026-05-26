# Recommended Implementation Path

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Recommendation

**Phase 3.5.2-Impl — Minimal Demo Runner**

One stdlib script: `demos/review-assistant-runner/demo_runner.py`

Option B from [IMPLEMENTATION_OPTIONS.md](IMPLEMENTATION_OPTIONS.md).

---

## Future folder structure (impl phase only)

```text
demos/review-assistant-runner/
├── demo_runner.py       # single entry point
├── README.md            # how to run, warnings
└── transcripts/         # gitignored optional saves
    └── .gitkeep
```

**Do not create in Phase 3.5.2-Plan.**

---

## Allowed future behavior

| Feature | Detail |
|---------|--------|
| Fixed menu | Groups 1–4 from [SCENARIO_MENU_PLAN.md](SCENARIO_MENU_PLAN.md) |
| subprocess | Run existing `minimal_demo.py` or eval scripts |
| Parse decision | `decision=`, `delivered=` lines |
| Parse trace | Lines `- event` under TRACE section |
| Russian summary | [OPERATOR_OUTPUT_FORMAT_RU.md](OPERATOR_OUTPUT_FORMAT_RU.md) |
| Provider warning | [REAL_PROVIDER_WARNING_POLICY.md](REAL_PROVIDER_WARNING_POLICY.md) |
| Transcript save | `--save-transcript` only if explicit |
| Exit / loop | Simple REPL menu until 0 |

---

## Forbidden future behavior

| Forbidden | Policy |
|-----------|--------|
| Modifying agent | [NO_AGENT_LOGIC_CHANGE_POLICY.md](NO_AGENT_LOGIC_CHANGE_POLICY.md) |
| Adding scenarios | Frozen names only |
| Provider default call | Confirm + env required |
| pip dependencies | Stdlib only |
| Runtime / factory | [NO_RUNTIME_NO_FACTORY_POLICY.md](NO_RUNTIME_NO_FACTORY_POLICY.md) |
| UI / web app | Out of scope |
| Rich/typer/click | Out of scope v0.1 |
| Custom user task text | Phase 3.5.3+ Interactive CLI |

---

## Implementation sequence (future)

```text
1. Create demos/review-assistant-runner/ + README
2. Implement menu display (static dict)
3. Implement subprocess runner for group 1 scenario (happy)
4. Implement parse + Russian summary for happy
5. Add remaining group 1–2 scenarios
6. Add provider warning + group 3
7. Add group 4 eval shortcuts
8. Optional --save-transcript
9. Manual test all menu items
10. Run 6 baseline eval scripts — must PASS
11. Governance review Phase 3.5.2-Impl
```

---

## Parse contract (stable interface)

Runner depends on **existing** demo output format:

```text
decision=DELIVERED
delivered=True
TRACE
- task_started
...
```

If thin demo output format changes in future → update runner only (or version pin in runner README). **Do not change demo for runner convenience without separate freeze review.**

---

## After runner ships

| Next | Phase |
|------|-------|
| Interactive CLI (free-form task) | 3.5.3-Plan |
| Task Triage thin impl plan | 3.6-Plan |
| Operator Console | Backlog |

---

## Preconditions

See [PRECONDITIONS_FOR_3_5_2_IMPL.md](PRECONDITIONS_FOR_3_5_2_IMPL.md), [PHASE_3_5_2_GO_NO_GO.md](PHASE_3_5_2_GO_NO_GO.md).
