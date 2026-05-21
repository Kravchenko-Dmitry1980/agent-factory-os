# CURRENT STATE AUDIT

**Дата:** 2026-05-21  
**Путь:** `C:\Dima\Projects\CURSOR\AGENT`  
**Цель:** зафиксировать фактическое состояние перед Phase 1 — Knowledge OS Bootstrap  
**Метод:** только чтение файловой системы, без перемещений/удалений/переименований

---

## 1. Repository Overview

| Параметр | Значение |
|----------|----------|
| Корневая папка | `AGENT/` |
| Назначение (по README) | Engineering knowledge operating system for AI agents |
| Git | инициализирован (`git init` выполнен), **коммитов нет** |
| Ветка | `master` |
| Файлов (без `.git`, `.venv`) | **156** |
| Markdown-файлов | **153** |
| Прочие файлы | `1× .pdf`, `1× .py`, `1× .txt` |
| Общий размер (без `.git`, `.venv`) | **~11,2 MB** |
| `.venv` | **~14,1 MB** (Python 3.12, pymupdf/pymupdf4llm для PDF-пайплайна) |

### Корневая структура

```
AGENT/
├── .git/              # init выполнен, commits = 0
├── .venv/             # локальное venv для PDF-конвертации
├── README.md          # точка входа → agent-os/README.md
├── Books/
│   ├── agents/        # корпус «Code as Agent Harness» (PDF + pipeline)
│   └── claude/        # корпус «Claude Code architecture» (18 глав)
└── agent-os/          # Knowledge OS skeleton (13 секций + templates)
```

### Два независимых источника знаний

| Корпус | Файлов | О чём | Роль в проекте |
|--------|--------|-------|----------------|
| `Books/claude/` | 18 глав MD | Архитектура Claude Code (production agent CLI) | **Канонический source** для Agent-OS (указан в README и `sources.md`) |
| `Books/agents/` | 1 PDF → 6 глав MD | Survey «Code as Agent Harness» (arXiv 2605.18747) | **Отдельный корпус**, конвертирован PDF-пайплайном; в Agent-OS пока **не интегрирован** |

---

## 2. Folder Inventory

### 2.1 `Books/agents/` — PDF-пайплайн и survey-книга

| Путь | Тип | Размер | Назначение |
|------|-----|--------|------------|
| `all.pdf` | source | 9,9 MB | Исходный PDF (102 стр.) |
| `convert_pdf_to_md.py` | tool | 13,8 KB | Скрипт конвертации |
| `requirements.txt` | config | 91 B | `pymupdf==1.27.2.3`, `pymupdf4llm==1.27.2.3` |
| `README_CONVERSION.md` | docs | 2,2 KB | Документация пайплайна |
| `index.md` | generated | 1,2 KB | Навигация по главам |
| `conversion_report.md` | generated | 1,5 KB | Отчёт конвертации |
| `READA.md` | **orphan** | 79,2 KB | README из GitHub-репозитория Awesome Papers (не артеfact пайплайна) |
| `raw/all.raw.md` | generated | 369 KB | Сырой вывод pymupdf4llm |
| `cleaned/all.cleaned.md` | generated | 366 KB | Нормализованный markdown |
| `chapters/ch01-introduction.md` | generated | 16,6 KB | Глава 1 (стр. 0–5) |
| `chapters/ch02-harness-interface-…md` | generated | 35,8 KB | Глава 2 (стр. 6–14) |
| `chapters/ch03-harness-mechanisms-…md` | generated | 65,3 KB | Глава 3 (стр. 15–32) |
| `chapters/ch04-scaling-the-harness-…md` | generated | 48,6 KB | Глава 4 (стр. 33–47) |
| `chapters/ch05-emerging-fields-and-open-problems.md` | generated | 74,2 KB | Глава 5 (стр. 48–65) |
| `chapters/ch06-references.md` | generated | 126 KB | References (стр. 66–101) |

### 2.2 `Books/claude/` — канонические главы Claude Code

18 markdown-файлов, суммарно ~500 KB:

