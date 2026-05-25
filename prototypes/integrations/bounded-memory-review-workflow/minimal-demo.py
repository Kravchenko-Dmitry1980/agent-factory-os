#!/usr/bin/env python3
"""Bounded memory review: context → execute → critique → verify → writeback/reject."""

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

MAX_MEMORY_CHARS = 2000


class CritiqueVerdict(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    UNCERTAIN = "uncertain"


@dataclass
class MemoryReviewWorkflow:
    snapshot: str = ""
    durable: str = ""
    audit: AuditLog = field(default_factory=AuditLog)

    def start_session(self, curated: str) -> None:
        self.snapshot = curated[:MAX_MEMORY_CHARS]
        self.audit.record("system", "snapshot_frozen", chars=len(self.snapshot))

    def load_context(self) -> str:
        self.audit.record("agent", "context_load")
        return f"[snapshot]\n{self.snapshot}\n[durable]\n{self.durable[:400]}"

    def execute(self, task: str) -> str:
        self.audit.record("agent", "execute", task=task)
        return f"Learned: {task} prefers fail-closed defaults"

    def critique(self, entry: str, scenario: str) -> CritiqueVerdict:
        if scenario == "uncertain":
            return CritiqueVerdict.UNCERTAIN
        if len(entry) < 5:
            return CritiqueVerdict.FAIL
        return CritiqueVerdict.PASS

    def verify(self, entry: str, scenario: str) -> GateResult:
        if scenario == "unverified":
            return GateResult.FAIL
        if scenario == "uncertain":
            return GateResult.UNCERTAIN
        if "hallucinated" in entry.lower():
            return GateResult.FAIL
        return GateResult.PASS

    def writeback(self, entry: str, verified: GateResult, critique: CritiqueVerdict) -> tuple[bool, str]:
        if critique == CritiqueVerdict.UNCERTAIN or verified == GateResult.UNCERTAIN:
            self.audit.record("memory", "blocked", reason="uncertainty")
            return False, "fail-closed: uncertainty block"
        if verified != GateResult.PASS:
            self.audit.record("memory", "rejected", reason="verification failed")
            return False, "fail-closed: verification failed"
        if critique == CritiqueVerdict.FAIL:
            return False, "fail-closed: critique failed"

        projected = len(self.durable) + len(entry) + 1
        if projected > MAX_MEMORY_CHARS or "overflow" in entry:
            self.audit.record("memory", "rejected", reason="overflow", projected=projected)
            return False, f"fail-closed: overflow ({projected}>{MAX_MEMORY_CHARS})"

        before = self.durable
        self.durable = (self.durable + "\n" + entry).strip()
        self.audit.record("memory", "writeback", size=len(self.durable))
        # Snapshot rollback semantics: on reject durable unchanged; snapshot never touched
        assert self.snapshot  # frozen
        if before == self.durable:
            pass
        return True, "writeback accepted (snapshot unchanged)"

    def run(self, task: str, scenario: str) -> tuple[bool, str]:
        curated = "User: concise answers. Project: AGENT."
        self.start_session(curated)
        ctx = self.load_context()
        print(f"  Context loaded ({len(ctx)} chars)")

        entry = self.execute(task)
        if scenario == "overflow":
            entry = "x" * (MAX_MEMORY_CHARS + 50)

        critique = self.critique(entry, scenario)
        self.audit.record("critic", "verdict", value=critique.value)

        verified = self.verify(entry, scenario)
        self.audit.record("verifier", "result", value=verified.value)

        return self.writeback(entry, verified, critique)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scenario",
        default="happy",
        choices=["happy", "overflow", "uncertain", "unverified"],
    )
    args = parser.parse_args()

    print("=== Bounded Memory Review Workflow (integration) ===\n")
    wf = MemoryReviewWorkflow()
    ok, msg = wf.run("memory policy", args.scenario)
    print(f"Writeback: {msg}")
    print(f"Snapshot unchanged: {wf.snapshot.startswith('User:')}")
    print("\nAudit:")
    for row in wf.audit.dump():
        print(f"  {row}")


if __name__ == "__main__":
    main()
