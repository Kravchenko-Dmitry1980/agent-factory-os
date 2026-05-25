#!/usr/bin/env python3
"""Escalation workflow: task → execute → uncertainty → retry → escalate → stop."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prototypes.shared.audit import AuditLog
from prototypes.shared.types import GateResult

MAX_RETRIES = 3


class WorkflowStatus(str, Enum):
    RUNNING = "running"
    RETRYING = "retrying"
    COMPLETED = "completed"
    ESCALATED = "escalated"
    STOPPED = "stopped"


@dataclass
class EscalationWorkflow:
    retry_count: int = 0
    status: WorkflowStatus = WorkflowStatus.RUNNING
    audit: AuditLog = field(default_factory=AuditLog)

    def execute(self, task: str, attempt: int, scenario: str) -> GateResult:
        self.audit.record("worker", "execute", task=task, attempt=attempt)
        if scenario == "immediate-uncertainty":
            return GateResult.UNCERTAIN
        if scenario == "retry-storm":
            return GateResult.UNCERTAIN
        if attempt < 2:
            return GateResult.UNCERTAIN
        return GateResult.PASS

    def run(self, task: str, scenario: str = "happy") -> WorkflowStatus:
        self.audit.record("system", "task_received", task=task)
        attempt = 0
        result = GateResult.UNCERTAIN

        while attempt <= MAX_RETRIES:
            attempt += 1
            result = self.execute(task, attempt, scenario)

            if result == GateResult.PASS:
                self.status = WorkflowStatus.COMPLETED
                self.audit.record("system", "completed", attempts=attempt)
                return self.status

            if result == GateResult.UNCERTAIN:
                self.retry_count += 1
                self.status = WorkflowStatus.RETRYING
                self.audit.record("system", "uncertainty", retry=self.retry_count)
                if self.retry_count >= MAX_RETRIES:
                    break
                continue

            # FAIL
            self.audit.record("system", "hard_fail")
            self.status = WorkflowStatus.STOPPED
            self.audit.record("gate", "denied", reason="hard failure — fail-closed stop")
            return self.status

        self.status = WorkflowStatus.ESCALATED
        self.audit.record(
            "supervisor",
            "escalated",
            reason="retry ceiling — human required",
            retries=self.retry_count,
        )
        self.audit.record("gate", "denied", reason="fail-closed: escalated, not completed")
        return self.status


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scenario",
        default="happy",
        choices=["happy", "retry-storm", "immediate-uncertainty"],
    )
    args = parser.parse_args()

    print("=== Escalation Workflow (integration) ===\n")
    wf = EscalationWorkflow()
    final = wf.run("Resolve ambiguous customer refund", args.scenario)

    print(f"Final status: {final.value}")
    print(f"Retries: {wf.retry_count}")
    print(f"Completed: {final == WorkflowStatus.COMPLETED}")
    print("\nAudit:")
    for row in wf.audit.dump():
        print(f"  {row}")


if __name__ == "__main__":
    main()