| Файл | Размер |
|------|--------|
| ch01-architecture.md | 17,3 KB |
| ch02-bootstrap.md | 16,0 KB |
| ch03-state.md | 22,9 KB |
| ch04-api-layer.md | 14,3 KB |
| ch05-agent-loop.md | 29,2 KB |
| ch06-tools.md | 23,8 KB |
| ch07-concurrency.md | 29,0 KB |
| ch08-sub-agents.md | 58,7 KB |
| ch09-fork-agents.md | 21,0 KB |
| ch10-coordination.md | 51,8 KB |
| ch11-memory.md | 27,4 KB |
| ch12-extensibility.md | 18,4 KB |
| ch13-terminal-ui.md | 40,2 KB |
| ch14-input-interaction.md | 46,6 KB |
| ch15-mcp.md | 13,1 KB |
| ch16-remote.md | 11,7 KB |
| ch17-performance.md | 13,1 KB |
| ch18-epilogue.md | 17,8 KB |

> **Примечание:** ch15 и ch17 имеют одинаковый размер (13 085 B), но **разные хеши** — это не дубликаты содержимого.

### 2.3 `agent-os/` — Knowledge OS skeleton

| Секция | MD-файлов | Содержание |
|--------|-----------|------------|
| `00_foundations/` | 11 | Базовые концепты (agent, harness, loops, verification…) |
| `01_agent-runtime/` | 11 | Query loop, tools, concurrency, terminal states… |
| `02_memory/` | 9 | Memory taxonomy, recall, compaction… |
| `03_harness-engineering/` | 10 | Permissions, hooks, verification, feedback… |
| `04_multi-agent/` | 7 | Subagents, swarms, coordination… |
| `05_mcp/` | 7 | MCP protocol, transports, integrations… |
| `06_digital-twins/` | 6 | Identity, evolving memory, personas… |
| `07_projects/` | 6 | Applied projects (neuro-secretary, pkb-assistant…) |
| `08_patterns/` | 8 | Architecture patterns |
| `09_antipatterns/` | 6 | Known failures |
| `10_research/` | 30 | Catalog, extraction plans, chapter stubs |
| `11_glossary/` | 5 | Short glossary entries |
| `12_diagrams/` | 4 | Mermaid diagrams |
| `templates/` | 1 | `concept-note-template.md` |
| **Итого agent-os** | **122** | + `agent-os/README.md` |

**Характер заметок в `00–09`:** полноценные atomic notes по шаблону (Definition, Key Ideas, Architecture Implications, Production Implications, Related Concepts, Sources, My Notes). Пример: `02_memory/memory-recall.md` — 1 194 B, 38 строк, с wikilinks и provenance.

**`10_research/`** — research layer:
- `sources.md` — политика сохранения `Books/claude/`
- `extraction-plan.md` — master plan (18 глав → atomic notes)
- `concepts/`, `patterns/`, `glossary/` — domain extraction plans
- `chapters/ch01–ch18` — **index stubs** (~700–800 B каждый), ссылаются на `Books/claude/`, не содержат текста глав

---

## 3. Git State

| Проверка | Результат |
|----------|-----------|
| `git init` | ✅ Выполнен (`.git/` существует) |
| Коммиты | ❌ **Нет** (`fatal: your current branch 'master' does not have any commits yet`) |
| `.gitignore` | ❌ **Отсутствует** |
| Remote | не настроен (нет commits) |

### Untracked (все файлы проекта)

```
?? .venv/
?? Books/
?? README.md
?? agent-os/
```

### Рекомендуемые исключения для `.gitignore`

| Путь/паттерн | Причина |
|--------------|---------|
| `.venv/` | Локальное Python-окружение (~14 MB) |
| `__pycache__/`, `*.pyc` | Python bytecode |
| `.env`, `*.env` | Секреты (на будущее) |
| `Thumbs.db`, `.DS_Store` | OS metadata |
| `*.log` | Логи |

### Что **стоит** включить в Git

| Путь | Обоснование |
|------|-------------|
| `README.md` | Точка входа |
| `agent-os/**` | Knowledge OS (основной deliverable) |
| `Books/claude/*.md` | Канонический source corpus |
| `Books/agents/all.pdf` | Source PDF (9,9 MB — приемлемо для git) |
| `Books/agents/convert_pdf_to_md.py` | Reproducible pipeline |
| `Books/agents/requirements.txt` | Зависимости пайплайна |
| `Books/agents/README_CONVERSION.md` | Документация пайплайна |
| `Books/agents/index.md`, `conversion_report.md` | Метаданные конвертации |
| `Books/agents/chapters/*.md` | Generated chapters (если нужна воспроизводимость без re-run) |

