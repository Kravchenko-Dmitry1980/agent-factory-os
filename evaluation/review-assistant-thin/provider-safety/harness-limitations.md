# Harness Limitations — Phase 3.4

This harness is intentionally small and local. It does **not** prove:

---

## Does not prove model quality

- No intelligence scoring
- No writing quality assessment
- No factual accuracy check

---

## Does not test live prompt injection against a model

- Cases are synthetic strings classified locally
- No LM Studio or cloud provider calls by default
- Live model compliance with injection text is **not** directly tested

---

## Does not test provider-specific quirks

- No OpenAI / Anthropic / local server-specific behavior
- No rate-limit, timeout, or HTTP error matrix
- Real provider contract covered separately in Phase 3.3 scripts

---

## Does not test production readiness

- No load, soak, or chaos testing
- No staging environment validation
- No SLO or uptime checks

---

## Does not replace human review

- Fixed 16-case matrix only
- Human reviewer still required for promotion decisions
- See governance human review requirements

---

## Does not compare models

- No leaderboard
- No ranking
- No A/B provider comparison

---

## What it does prove

That a deterministic v0.3-aligned safety classifier maps known bad synthetic provider outputs to BLOCKED, ESCALATED, or FAILED — and only a clean neutral draft to DELIVERED after verification and approval.
