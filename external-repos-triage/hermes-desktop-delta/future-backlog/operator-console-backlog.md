# Operator Console Backlog

Future work — **not scheduled for implementation**.

---

## Phase 4+ (MVP concepts)

| Item | Priority | Notes |
|------|----------|-------|
| Trace viewer | high | Parse stdout/JSON events; link to scenario baseline |
| Approval queue | high | Pending approvals; no auto-grant |
| Evaluation run viewer | high | Surface check script results |
| Template status viewer | medium | Frozen spec + sign-off links |
| Freeze records browser | medium | v0.1/v0.2 history |
| Governance status dashboard | medium | Phase, verdict, change lock |

---

## Phase 5+

| Item | Notes |
|------|-------|
| Provider config UI | Single provider; env-based secrets; masked |
| Skill review UI | Read-only metadata; no installer |
| Memory boundary UI | Show limits; no writeback |
| Tool boundary toggles | Per template; gated changes |

---

## Much Later

| Item | Notes |
|------|-------|
| Schedules | Only with heavy governance — likely never |
| Gateways | Likely never for Lab |
| Desktop installer | Electron/Tauri — separate product decision |
| Remote mode | High risk; defer indefinitely |

---

## Explicit non-goals

- Hermes-style chat-first home screen
- Kanban / 3D Office
- Skill marketplace
- Multi-provider router

---

## Entry criterion

Start Phase 4 console **plan** when:

- Real provider boundary frozen (post-3.3 impl)
- 2+ templates with eval baselines
- Team pain on manual trace/approval review documented