### Что **можно** исключить из Git (опционально)

| Путь | Обоснование |
|------|-------------|
| `Books/agents/raw/all.raw.md` | Regenerable из PDF |
| `Books/agents/cleaned/all.cleaned.md` | Regenerable из PDF |
| `Books/agents/READA.md` | Orphan, не часть пайплайна |

---

## 4. Source Materials

### 4.1 Канонические источники (не редактировать на research phase)

| Материал | Путь | Статус |
|----------|------|--------|
| Claude Code book (18 глав) | `Books/claude/ch01–ch18*.md` | ✅ Полный корпус, English, decomposed from PDF |
| Survey PDF | `Books/agents/all.pdf` | ✅ 102 страницы, 9,9 MB |
| Survey raw extraction | `Books/agents/raw/all.raw.md` | ✅ 369 KB (regenerable) |

### 4.2 Source chapters — классификация

**Claude Code (`Books/claude/`) — 18 source chapters:**

```
ch01-architecture, ch02-bootstrap, ch03-state, ch04-api-layer,
ch05-agent-loop, ch06-tools, ch07-concurrency, ch08-sub-agents,
ch09-fork-agents, ch10-coordination, ch11-memory, ch12-extensibility,
ch13-terminal-ui, ch14-input-interaction, ch15-mcp, ch16-remote,
ch17-performance, ch18-epilogue
```

**Code as Agent Harness (`Books/agents/chapters/`) — 6 source chapters (post-conversion):**

```
ch01-introduction,
ch02-harness-interface-code-for-reasoning-acting-and,
ch03-harness-mechanisms-planning-memory-tool-use-cont,
ch04-scaling-the-harness-multi-agent-orchestration-ov,
ch05-emerging-fields-and-open-problems,
ch06-references
```

### 4.3 Прочие source-like файлы

| Файл | Статус |
|------|--------|
| `Books/agents/READA.md` | Внешний README (GitHub Awesome Papers list), **не** результат конвертации PDF; вероятная опечатка от `README.md` |

---

## 5. Generated Materials

### 5.1 PDF-to-MD pipeline (`Books/agents/`)

| Артефакт | Существует | Статус |
|----------|------------|--------|
| `all.pdf` | ✅ | Source |
| `convert_pdf_to_md.py` | ✅ | Tool |
| `raw/` | ✅ | `all.raw.md` |
| `cleaned/` | ✅ | `all.cleaned.md` |
| `chapters/` | ✅ | 6 файлов |
| `index.md` | ✅ | Навигация |
| `conversion_report.md` | ✅ | Без ошибок |
| `README_CONVERSION.md` | ✅ | Документация |

**Отчёт конвертации (2026-05-21 20:10:20 UTC):**
- Pages: 102
- Raw: 368 755 chars → Cleaned: 365 124 chars
- Errors: **None**
- Warnings: legacy mode (`use_layout=False`); удалены running headers «Code as Agent Harness»
- Chapters: 6 (Introduction → References)

**Качество конвертации (spot-check):**
- ✅ Главы содержат YAML frontmatter (`source_pdf`, `chapter_number`, `title`, `source_page_start/end`)
- ✅ Page provenance markers (`<!-- source-page: N -->`)
- ✅ ch05 — полный текст (~957 строк, 74 KB), не пустой
- ✅ ch06-references — большой bibliography (~1366 строк) — ожидаемо для References
- ⚠️ Требует ручной проверки: таблицы, формулы, figure captions (отмечено в `conversion_report.md` Next Steps)
- ⚠️ Длинные имена файлов ch02–ch04 обрезаны regex-slug (до ~50 символов)

### 5.2 Agent-OS generated/planned materials

| Материал | Тип | Кол-во |
|----------|-----|--------|
| `agent-os/10_research/chapters/ch01–ch18` | Index stubs (generated catalog) | 18 |
| `agent-os/10_research/*/extraction-plan.md` | Planning docs | 4 |
| `agent-os/00–09/*.md` (кроме index) | Extracted atomic notes | ~85 |
| `agent-os/*/index.md` | Section indexes | 14 |
| `agent-os/12_diagrams/*.md` | Mermaid diagrams | 3 |

