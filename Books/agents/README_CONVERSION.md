# PDF → Markdown Conversion Pipeline

Converts `all.pdf` into LLM-ready Markdown **inside `Books/agents/` only**.

## Quick Start (Windows PowerShell)

```powershell
cd C:\Dima\Projects\CURSOR\AGENT\Books\agents
pip install -r requirements.txt
python convert_pdf_to_md.py
```

## Output Layout

```
Books/agents/
├── all.pdf                  # source (never modified by script)
├── requirements.txt
├── convert_pdf_to_md.py
├── README_CONVERSION.md
├── raw/all.raw.md           # direct pymupdf4llm extraction
├── cleaned/all.cleaned.md   # normalized markdown
├── chapters/chXX-*.md       # split by section headings
├── index.md                 # navigation
└── conversion_report.md     # stats + warnings
```

## Pipeline Stages

| Stage | Action |
|-------|--------|
| Extract | `pymupdf4llm.to_markdown()` with page separators |
| Clean | Remove running headers, page numbers, extra blank lines |
| Split | Detect `N. Title` / `References` headings → chapter files |
| Index | Generate `index.md` + `conversion_report.md` |

## Design Choices

- **Legacy extraction mode** (`pymupdf4llm.use_layout(False)`) — avoids ONNX layout failures on some Windows builds.
- **Page provenance** — `--- end of page=N ---` → `<!-- source-page: N -->` (0-based page index from extractor).
- **No semantic rewriting** — no summarization, no invented content.
- **RAG frontmatter** — each chapter file includes YAML metadata (title, page range).

## Cleaning Rules

- Remove repeated running headers (e.g. document title on every page) when safely detected (≥8 repeats).
- Remove isolated numeric page index lines near page markers.
- Preserve code blocks and tables from extractor output.
- Collapse 4+ blank lines to 3.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `all.pdf not found` | Place PDF at `Books/agents/all.pdf` |
| ONNX / layout error | Script forces legacy mode; upgrade pinned versions together |
| Wrong chapter splits | Adjust heading regexes in `split_into_chapters()` |

## Next Phase (manual)

1. Review tables and equations in PDF vs markdown.
2. Tune chapter regex if PDF structure differs.
3. Later migrate curated notes into Agent-OS (outside this folder).
