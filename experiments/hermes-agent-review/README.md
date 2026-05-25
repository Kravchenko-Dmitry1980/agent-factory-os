# Hermes Agent — Research Ingestion Workspace

**Статус:** Architecture audit (Phase 1)  
**Источник:** [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)  
**Локальная копия:** `source/hermes-agent/`  
**Дата начала:** 2026-05-25

---

## Назначение

Изолированный research sandbox для анализа архитектуры Hermes Agent.  
**Не является deployment-слоем.** Hermes не установлен глобально и не интегрирован в Agent-OS.

## Ограничения

| Разрешено | Запрещено |
|-----------|-----------|
| Чтение исходников и docs | `pip install`, `hermes setup`, запуск gateway |
| Architecture extraction | Интеграция в Agent-OS |
| Pattern comparison | Изменение существующей структуры AGENT/ |
| Mermaid diagrams | Production config changes |

## Структура

```
hermes-agent-review/
├── README.md                 ← вы здесь
├── RESEARCH_STATUS.md        ← текущее понимание + next steps
├── source/hermes-agent/      ← shallow clone (read-only reference)
│
├── architecture/             ← repo inventory, architecture map
├── memory/                   ← MEMORY.md, USER.md, providers
├── skills/                   ← agentskills.io, curator, self-improving
├── mcp/                      ← MCP client/server integration
├── multi-agent/              ← delegate_task, kanban swarm
├── runtime/                  ← agent loop, sandbox backends, profiles
├── prompts/                  ← prompt assembly, SOUL.md, context files
│
├── extracted-patterns/       ← reusable patterns & ideas
├── anti-patterns/            ← dangerous complexity
├── comparisons/              ← Claude Code / Harness / Agent-OS vs Hermes
├── diagrams/                 ← Mermaid architecture diagrams
├── notes/                    ← ad-hoc concept notes
├── references/               ← external links & doc index
└── experiments/              ← future isolated experiments (empty)
```

## Быстрый старт для исследователя

1. Прочитать `RESEARCH_STATUS.md` — текущее понимание
2. `architecture/ARCHITECTURE_MAP.md` — top-level map
3. `architecture/REPOSITORY_INVENTORY.md` — что где лежит
4. `comparisons/` — сравнение с Agent-OS корпусами
5. `source/hermes-agent/website/docs/developer-guide/architecture.md` — каноническая docs

## Ключевые находки (кратко)

Hermes Agent v0.14.0 — **production monolith** (~400 Python modules, 3000+ tests):

- **Closed learning loop:** MEMORY.md + USER.md + skills + curator + session search
- **Multi-platform gateway:** 20+ messaging adapters из одного процесса
- **Subagents + Kanban:** RPC delegation vs durable work queue
- **MCP:** first-class client + optional Hermes-as-MCP-server
- **7 sandbox backends:** local, Docker, SSH, Singularity, Modal, Daytona, Vercel
- **Profiles:** isolated agent instances с собственным HERMES_HOME

## Связь с Agent-OS

| Agent-OS секция | Hermes аналог |
|-----------------|---------------|
| `01_agent-runtime/` | `run_agent.py`, `agent/conversation_loop.py` |
| `02_memory/` | `tools/memory_tool.py`, `agent/memory_manager.py` |
| `03_harness-engineering/` | `hermes_cli/callbacks.py`, `tools/approval.py` |
| `04_multi-agent/` | `tools/delegate_tool.py`, `hermes_cli/kanban*.py` |
| `05_mcp/` | `tools/mcp_tool.py` |
| `06_digital-twins/` | Profiles + Honcho + Kanban persistent workers |
| `08_patterns/` | Frozen memory snapshot, progressive skill disclosure |

## Верификация (без запуска)

```powershell
# Проверить clone
Test-Path experiments\hermes-agent-review\source\hermes-agent\run_agent.py

# Посмотреть версию
Select-String -Path experiments\hermes-agent-review\source\hermes-agent\pyproject.toml -Pattern "version"

# Architecture docs
Get-Content experiments\hermes-agent-review\source\hermes-agent\website\docs\developer-guide\architecture.md -TotalCount 50
```
