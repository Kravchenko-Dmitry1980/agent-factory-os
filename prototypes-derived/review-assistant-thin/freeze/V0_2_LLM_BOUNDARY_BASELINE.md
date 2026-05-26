# LLM Boundary Baseline — Review Assistant Thin v0.2

Frozen mock-only LLM boundary specification.

---

## Boundary type

**Mock-only LLM boundary** — local deterministic payloads. No external provider.

---

## Inputs

| Input | Description |
|-------|-------------|
| Scenario name | One of `llm_valid_draft`, `llm_malformed_output`, `llm_timeout`, `llm_uncertain`, `llm_unsafe_output` |
| Mock payload | In-memory dict from `get_mock_llm_raw(scenario)` — no network |
| Task text | Scenario-driven task string passed into mock boundary |

---

## Outputs

| Output | Description |
|--------|-------------|
| Parsed draft | Structured draft after parse (when parse succeeds) |
| Parse status | `llm_parse_passed` or `llm_parse_failed` |
| Failure reason | Event-specific (timeout, uncertain, unsafe, malformed) |
| Decision | DELIVERED, FAILED, ESCALATED, BLOCKED |
| Trace events | Human-readable stdout events per scenario |

---

## Required safety chain

```text
mock LLM output
  → parse
  → safety check
  → verification
  → human approval
  → delivery or block
```

**Valid LLM output still requires verification and approval before delivery.**

---

## Failure cases

| Case | Event(s) | Outcome | Rule |
|------|----------|---------|------|
| Malformed output | `llm_parse_failed` | FAILED | Never reaches approval |
| Timeout | `llm_timeout`, `escalation_triggered` | ESCALATED | No hallucinated fallback draft |
| Uncertain output | `llm_uncertain`, `escalation_triggered` | ESCALATED | Uncertainty must not become delivery |
| Unsafe output | `llm_unsafe_output`, `unsafe_action_blocked` | FAILED | Blocked before verification/approval |

---

## Non-negotiable rules

| Rule | Enforcement |
|------|-------------|
| LLM output is not truth | Parse + verification + approval required |
| No real provider by default | Mock dict only; no HTTP/API |
| No API key | No secrets in repo or env for this impl |
| No network | Stdlib only; no outbound calls |
| No tool execution from LLM output | Output is text → parse → gates only |
| No hidden memory writeback | No persistence between runs |
| No auto-publish | Delivery only after `approval_granted` |

---

## Implementation reference

- Docs: [llm_boundary.md](../llm_boundary.md)
- Code: `minimal_demo.py` — `get_mock_llm_raw`, `parse_mock_llm_response`, `run_mock_llm_boundary`
- Eval: `evaluation/scripts/check_review_assistant_llm_mock.py`

---

## What this is NOT

- Provider abstraction framework
- Model router or registry
- OpenAI / Anthropic integration
- Model quality proof
- Production LLM adapter

Real provider requires separate governance phase and explicit approval.
