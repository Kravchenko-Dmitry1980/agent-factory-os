#!/usr/bin/env python3
"""Production PDF → Markdown conversion pipeline for Books/agents/all.pdf."""

from __future__ import annotations

import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import pymupdf
import pymupdf4llm

# ---------------------------------------------------------------------------
# Paths (all outputs stay inside Books/agents/)
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
PDF_PATH = BASE_DIR / "all.pdf"
RAW_DIR = BASE_DIR / "raw"
CLEANED_DIR = BASE_DIR / "cleaned"
CHAPTERS_DIR = BASE_DIR / "chapters"
RAW_MD_PATH = RAW_DIR / "all.raw.md"
CLEANED_MD_PATH = CLEANED_DIR / "all.cleaned.md"
INDEX_PATH = BASE_DIR / "index.md"
REPORT_PATH = BASE_DIR / "conversion_report.md"

PAGE_SEP_RE = re.compile(r"^--- end of page=(\d+) ---\s*$", re.MULTILINE)
CHAPTER_NUM_RE = re.compile(
    r"^(#{1,6})\s+(?:\*\*)?(\d+)\.\s+(.+?)(?:\*\*)?\s*$",
    re.MULTILINE,
)
CHAPTER_NAMED_RE = re.compile(
    r"^(#{1,6})\s+(?:\*\*)?(References|Appendix(?:\s+[A-Z0-9]+)?)(?:\*\*)?\s*$",
    re.MULTILINE | re.IGNORECASE,
)
SKIP_CHAPTER_TITLES = {"contents", "table of contents"}


@dataclass
class ChapterChunk:
    number: int | None
    title: str
    slug: str
    filename: str
    content: str
    start_page: int | None = None
    end_page: int | None = None


@dataclass
class ConversionReport:
    source_pdf: Path = PDF_PATH
    page_count: int = 0
    raw_chars: int = 0
    cleaned_chars: int = 0
    chapters: list[ChapterChunk] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)


def ensure_directories() -> None:
    for path in (RAW_DIR, CLEANED_DIR, CHAPTERS_DIR):
        path.mkdir(parents=True, exist_ok=True)


def slugify(title: str, max_len: int = 48) -> str:
    text = unicodedata.normalize("NFKC", title)
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_]+", "-", text).strip("-")
    if len(text) > max_len:
        text = text[:max_len].rstrip("-")
    return text or "section"


def extract_raw_markdown(report: ConversionReport) -> str:
    if not PDF_PATH.is_file():
        raise FileNotFoundError(f"Source PDF not found: {PDF_PATH}")

    doc = pymupdf.open(PDF_PATH)
    report.page_count = doc.page_count
    doc.close()

    # Layout mode may fail on some ONNXRuntime builds; legacy mode is stable.
    pymupdf4llm.use_layout(False)
    report.add_warning(
        "Using pymupdf4llm legacy mode (use_layout=False) for stable extraction."
    )

    markdown = pymupdf4llm.to_markdown(
        str(PDF_PATH),
        page_separators=True,
        page_chunks=False,
        show_progress=True,
        force_text=True,
        table_strategy="lines_strict",
        ignore_code=False,
    )
    report.raw_chars = len(markdown)
    return markdown


def _convert_page_separators(text: str) -> str:
    """Keep page provenance as HTML comments for RAG chunking."""

    return PAGE_SEP_RE.sub(r"<!-- source-page: \1 -->", text)


def _remove_repeated_running_headers(text: str, report: ConversionReport) -> str:
    lines = text.splitlines()
    counts = Counter(line.strip() for line in lines if line.strip())
    repeated_headers = {
        line
        for line, count in counts.items()
        if count >= 8 and len(line) <= 80 and line.startswith("**") and line.endswith("**")
    }
    if repeated_headers:
        report.add_warning(
            f"Removed repeated running headers: {', '.join(sorted(repeated_headers))}"
        )

    cleaned: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped in repeated_headers:
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def _remove_standalone_page_numbers(text: str) -> str:
    """Drop isolated page index lines inserted by PDF layout (not list content)."""

    lines = text.splitlines()
    out: list[str] = []

    def near_page_marker(index: int, window: int = 5) -> bool:
        for j in range(max(0, index - window), min(len(lines), index + window + 1)):
            if "<!-- source-page:" in lines[j]:
                return True
        return False

    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.fullmatch(r"\d{1,3}", stripped):
            prev_blank = i == 0 or not lines[i - 1].strip()
            next_blank = i == len(lines) - 1 or not lines[i + 1].strip()
            if near_page_marker(i) or (prev_blank and next_blank):
                continue
        out.append(line)
    return "\n".join(out)


