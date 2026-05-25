# Reflection

Post-action self-critique loop in MobileAgent family.

---

## Purpose

After executing an action, determine:
1. Did the UI change correctly?
2. Should the agent retry, go back, or continue?
3. What error signal to feed forward?

---

## v2 Reflection Prompt

`get_reflect_prompt()` structure:
- Before screenshot info + keyboard state
- After screenshot info + keyboard state
- Last operation description + action taken
- Optional hints (`add_info`)

Model outputs outcome class **A**, **B**, or **C** with explanation.

**Switch:** `reflection_switch = False` disables — README warns reflection can cause **dead cycles** but `add_info` can mitigate.

---

## v3 ActionReflector

Class in `mobile_agent_e.py`:
- Ingests InfoPool histories
- Compares before/after screenshots (multimodal)
- Writes to `action_outcomes`, `error_descriptions`
- Influences `error_flag_plan` for Manager

More structured than v2 — ties into replan threshold.

---

## PC-Agent Reflection

Same A/B/C pattern in `prompt_qwen.py` + `run.py` for desktop context.

---

## Mobile-Agent-E

`ActionReflector` + experience reflectors:
- Session-level action reflection
- Cross-session shortcut/tip evolution

---

## GUI-Critic-R1 — Pre-Reflection

Not the same mechanism:
- Critic runs **before** action
- Predicts likely failure / suggests fix
- Trained with S-GRPO (per paper); repo has inference only

Complementary: pre-op + post-op verification stack.

---

## Reflection vs Benchmark Eval

| Mechanism | When | Signal |
|-----------|------|--------|
| Inline reflect | Each step | A/B/C visual |
| GUI-Critic | Before step | Critique text |
| AndroidWorld | Episode end | Task success boolean |
| Web judges | After trajectory | LLM rubric score |

---

## Failure Modes

1. **False A** — model thinks success but task incomplete
2. **Reflection loop** — B/C repeats without progress (no hard circuit breaker in v2)
3. **Cost** — doubles multimodal calls per step
4. **Perception noise** — bad OCR lists confuse reflector in v2

---

## Agent-OS Relevance

Aligns with `agent-os/03_harness-engineering/execution-feedback.md` and error recovery ladder — but MobileAgent uses **vision-based** feedback, not tool stderr.
