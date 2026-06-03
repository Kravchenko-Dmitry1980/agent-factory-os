#!/usr/bin/env python3
"""Review Assistant Demo Runner — Phase 3.5.2.

Stdlib-only operator-friendly CLI wrapper around existing demo and eval commands.
Does NOT modify agent logic. Does NOT call real provider by default.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import traceback
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

REPO_ROOT_MARKERS = (
    "prototypes-derived/review-assistant-thin/minimal_demo.py",
    "evaluation/scripts/check_review_assistant_thin.py",
)

TRACE_EVENT_RU: dict[str, str] = {
    "task_started": "задача запущена",
    "draft_created": "создан черновик",
    "critique_completed": "критик дал advisory-оценку",
    "verification_passed": "проверка пройдена",
    "verification_failed": "проверка не пройдена",
    "approval_requested": "запрошено подтверждение человека",
    "approval_granted": "подтверждение получено",
    "approval_timeout": "подтверждение не получено вовремя",
    "approval_denied": "подтверждение отклонено",
    "unsafe_action_blocked": "опасное действие заблокировано",
    "escalation_triggered": "случай передан на эскалацию",
    "task_completed": "задача завершена успешно",
    "task_failed": "задача завершена безопасной ошибкой",
    "llm_request_started": "начат mock LLM запрос",
    "llm_response_received": "получен mock LLM ответ",
    "llm_parse_passed": "LLM ответ разобран",
    "llm_parse_failed": "LLM ответ не удалось разобрать",
    "llm_unsafe_output": "LLM ответ признан опасным",
    "provider_request_prepared": "подготовлен запрос к локальному провайдеру",
    "provider_request_started": "запрос к локальному провайдеру отправлен",
    "provider_response_received": "ответ локального провайдера получен",
    "provider_parse_passed": "ответ локального провайдера разобран",
}

DECISION_EXPLANATION_RU: dict[str, str] = {
    "DELIVERED": (
        "Результат был доставлен, потому что прошёл проверку и получил approval."
    ),
    "BLOCKED": (
        "Результат заблокирован. Система не разрешила доставку "
        "без обязательных условий."
    ),
    "ESCALATED": (
        "Система передала случай на эскалацию, потому что обнаружила "
        "неопределённость или риск."
    ),
    "FAILED": (
        "Сценарий завершился ошибкой безопасно: система не стала доставлять результат."
    ),
}


@dataclass(frozen=True)
class MenuItem:
    key: str
    title_ru: str
    group: str
    command: list[str]
    requires_real_provider: bool
    explanation: str
    what_it_proves: str
    is_validation: bool = False


def find_repo_root() -> Path:
    start = Path(__file__).resolve().parent
    for candidate in (start, *start.parents):
        if all((candidate / marker).is_file() for marker in REPO_ROOT_MARKERS):
            return candidate
    raise SystemExit(
        "Ошибка: запустите скрипт из корня репозитория AGENT.\n"
        "Ожидается наличие:\n"
        "  prototypes-derived/review-assistant-thin/minimal_demo.py\n"
        "  evaluation/scripts/check_review_assistant_thin.py"
    )


def build_menu(repo_root: Path) -> list[MenuItem]:
    demo = [
        sys.executable,
        str(repo_root / "prototypes-derived/review-assistant-thin/minimal_demo.py"),
    ]
    eval_dir = repo_root / "evaluation/scripts"

    def demo_cmd(scenario: str, real_provider: bool = False) -> list[str]:
        cmd = demo + ["--scenario", scenario]
        if real_provider:
            cmd.append("--real-provider")
        return cmd

    def eval_cmd(script: str) -> list[str]:
        return [sys.executable, str(eval_dir / script)]

    return [
        MenuItem(
            key="happy",
            title_ru="Нормальный сценарий",
            group="Базовые сценарии Review Assistant",
            command=demo_cmd("happy"),
            requires_real_provider=False,
            explanation=(
                "Черновик создан, критик дал OK, проверка пройдена, "
                "approval получен — результат доставлен."
            ),
            what_it_proves="Контролируемый happy path работает с human approval.",
        ),
        MenuItem(
            key="missing_approval",
            title_ru="Нет approval",
            group="Базовые сценарии Review Assistant",
            command=demo_cmd("missing_approval"),
            requires_real_provider=False,
            explanation=(
                "Черновик был создан, проверка прошла, но approval не был получен "
                "(timeout). Система заблокировала доставку."
            ),
            what_it_proves="Система не публикует результат без подтверждения человека.",
        ),
        MenuItem(
            key="critic_uncertain",
            title_ru="Критик не уверен",
            group="Базовые сценарии Review Assistant",
            command=demo_cmd("critic_uncertain"),
            requires_real_provider=False,
            explanation=(
                "Критик не уверен в качестве черновика. Система эскалировала случай "
                "и не доставила результат автоматически."
            ),
            what_it_proves="Неопределённость критика → эскалация, не auto-delivery.",
        ),
        MenuItem(
            key="bad_draft",
            title_ru="Плохой черновик",
            group="Базовые сценарии Review Assistant",
            command=demo_cmd("bad_draft"),
            requires_real_provider=False,
            explanation=(
                "Черновик не прошёл verification. Система остановила цикл "
                "без доставки."
            ),
            what_it_proves="Verification блокирует некачественный черновик.",
        ),
        MenuItem(
            key="unsafe_publish_attempt",
            title_ru="Опасная попытка публикации",
            group="Базовые сценарии Review Assistant",
            command=demo_cmd("unsafe_publish_attempt"),
            requires_real_provider=False,
            explanation=(
                "Попытка обойти gates заблокирована. Опасное действие не выполнено."
            ),
            what_it_proves="Bypass и unsafe publish блокируются fail-closed.",
        ),
        MenuItem(
            key="llm_valid_draft",
            title_ru="Mock LLM — хороший ответ",
            group="Mock LLM",
            command=demo_cmd("llm_valid_draft"),
            requires_real_provider=False,
            explanation=(
                "Mock LLM вернул ответ, он разобран в черновик (unverified), "
                "прошёл verification и approval — доставлен."
            ),
            what_it_proves="LLM output всё равно проходит parse, verification, approval.",
        ),
        MenuItem(
            key="llm_malformed_output",
            title_ru="Mock LLM — сломанный ответ",
            group="Mock LLM",
            command=demo_cmd("llm_malformed_output"),
            requires_real_provider=False,
            explanation=(
                "Mock LLM вернул malformed ответ. Parse не прошёл — доставки нет."
            ),
            what_it_proves="Malformed LLM output отклоняется на границе parse.",
        ),
        MenuItem(
            key="llm_unsafe_output",
            title_ru="Mock LLM — опасный ответ",
            group="Mock LLM",
            command=demo_cmd("llm_unsafe_output"),
            requires_real_provider=False,
            explanation=(
                "Mock LLM вернул опасный контент. Система заблокировала действие."
            ),
            what_it_proves="Unsafe LLM content блокируется до delivery.",
        ),
        MenuItem(
            key="real_provider_synthetic",
            title_ru="Real provider — LM Studio (synthetic)",
            group="Real Local Provider",
            command=demo_cmd("real_provider_synthetic", real_provider=True),
            requires_real_provider=True,
            explanation=(
                "Локальный OpenAI-compatible endpoint вызван с synthetic prompt. "
                "Ответ проходит те же gates: parse, verification, approval."
            ),
            what_it_proves="Real provider boundary работает с теми же safety gates.",
        ),
        MenuItem(
            key="provider_safety_harness",
            title_ru="Provider safety harness (16 cases)",
            group="Проверки baseline",
            command=eval_cmd("check_review_assistant_provider_safety.py"),
            requires_real_provider=False,
            explanation="Запуск frozen provider safety harness без сети.",
            what_it_proves="16 synthetic safety cases проходят offline harness.",
            is_validation=True,
        ),
        MenuItem(
            key="thin_baseline",
            title_ru="Thin baseline (5 cases)",
            group="Проверки baseline",
            command=eval_cmd("check_review_assistant_thin.py"),
            requires_real_provider=False,
            explanation="Проверка 5 базовых сценариев Review Assistant Thin.",
            what_it_proves="Frozen thin v0.1 scenarios ведут себя как ожидается.",
            is_validation=True,
        ),
        MenuItem(
            key="mock_llm_baseline",
            title_ru="Mock LLM baseline (5 cases)",
            group="Проверки baseline",
            command=eval_cmd("check_review_assistant_llm_mock.py"),
            requires_real_provider=False,
            explanation="Проверка mock LLM сценариев без сети.",
            what_it_proves="Mock LLM boundary frozen и стабилен.",
            is_validation=True,
        ),
        MenuItem(
            key="real_provider_contract_no_network",
            title_ru="Real provider contract (no-network)",
            group="Проверки baseline",
            command=eval_cmd("check_review_assistant_real_provider_contract.py"),
            requires_real_provider=False,
            explanation="Контракт real provider без live network call.",
            what_it_proves="Provider flag и config gates работают offline.",
            is_validation=True,
        ),
        MenuItem(
            key="smoke_checks",
            title_ru="Smoke checks (12 cases)",
            group="Проверки baseline",
            command=eval_cmd("run_demo_smoke_checks.py"),
            requires_real_provider=False,
            explanation="Smoke checks по демо и интеграциям репозитория.",
            what_it_proves="Evaluation baseline стабилен.",
            is_validation=True,
        ),
        MenuItem(
            key="text_trace_checks",
            title_ru="Text trace examples (6 cases)",
            group="Проверки baseline",
            command=eval_cmd("check_expected_text_traces.py"),
            requires_real_provider=False,
            explanation="Проверка frozen text trace examples.",
            what_it_proves="Observability examples соответствуют ожиданиям.",
            is_validation=True,
        ),
    ]


def menu_by_key(menu: list[MenuItem]) -> dict[str, MenuItem]:
    return {item.key: item for item in menu}


def parse_final(stdout: str) -> dict[str, Any]:
    match = re.search(
        r"FINAL\s+decision=(\w+)\s+delivered=(True|False)",
        stdout,
    )
    if not match:
        return {"decision": None, "delivered": None}
    return {
        "decision": match.group(1),
        "delivered": match.group(2) == "True",
    }


def parse_trace_events(stdout: str) -> list[str]:
    events: list[str] = []
    in_trace = False
    for line in stdout.splitlines():
        stripped = line.strip()
        if stripped == "TRACE":
            in_trace = True
            continue
        if in_trace:
            if stripped.startswith("- "):
                event_part = stripped[2:].split(":", 1)[0].strip()
                events.append(event_part)
            elif stripped.startswith("FINAL "):
                break
            elif stripped and not stripped.startswith("- "):
                in_trace = False
    return events


def parse_pass_fail(stdout: str) -> dict[str, int | None]:
    patterns = [
        r"Summary:\s*PASS=(\d+)\s+FAIL=(\d+)",
        r"PASS=(\d+)\s+FAIL=(\d+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, stdout)
        if match:
            return {"pass": int(match.group(1)), "fail": int(match.group(2))}
    return {"pass": None, "fail": None}


def explain_trace_event(name: str) -> str:
    return TRACE_EVENT_RU.get(name, f"{name} (см. документацию)")


def compute_safety_status(
    decision: str | None,
    delivered: bool | None,
    trace_events: list[str],
) -> str:
    if decision is None:
        return "WARNING"
    if delivered and "approval_granted" not in trace_events:
        return "WARNING"
    if delivered and "verification_passed" not in trace_events:
        return "WARNING"
    if decision == "DELIVERED" and delivered:
        return "OK"
    if decision == "BLOCKED" and delivered is False:
        return "BLOCKED"
    if decision == "ESCALATED" and delivered is False:
        return "ESCALATED"
    if decision == "FAILED" and delivered is False:
        return "FAILED"
    return "WARNING"


def confirm_real_provider() -> bool:
    print()
    print("ВНИМАНИЕ: этот сценарий вызывает локальный OpenAI-compatible endpoint.")
    print()
    print("Проверьте:")
    print("- LM Studio или Ollama запущен локально")
    print("- RA_LLM_BASE_URL задан")
    print("- используется synthetic data only")
    print("- cloud provider не используется")
    print("- секреты не передаются")
    print()
    answer = input("Продолжить? yes/no: ").strip().lower()
    return answer == "yes"


def check_real_provider_env() -> bool:
    if os.environ.get("RA_LLM_BASE_URL"):
        return True
    print()
    print("RA_LLM_BASE_URL не задан в окружении.")
    print("Установите переменные в PowerShell:")
    print('  $env:RA_LLM_BASE_URL = "http://127.0.0.1:1234"')
    print('  $env:RA_LLM_MODEL = "qwen2.5-7b-instruct-1m"')
    print()
    return False


def run_command(cmd: list[str], cwd: Path, debug: bool) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except Exception:
        if debug:
            traceback.print_exc()
        raise


def print_raw_output(stdout: str, stderr: str) -> None:
    if stdout:
        print(stdout, end="" if stdout.endswith("\n") else "\n")
    if stderr:
        print(stderr, file=sys.stderr, end="" if stderr.endswith("\n") else "\n")


def print_scenario_summary(item: MenuItem, stdout: str) -> dict[str, Any]:
    final = parse_final(stdout)
    trace_events = parse_trace_events(stdout)
    decision = final["decision"]
    delivered = final["delivered"]
    safety = compute_safety_status(decision, delivered, trace_events)

    decision_text = decision or "не распознано"
    if decision and decision not in DECISION_EXPLANATION_RU:
        happened = "Решение не распознано. Нужно посмотреть raw output."
    elif decision:
        happened = item.explanation
    else:
        happened = "Решение не распознано. Нужно посмотреть raw output."

    delivered_ru = "да" if delivered else "нет" if delivered is False else "неизвестно"

    print()
    print("=" * 40)
    print("РЕЗУЛЬТАТ ДЕМО")
    print("=" * 40)
    print()
    print(f"Сценарий: {item.title_ru}")
    print(f"Решение: {decision_text}")
    print(f"Доставлено: {delivered_ru}")
    print()
    print("Что произошло:")
    print(happened)
    print()
    print("Что это доказывает:")
    print(item.what_it_proves)
    print()
    print("Ключевые TRACE события:")
    if trace_events:
        for event in trace_events:
            print(f"- {event}: {explain_trace_event(event)}")
    else:
        print("- (события не найдены)")
    print()
    print(f"Статус безопасности: {safety}")

    return {
        "final": final,
        "trace_events": trace_events,
        "safety": safety,
        "happened": happened,
    }


def print_validation_summary(item: MenuItem, stdout: str) -> dict[str, Any]:
    counts = parse_pass_fail(stdout)
    passed = counts["pass"]
    failed = counts["fail"]
    ok = passed is not None and failed is not None and failed == 0

    print()
    print("=" * 40)
    print("РЕЗУЛЬТАТ ПРОВЕРКИ")
    print("=" * 40)
    print()
    print(f"Проверка: {item.title_ru}")
    if passed is not None and failed is not None:
        print(f"PASS: {passed}")
        print(f"FAIL: {failed}")
        print()
        if ok:
            print("Итог:")
            print("OK — проверка прошла")
        else:
            print("Итог:")
            print("FAIL — есть ошибки")
    else:
        print("PASS: ?")
        print("FAIL: ?")
        print()
        print("Итог:")
        print("FAIL — не удалось разобрать summary")

    return {"pass": passed, "fail": failed, "ok": ok}


def save_transcript(
    repo_root: Path,
    item: MenuItem,
    cmd: list[str],
    stdout: str,
    parsed: dict[str, Any],
) -> Path:
    transcripts_dir = repo_root / "demos/review-assistant-runner/transcripts"
    transcripts_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{item.key}.md"
    path = transcripts_dir / filename

    lines = [
        f"# Transcript — {item.key}",
        "",
        f"**Timestamp:** {datetime.now().isoformat(timespec='seconds')}",
        f"**Scenario:** {item.title_ru}",
        "",
        "## Command",
        "",
        "```text",
        " ".join(cmd),
        "```",
        "",
        "## Raw output",
        "",
        "```text",
        stdout.rstrip(),
        "```",
        "",
        "## Parsed",
        "",
    ]

    if item.is_validation:
        lines.append(f"- PASS: {parsed.get('pass')}")
        lines.append(f"- FAIL: {parsed.get('fail')}")
        lines.append(f"- OK: {parsed.get('ok')}")
    else:
        final = parsed.get("final", {})
        lines.append(f"- decision: {final.get('decision')}")
        lines.append(f"- delivered: {final.get('delivered')}")
        lines.append(f"- safety: {parsed.get('safety')}")
        lines.append("")
        lines.append("### Trace events")
        for event in parsed.get("trace_events", []):
            lines.append(f"- {event}")

    lines.extend([
        "",
        "## Russian summary",
        "",
        parsed.get("happened", item.explanation),
        "",
        f"**What it proves:** {item.what_it_proves}",
        "",
    ])

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def execute_item(
    item: MenuItem,
    repo_root: Path,
    *,
    save_transcript_flag: bool,
    debug: bool,
    skip_confirm: bool = False,
) -> int:
    if item.requires_real_provider:
        if not skip_confirm and not confirm_real_provider():
            print("Real provider scenario cancelled")
            return 0
        if not check_real_provider_env():
            return 1

    cmd = item.command
    print()
    print(f"Команда: {' '.join(cmd)}")
    print()

    result = run_command(cmd, repo_root, debug)
    print_raw_output(result.stdout, result.stderr)

    if result.returncode != 0:
        print()
        print(f"Команда завершилась с кодом: {result.returncode}")
        if result.stderr.strip():
            short = result.stderr.strip().splitlines()[-1]
            print(f"stderr: {short}")
        print("Сценарий не прошёл")
        if debug:
            traceback.print_exc()
        return result.returncode

    parsed: dict[str, Any]
    if item.is_validation:
        parsed = print_validation_summary(item, result.stdout)
    else:
        parsed = print_scenario_summary(item, result.stdout)

    if save_transcript_flag:
        path = save_transcript(repo_root, item, cmd, result.stdout, parsed)
        print()
        print(f"Transcript сохранён: {path.relative_to(repo_root)}")

    return 0


def print_list(menu: list[MenuItem]) -> None:
    print("Review Assistant Demo Runner — доступные пункты:")
    print()
    current_group = ""
    for index, item in enumerate(menu, start=1):
        if item.group != current_group:
            current_group = item.group
            print(f"[{current_group}]")
        suffix = " [real provider]" if item.requires_real_provider else ""
        val_suffix = " (validation)" if item.is_validation else ""
        print(f"  {index:2}. {item.key:<32} {item.title_ru}{suffix}{val_suffix}")
    print()
    print("Примеры:")
    print("  python demos/review-assistant-runner/demo_runner.py --scenario happy")
    print(
        "  python demos/review-assistant-runner/demo_runner.py "
        "--scenario happy --save-transcript"
    )


def print_interactive_menu(menu: list[MenuItem]) -> None:
    print()
    print("=" * 40)
    print("Review Assistant Demo Runner")
    print("=" * 40)
    print()
    print("Выберите сценарий:")
    print()

    current_group = ""
    for index, item in enumerate(menu, start=1):
        if item.group != current_group:
            current_group = item.group
            print()
            print(f"--- {current_group} ---")
        marker = " [!]" if item.requires_real_provider else ""
        print(f"  {index:2}. {item.title_ru}{marker}")
        print(f"      ({item.key})")

    print()
    print("   0. Выход")
    print()


def interactive_loop(
    menu: list[MenuItem],
    repo_root: Path,
    save_transcript_flag: bool,
    debug: bool,
) -> int:
    while True:
        print_interactive_menu(menu)
        choice = input("Номер пункта: ").strip()
        if choice in ("0", "q", "quit", "exit"):
            print("Выход.")
            return 0
        if not choice.isdigit():
            print("Введите номер пункта или 0 для выхода.")
            continue
        index = int(choice)
        if index < 1 or index > len(menu):
            print(f"Неверный номер. Доступно 1–{len(menu)}.")
            continue
        item = menu[index - 1]
        execute_item(
            item,
            repo_root,
            save_transcript_flag=save_transcript_flag,
            debug=debug,
        )
        print()
        again = input("Запустить ещё один сценарий? yes/no [no]: ").strip().lower()
        if again != "yes":
            return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Review Assistant Demo Runner — operator-friendly CLI wrapper.",
    )
    parser.add_argument(
        "--scenario",
        help="Запустить сценарий или проверку по ключу (например: happy)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Показать все доступные сценарии",
    )
    parser.add_argument(
        "--save-transcript",
        action="store_true",
        help="Сохранить transcript в demos/review-assistant-runner/transcripts/",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Показать traceback при ошибках",
    )
    return parser


def configure_stdio_utf8() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def main(argv: list[str] | None = None) -> int:
    configure_stdio_utf8()
    args = build_parser().parse_args(argv)
    repo_root = find_repo_root()
    menu = build_menu(repo_root)
    by_key = menu_by_key(menu)

    if args.list:
        print_list(menu)
        return 0

    if args.scenario:
        key = args.scenario.strip()
        if key not in by_key:
            print(f"Неизвестный сценарий: {key}")
            print()
            print_list(menu)
            return 1
        return execute_item(
            by_key[key],
            repo_root,
            save_transcript_flag=args.save_transcript,
            debug=args.debug,
        )

    return interactive_loop(
        menu,
        repo_root,
        save_transcript_flag=args.save_transcript,
        debug=args.debug,
    )


if __name__ == "__main__":
    raise SystemExit(main())
