# Original Sources — Preservation Policy

Two independent source corpora feed the Knowledge OS. **Books/** is the source layer; **agent-os/** is the curated knowledge layer.

---

## A. Claude Code Architecture Corpus

| Field | Value |
|-------|-------|
| **Path** | `Books/claude/` |
| **Status** | Canonical source |
| **Format** | Markdown chapters (18 files) |
| **Policy** | Read-only during extraction |

```
Books/claude/
├── ch01-architecture.md
├── ch02-bootstrap.md
├── …
└── ch18-epilogue.md
```

| Rule | Policy |
|------|--------|
| Modify chapter text | ❌ Forbidden during research phase |
| Move chapter files | ❌ Keep in `Books/claude/` |
| Copy chapter bodies into research | ❌ Use index stubs + links only |
| Extract to atomic notes | ✅ Into `agent-os/00–09/` per [extraction-plan.md](extraction-plan.md) |
| Cite source in extractions | ✅ `Books/claude/chXX-*.md` in `## Sources` |

**Provenance:** Markdown chapters decomposed from PDF book on Claude Code architecture. Language: English (source).

**Research catalog:** [chapters/index.md](chapters/index.md) — index stubs only, no chapter body copies.

---

## B. Code as Agent Harness Survey Corpus

| Field | Value |
|-------|-------|
| **Source PDF** | `Books/agents/all.pdf` |
| **Converted chapters** | `Books/agents/chapters/` (6 files) |
| **Raw extraction** | `Books/agents/raw/all.raw.md` |
| **Cleaned extraction** | `Books/agents/cleaned/all.cleaned.md` |
| **Status** | Converted source corpus, not yet fully cataloged in Agent-OS |
| **Policy** | PDF is immutable source; generated markdown should not be manually edited until QA is complete |

```
Books/agents/
├── all.pdf                      ← immutable source (102 pages)
├── convert_pdf_to_md.py         ← reproducible pipeline
├── raw/all.raw.md               ← regenerable intermediate
├── cleaned/all.cleaned.md       ← regenerable intermediate
├── chapters/ch01–ch06*.md       ← converted chapters (post-pipeline)
├── index.md                     ← chapter navigation
└── conversion_report.md         ← pipeline report
```

| Rule | Policy |
|------|--------|
| Modify `all.pdf` | ❌ Immutable source |
| Manually edit `chapters/*.md` | ❌ Until conversion QA is complete |
| Re-run pipeline | ✅ Via `convert_pdf_to_md.py` (overwrites generated outputs) |
| Extract to atomic notes | ⬜ Planned — catalog not yet in `10_research/` |
| Cite source in extractions | ✅ `Books/agents/chapters/chXX-*.md` or `all.pdf` in `## Sources` |

**Provenance:** Survey *Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems* (arXiv 2605.18747). Converted 2026-05-21; see `Books/agents/conversion_report.md`.

---

## Layer Model

```
Books/                 ← source layer (canonical corpora, read-only policy)
agent-os/10_research/  ← catalog, plans, navigation (no semantic rewrites)
agent-os/00–09/        ← curated atomic knowledge (partial extraction)
```

## Up

- [Research README](README.md)
- [Claude chapters index](chapters/index.md)
- [Master extraction plan](extraction-plan.md)
