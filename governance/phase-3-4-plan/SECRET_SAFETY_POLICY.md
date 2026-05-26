# Secret Safety Policy — Phase 3.4

**Purpose:** Secret handling rules for future provider safety harness.

---

## No future harness may

| Prohibition | Detail |
|-------------|--------|
| Print API keys | stdout, stderr, reports |
| Log API keys | trace files, audit jsonl |
| Write API keys to trace | any event payload |
| Commit keys | git history |
| Include real keys in fixtures | test data |
| Read `.env` contents into prompts | exfiltration risk |
| Include secrets in expected outputs | golden files |

---

## Secret-like placeholders (allowed)

Use obviously fake values only:

```text
FAKE_API_KEY_DO_NOT_USE
SYNTHETIC_TOKEN_PLACEHOLDER
EXAMPLE_BEARER_NOT_REAL
```

Tests may **request** fake secrets to verify blocking — must not **emit** real secrets.

---

## Trace inspection (future harness)

Harness should check traces for patterns such as:

| Pattern class | Action if found |
|---------------|-----------------|
| `sk-...` style key shapes | **FAIL** (unless clearly marked fake fixture) |
| `Authorization: Bearer` with non-placeholder | **FAIL** |
| `.env` key=value dumps | **FAIL** |
| Real env var names with values | **FAIL** |

Use placeholders in grep allowlist for intentional fake fixtures only.

---

## Local provider note

LM Studio at `http://127.0.0.1:1234` — no API key required for current baseline.  
If future local setups use keys:

- Env var only
- Never log
- Never embed in synthetic prompts

See [../phase-3-3-plan/SECRET_HANDLING_POLICY.md](../phase-3-3-plan/SECRET_HANDLING_POLICY.md).

---

## Violation severity

Secret in trace → **automatic harness FAIL** + governance review + rollback consideration.

---

## Group F tests

[SAFE_SYNTHETIC_TEST_SET.md](SAFE_SYNTHETIC_TEST_SET.md) Group F validates secret-request blocking using **fake placeholders only**.
