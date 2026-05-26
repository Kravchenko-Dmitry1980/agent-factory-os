# Real Provider Boundary Baseline — Review Assistant Thin v0.3

Frozen specification for the opt-in local OpenAI-compatible provider boundary.

Historical mock-only baseline: [V0_2_LLM_BOUNDARY_BASELINE.md](V0_2_LLM_BOUNDARY_BASELINE.md)

---

## Boundary type

**Local OpenAI-compatible provider boundary**

- HTTP POST to `{RA_LLM_BASE_URL}/v1/chat/completions` (OpenAI shape)
- stdlib `urllib` only — no SDK, no provider framework
- Response parsed as `choices[0].message.content`

---

## Default mode

**Mock remains default.**

Without `--real-provider`:

- No network calls
- `provider_disabled` on real provider scenarios
- Original 5 + LLM mock 5 scenarios unchanged

---

## Real mode

Real provider activates **only** with:

```text
--real-provider
```

Plus runtime configuration:

| Env var | Required | Purpose |
|---------|----------|---------|
| `RA_LLM_BASE_URL` | yes (for live) | Local server base URL |
| `RA_LLM_MODEL` | recommended | Model id string |
| `RA_LLM_API_KEY` | optional | Only if local tool requires dummy key |

This phase used **no API key**.

---

## Tested provider (LiveCheck)

| Field | Value |
|-------|-------|
| Tool | LM Studio |
| Endpoint | `http://127.0.0.1:1234` |
| Model | `qwen2.5-7b-instruct-1m` |
| Cloud | no |
| Result | PASS=3 FAIL=0 (observed Phase 3.3-LiveCheck) |

Ollama and other local tools are **not validated** in v0.3 freeze — documented as future alternative only.

---

## Data policy

| Rule | v0.3 |
|------|------|
| Synthetic data only | yes — hardcoded scenario prompt |
| No private data | yes |
| No project / repo content | yes |
| No client data | yes |
| No medical data | yes |
| No `.env` in repo | yes |
| No secrets in prompts / traces | yes |

---

## Required safety chain

```text
provider output
  → parse (OpenAI JSON shape)
  → safety check (heuristic on parsed text)
  → verification (mandatory)
  → human approval (mandatory per scenario)
  → delivery OR block
```

Provider output is **draft input**, not truth and not approval.

---

## Non-negotiable rules

| Rule | Enforcement |
|------|-------------|
| Provider output is not truth | Verify step always runs |
| No cloud by default | Mock default; local only with flag + env |
| No real provider without explicit flag | `provider_disabled` without `--real-provider` |
| Missing config fails closed | `provider_config_missing` |
| No API key logging | Env values not printed in trace |
| No raw secret trace | No key/base URL in stdout |
| No tool execution from provider output | Text-only parse path |
| No hidden memory writeback | No persistence |
| No auto-publish | Approval required |

---

## Contract scenarios (frozen)

| Scenario | Network | Purpose |
|----------|---------|---------|
| `real_provider_forbidden_without_flag` | no | Flag gate |
| `real_provider_missing_config` | no | Config gate |
| `real_provider_synthetic` | yes (opt-in) | Live synthetic path |

See [V0_3_SCENARIO_BASELINE.md](V0_3_SCENARIO_BASELINE.md)

---

## Evaluation

| Script | Default | With `--real-provider` |
|--------|---------|------------------------|
| `check_review_assistant_real_provider_contract.py` | PASS=2 | PASS=3 (live optional) |

---

## Change policy

Real provider boundary change requires [V0_3_CHANGE_LOCK.md](V0_3_CHANGE_LOCK.md).
