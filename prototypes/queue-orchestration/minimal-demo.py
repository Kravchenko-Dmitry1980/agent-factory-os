#!/usr/bin/env python3
"""Queue orchestration: goal → queue → worker → verify → escalate."""

from __future__ import annotations

import argparse
import sys
import uuid
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prototypes.shared.audit import AuditLog  # noqa: E402
from prototypes.shared.types import GateResult  # noqa: E402

MAX_RETRIES = 3


class TaskStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    VERIFYING = "verifying"
    COMPLETED = "completed"
    RETRYING = "retrying"
    ESCALATED = "escalated"
    FAILED = "failed"


@dataclass
class Task:
    task_id: str
    goal: str
    status: TaskStatus = TaskStatus.QUEUED
    retry_count: int = 0
    result: str = ""
    fail_until_attempt: int = 0  # mock: fail verification until N


@dataclass
class Orchestrator:
    queue: list[Task] = field(default_factory=list)
    audit: AuditLog = field(default_factory=AuditLog)

    def enqueue(self, goal: str, fail_until: int = 0) -> Task:
        task = Task(task_id=str(uuid.uuid4())[:8], goal=goal, fail_until_attempt=fail_until)
        self.queue.append(task)
        self.audit.record("orchestrator", "enqueued", task_id=task.task_id, goal=goal)
        return task

    def mock_worker(self, task: Task) -> str:
        task.status = TaskStatus.RUNNING
        self.audit.record("worker", "running", task_id=task.task_id)
        return f"Output for: {task.goal} (attempt {task.retry_count + 1})"

    def verify(self, task: Task, output: str) -> GateResult:
        task.status = TaskStatus.VERIFYING
        attempt = task.retry_count + 1
        if attempt <= task.fail_until_attempt:
            self.audit.record("verifier", "fail", task_id=task.task_id, attempt=attempt)
            return GateResult.FAIL
        self.audit.record("verifier", "pass", task_id=task.task_id)
        return GateResult.PASS

    def process_one(self, task: Task) -> TaskStatus:
        while task.retry_count <= MAX_RETRIES:
            output = self.mock_worker(task)
            result = self.verify(task, output)

            if result == GateResult.PASS:
                task.result = output
                task.status = TaskStatus.COMPLETED
                self.audit.record("orchestrator", "completed", task_id=task.task_id)
                return task.status

            task.retry_count += 1
            if task.retry_count >= MAX_RETRIES:
                task.status = TaskStatus.ESCALATED
                self.audit.record(
                    "supervisor",
                    "escalated",
                    task_id=task.task_id,
                    reason="max retries — fail-closed stop",
                )
                return task.status

            task.status = TaskStatus.RETRYING
            self.audit.record("orchestrator", "retry", task_id=task.task_id, count=task.retry_count)

        task.status = TaskStatus.FAILED
        return task.status


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="happy", choices=["happy", "max-retries"])
    args = parser.parse_args()

    print("=== Queue Orchestration (prototype) ===\n")
    orch = Orchestrator()
    fail_until = MAX_RETRIES if args.scenario == "max-retries" else 0
    task = orch.enqueue("Generate deployment checklist", fail_until=fail_until)
    final = orch.process_one(task)

    print(f"Task {task.task_id}: {task.goal}")
    print(f"Final status: {final.value}")
    print(f"Retries: {task.retry_count}")
    if task.status == TaskStatus.COMPLETED:
        print(f"Result: {task.result}")
    print("\nAudit:")
    for row in orch.audit.dump():
        print(f"  {row}")


if __name__ == "__main__":
    main()
