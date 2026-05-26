# Harness v0.1 Manifest — Provider Safety Harness

**Version:** v0.1  
**Status:** FROZEN_WITH_NOTES  
**Freeze date:** 2026-05-26

---

## Frozen artifacts

| File | Purpose | Frozen? | Notes |
|------|---------|---------|-------|
| `evaluation/scripts/check_review_assistant_provider_safety.py` | 16-case stdlib safety harness | **Yes** | Local classification only; no network |
| `evaluation/review-assistant-thin/provider-safety/README.md` | Harness overview | **Yes** | Run instructions and boundaries |
| `provider-safety-cases.md` | Case list by group | **Yes** | 16 synthetic cases |
| `expected-decisions.md` | Decision rules | **Yes** | DELIVERED / BLOCKED / ESCALATED / FAILED |
| `expected-trace-events.md` | Trace event glossary | **Yes** | v0.3-compatible event names |
| `harness-limitations.md` | Scope limits | **Yes** | Pre-freeze limitations doc |
| `no-benchmark-note.md` | No scoring policy | **Yes** | No leaderboard |
| `no-red-team-note.md` | No red-team policy | **Yes** | No exploit library |
| `data-and-secret-safety.md` | Synthetic-only policy | **Yes** | No real secrets |
| `rollback.md` | Pre-freeze rollback notes | **Yes** | Superseded in part by freeze rollback record |
| `freeze/README.md` | Freeze index | **Yes** | Phase 3.4.1 |
| `freeze/HARNESS_V0_1_*.md` | Freeze records | **Yes** | This manifest and siblings |
| `governance/PHASE_3_4_PROVIDER_SAFETY_HARNESS_REVIEW.md` | Phase 3.4-Impl review | **Reference** | Impl baseline; not modified at freeze |
| `governance/PHASE_3_4_1_FREEZE_PROVIDER_SAFETY_HARNESS_V0_1_REVIEW.md` | Phase 3.4.1 review | **Yes** | Freeze governance verdict |

---

## Explicit non-artifacts (must not appear)

| Forbidden | Status |
|-----------|--------|
| Provider framework / registry / router | Not present |
| Runtime / factory | Not present |
| pytest suite | Not present |
| CI/CD pipeline | Not present |
| Benchmark / leaderboard | Not present |
| Red-team platform / exploit corpus | Not present |
| New dependencies | Not present |
| Agent behavior change (`minimal_demo.py`) | Not changed |

---

## Technical properties (frozen)

- **Stdlib only** — no external imports
- **No network** — no provider calls by default
- **No provider calls** — local deterministic classification
- **No pytest** — single script, PASS/FAIL output
- **No CI** — manual local run only
- **No agent behavior change** — Review Assistant Thin v0.3 unchanged
- **PASS/FAIL only** — no scores or rankings

---

## Upstream baseline

| Baseline | Record |
|----------|--------|
| Review Assistant Thin v0.3 | [V0_3_FREEZE_RECORD.md](../../../../prototypes-derived/review-assistant-thin/freeze/V0_3_FREEZE_RECORD.md) |
