# MobileAgent Research Ingestion Workspace

Изолированное исследовательское пространство для анализа [X-PLUG/MobileAgent](https://github.com/X-PLUG/MobileAgent) как источника архитектуры GUI/OS-агентов.

## Границы

| Разрешено | Запрещено |
|-----------|-----------|
| Чтение и документирование исходников | Установка зависимостей / запуск моделей |
| Клонирование в `source/MobileAgent/` | Интеграция в Agent-OS runtime |
| Сравнения и паттерны для будущей работы | Изменение taxonomy Agent-OS |
| Рекомендации в `integration-candidates.md` | Настройка Android emulator / ADB |

## Структура

```
experiments/mobile-agent-review/
├── README.md                 ← вы здесь
├── RESEARCH_STATUS.md        ← сводный статус исследования
├── repository-inventory.md   ← инвентарь репозитория
├── integration-candidates.md   ← что интегрировать позже
├── source/MobileAgent/       ← shallow clone (depth=1)
├── architecture/             ← архитектура и runtime
├── perception/               ← OCR, grounding, screenshots
├── action-runtime/           ← контракты действий, ADB, verification
├── multi-agent/              ← роли, reflection, progress
├── memory/                   ← GUI memory, task history
├── mcp-integration/          ← MCP relevance
├── extracted-patterns/       ← переиспользуемые паттерны
├── anti-patterns/            ← риски и антипаттерны
├── comparisons/              ← сравнение с другими источниками
└── diagrams/                 ← Mermaid-диаграммы
```

## Источник

- **Repo:** https://github.com/X-PLUG/MobileAgent
- **Clone path:** `source/MobileAgent/`
- **Commit (shallow):** `0e5065e` — *Update README_zh.md*
- **Дата ingestion:** 2026-05-25

## Ключевые линии работ в репозитории

| Линия | Папка | Фокус |
|-------|-------|-------|
| Mobile-Agent v1 | `Mobile-Agent-v1/` | Single-agent + heavy perception (OCR + DINO) |
| Mobile-Agent v2 | `Mobile-Agent-v2/` | Multi-agent prompts (NeurIPS 2024) |
| Mobile-Agent v3 | `Mobile-Agent-v3/` | GUI-Owl + MA3 framework, OSWorld/AndroidWorld |
| Mobile-Agent v3.5 | `Mobile-Agent-v3.5/` | GUI-Owl 1.5, multi-platform (mobile/PC/browser) |
| PC-Agent | `PC-Agent/` | Desktop multi-agent (pyautogui) |
| Mobile-Agent-E | `Mobile-Agent-E/` | Self-evolving mobile agent |
| GUI-Critic-R1 | `GUI-Critic-R1/` | Pre-operative error diagnosis |
| UI-S1 | `UI-S1/` | Semi-online RL training (VERL) |

## Как читать результаты

1. Начните с `RESEARCH_STATUS.md` — executive summary.
2. `repository-inventory.md` — что где лежит в clone.
3. `architecture/` — как устроен GUI agent loop.
4. `extracted-patterns/` + `anti-patterns/` — что переносить / чего избегать.
5. `comparisons/` + `integration-candidates.md` — связь с Agent-OS.

## Связанные материалы в AGENT

- `Books/claude/` — Claude Code architecture (канон Agent-OS)
- `Books/agents/` — Code as Agent Harness survey
- `agent-os/` — Knowledge OS skeleton (не изменялся в этом эксперименте)
