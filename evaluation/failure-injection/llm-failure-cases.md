# LLM Failure Cases

Adapter: `integrations-real/llm-verification-adapter/`

---

## Case 1: Malformed JSON

**Inject:**

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
```

**Expected:** `llm_malformed_output`, reject, no downstream action  
**Trace:** `observability/examples/malformed-llm-trace.txt`

---

## Case 2: Uncertain Response

**Inject:**

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario uncertain
```

**Expected:** verification_failed or escalate; no auto-allow

---

## Case 3: Timeout

**Inject:**

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --timeout 1
```

**Expected:** llm_timeout or reject (mock may complete fast — verify adapter docs)

---

## Case 4: Valid Structure, Wrong Content

**Inject:** `--scenario happy` + manual review of content

**Expected:** Structural pass; human must not treat as factual verification

**Human check:** Reminder "LLM output != truth" present

---

## Regression Watch

- Parser try/except that swallows errors
- Default values on parse failure
- `--real` mode without timeout

Mock mode must exercise all failure paths without API key.
