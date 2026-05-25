# Model Output Fragility

---

## Anti-Pattern

Pipeline correctness depends on single VLM call returning perfectly formatted action every step.

---

## Failure Modes

| Failure | Consequence |
|---------|-------------|
| Coordinate drift | Missed taps |
| Wrong action kind | Type when should tap |
| Premature Stop | Incomplete task |
| Hallucinated UI elements | Actions on nonexistent targets |
| Context overflow | Truncated history → repeat loops |

---

## Amplifying Factors in MobileAgent

1. **Multi-agent = multi-call** — compounding failure rates (v2/v3)
2. **No circuit breaker** — reflection dead cycles (v2 README)
3. **Coordinate space confusion** — forgetting `--coor_type qwen-vl`
4. **Multimodal API variance** — different behavior API vs local vLLM

---

## Version Mitigations

| Version | Mitigation |
|---------|------------|
| v2 | Perception list reduces search space |
| v3 | Manager replan on stuck |
| v3.5 Thinking models | Internal chain-of-thought |
| GUI-Critic | Pre-op error diagnosis (offline) |
| UI-S1 RL | Policy robustness training (separate) |

---

## Contrast Claude Code

- Typed tool schema from SDK
- Permission checks before execution
- 10 terminal states with circuit breakers
- Context compression between turns

MobileAgent lacks harness-level defenses — relies on model quality.

---

## Research Takeaway

**Model output fragility** is why GUI agents need **harness engineering** (survey ch03) as much as better VLMs.

For Agent-OS: extract verification + replan patterns; do not copy bare run loops as production template.

---

## Security Note

`GUI-Critic-R1/statistic.py` contains hardcoded API key in source — example of fragile secret handling in research code. Never replicate in Agent-OS tooling.