def _normalize_blank_lines(text: str) -> str:
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def _preserve_code_and_tables(text: str) -> str:
    # No transformation here — explicit hook documents intent for future rules.
    return text


def clean_markdown(raw: str, report: ConversionReport) -> str:
    text = raw
    text = _convert_page_separators(text)
    text = _remove_repeated_running_headers(text, report)
    text = _remove_standalone_page_numbers(text)
    text = _preserve_code_and_tables(text)
    text = _normalize_blank_lines(text)
    report.cleaned_chars = len(text)
    return text


def _page_range_from_content(content: str) -> tuple[int | None, int | None]:
    pages = [int(m.group(1)) for m in re.finditer(r"<!-- source-page: (\d+) -->", content)]
    if not pages:
        return None, None
    # pymupdf page markers are 0-based in extraction output
    return min(pages), max(pages)


def _normalize_chapter_heading(title: str, number: int | None) -> str:
    clean_title = re.sub(r"\*+", "", title).strip()
    if number is None:
        return f"# {clean_title}"
    return f"# Chapter {number}: {clean_title}"


def split_into_chapters(cleaned: str, report: ConversionReport) -> list[ChapterChunk]:
    matches: list[tuple[int, int | None, str, str]] = []

    for match in CHAPTER_NUM_RE.finditer(cleaned):
        level = match.group(1)
        number = int(match.group(2))
        title = match.group(3).strip()
        title_plain = re.sub(r"\*+", "", title).strip()
        if title_plain.lower() in SKIP_CHAPTER_TITLES:
            continue
        matches.append((match.start(), number, title_plain, level))

    for match in CHAPTER_NAMED_RE.finditer(cleaned):
        title = match.group(2).strip()
        if title.lower() in SKIP_CHAPTER_TITLES:
            continue
        matches.append((match.start(), None, title, match.group(1)))

    if not matches:
        report.add_warning(
            "No numbered chapter headings detected; writing single chapter file."
        )
        chunk = ChapterChunk(
            number=1,
            title="Full Document",
            slug="full-document",
            filename="ch01-full-document.md",
            content=_normalize_chapter_heading("Full Document", 1)
            + "\n\n"
            + cleaned.strip()
            + "\n",
        )
        chunk.start_page, chunk.end_page = _page_range_from_content(chunk.content)
        return [chunk]

    matches.sort(key=lambda item: item[0])

    chunks: list[ChapterChunk] = []
    used_slugs: set[str] = set()

    for idx, (start, number, title, _level) in enumerate(matches):
        end = matches[idx + 1][0] if idx + 1 < len(matches) else len(cleaned)
        body = cleaned[start:end].strip()
        body = CHAPTER_NUM_RE.sub("", body, count=1)
        body = CHAPTER_NAMED_RE.sub("", body, count=1)
        body = body.strip()

        if number is None:
            file_number = len([c for c in chunks if c.number is not None]) + len(
                [1 for c in chunks if c.number is None]
            ) + 1
            slug = slugify(title)
            heading = _normalize_chapter_heading(title, None)
        else:
            file_number = number
            slug = slugify(title)
            heading = _normalize_chapter_heading(title, number)

        base_slug = slug
        suffix = 2
        while slug in used_slugs:
            slug = f"{base_slug}-{suffix}"
            suffix += 1
        used_slugs.add(slug)

        filename = f"ch{file_number:02d}-{slug}.md"
        start_page, end_page = _page_range_from_content(body)
        safe_title = title.replace('"', "'")
        frontmatter = (
            "---\n"
            f'source_pdf: "{PDF_PATH.name}"\n'
            f"chapter_number: {number if number is not None else 'null'}\n"
            f'title: "{safe_title}"\n'
            f"source_page_start: {start_page if start_page is not None else 'null'}\n"
            f"source_page_end: {end_page if end_page is not None else 'null'}\n"
            "---\n\n"
        )
        content = frontmatter + heading + "\n\n" + body + "\n"

        chunks.append(
            ChapterChunk(
                number=number,
                title=title,
                slug=slug,
                filename=filename,
                content=content,
                start_page=start_page,
                end_page=end_page,
            )
        )

    if not chunks:
        report.errors.append("Chapter split produced zero files.")
    return chunks


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")


