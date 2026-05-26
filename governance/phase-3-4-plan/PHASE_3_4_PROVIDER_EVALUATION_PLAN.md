# Phase 3.4 Provider Evaluation Plan

**Date:** 2026-05-26  
**Scope:** Planning only — Provider Evaluation / Prompt Injection Harness  
**Baseline:** review-assistant-thin-v0.3

---

## Goal

Plan how to test **provider behavior safely** before adding more providers, more agents, or production features.

The question is not *which model is smartest*. The question is:

> Can the system stay safe when the model output is messy, unsafe, injected, or wrong?

---

## Why this matters

A real LLM can:

| Risk | Impact on safety chain |
|------|------------------------|
| Hallucinate | Wrong draft treated as fact |
| Produce malformed output | Parse failure or silent mis-parse |
| Follow injected instructions | Bypass approval or verification |
| Claim approval happened | False completion / auto-delivery risk |
| Suggest unsafe actions | Command/tool execution drift |
| Leak assumptions | Hidden config or secret requests |
| Ignore formatting | Parser bypass or ambiguous state |
| Produce overconfident wrong drafts | False safety claims |

v0.3 proved **connectivity**. Phase 3.4 plans **behavioral safety verification**.

---

## What we evaluate

| Area | Focus |
|------|-------|
| Boundary behavior | Provider disabled by default; explicit opt-in only |
| Parsing behavior | Malformed/empty/huge output handled fail-closed |
| Safety behavior | Unsafe text blocked; uncertain text escalated |
| Approval integrity | No delivery without human approval |
| Trace visibility | Required events present; no secrets logged |
| Fail-closed behavior | Timeout/error/malformed → block or escalate, never silent deliver |

---

## What we do not evaluate

| Out of scope | Reason |
|--------------|--------|
| Model intelligence leaderboard | Not a benchmark phase |
| General benchmark score | Safety boundary only |
| Production accuracy | No production deployment |
| Domain-specific knowledge | Not medical/legal QA |
| Medical/legal correctness | Forbidden domain claims |
| Multi-provider ranking | Single local provider baseline |

---

## Expected decision

Plan a **small future harness**:

- Synthetic test prompts only
- Local provider optional (mock remains default)
- No secrets, no cloud
- No benchmark, no leaderboard
- No pytest initially
- No CI initially
- No provider framework
- One stdlib script with fixed cases (future Phase 3.4-Impl)

See [RECOMMENDED_HARNESS_SCOPE.md](RECOMMENDED_HARNESS_SCOPE.md) and [HARNESS_ARCHITECTURE_OPTIONS.md](HARNESS_ARCHITECTURE_OPTIONS.md).

---

## Safety chain (unchanged)

```text
provider output
  → parse
  → safety check
  → verification
  → human approval
  → delivery or block
  → trace
```

**No provider output can directly decide final status.**

---

## Document map

| Document | Purpose |
|----------|---------|
| [EVALUATION_SCOPE.md](EVALUATION_SCOPE.md) | In/out scope |
| [PROMPT_INJECTION_TAXONOMY.md](PROMPT_INJECTION_TAXONOMY.md) | Attack categories (synthetic) |
| [SAFE_SYNTHETIC_TEST_SET.md](SAFE_SYNTHETIC_TEST_SET.md) | Future test cases |
| [PROVIDER_BEHAVIOR_CHECKS.md](PROVIDER_BEHAVIOR_CHECKS.md) | Harness checks |
| [PROVIDER_OUTPUT_RISK_MATRIX.md](PROVIDER_OUTPUT_RISK_MATRIX.md) | Risk severity matrix |
| [EXPECTED_SAFE_RESPONSES.md](EXPECTED_SAFE_RESPONSES.md) | DELIVERED / BLOCKED / ESCALATED / FAILED |
| [PASS_FAIL_CRITERIA.md](PASS_FAIL_CRITERIA.md) | Test pass/fail rules |
| [TRACE_REQUIREMENTS.md](TRACE_REQUIREMENTS.md) | Required trace events |
| [HUMAN_REVIEW_REQUIREMENTS.md](HUMAN_REVIEW_REQUIREMENTS.md) | When human must review |
| Policies | Data, secret, no-benchmark, no-red-team |
| [PRECONDITIONS_FOR_3_4_IMPLEMENTATION.md](PRECONDITIONS_FOR_3_4_IMPLEMENTATION.md) | Impl gates |
| [ROLLBACK_AND_FREEZE_PLAN.md](ROLLBACK_AND_FREEZE_PLAN.md) | Drift rollback |
| [PHASE_3_4_GO_NO_GO.md](PHASE_3_4_GO_NO_GO.md) | GO/NO-GO verdict |

---

## Hard boundaries (this phase)

**DO NOT:** write Python, modify `minimal_demo.py`, call providers, create pytest/CI, create benchmark platform, use real private data.

**ALLOWED:** Markdown planning documents only.

---

## Next step

After plan approval: user chooses Phase 3.4-Impl (explicit message) or pause on v0.3 baseline.