**Extraction status (по `extraction-plan.md`):**
- 🟡 Partially extracted: ch01–08, ch10–11, ch15
- ⬜ Not yet extracted: ch09, ch12–14, ch16–18

---

## 6. Duplicates / Conflicts

### 6.1 Намеренные «дубликаты» (разное назначение)

| Имя файла | Копии | Конфликт? |
|-----------|-------|-----------|
| `index.md` | 18 (по секциям + Books/agents) | ❌ Разные scope |
| `extraction-plan.md` | 4 (master + 3 domain) | ❌ Иерархия планов |
| `README.md` | 3 (root, agent-os, 10_research) | ❌ Разный уровень |
| `harness.md` | 2 (00_foundations + 11_glossary) | ❌ Concept vs glossary entry |
| `query-loop.md` | 2 (01_agent-runtime + 11_glossary) | ❌ Concept vs glossary entry |
| `six-abstractions.md` | 2 (00_foundations + 12_diagrams) | ❌ Concept vs diagram |

### 6.2 Claude chapters: source vs stubs

| Путь | Размер | Содержание |
|------|--------|------------|
| `Books/claude/ch01-architecture.md` | 17,3 KB | **Full source text** |
| `agent-os/10_research/chapters/ch01-architecture.md` | 812 B | **Stub** с ссылкой на source |

Все 18 глав Claude Code имеют пару source/stub. Stubs **не дублируют** текст — это catalog entries (by design, см. `10_research/README.md`).

### 6.3 Реальные проблемы пересечения

| Проблема | Детали |
|----------|--------|
| Два корпуса без единого catalog | `Books/claude` интегрирован в Agent-OS; `Books/agents` — **нет** |
| `sources.md` не упоминает `Books/agents` | Только `Books/claude/` как canonical |
| Root `README.md` | Упоминает `Books/claude`, **не** упоминает `Books/agents` |
| `READA.md` | Посторонний файл в `Books/agents/`, может путать с pipeline output |

### 6.4 Битые/пустые файлы

| Проверка | Результат |
|----------|-----------|
| Файлы размером 0 bytes | **Не найдены** |
| MD < 500 B (кроме glossary/index) | Только index stubs и glossary entries — **ожидаемо** |
| Битые wikilinks | Не проверялись автоматически (out of scope) |

---

## 7. Problems Found

### P1 — Git не готов к работе
- Нет `.gitignore` → риск случайного commit `.venv/` (14 MB)
- Нет initial commit → нет baseline для Phase 1

### P2 — Два корпуса, одна документация
- Agent-OS documentation (`sources.md`, root README) описывает только `Books/claude/`
- Survey «Code as Agent Harness» (`Books/agents/`) конвертирован, но **не cataloged** в research layer

### P3 — Source и generated смешаны в `Books/agents/`
```
Books/agents/
├── all.pdf              ← source
├── raw/, cleaned/       ← intermediate generated
├── chapters/            ← final generated
├── convert_pdf_to_md.py ← tool
└── READA.md             ← orphan (не pipeline)
```
При повторной конвертации или ручном редактировании легко перезаписать generated поверх curated.

### P4 — Orphan `READA.md`
- 79 KB, содержит README GitHub-репозитория Awesome Papers
- Не упомянут в `index.md`, `conversion_report.md`, `README_CONVERSION.md`
- Не является output пайплайна

### P5 — Partial extraction без file-level status
- Atomic notes в `00–09` созданы, но в самих файлах нет поля `extraction_status`
- Статус только в `extraction-plan.md` (может рассинхронизироваться)

### P6 — Glossary vs concept overlap
- `11_glossary/harness.md` (303 B) — stub со ссылкой на `00_foundations/harness.md`
- `11_glossary/query-loop.md` — аналогично
- Риск дублирования при RAG, если не разделить роли (glossary = pointer, concept = canonical)

