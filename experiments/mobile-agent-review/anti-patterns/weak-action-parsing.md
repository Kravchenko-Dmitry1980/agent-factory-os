# Weak Action Parsing

---

## Anti-Pattern

Fragile regex/string parsing of LLM output for executable actions.

---

## Instances in Repo

### v2 Natural Language Actions

```
### Action ###
Tap (540, 1200)
```

Parsed from free text in `run.py` — sensitive to:
- Extra punctuation
- Localized action names
- Model adding markdown or explanation inside Action block

### v3 JSON in Prose

`parse_response()` in agent classes must extract JSON from model response — typical VLM failure: invalid JSON, trailing commas, markdown fences.

### OSWorld pyautogui strings

`exec()` of generated Python — **highest risk** if model emits arbitrary code.

---

## Symptoms

- Silent skip of step
- Wrong action type executed
- Crash on parse exception (inconsistent handling)

---

## Mitigations Used Partially

- Strict output format sections in prompts (Thought/Action/Operation)
- JSON schema examples in v3 executor prompts
- Thinking models (GUI-Owl 1.5) for structured reasoning

---

## Better Patterns (Not in Repo)

- JSON mode / constrained decoding
- Pydantic validation with repair loop
- Tool-call API instead of prose actions
- Sandboxed action DSL (no exec)

---

## Agent-OS Link

Relates to `agent-os/09_antipatterns/` themes — treat model output as untrusted input.

Code harness uses structured tool_use blocks; GUI agents should converge on **typed tool calls** for actions.
