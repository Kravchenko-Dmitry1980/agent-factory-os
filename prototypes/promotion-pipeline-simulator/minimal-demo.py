#!/usr/bin/env python3
"""Promotion pipeline simulator: source → review → governance → promote OR reject."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prototypes.shared.audit import AuditLog  # noqa: E402


class PromotionDecision(str, Enum):
    PROMOTE_NOW = "promote_now"
    PROMOTE_LATER = "promote_later"
    RESEARCH_ONLY = "research_only"
    REJECT = "reject"


@dataclass
class Scores:
    value: int
    maturity: int
    fit: int
    risk: int  # higher = worse


@dataclass
class Provenance:
    origin: str
    source_path: str
    extracted_at: str


@dataclass
class Artifact:
    title: str
    artifact_type: str
    provenance: Provenance
    scores: Scores
    duplicate: bool = False


@dataclass
class PromotionPipeline:
    audit: AuditLog = field(default_factory=AuditLog)

    def review(self, artifact: Artifact) -> tuple[bool, str]:
        if not artifact.provenance.origin or not artifact.provenance.source_path:
            return False, "missing provenance"
        if artifact.duplicate:
            return False, "duplicate of existing canonical note"
        self.audit.record("reviewer", "review_pass", title=artifact.title)
        return True, "review ok"

    def governance(self, artifact: Artifact) -> PromotionDecision:
        s = artifact.scores
        if s.value >= 4 and s.fit >= 4 and s.risk <= 2:
            decision = PromotionDecision.PROMOTE_NOW
        elif s.value >= 4 and (s.maturity < 4 or s.risk >= 3):
            decision = PromotionDecision.PROMOTE_LATER
        elif s.value < 4:
            decision = PromotionDecision.RESEARCH_ONLY
        else:
            decision = PromotionDecision.REJECT

        self.audit.record(
            "governance",
            "decision",
            decision=decision.value,
            scores={"value": s.value, "maturity": s.maturity, "fit": s.fit, "risk": s.risk},
        )
        return decision

    def promote(self, artifact: Artifact, decision: PromotionDecision) -> tuple[bool, str]:
        if decision != PromotionDecision.PROMOTE_NOW:
            reason = f"not promoted: {decision.value}"
            self.audit.record("integrator", "skipped", reason=reason)
            return False, reason

        target = f"agent-os/08_patterns/{artifact.title.lower().replace(' ', '-')}.md"
        self.audit.record("integrator", "promoted", target=target, provenance=artifact.provenance.origin)
        return True, f"promoted to {target} (simulated — no file written)"

    def run(self, artifact: Artifact) -> PromotionDecision:
        self.audit.record("pipeline", "source_received", path=artifact.provenance.source_path)

        ok, reason = self.review(artifact)
        if not ok:
            self.audit.record("pipeline", "rejected", stage="review", reason=reason)
            return PromotionDecision.REJECT

        decision = self.governance(artifact)
        self.promote(artifact, decision)
        return decision


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="promote", choices=["promote", "later", "reject"])
    args = parser.parse_args()

    print("=== Promotion Pipeline Simulator (prototype) ===\n")

    if args.scenario == "reject":
        artifact = Artifact(
            title="Chaos Pattern",
            artifact_type="pattern",
            provenance=Provenance(origin="", source_path="experiments/x.md", extracted_at="2026-05-25"),
            scores=Scores(value=5, maturity=5, fit=5, risk=1),
        )
    elif args.scenario == "later":
        artifact = Artifact(
            title="Emerging Pattern",
            artifact_type="pattern",
            provenance=Provenance(
                origin="experiments/hermes-agent-review",
                source_path="experiments/hermes-agent-review/patterns/x.md",
                extracted_at="2026-05-25",
            ),
            scores=Scores(value=4, maturity=2, fit=4, risk=4),
        )
    else:
        artifact = Artifact(
            title="Fail Closed Agent Loop",
            artifact_type="pattern",
            provenance=Provenance(
                origin="Books/swarm-playbooks",
                source_path="Books/swarm-playbooks/patterns/queue-backed-execution.md",
                extracted_at="2026-05-25",
            ),
            scores=Scores(value=5, maturity=4, fit=5, risk=2),
        )

    pipeline = PromotionPipeline()
    decision = pipeline.run(artifact)

    print(f"Artifact: {artifact.title}")
    print(f"Decision: {decision.value}")
    print("\nAudit:")
    for row in pipeline.audit.dump():
        print(f"  {row}")


if __name__ == "__main__":
    main()
