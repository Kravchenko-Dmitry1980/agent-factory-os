#!/usr/bin/env python3
"""Governed promotion: source → review → anti-pattern scan → governance → decision."""

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

SCAN_PATTERNS = [
    ("universal multi-agent", "dangerous-topology"),
    ("self-improving", "dangerous-topology"),
    ("100% autonomous", "unsupported-claims"),
    ("guaranteed accuracy", "unsupported-claims"),
    ("unreviewed", "research-leakage"),
    ("TODO promote", "research-leakage"),
]


class Decision(str, Enum):
    PROMOTE_NOW = "promote_now"
    PROMOTE_LATER = "promote_later"
    RESEARCH_ONLY = "research_only"
    REJECT = "reject"


@dataclass
class Scores:
    value: int
    maturity: int
    fit: int
    risk: int


@dataclass
class Artifact:
    title: str
    source_path: str
    origin: str
    content: str
    scores: Scores


@dataclass
class GovernedPromotionWorkflow:
    audit: AuditLog = field(default_factory=AuditLog)
    scan_passed: bool = True
    skip_scan: bool = False

    def review(self, art: Artifact) -> tuple[bool, str]:
        if not art.origin or not art.source_path:
            return False, "missing provenance"
        self.audit.record("reviewer", "pass", title=art.title)
        return True, "ok"

    def anti_pattern_scan(self, art: Artifact) -> list[str]:
        if self.skip_scan:
            self.audit.record("scan", "bypass_attempt")
            return []
        flags: list[str] = []
        lower = art.content.lower()
        for phrase, flag in SCAN_PATTERNS:
            if phrase in lower:
                flags.append(flag)
        self.audit.record("scan", "complete", flags=flags)
        return flags

    def governance(self, art: Artifact) -> Decision:
        s = art.scores
        if s.value >= 4 and s.fit >= 4 and s.risk <= 2:
            return Decision.PROMOTE_NOW
        if s.value >= 4 and (s.maturity < 4 or s.risk >= 3):
            return Decision.PROMOTE_LATER
        if s.value < 4:
            return Decision.RESEARCH_ONLY
        return Decision.REJECT

    def run(self, art: Artifact, scenario: str) -> Decision:
        self.audit.record("pipeline", "source", path=art.source_path)

        if scenario == "governance-bypass":
            self.skip_scan = True

        ok, reason = self.review(art)
        if not ok or scenario == "missing-provenance":
            if scenario == "missing-provenance":
                reason = "missing provenance"
            self.audit.record("pipeline", "reject", stage="review", reason=reason)
            return Decision.REJECT

        flags = self.anti_pattern_scan(art)
        if scenario == "dangerous-topology":
            flags.append("dangerous-topology")
        if flags:
            self.audit.record("pipeline", "reject", stage="scan", flags=flags)
            return Decision.REJECT

        if self.skip_scan:
            self.audit.record("pipeline", "reject", stage="governance", reason="scan bypass denied")
            return Decision.REJECT

        decision = self.governance(art)
        self.audit.record("governance", "decision", decision=decision.value)

        if decision == Decision.PROMOTE_NOW:
            target = f"agent-os/08_patterns/{art.title.lower().replace(' ', '-')}.md"
            self.audit.record("integrator", "simulated_promote", target=target)
        elif decision == Decision.PROMOTE_LATER:
            self.audit.record("backlog", "promote_later", title=art.title)

        return decision


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scenario",
        default="happy",
        choices=["happy", "missing-provenance", "dangerous-topology", "governance-bypass"],
    )
    args = parser.parse_args()

    print("=== Governed Promotion Workflow (integration) ===\n")

    if args.scenario == "missing-provenance":
        art = Artifact(
            title="Orphan Pattern",
            source_path="experiments/x.md",
            origin="",
            content="A valid pattern description.",
            scores=Scores(5, 4, 5, 2),
        )
    elif args.scenario == "dangerous-topology":
        art = Artifact(
            title="Universal Swarm",
            source_path="experiments/swarm.md",
            origin="experiments",
            content="Build a universal multi-agent template for all tasks.",
            scores=Scores(5, 4, 5, 2),
        )
    else:
        art = Artifact(
            title="Queue Backed Execution",
            source_path="Books/swarm-playbooks/patterns/queue-backed-execution.md",
            origin="Books/swarm-playbooks",
            content="Use a queue for durable task handoff with verification.",
            scores=Scores(5, 4, 5, 2),
        )

    wf = GovernedPromotionWorkflow()
    decision = wf.run(art, args.scenario)
    print(f"Artifact: {art.title}")
    print(f"Decision: {decision.value}")
    print("\nAudit:")
    for row in wf.audit.dump():
        print(f"  {row}")


if __name__ == "__main__":
    main()
