# MobileAgent vs Hermes Agent

---

## Status of Hermes in AGENT Repo

На момент ingestion (2026-05-25) **отдельный Hermes review workspace в репозитории не найден** (`experiments/hermes-agent-review/` отсутствует).

Сравнение выполнено на уровне **известных классов GUI/general agents**, не file-by-file diff.

---

## Expected Hermes Themes (General Agent Frameworks)

Typical Hermes-style agents emphasize:
- General tool use over specialized GUI drivers
- Conversation-driven task execution
- Plugin/skill extensibility
- Often text-first environment (API, browser text, code)

---

## MobileAgent Distinctives

| Aspect | MobileAgent | Typical general agent (Hermes-class) |
|--------|-------------|--------------------------------------|
| Primary modality | Vision + motor GUI | Text + generic tools |
| Domain | OS/mobile/browser UI | Open-ended assistant tasks |
| Perception | GUI-Owl, OCR pipelines | Text parsing, optional vision |
| Benchmarks | AndroidWorld, OSWorld, ScreenSpot | varied (MMLU, tool benches) |
| Multi-agent | Role decomposition for navigation | Often single agent or task agents |

---

## Overlap Zone

- **Browser automation** — both may use Playwright-like stacks (v3.5 browser_use)
- **MCP tools** — GUI-Owl 1.5 native MCP vs Hermes MCP plugins
- **Multi-step planning** — Manager agent ≈ planner modules

---

## Complementary Value

MobileAgent fills **GUI/OS modality gap** that general agents (including Hermes) typically treat as optional skill, not core architecture.

---

## Recommended Follow-Up

When Hermes ingestion exists in `experiments/hermes-agent-review/`:
- Re-run this comparison with concrete file citations
- Map Hermes tool registry → `possible-tool-contracts.md`
- Identify shared multi-agent coordination patterns

---

## Placeholder Verdict

**Not competing architectures** — MobileAgent is GUI-specialized; Hermes-class systems are broader harnesses. Agent-OS may need **both layers**: Claude-style harness + GUI twin adapter.
