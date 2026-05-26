# No Red Team Platform Policy — Phase 3.4

**Purpose:** Clarify that this project is **not** creating a red-team platform.

---

## Statement

Phase 3.4 plans a **minimal synthetic safety check** for Review Assistant Thin provider output.  
It does **not** plan an automated attack platform, exploit library, or public attack corpus.

---

## Allowed later (Phase 3.4-Impl)

| Allowed | Constraints |
|---------|-------------|
| Small synthetic safety checks | Fixed cases in [SAFE_SYNTHETIC_TEST_SET.md](SAFE_SYNTHETIC_TEST_SET.md) |
| Controlled injection-like prompts | Harmless shapes only; see [PROMPT_INJECTION_TAXONOMY.md](PROMPT_INJECTION_TAXONOMY.md) |
| Local-only tests | Mock default; real provider opt-in |
| No sensitive data | [DATA_SAFETY_POLICY.md](DATA_SAFETY_POLICY.md) |

---

## Forbidden

| Forbidden | Reason |
|-----------|--------|
| Automated attack platform | Scope creep; security tool product |
| Exploit payload library | Real-world harm risk |
| Real data exfiltration attempts | Privacy/legal |
| Commands that perform harmful actions | Safety |
| Bypass instructions targeting **real** systems | Operational risk |
| Public exploit corpus ingestion | Uncontrolled payload growth |
| Continuous adversarial fuzzing | Red-team platform behavior |
| "Jailbreak leaderboard" | Benchmark drift |

---

## Distinction

| Red-team platform | Phase 3.4 harness |
|-------------------|-------------------|
| Discover new vulnerabilities | Verify known safety gates |
| Broad adversarial generation | Fixed synthetic cases |
| Attack scoring | Pass/fail safety outcome |
| External corpus | Internal spec only |

---

## If needs grow later

Any expansion toward red-team tooling requires **new governance phase**, explicit user approval, and separate policy — not silent growth from harness script.

---

## Rollback trigger

Broad attack corpus imported or automated exploit generation added → remove harness; rollback per [ROLLBACK_AND_FREEZE_PLAN.md](ROLLBACK_AND_FREEZE_PLAN.md).
