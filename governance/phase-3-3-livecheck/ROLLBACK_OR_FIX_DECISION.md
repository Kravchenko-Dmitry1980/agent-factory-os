# Rollback or Fix Decision

Decision tree after Phase 3.3-LiveCheck results.

---

## If live check passes (current state)

**Observed:** PASS=3 FAIL=0 live; all baseline PASS.

**Decision:**

1. Document PASS in [LIVE_CHECK_RESULT.md](LIVE_CHECK_RESULT.md) — done
2. Record governance review — done
3. **Proceed to Phase 3.3.1-Freeze Real Provider Boundary v0.3**
4. Do not add provider framework before freeze

---

## If setup fails

**Symptoms:** connection errors, server down, wrong port, model unloaded.

**Decision:**

1. Fix LM Studio (or Ollama) **manually**
2. **Do not patch** `minimal_demo.py` or contract script for setup issues
3. Re-run baseline then live check
4. Update live check result doc with new run date

**Rollback:** Not required — mock default unchanged.

---

## If provider shape differs

**Symptoms:** valid local server but JSON not parsed; missing `choices`.

**Decision:**

1. Document tool name, URL, model, and response shape mismatch
2. Try OpenAI-compatible mode in local tool settings
3. **Do not create provider framework** to "support everything"
4. If boundary should accept standard OpenAI shape but rejects valid response → **Phase 3.3-Fix** (scoped parser only)
5. Re-run live check after fix

**Rollback:** Only if fix cannot be scoped safely; revert to mock-only v0.2.

---

## If safety violation occurs

**Symptoms:** approval bypass, secrets in trace, unverified delivery, non-synthetic data path.

**Decision:**

1. **Stop** — do not freeze v0.3
2. **Rollback** real provider boundary changes from Phase 3.3-Impl
3. Keep **mock v0.2** as production-safe default
4. Incident note in governance (no secrets)
5. Do not proceed until independent review

---

## If baseline regresses while live passes

**Symptoms:** thin/mock/smoke/trace FAIL but live PASS.

**Decision:**

1. Do not freeze
2. Identify regression separately from provider work
3. Fix regression in appropriate phase (not LiveCheck docs)
4. Re-run full matrix before freeze

---

## Summary table

| Condition | Action | Next phase |
|-----------|--------|------------|
| Live + baseline PASS | Document; freeze | **3.3.1-Freeze v0.3** |
| Setup fail | Fix LM Studio manually | Retry LiveCheck |
| Shape mismatch | Document; optional 3.3-Fix | Fix then LiveCheck |
| Safety violation | Rollback boundary | Mock v0.2 only |
| Baseline fail | Fix regression first | Block freeze |

---

## Current recommendation

**Phase 3.3.1-Freeze Real Provider Boundary v0.3** — all gates green on 2026-05-26.
