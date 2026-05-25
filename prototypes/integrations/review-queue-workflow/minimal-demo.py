#!/usr/bin/env python3
"""Review queue workflow: task → queue → draft → critique → review → publish."""

from __future__ import annotations

import argparse
import sys
import uuid
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prototypes.shared.audit import AuditLog
from prototypes.shared.gates import fail_closed, require_approval
from prototypes.shared.types import GateResult

MAX_REWORK = 2


class QueueStatus(str, Enum):
    QUEUED = "queued"
    PROCESSING = "processing"
    ESCALATED = "escalated"
    COMPLETED = "completed"
    REJECTED = "rejected"
    CORRUPT = "corrupt"


class CritiqueVerdict(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    UNCERTAIN = "uncertain"


@dataclass
class QueueTask:
    task_id: str
    description: str
    status: QueueStatus = QueueStatus.QUEUED
    draft: str = ""
    critique: CritiqueVerdict | None = None
    rework_count: int = 0
    human_approved: bool | None = None
    published: bool = False
    dequeued: bool = False


@dataclass
class ReviewQueueWorkflow:
    queue: list[QueueTask] = field(default_factory=list)
    audit: AuditLog = field(default_factory=AuditLog)

    def enqueue(self, description: str) -> QueueTask:
        task = QueueTask(task_id=str(uuid.uuid4())[:8], description=description)
        self.queue.append(task)
        self.audit.record("queue", "enqueued", task_id=task.task_id)
        return task

    def dequeue(self, scenario: str) -> QueueTask | None:
        if scenario == "queue-corruption":
            self.audit.record("queue", "corruption_detected", reason="duplicate head")
            if self.queue:
                self.queue[0].status = QueueStatus.CORRUPT
            return None
        for task in self.queue:
            if task.status == QueueStatus.QUEUED:
                if task.dequeued:
                    task.status = QueueStatus.CORRUPT
                    self.audit.record("queue", "corruption_detected", task_id=task.task_id)
                    return None
                task.dequeued = True
                task.status = QueueStatus.PROCESSING
                self.audit.record("queue", "dequeued", task_id=task.task_id)
                return task
        return None

    def draft(self, task: QueueTask) -> None:
        task.draft = f"Draft for: {task.description}"
        self.audit.record("worker", "drafted", task_id=task.task_id)

    def critique(self, task: QueueTask, scenario: str) -> CritiqueVerdict:
        if scenario == "escalation":
            return CritiqueVerdict.UNCERTAIN
        if scenario == "retry-exhaustion":
            return CritiqueVerdict.FAIL
        if scenario == "critic-disagreement":
            return CritiqueVerdict.PASS  # human will disagree
        return CritiqueVerdict.PASS

    def human_review(self, task: QueueTask, scenario: str) -> bool | None:
        if scenario == "approval-denied" or scenario == "critic-disagreement":
            return False
        if task.critique == CritiqueVerdict.UNCERTAIN and scenario != "escalation":
            return None
        if scenario == "escalation":
            return None
        return True

    def publish(self, task: QueueTask) -> tuple[bool, str]:
        allowed, reason = require_approval(task.human_approved, "publish")
        if not allowed:
            self.audit.record("publisher", "denied", reason=reason)
            return False, reason
        if task.critique == CritiqueVerdict.UNCERTAIN:
            return False, "fail-closed: uncertain critique"
        gate_ok, reason = fail_closed(GateResult.PASS, "publish")
        if not gate_ok:
            return False, reason
        task.published = True
        task.status = QueueStatus.COMPLETED
        self.audit.record("publisher", "published", task_id=task.task_id)
        return True, "published"

    def run(self, description: str, scenario: str = "happy") -> QueueTask | None:
        task = self.enqueue(description)
        current = self.dequeue(scenario)
        if current is None:
            return self.queue[0] if self.queue else None

        self.draft(current)
        verdict = self.critique(current, scenario)
        current.critique = verdict
        self.audit.record("critic", "verdict", verdict=verdict.value)

        while verdict == CritiqueVerdict.FAIL and current.rework_count < MAX_REWORK:
            current.rework_count += 1
            self.draft(current)
            verdict = self.critique(current, scenario)
            current.critique = verdict
            self.audit.record("worker", "rework", round=current.rework_count)

        if verdict == CritiqueVerdict.FAIL and current.rework_count >= MAX_REWORK:
            current.status = QueueStatus.ESCALATED
            self.audit.record("supervisor", "escalated", reason="retry exhaustion")
            return current

        if verdict == CritiqueVerdict.UNCERTAIN:
            current.status = QueueStatus.ESCALATED
            self.audit.record("supervisor", "escalated", reason="uncertain critique")
            if scenario != "escalation":
                return current

        current.human_approved = self.human_review(current, scenario)
        self.audit.record("human", "review", approved=current.human_approved)

        if current.human_approved is False:
            current.status = QueueStatus.REJECTED
            self.audit.record("system", "rejected", reason="approval denied")
            return current

        if current.human_approved is True:
            ok, msg = self.publish(current)
            print(f"  publish: {msg}")
        else:
            current.status = QueueStatus.ESCALATED
            self.audit.record("supervisor", "escalated", reason="no human decision")

        return current


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scenario",
        default="happy",
        choices=[
            "happy",
            "critic-disagreement",
            "retry-exhaustion",
            "approval-denied",
            "escalation",
            "queue-corruption",
        ],
    )
    args = parser.parse_args()

    print("=== Review Queue Workflow (integration) ===\n")
    wf = ReviewQueueWorkflow()
    task = wf.run("External blog post Q1 summary", args.scenario)

    if task is None:
        print("Queue corrupt — workflow stopped")
    else:
        print(f"Task {task.task_id}: {task.status.value}")
        print(f"Published: {task.published}")
        print(f"Rework rounds: {task.rework_count}")

    print("\nAudit:")
    for row in wf.audit.dump():
        print(f"  {row}")


if __name__ == "__main__":
    main()
