# Desktop vs CLI / Markdown

Comparison for Agent-OS direction.

| Dimension | CLI / Markdown (current) | Desktop Operator Console (future) |
|-----------|--------------------------|-----------------------------------|
| **Learning** | Excellent — repo is curriculum | Risk of hiding architecture behind UI |
| **Governance** | Visible in git + freeze docs | Must mirror freeze/change-lock in UI |
| **Approvals** | Scenario flags / stdout events | Needs queue + audit trail viewer |
| **Traces** | Text logs + eval scripts | Structured timeline, filter, export |
| **Provider setup** | Env/docs only (mock now) | Wizard tempting — needs gate-heavy design |
| **Skill review** | Spec/docs | Enable/disable UI + supply-chain warnings |
| **Security** | Smaller surface (stdlib demo) | Electron IPC, secrets, FS, updater |
| **Complexity** | Low | High — separate team/domain |
| **RU UX** | `curriculum/ru/` | Needs RU-first mode when built |
| **Autonomy risk** | Low (thin demo) | High (Hermes: tools/schedules/gateways) |

---

## Conclusion

Keep **markdown-first for builders** through Phase 3.

Plan **GUI for operators** when approval/trace/eval pain is real — not because Hermes has Electron.

---

## Hermes Desktop position

Full desktop **before** governance maturity — inverse of our order (specs → impl → eval → freeze → console).
