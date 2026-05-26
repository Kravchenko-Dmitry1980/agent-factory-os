# Harness v0.1 Limitations — Provider Safety Harness

**Version:** v0.1  
**Status:** FROZEN_WITH_NOTES

---

## What v0.1 proves

| Claim | Evidence |
|-------|----------|
| Local deterministic safety matrix is consistent | 16 cases → expected decisions and events |
| Expected decisions are enforced | DELIVERED only on A01; unsafe cases → BLOCKED/ESCALATED/FAILED |
| Unsafe synthetic provider-like outputs map to safe outcomes | Bypass, injection-style, command, secret cases blocked or escalated |
| Baseline checks remain green | All six validation scripts PASS at freeze |
| No network or provider dependency | Stdlib script runs offline |

---

## What v0.1 does not prove

| Gap | Detail |
|-----|--------|
| Real model resists prompt injection | No live model calls in harness |
| Live provider output is always safe | Classification is simulated locally |
| Production readiness | Not load/soak/staging validation |
| Model quality | No intelligence or writing assessment |
| Provider-specific compatibility | One local stack validated separately (Phase 3.3-LiveCheck) |
| All possible injection patterns | Fixed 16-case matrix only |
| Complete security | Narrow safety-boundary check, not certification |
| Full CLI path per case | Harness classifies locally; does not invoke `minimal_demo.py` per injection string |

---

## Why this is acceptable

v0.1 is a **narrow safety harness**, not final security certification.

It answers:

> If provider-like output is bad, injected, unsafe, or wrong, does the safety decision model still block / escalate / fail closed?

It does **not** answer:

> Which model is smartest? Is the system production-ready? Will live LM Studio resist every injection?

That scope separation is intentional and recorded in governance.

---

## Weakest area (recorded at freeze)

Harness performs **local deterministic classification** aligned with v0.3 rules rather than executing the full Review Assistant CLI pipeline for each synthetic injection case.

---

## Related

- Pre-freeze: [../harness-limitations.md](../harness-limitations.md)
- Impl review: [PHASE_3_4_PROVIDER_SAFETY_HARNESS_REVIEW.md](../../../../governance/PHASE_3_4_PROVIDER_SAFETY_HARNESS_REVIEW.md)
