#!/usr/bin/env python3
"""Review loop prototype: task → draft → critique → review → publish.

Demonstrates: critic != truth, human review mandatory, fail-closed on uncertainty.
"""

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
from prototypes.shared.gates import fail_closed  # noqa: E402
from prototypes.shared.types import GateResult  # noqa: E402


class CritiqueVerdict(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    UNCERTAIN = "uncertain"


class HumanDecision(str, Enum):
    APPROVE = "approve"
    REJECT = "reject"
    PENDING = "pending"


MAX_REWORK = 2


@dataclass
class ReviewState:
    task_id: str
    task_description: str
    draft: str = ""
    critique_verdict: CritiqueVerdict | None = None
    critique_notes: str = ""
    human_decision: HumanDecision = HumanDecision.PENDING
    rework_count: int = 0
    published: bool = False
    blocked_reason: str | None = None
    audit: AuditLog = field(default_factory=AuditLog)


def mock_draft(task: str) -> str:
    """Mock executor — deterministic, not an LLM."""
    return f"Draft response for: {task}"


def mock_critic(draft: str, scenario: str) -> tuple[CritiqueVerdict, str]:
    """Mock critic — advisory only, can be wrong."""
    if scenario == "uncertain-critic":
        return CritiqueVerdict.UNCERTAIN, "Cannot verify factual claims in draft"
    if "fabricated" in draft.lower():
        return CritiqueVerdict.PASS, "Looks fine"  # deliberately wrong
    if len(draft) < 10:
        return CritiqueVerdict.FAIL, "Draft too short"
    return CritiqueVerdict.PASS, "Structure acceptable; facts not verified"


def mock_human_review(state: ReviewState, scenario: str) -> HumanDecision:
    """Mock human — mandatory gate."""
    if state.blocked_reason:
        return HumanDecision.APPROVE if scenario == "human-overrides-block" else HumanDecision.PENDING
    if state.critique_verdict == CritiqueVerdict.FAIL:
        return HumanDecision.REJECT
    return HumanDecision.APPROVE


def publish(state: ReviewState, force: bool = False) -> tuple[bool, str]:
    """Fail-closed publish — requires human approval."""
    if force:
        state.audit.record("system", "bypass_attempt", task_id=state.task_id)
        return False, "governance bypass denied: publish requires approval token"

    if state.human_decision != HumanDecision.APPROVE:
        return False, "fail-closed: human approval missing"

    if state.critique_verdict == CritiqueVerdict.UNCERTAIN and not state.blocked_reason:
        return False, "fail-closed: uncertain critique unresolved"

    if state.blocked_reason and state.human_decision != HumanDecision.APPROVE:
        return False, f"fail-closed: {state.blocked_reason}"

    gate = GateResult.PASS if state.human_decision == HumanDecision.APPROVE else GateResult.FAIL
    allowed, reason = fail_closed(gate, "publish gate")
    if not allowed:
        return False, reason

    state.published = True
    state.audit.record("publisher", "published", task_id=state.task_id)
    return True, "published"


def run_pipeline(task: str, scenario: str = "happy") -> ReviewState:
    state = ReviewState(task_id="task-001", task_description=task)
    state.audit.record("executor", "task_received", task=task)

    state.draft = mock_draft(task)
    state.audit.record("executor", "draft_created", length=len(state.draft))

    verdict, notes = mock_critic(state.draft, scenario)
    state.critique_verdict = verdict
    state.critique_notes = notes
    state.audit.record("critic", "critique", verdict=verdict.value, notes=notes)

    if verdict == CritiqueVerdict.UNCERTAIN:
        state.blocked_reason = "critic uncertain — fail-closed until human inspects"
        state.audit.record("system", "blocked", reason=state.blocked_reason)

    while verdict == CritiqueVerdict.FAIL and state.rework_count < MAX_REWORK:
        state.rework_count += 1
        state.draft = mock_draft(task) + f" (rework {state.rework_count})"
        verdict, notes = mock_critic(state.draft, scenario)
        state.critique_verdict = verdict
        state.critique_notes = notes
        state.audit.record("executor", "rework", round=state.rework_count)

    if verdict == CritiqueVerdict.FAIL and state.rework_count >= MAX_REWORK:
        state.blocked_reason = "rework exhausted — escalate to human"
        state.audit.record("system", "escalate", reason=state.blocked_reason)

    if scenario == "bypass-attempt":
        ok, msg = publish(state, force=True)
        print(f"  bypass result: {msg}")
        return state

    state.human_decision = mock_human_review(state, scenario)
    state.audit.record("human", "decision", decision=state.human_decision.value)

    if state.human_decision == HumanDecision.APPROVE:
        ok, msg = publish(state)
        print(f"  publish: {msg}")
    else:
        state.audit.record("system", "stopped", reason="human rejected or pending")
        print("  publish: denied (human gate)")

    return state


def main() -> None:
    parser = argparse.ArgumentParser(description="Review loop prototype")
    parser.add_argument(
        "--scenario",
        default="happy",
        choices=["happy", "uncertain-critic", "bypass-attempt", "human-overrides-block"],
    )
    args = parser.parse_args()

    print("=== Review Loop Agent (prototype) ===")
    print("Principle: critic != truth; human review mandatory\n")

    task = "Summarize Q1 metrics for external blog post"
    if args.scenario == "uncertain-critic":
        task = "Report includes fabricated revenue figures"

    state = run_pipeline(task, args.scenario)

    print(f"\nTask: {state.task_description}")
    print(f"Critic verdict: {state.critique_verdict} — {state.critique_notes}")
    print(f"Human decision: {state.human_decision.value}")
    print(f"Published: {state.published}")
    if state.blocked_reason:
        print(f"Blocked: {state.blocked_reason}")
    print(f"\nAudit ({len(state.audit.events)} events):")
    for row in state.audit.dump():
        print(f"  {row}")


if __name__ == "__main__":
    main()
