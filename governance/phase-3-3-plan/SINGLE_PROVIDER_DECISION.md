# Single Provider Decision

**Phase 3.3-Plan** — normative for future implementation.

---

## Decision

Future Phase 3.3 **implementation** may support **only one explicitly approved provider mode** per impl baseline.

**No multi-provider framework.**

---

## Allowed future modes

| Mode | Rule |
|------|------|
| **mock** | Remains **default** (v0.2 behavior preserved) |
| **real** | Behind explicit flag (e.g. `--provider-mode real`) |
| **Config** | One provider selected via env + explicit config — no auto-switch |
| **Fallback** | **None** — no silent switch to another provider |

---

## Forbidden

| Item | Why |
|------|-----|
| Provider registry | Framework drift (Hermes anti-pattern) |
| Provider router | Multi-path complexity |
| Fallback provider chain | Hidden resilience → wrong model/data path |
| Model leaderboard | Out of scope; no benchmarking platform |
| Automatic provider selection | Unapproved egress |
| Hidden cloud call | Violates mock default |
| Default external call | Real mode must be opt-in every run |

---

## Relationship to mock v0.2

- All 5 original + 5 mock LLM scenarios must **keep passing** with `--provider-mode mock`
- Real provider adds **new scenarios** — does not replace mock path
- Freeze v0.2 history preserved; real provider → v0.3+ with new freeze record

---

## Extension path (not Phase 3.3)

Second provider requires:

- New governance phase
- Separate security review
- Separate eval + freeze
- Still **no** generic framework unless explicitly approved years later

---

## Summary

**One provider. One mode. Mock default. Real opt-in. No router.**
