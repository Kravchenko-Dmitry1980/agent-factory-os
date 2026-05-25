#!/usr/bin/env python3
"""Local queue worker: durable SQLite queue, retry ceiling, recovery."""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHARED = ROOT / "integrations-real" / "shared"
sys.path.insert(0, str(SHARED))
import local_paths  # noqa: E402

MAX_RETRIES = 3


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    ESCALATED = "escalated"
    CORRUPT = "corrupt"


def _db() -> Path:
    return local_paths.adapter_dir("local-queue-worker") / "queue.db"


def _audit(event: dict) -> None:
    path = local_paths.adapter_dir("local-queue-worker") / "audit.jsonl"
    event["timestamp"] = datetime.now(timezone.utc).isoformat()
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")


def init_db() -> None:
    conn = sqlite3.connect(_db())
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            goal TEXT NOT NULL,
            status TEXT NOT NULL,
            retry_count INTEGER NOT NULL DEFAULT 0,
            fail_until INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()


def enqueue(goal: str, fail_until: int = 0) -> str:
    init_db()
    tid = str(uuid.uuid4())[:8]
    conn = sqlite3.connect(_db())
    conn.execute(
        "INSERT INTO tasks (id, goal, status, retry_count, fail_until) VALUES (?,?,?,?,?)",
        (tid, goal, TaskStatus.PENDING.value, 0, fail_until),
    )
    conn.commit()
    conn.close()
    _audit({"actor": "queue", "action": "enqueued", "task_id": tid, "goal": goal})
    return tid


def fetch_pending() -> sqlite3.Row | None:
    init_db()
    conn = sqlite3.connect(_db())
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        "SELECT * FROM tasks WHERE status=? ORDER BY id LIMIT 1",
        (TaskStatus.PENDING.value,),
    ).fetchone()
    conn.close()
    return row


def worker_verify(attempt: int, fail_until: int) -> bool:
    return attempt > fail_until


def process_task(row: sqlite3.Row) -> TaskStatus:
    tid = row["id"]
    goal = row["goal"]
    retries = row["retry_count"]
    fail_until = row["fail_until"]

    conn = sqlite3.connect(_db())
    conn.execute("UPDATE tasks SET status=? WHERE id=?", (TaskStatus.RUNNING.value, tid))
    conn.commit()
    conn.close()
    _audit({"actor": "worker", "action": "running", "task_id": tid})

    attempt = retries + 1
    ok = worker_verify(attempt, fail_until)
    _audit({"actor": "verifier", "action": "check", "task_id": tid, "pass": ok})

    conn = sqlite3.connect(_db())
    if ok:
        conn.execute(
            "UPDATE tasks SET status=?, retry_count=? WHERE id=?",
            (TaskStatus.COMPLETED.value, attempt, tid),
        )
        conn.commit()
        conn.close()
        _audit({"actor": "queue", "action": "completed", "task_id": tid})
        return TaskStatus.COMPLETED

    if attempt >= MAX_RETRIES:
        conn.execute(
            "UPDATE tasks SET status=?, retry_count=? WHERE id=?",
            (TaskStatus.ESCALATED.value, attempt, tid),
        )
        conn.commit()
        conn.close()
        _audit({"actor": "supervisor", "action": "escalated", "task_id": tid, "retries": attempt})
        return TaskStatus.ESCALATED

    conn.execute(
        "UPDATE tasks SET status=?, retry_count=? WHERE id=?",
        (TaskStatus.PENDING.value, attempt, tid),
    )
    conn.commit()
    conn.close()
    _audit({"actor": "queue", "action": "retry", "task_id": tid, "retry": attempt})
    return TaskStatus.PENDING


def run_worker(fail_until: int = 0) -> TaskStatus | None:
    final: TaskStatus | None = None
    while True:
        row = fetch_pending()
        if row is None:
            break
        status = process_task(row)
        final = status
        if status in (TaskStatus.COMPLETED, TaskStatus.ESCALATED):
            break
        if status == TaskStatus.PENDING and row["retry_count"] + 1 < MAX_RETRIES:
            continue
        break
    return final


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="happy", choices=["happy", "retry-exhaustion", "recovery"])
    args = parser.parse_args()

    print("=== Local Queue Worker (Phase 2.2) ===\n")

    fail_until = MAX_RETRIES if args.scenario == "retry-exhaustion" else 0

    if args.scenario == "recovery":
        tid = enqueue("Recoverable task", fail_until=1)
        print(f"  enqueued {tid}, simulating crash before complete...")
        # partial run
        row = fetch_pending()
        if row:
            process_task(row)  # fail once → back to pending
        print("  recovery: reloading pending from SQLite...")
        final = run_worker()
        print(f"  after recovery: {final.value if final else 'none'}")
        return

    tid = enqueue("Generate audit report", fail_until=fail_until)
    print(f"  enqueued: {tid}")
    while True:
        row = fetch_pending()
        if not row:
            break
        status = process_task(row)
        print(f"  task {row['id']}: {status.value} (retries={row['retry_count']})")
        if status != TaskStatus.PENDING:
            break


if __name__ == "__main__":
    main()
