# LLM Failure Modes — Phase 3.2 Plan

| Failure mode | What it looks like | Risk | Safe response |
|--------------|-------------------|------|---------------|
| Hallucinated draft | Plausible false facts in draft | High — wrong delivery | verification + human; never auto-trust |
| Malformed JSON/text | Unparseable structure | Medium — crash or skip gates | `llm_parse_failed`; verification_failed |
| Empty response | Blank or whitespace | Medium — silent fail | reject; task_failed |
| Overconfident wrong answer | High confidence, false | High | critic advisory; human mandatory |
| Unsafe instruction | "Delete all files" in output | Critical | `llm_unsafe_output`; block |
| Prompt injection | User task overrides system rules | Critical | Input sanitization; policy gate; block |
| Policy bypass attempt | Model suggests skip approval | Critical | unsafe_action_blocked |
| Irrelevant output | Off-topic draft | Medium | verification_failed (format/ relevance) |
| Timeout | No response in time | Medium | `llm_timeout`; fail-closed |
| Rate limit | Provider 429 (future real mode) | Low-Medium | retry bounded or fail-closed |
| Provider unavailable | Network/API error | Medium | provider_error; no delivery |
| Hidden assumption | Model assumes facts not in input | High | uncertainty flag; human review |
| Critic falsely approves bad draft | Critique says OK on bad content | High | critic advisory; human final |

---

## Response principles

1. **Fail-closed** default on ambiguity
2. **Never** treat LLM output as verification_passed without explicit gate
3. **Trace** every failure with canonical event name
4. **Mock scenarios** must cover each row before real provider

---

## Mock test scenarios (future impl)

| Scenario | Simulates |
|----------|-----------|
| `llm_malformed` | malformed_output |
| `llm_timeout` | timeout |
| `llm_uncertain` | uncertain_output |
| `llm_unsafe` | unsafe_output |
| `llm_empty` | empty_output |

---

## Diagram

[diagrams/llm-failure-flow.md](diagrams/llm-failure-flow.md)
