# MobileAgent vs Code as Agent Harness

Сравнение с survey «Code as Agent Harness» (`Books/agents/`).

---

## Survey Framework (Ch02–Ch03)

Harness = **interface** (what agent sees) + **mechanisms** (how loop enforces behavior) + **scaling** (multi-agent, RL, etc.).

---

## Interface Layer

| Survey concept | MobileAgent instantiation |
|----------------|---------------------------|
| Observation channel | Screenshot multimodal messages |
| Action channel | GUI DSL (Tap/JSON/pyautogui) |
| Feedback channel | Visual delta, not stdout |
| Contract | Prompt-defined (v2) or JSON schema (v3) |

Code harness: files, shell, structured tool JSON.

GUI harness: pixels, coordinates — **different interface contract**.

---

## Mechanisms

| Mechanism | Survey emphasis | MobileAgent |
|-----------|-----------------|-------------|
| Stop conditions | Explicit terminal types | Weak (Stop string) |
| Error recovery | Retry policies, limits | A/B/C + replan threshold |
| Verification | Tests, linters | Reflection, critics |
| Sandboxing | Container, permissions | Real device / VM |
| Context management | Compression | Text history truncation |

MobileAgent implements **some mechanisms** but not harness-grade hardening.

---

## Scaling (Ch04–Ch05)

| Topic | Survey | MobileAgent |
|-------|--------|-------------|
| Multi-agent | Orchestration patterns | v2/v3 role decomposition |
| RL training | Policy improvement | UI-S1 (VERL semi-online RL) |
| Evaluation | Benchmark suites | AndroidWorld, OSWorld, web benches |

UI-S1 connects MobileAgent family to **training scaling** separate from deployment loops.

---

## Emerging Fields (Ch05)

Survey open problems:
- Long-horizon reliability → MobileAgent memory/notetaker/progress agents
- Safety → largely unaddressed in MobileAgent open source
- Unified harness → each MobileAgent version is separate script

---

## Integration Insight

MobileAgent demonstrates **GUI-specific harness interface** that survey's code-centric framing under-specifies.

Agent-OS should treat GUI as **parallel harness surface**, not subset of bash tools.

---

## Sources

- `Books/agents/chapters/ch02-harness-interface-code-for-reasoning-acting-and.md`
- `Books/agents/chapters/ch03-harness-mechanisms-*.md` (if present)
- MobileAgent v2/v3 architecture docs in this workspace
