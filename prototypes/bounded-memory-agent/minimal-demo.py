#!/usr/bin/env python3
"""Bounded memory prototype: snapshot, limits, verified writeback only."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prototypes.shared.audit import AuditLog  # noqa: E402

MAX_MEMORY_CHARS = 2000


@dataclass
class MemoryAgent:
    durable: str = ""
    snapshot: str = ""
    audit: AuditLog = field(default_factory=AuditLog)

    def start_session(self, curated: str) -> str:
        """Frozen snapshot — does not change until reset_session."""
        self.snapshot = curated[:MAX_MEMORY_CHARS]
        self.audit.record("system", "snapshot_created", chars=len(self.snapshot))
        return self.snapshot

    def reset_session(self, curated: str) -> None:
        """New session = new snapshot from current durable + curated."""
        combined = (curated + "\n" + self.durable).strip()
        self.start_session(combined)
        self.audit.record("system", "session_reset")

    @property
    def durable_size(self) -> int:
        return len(self.durable)

    def write(self, entry: str, *, verified: bool, source: str) -> tuple[bool, str]:
        """No uncontrolled writeback — verification + size gate."""
        if not verified:
            self.audit.record("memory", "write_rejected", reason="unverified", source=source)
            return False, "fail-closed: unverified writeback denied"

        projected = len(self.durable) + len(entry) + 1
        if projected > MAX_MEMORY_CHARS:
            self.audit.record(
                "memory",
                "write_rejected",
                reason="overflow",
                projected=projected,
                limit=MAX_MEMORY_CHARS,
            )
            return False, f"fail-closed: memory overflow ({projected}>{MAX_MEMORY_CHARS})"

        self.durable = (self.durable + "\n" + entry).strip()
        self.audit.record("memory", "write_accepted", source=source, size=self.durable_size)
        return True, "write accepted to durable (snapshot unchanged this session)"

    def load_context(self, query: str) -> str:
        """Explicit context load — snapshot + optional durable slice."""
        self.audit.record("agent", "context_load", query=query)
        durable_slice = self.durable[:500] if query in self.durable else ""
        return f"[snapshot]\n{self.snapshot}\n\n[durable_slice]\n{durable_slice}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="happy", choices=["happy", "overflow", "unverified-writeback"])
    args = parser.parse_args()

    print("=== Bounded Memory Agent (prototype) ===\n")
    agent = MemoryAgent()
    curated = "User prefers concise answers. Project: AGENT repo."
    agent.start_session(curated)

    print(f"Snapshot (frozen): {agent.snapshot[:80]}...")

    if args.scenario == "unverified-writeback":
        ok, msg = agent.write("Agent hallucinated fact", verified=False, source="agent")
        print(f"Write attempt: {msg}")
    elif args.scenario == "overflow":
        big = "x" * (MAX_MEMORY_CHARS + 100)
        ok, msg = agent.write(big, verified=True, source="test")
        print(f"Write attempt: {msg}")
    else:
        ok, msg = agent.write("Verified: use fail-closed defaults.", verified=True, source="human")
        print(f"Write attempt: {msg}")
        ctx = agent.load_context("fail-closed")
        print(f"\nExplicit context load:\n{ctx[:200]}...")
        print(f"\nSnapshot still frozen: {agent.snapshot == curated}")

    print(f"\nDurable size: {agent.durable_size} / {MAX_MEMORY_CHARS}")
    print("Audit:")
    for row in agent.audit.dump():
        print(f"  {row}")


if __name__ == "__main__":
    main()
