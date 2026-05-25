# Failure Recovery Pattern

---

## Pattern Statement

> Detect failed actions via visual feedback, escalate from retry → back navigation → replan.

---

## Recovery Ladder in MobileAgent

```
Level 0: Executor retry with error_flag in prompt (same subgoal)
Level 1: Reflection outcome B → back button + error context
Level 2: Reflection outcome C → retry with revised action
Level 3: error_flag_plan (≥2 failures) → Manager replan
Level 4: User hints via add_info (manual domain knowledge)
Level 5: Stop / terminate (give up or partial answer)
```

No equivalent to Claude Code circuit breakers or max-turn typed terminals.

---

## v2-Specific Risk

README: reflection can cause **infinite dead cycles** — mitigated by:
- Turning off `reflection_switch`
- Adding operational knowledge to `add_info`

---

## Mobile-Agent-E Evolution

Failed patterns may update **negative tips** via experience reflector — cross-session recovery learning.

---

## Benchmark Recovery

Eval harnesses reset env on failure — recovery policy affects score but not exposed as API.

---

## Missing Mechanisms

- Exponential backoff on ADB failures
- Structured exception types from controller
- Explicit max_retry per subgoal in config (partial — `err_to_manager_thresh` only)
- Rollback to checkpoint UI state (no snapshot restore)

---

## Agent-OS Analog

Maps partially to `agent-os/01_agent-runtime/error-recovery-ladder.md` — MobileAgent version is **vision-triggered** without withheld errors or SDK disconnect handling.

---

## Recommendation

When integrating GUI into Agent-OS:
- Import **A/B/C + replan threshold** as minimal recovery
- Add **hard step budget** from harness survey best practices
- Wire GUI-Critic as optional **pre-op hook**
