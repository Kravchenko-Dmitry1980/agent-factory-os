# Failure Decision Guide

How to classify and respond to failures in future local live checks.

---

## 1. Setup failure

**Symptoms:**

- Connection refused / timeout to `127.0.0.1:1234`
- LM Studio Local Server stopped
- Wrong port configured
- Model not loaded

**Classification:** Setup failure (operator environment)

**Action:**

1. Fix LM Studio setup manually (start server, load model, verify port)
2. Re-run live contract script with env vars
3. **Do not change repo code** for setup issues
4. Record result in updated live check doc if re-validating

---

## 2. Provider compatibility failure

**Symptoms:**

- HTTP 200 but JSON shape mismatch
- Missing `choices` or `message` fields
- Empty `content` despite 200
- Wrong API path on local tool

**Classification:** Provider compatibility failure

**Action:**

1. Document endpoint tool, URL, model, and error in live check notes
2. Verify OpenAI-compatible mode in LM Studio / Ollama settings
3. **Do not create provider framework or router**
4. If boundary parser is correct for OpenAI shape, treat as operator/tool config issue first
5. If multiple local tools fail same way, consider **Phase 3.3-Fix** for parser only

---

## 3. Code boundary bug

**Symptoms:**

- Valid OpenAI-compatible response rejected by parser
- Incorrect timeout handling
- Real mode activates without `--real-provider`
- Missing config does not block

**Classification:** Code boundary bug

**Action:**

1. Reproduce with no-network scenarios first
2. Create **Phase 3.3-Fix** scoped to boundary module only
3. No provider framework, runtime, or factory
4. Re-run full baseline + live check after fix

---

## 4. Safety violation

**Symptoms:**

- Delivery without approval in trace
- API key or env secret printed in trace/logs
- Provider output bypasses verification
- Non-synthetic data sent by scenario change

**Classification:** Safety violation — **stop**

**Action:**

1. Stop live testing immediately
2. Do not proceed to freeze
3. Rollback real provider boundary per [ROLLBACK_OR_FIX_DECISION.md](ROLLBACK_OR_FIX_DECISION.md)
4. Keep mock v0.2 as safe default
5. Write incident note in governance (what happened, no secrets in note)

---

## Decision matrix

| Failure type | Change code? | Create framework? | Proceed to freeze? |
|--------------|--------------|-------------------|--------------------|
| Setup | No | No | After green rerun |
| Compatibility | Maybe (Phase 3.3-Fix) | No | After fix + live PASS |
| Boundary bug | Yes (scoped fix) | No | After fix + live PASS |
| Safety | Rollback | No | **No** |

---

## Escalation

If unsure whether failure is setup vs bug:

1. Run no-network contract (`PASS=2` expected)
2. Run mock LLM checks (`PASS=5`)
3. If no-network PASS but live FAIL → likely setup or compatibility
4. If no-network FAIL → boundary bug before live retest
