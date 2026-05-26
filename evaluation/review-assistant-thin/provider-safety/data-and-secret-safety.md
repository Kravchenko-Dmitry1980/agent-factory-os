# Data and Secret Safety — Phase 3.4 Provider Safety

---

## Synthetic only

All harness inputs are synthetic strings defined in the script and documentation. No real client, project, or medical data.

---

## No real secrets

- No API keys
- No passwords
- No tokens
- No `.env` values
- No repository content sent to any provider

---

## Fake placeholders only

Case F02 uses `FAKE_API_KEY_DO_NOT_USE` as an inert placeholder string. It is not a real credential and must not be treated as one.

---

## No network by default

The harness performs local classification only. No provider calls. No cloud endpoints.

---

## Trace safety

The harness asserts that real secret-like patterns (e.g. `sk-`, `password=`) do not appear in output or events, except the allowed fake placeholder reference.

---

## Relation to governance

See also:

- [governance/phase-3-4-plan/DATA_SAFETY_POLICY.md](../../../governance/phase-3-4-plan/DATA_SAFETY_POLICY.md)
- [governance/phase-3-4-plan/SECRET_SAFETY_POLICY.md](../../../governance/phase-3-4-plan/SECRET_SAFETY_POLICY.md)
