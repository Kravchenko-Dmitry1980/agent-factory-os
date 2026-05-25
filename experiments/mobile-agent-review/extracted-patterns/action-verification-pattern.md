# Action Verification Pattern

---

## Pattern Statement

> Never treat action execution as success until observation confirms expected UI transition.

---

## Implementations

### Post-Op Visual Verification (Inline)

- v2/v3/PC **Reflector** with A/B/C taxonomy
- Dual screenshot comparison
- Feeds `error_flag` or `error_flag_plan`

### Pre-Op Critic (Offline)

- GUI-Critic-R1 before step execution
- Suggests corrections to proposed action
- Not wired into main loops in repo

### Environment Verification (Eval)

- AndroidWorld / OSWorld task checkers
- Ground truth for research, not agent self-verification

---

## Outcome Semantics

| Outcome | Agent response (typical) |
|---------|--------------------------|
| A | Proceed to next subgoal |
| B | Navigate back, replan or retry |
| C | Retry same action with revised coords |

---

## Composition

Ideal stack (not fully integrated in repo):

```
Pre-critic → Execute → Post-reflect → Progress update
```

---

## Agent-OS Link

Extends `agent-os/00_foundations/verification.md` into **visual modality**.

Production needs:
- Circuit breaker on repeated C outcomes
- Typed verification records in message history
- Separation of "action succeeded" vs "task succeeded"

---

## Source Files

- `Mobile-Agent-v2/MobileAgent/prompt.py` — `get_reflect_prompt`
- `Mobile-Agent-v3/mobile_v3/utils/mobile_agent_e.py` — ActionReflector
- `GUI-Critic-R1/test.py` — pre-op critic
