# Failure Injection Guide

**Purpose:** Intentionally trigger failures to verify fail-closed behavior.

This is **local manual injection** via demo `--scenario` flags — not chaos engineering platform.

---

## Principles

1. Inject one failure at a time
2. Observe trace, not just exit code
3. Confirm deny/escalate/reject — not crash-only
4. Compare to `observability/examples/` when available
5. Never inject in production systems (N/A here — demos only)

---

## Injection Methods

| Method | Example |
|--------|---------|
| Demo scenario flag | `--scenario malformed` |
| Missing approval | `--scenario no-approval` |
| Timeout | `--timeout 1` on LLM adapter |
| Human deny | `--scenario approval-denied` |
| GUI mismatch | `--scenario mismatch` |

---

## Injection Workflow

```text
1. Select failure class (LLM, queue, memory, GUI, approval)
2. Run demo with failure scenario
3. Capture audit output
4. Compare to expected-outcomes/
5. Record PASS/FAIL in local notes
```

---

## Expected Universal Response

```text
Failure injected → gate catches → terminal deny/reject/escalate → audit explains why
```

**Never acceptable:** failure injected → silent success → side effect

---

## Files By Domain

- [llm-failure-cases.md](llm-failure-cases.md)
- [queue-failure-cases.md](queue-failure-cases.md)
- [memory-failure-cases.md](memory-failure-cases.md)
- [gui-failure-cases.md](gui-failure-cases.md)
- [approval-failure-cases.md](approval-failure-cases.md)

---

## After Injection

If fail-closed breaks → file evolution change proposal + rollback before continuing feature work.