def generate_index(chapters: list[ChapterChunk]) -> str:
    lines = [
        "# Agents Book — Markdown Index",
        "",
        f"Source PDF: [`{PDF_PATH.name}`]({PDF_PATH.name})",
        "",
        "## Chapters",
        "",
    ]
    for chapter in chapters:
        page_note = ""
        if chapter.start_page is not None and chapter.end_page is not None:
            page_note = f" (pages {chapter.start_page}–{chapter.end_page})"
        lines.append(
            f"- [{chapter.filename}](chapters/{chapter.filename}) — "
            f"{chapter.title}{page_note}"
        )
    lines.extend(
        [
            "",
            "## Pipeline Artifacts",
            "",
            f"- [Raw extraction](raw/all.raw.md)",
            f"- [Cleaned markdown](cleaned/all.cleaned.md)",
            f"- [Conversion report](conversion_report.md)",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def generate_report_md(report: ConversionReport) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# Conversion Report",
        "",
        f"Generated: {now}",
        "",
        "## Source",
        "",
        f"- PDF: `{report.source_pdf}`",
        f"- Pages: {report.page_count}",
        f"- Raw size: {report.raw_chars:,} characters",
        f"- Cleaned size: {report.cleaned_chars:,} characters",
        "",
        "## Outputs",
        "",
        f"- `{RAW_MD_PATH.relative_to(BASE_DIR)}`",
        f"- `{CLEANED_MD_PATH.relative_to(BASE_DIR)}`",
        f"- `{CHAPTERS_DIR.relative_to(BASE_DIR)}/` ({len(report.chapters)} files)",
        f"- `{INDEX_PATH.relative_to(BASE_DIR)}`",
        "",
        "## Chapters",
        "",
        "| File | Title | Pages |",
        "|------|-------|-------|",
    ]
    for chapter in report.chapters:
        pages = "—"
        if chapter.start_page is not None and chapter.end_page is not None:
            pages = f"{chapter.start_page}–{chapter.end_page}"
        lines.append(f"| `{chapter.filename}` | {chapter.title} | {pages} |")

    lines.extend(["", "## Warnings", ""])
    if report.warnings:
        lines.extend(f"- {warning}" for warning in report.warnings)
    else:
        lines.append("- None")

    lines.extend(["", "## Errors", ""])
    if report.errors:
        lines.extend(f"- {error}" for error in report.errors)
    else:
        lines.append("- None")

    lines.extend(
        [
            "",
            "## Next Steps",
            "",
            "1. Manually review `cleaned/all.cleaned.md` for table/code fidelity.",
            "2. Validate chapter boundaries against PDF section headings.",
            "3. Spot-check repeated headers/footers and citation blocks.",
            "4. Add semantic frontmatter tags for RAG (topics, entities).",
            "5. When ready, migrate atomic notes into Agent-OS (separate phase).",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def run_conversion() -> ConversionReport:
    report = ConversionReport()
    ensure_directories()

    try:
        raw_md = extract_raw_markdown(report)
        write_text(RAW_MD_PATH, raw_md)

        cleaned_md = clean_markdown(raw_md, report)
        write_text(CLEANED_MD_PATH, cleaned_md)

        chapters = split_into_chapters(cleaned_md, report)
        report.chapters = chapters

        for chapter in chapters:
            write_text(CHAPTERS_DIR / chapter.filename, chapter.content)

        write_text(INDEX_PATH, generate_index(chapters))
        write_text(REPORT_PATH, generate_report_md(report))

    except Exception as exc:
        report.errors.append(str(exc))
        write_text(REPORT_PATH, generate_report_md(report))
        raise

    return report


def main() -> int:
    print(f"Converting: {PDF_PATH}")
    report = run_conversion()
    print(f"Pages: {report.page_count}")
    print(f"Chapters: {len(report.chapters)}")
    print(f"Raw: {RAW_MD_PATH}")
    print(f"Cleaned: {CLEANED_MD_PATH}")
    print(f"Index: {INDEX_PATH}")
    print(f"Report: {REPORT_PATH}")
    if report.warnings:
        print(f"Warnings: {len(report.warnings)}")
    return 0 if not report.errors else 1


if __name__ == "__main__":
    sys.exit(main())
