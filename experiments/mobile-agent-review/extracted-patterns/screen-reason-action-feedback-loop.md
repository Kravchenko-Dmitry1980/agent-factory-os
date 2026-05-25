# Screen → Reason → Action → Feedback Loop

Канонический embodied loop из MobileAgent, переносимый в любой GUI agent harness.

---

## Loop Definition

```
1. SCREEN   — capture observation
2. REASON   — LLM/VLM plan next step (± multi-agent roles)
3. ACTION   — parse + execute on device
4. FEEDBACK — new screen + verification outcome
5. UPDATE   — memory, progress, error flags
→ goto 1 or STOP
```

---

## Instantiation by Version

| Stage | v2 | v3 |
|-------|----|----|
| Screen | ADB screencap + OCR list | Screenshot to GUI-Owl |
| Reason | Action prompt (+ progress/memory context) | Executor (+ Manager plan) |
| Action | Parse Tap/Type/... → controller | JSON → android_controller |
| Feedback | Reflect A/B/C | ActionReflector |
| Update | memory, completed_content | InfoPool fields |

---

## Feedback Types

1. **Visual delta** — primary (reflection)
2. **Structured error** — parse failures, ADB errors (weak handling)
3. **External reward** — benchmarks only
4. **Pre-op critic** — GUI-Critic (optional, offline)

---

## Harness Mapping (Code as Agent Harness)

Survey framing:
- **Interface:** multimodal messages + action DSL
- **Mechanism:** loop + verification
- **Scaling:** multi-agent decomposition (v2/v3)

MobileAgent is a **GUI-specialized harness**, not general code harness.

---

## Mermaid

See `diagrams/gui-agent-loop.md`.

---

## Agent-OS Golden Path Extension (Future)

Potential fifth modality alongside terminal tools:
`observe_gui → propose_gui_action → verify_gui → compress_history`

Not in canonical golden path yet.
