# Rollback and Freeze Plan — Phase 3.4

**Purpose:** Define rollback triggers and freeze policy for future provider safety harness.

---

## Rollback triggers

If future harness causes drift, rollback when **any** of:

| # | Trigger |
|---|---------|
| 1 | Harness becomes a **framework** (multi-module package, registry, plugin system) |
| 2 | **pytest / CI** introduced too early without governance approval |
| 3 | **Real secrets** used in tests or traces |
| 4 | **Real data** used (client/medical/code/production logs) |
| 5 | **Provider comparison** starts (ranking, A vs B scoring) |
| 6 | **Model leaderboard** appears in output or docs |
| 7 | **Broad attack corpus** imported |
| 8 | Evaluation **mutates agent behavior** (changes safety rules to pass tests) |
| 9 | **Baseline checks regress** (any of five eval scripts FAIL) |
| 10 | Unexpected **cloud/network** calls in default harness run |
| 11 | Harness output used as **production readiness** claim |

---

## Rollback actions

| Step | Action |
|------|--------|
| 1 | Remove or disable harness script |
| 2 | Keep **review-assistant-thin-v0.3** baseline unchanged |
| 3 | Keep governance plan docs (this folder) |
| 4 | Rerun all five baseline eval scripts |
| 5 | Document governance decision in governance note or PROMOTION_LOG |
| 6 | **NO_GO** further harness expansion until new phase |

Do **not** rollback v0.3 provider boundary unless provider code itself regressed (separate from harness rollback).

---

## If future harness succeeds

| Action | Detail |
|--------|--------|
| Freeze | **Provider safety harness v0.1** |
| Tag | After governance review (future) |
| Expand | Only with explicit new phase + user approval |
| Default | Mock safety cases remain default run |

---

## Freeze boundaries (harness v0.1)

Frozen means:

- Single script path locked
- Fixed case IDs locked (changes = new version)
- No new dependencies
- No CI requirement added silently

---

## Relationship to v0.3 freeze

| Layer | Freeze name |
|-------|-------------|
| Agent demo | review-assistant-thin-v0.3 |
| Safety harness (future) | provider-safety-harness-v0.1 |

Harness freeze does **not** change agent v0.3 unless separate impl phase approved.

---

## Diagram

See [diagrams/harness-scope-boundary.md](diagrams/harness-scope-boundary.md).

---

## Decision guide

| Situation | Action |
|-----------|--------|
| One safety test fails | Fix agent or harness spec — investigate before expand |
| Harness drift detected | Rollback harness |
| Agent regression | Fix agent or rollback agent change — v0.3 protected |
| User wants benchmark | New phase — not Phase 3.4 |