### P7 — ch06-references доминирует по размеру
- 126 KB / 1366 строк — это bibliography, не narrative chapter
- Для Knowledge OS нужна отдельная стратегия (не chunk'ить как обычную главу)

### P8 — Conversion quality — pending manual review
- Pipeline завершился без errors, но Next Steps в report требуют ручной проверки tables/code/citations

---

## 8. Recommended Target Structure

Предложение для Phase 1 (не выполнять сейчас — только целевая модель):

```
AGENT/
├── .gitignore
├── README.md
├── CURRENT_STATE_AUDIT.md          ← этот документ
│
├── sources/                        ← FROZEN raw sources (read-only policy)
│   ├── claude-code/
│   │   └── chapters/               ← move from Books/claude/
│   └── code-as-harness/
│       ├── all.pdf
│       └── README.md               ← provenance metadata
│
├── pipeline/                       ← tools + regenerable artifacts
│   └── pdf-to-md/
│       ├── convert_pdf_to_md.py
│       ├── requirements.txt
│       ├── README.md
│       ├── output/
│       │   ├── raw/
│       │   ├── cleaned/
│       │   └── chapters/
│       └── reports/
│           ├── index.md
│           └── conversion_report.md
│
└── agent-os/                       ← Knowledge OS (unchanged taxonomy)
    ├── 00_foundations/ … 12_diagrams/
    └── 10_research/
        ├── sources.md              ← both corpora
        ├── claude-code/            ← stubs + plans
        └── code-as-harness/        ← NEW: stubs + extraction plan
```

**Принципы:**
1. `sources/` — immutable, versioned, never edited by extraction
2. `pipeline/output/` — regenerable, optionally gitignored
3. `agent-os/` — curated knowledge only (atomic notes, no raw chapter text)
4. Один `sources.md` с provenance для обоих корпусов

---

## 9. Safe Next Steps

Порядок для Phase 1 — Knowledge OS Bootstrap (без перемещений на текущем шаге):

1. **Создать `.gitignore`** — `.venv/`, `__pycache__/`, OS files
2. **Initial commit** — зафиксировать baseline (agent-os + Books + README)
3. **Заморозить политику sources** — formalize в `sources.md`:
   - `Books/claude/` = Claude Code canonical
   - `Books/agents/all.pdf` + `chapters/` = Harness Survey canonical
4. **Добавить catalog для `Books/agents`** в `10_research/`:
   - 6 chapter stubs (по аналогии с claude stubs)
   - extraction plan для harness survey concepts
5. **Решить судьбу `READA.md`** — переименовать/переместить/удалить (после решения пользователя)
6. **Manual QA PDF conversion** — tables, figures, citations в ch02–ch05
7. **Продолжить extraction** по `extraction-plan.md` — ch09, ch12–14, ch16–18 (⬜ status)
8. **Добавить frontmatter `extraction_status`** в atomic notes template (optional)

---

## 10. Do Not Touch Yet

| Объект | Причина |
|--------|---------|
| `Books/claude/*.md` | Канонический source corpus; policy = read-only |
| `Books/agents/all.pdf` | Единственный source PDF для survey |
| `Books/agents/chapters/*.md` | Результат успешной конвертации; re-run перезапишет |
| `Books/agents/raw/`, `cleaned/` | Intermediate artifacts; regenerable но нужны для diff |
| `agent-os/00–09/*.md` | Уже извлечённые atomic notes с wikilinks |
| `agent-os/10_research/extraction-plan.md` | Master roadmap; менять только осознанно |
| `agent-os/10_research/chapters/` stubs | Catalog layer; ссылки на canonical paths |
| `.venv/` | Рабочее окружение для pipeline |
| Структура `agent-os/` (00–12) | Согласованная taxonomy; не реорганизовать до Phase 1 plan |

---

## Appendix: File Counts Summary

| Категория | Count |
|-----------|-------|
| Total files (excl. .git, .venv) | 156 |
| Markdown total | 153 |
| Source chapters (Claude) | 18 |
| Source chapters (Harness survey) | 6 |
| Generated pipeline artifacts | 4 (raw, cleaned, index, report) |
| Agent-OS atomic notes (~) | 85 |
| Agent-OS index/stub/plan files (~) | 37 |
| Empty files | 0 |

---

*Аудит выполнен read-only. Единственный созданный файл: `CURRENT_STATE_AUDIT.md`.*
