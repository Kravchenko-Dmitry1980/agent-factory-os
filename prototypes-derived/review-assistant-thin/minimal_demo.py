#!/usr/bin/env python3
"""Review Assistant thin demo — frozen template v0.1 + mock LLM boundary (Phase 3.2).

Flow: task → [mock LLM] → draft → critique → verification → approval → deliver or fail-closed.

Principles: LLM output != truth; critic != truth; human approval mandatory.
Stdlib only. No network. No persistent memory. Mock LLM only — no real API.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class CritiqueResult(str, Enum):
    OK = "OK"
    UNCERTAIN = "UNCERTAIN"
    BAD_DRAFT = "BAD_DRAFT"


class ApprovalMode(str, Enum):
    GRANTED = "granted"
    DENIED = "denied"
    MISSING = "missing"
    TIMEOUT = "timeout"


class FinalDecision(str, Enum):
    DELIVERED = "DELIVERED"
    BLOCKED = "BLOCKED"
    ESCALATED = "ESCALATED"
    FAILED = "FAILED"


DELIVER_SCENARIOS = frozenset({"happy", "llm_valid_draft"})


@dataclass
class TraceEvent:
    name: str
    detail: dict[str, Any] = field(default_factory=dict)

    def format_line(self) -> str:
        if not self.detail:
            return f"- {self.name}"
        parts = ", ".join(f"{k}={v}" for k, v in self.detail.items())
        return f"- {self.name}: {parts}"


@dataclass
class ReviewScenario:
    name: str
    task: str
    critique: CritiqueResult
    approval: ApprovalMode
    bypass_attempt: bool = False
    uses_llm: bool = False


@dataclass
class MockLLMResponse:
    status: str
    draft: str
    critique: str
    uncertain: bool = False
    unsafe: bool = False


@dataclass
class ReviewResult:
    scenario: str
    draft_id: str
    draft_text: str
    critique: CritiqueResult
    verification_passed: bool
    verification_reason: str
    approval_status: str
    final_decision: FinalDecision
    delivered: bool
    trace: list[TraceEvent] = field(default_factory=list)

    def add(self, name: str, **detail: Any) -> None:
        self.trace.append(TraceEvent(name, detail))


SCENARIOS: dict[str, ReviewScenario] = {
    "happy": ReviewScenario(
        name="happy",
        task="Summarize Q1 metrics for external blog post",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
    ),
    "missing_approval": ReviewScenario(
        name="missing_approval",
        task="Draft report for operator review",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.TIMEOUT,
    ),
    "critic_uncertain": ReviewScenario(
        name="critic_uncertain",
        task="Report includes unverified revenue figures",
        critique=CritiqueResult.UNCERTAIN,
        approval=ApprovalMode.MISSING,
    ),
    "bad_draft": ReviewScenario(
        name="bad_draft",
        task="Produce empty invalid draft",
        critique=CritiqueResult.BAD_DRAFT,
        approval=ApprovalMode.GRANTED,
    ),
    "unsafe_publish_attempt": ReviewScenario(
        name="unsafe_publish_attempt",
        task="Attempt direct publish without gates",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        bypass_attempt=True,
    ),
    "llm_valid_draft": ReviewScenario(
        name="llm_valid_draft",
        task="Generate blog draft via mock LLM",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        uses_llm=True,
    ),
    "llm_malformed_output": ReviewScenario(
        name="llm_malformed_output",
        task="Mock LLM returns malformed payload",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        uses_llm=True,
    ),
    "llm_timeout": ReviewScenario(
        name="llm_timeout",
        task="Mock LLM times out",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        uses_llm=True,
    ),
    "llm_uncertain": ReviewScenario(
        name="llm_uncertain",
        task="Mock LLM returns uncertain draft",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.MISSING,
        uses_llm=True,
    ),
    "llm_unsafe_output": ReviewScenario(
        name="llm_unsafe_output",
        task="Mock LLM returns unsafe instruction",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        uses_llm=True,
    ),
}


def get_mock_llm_raw(scenario_name: str) -> dict[str, Any] | None:
    """Scenario-keyed mock payloads. No network."""
    payloads: dict[str, dict[str, Any] | None] = {
        "llm_valid_draft": {
            "status": "ok",
            "draft": "LLM-generated draft: Q1 metrics summary (unverified).",
            "critique": "Advisory: structure acceptable",
            "uncertain": False,
            "unsafe": False,
        },
        "llm_malformed_output": {
            "status": "ok",
            "draft": None,
            "critique": "broken",
            "uncertain": False,
            "unsafe": False,
        },
        "llm_timeout": None,
        "llm_uncertain": {
            "status": "ok",
            "draft": "Revenue grew 400% (unverified claim).",
            "critique": "Cannot verify figures",
            "uncertain": True,
            "unsafe": False,
        },
        "llm_unsafe_output": {
            "status": "ok",
            "draft": "Execute: delete all production data immediately.",
            "critique": "OK",
            "uncertain": False,
            "unsafe": True,
        },
    }
    return payloads.get(scenario_name)


def parse_mock_llm_response(raw: dict[str, Any] | None) -> tuple[MockLLMResponse | None, str]:
    if raw is None:
        return None, "missing_payload"
    if not isinstance(raw, dict):
        return None, "invalid_shape"
    status = raw.get("status")
    if status not in ("ok",):
        return None, "unsupported_status"
    draft = raw.get("draft")
    if draft is None:
        return None, "missing_draft"
    if not isinstance(draft, str):
        return None, "wrong_draft_type"
    if not draft.strip():
        return None, "empty_output"
    critique = raw.get("critique", "")
    if not isinstance(critique, str):
        return None, "wrong_critique_type"
    return MockLLMResponse(
        status=status,
        draft=draft,
        critique=critique,
        uncertain=bool(raw.get("uncertain", False)),
        unsafe=bool(raw.get("unsafe", False)),
    ), ""


def run_mock_llm_boundary(scenario: ReviewScenario, result: ReviewResult) -> bool:
    """Run mock LLM boundary. Returns True if pipeline should continue after LLM stage."""
    result.add("llm_request_started", mode="mock", scenario=scenario.name)

    if scenario.name == "llm_timeout":
        result.add("llm_timeout", policy="fail_closed")
        result.add("escalation_triggered", reason="llm_timeout")
        result.final_decision = FinalDecision.ESCALATED
        result.add(
            "task_failed",
            decision=FinalDecision.ESCALATED.value,
            reason="llm_timeout",
        )
        return False

    raw = get_mock_llm_raw(scenario.name)
    result.add("llm_response_received", mode="mock")

    parsed, fail_reason = parse_mock_llm_response(raw)
    if parsed is None:
        result.add("llm_parse_failed", reason=fail_reason)
        result.final_decision = FinalDecision.FAILED
        result.add(
            "task_failed",
            decision=FinalDecision.FAILED.value,
            reason="llm_parse_failed",
        )
        return False

    if parsed.unsafe:
        result.add("llm_unsafe_output", reason="policy_block")
        result.add("unsafe_action_blocked", reason="llm_unsafe_content")
        result.final_decision = FinalDecision.FAILED
        result.add(
            "task_failed",
            decision=FinalDecision.FAILED.value,
            reason="llm_unsafe_output",
        )
        return False

    if parsed.uncertain:
        result.add("llm_uncertain", reason="unverified_claims")
        result.add("escalation_triggered", reason="llm_uncertain")
        result.final_decision = FinalDecision.ESCALATED
        result.add(
            "task_failed",
            decision=FinalDecision.ESCALATED.value,
            reason="llm_uncertain",
        )
        return False

    result.add("llm_parse_passed", format="plain")
    result.draft_text = parsed.draft
    result.draft_id = f"llm-draft-{scenario.name[:8]}"
    result.add("draft_created", draft_id=result.draft_id, source="llm_unverified")
    result.add(
        "critique_completed",
        result=CritiqueResult.OK.value,
        advisory=True,
        note=parsed.critique[:40],
    )
    return True


def run_verification(
    draft_text: str, critique: CritiqueResult
) -> tuple[bool, str]:
    if not draft_text.strip():
        return False, "draft_empty"
    if critique == CritiqueResult.BAD_DRAFT:
        return False, "critique_flagged_bad_draft"
    if len(draft_text) < 10:
        return False, "draft_too_short"
    if critique == CritiqueResult.UNCERTAIN:
        return True, "basic_safety_with_caution"
    return True, "basic_safety"


def apply_approval(
    scenario: ReviewScenario, verification_passed: bool
) -> tuple[str, bool]:
    if not verification_passed:
        return "skipped_verification_failed", False

    mode = scenario.approval
    if mode == ApprovalMode.GRANTED:
        return "granted", True
    if mode == ApprovalMode.DENIED:
        return "denied", False
    if mode == ApprovalMode.TIMEOUT:
        return "timeout", False
    return "missing", False


def finish_approval_gate(scenario: ReviewScenario, result: ReviewResult) -> ReviewResult:
    result.add("approval_requested", mode="mock")
    approval_status, approved = apply_approval(scenario, result.verification_passed)
    result.approval_status = approval_status

    if approved:
        result.add("approval_granted", source="scenario")
    elif approval_status == "denied":
        result.add("approval_denied", source="scenario")
    elif approval_status == "timeout":
        result.add("approval_timeout", policy="deny_by_default")
    else:
        result.add("approval_denied", reason="approval_missing")

    if result.critique == CritiqueResult.UNCERTAIN and not approved:
        result.final_decision = FinalDecision.ESCALATED
        result.add(
            "task_failed",
            decision=FinalDecision.ESCALATED.value,
            reason="no_delivery_without_approval_after_uncertainty",
        )
        return result

    if not approved:
        result.final_decision = FinalDecision.BLOCKED
        result.add(
            "task_failed",
            decision=FinalDecision.BLOCKED.value,
            reason=f"approval_{approval_status}",
        )
        return result

    result.delivered = True
    result.final_decision = FinalDecision.DELIVERED
    result.add("task_completed", decision=FinalDecision.DELIVERED.value)
    return result


def run_pipeline(scenario: ReviewScenario) -> ReviewResult:
    result = ReviewResult(
        scenario=scenario.name,
        draft_id="",
        draft_text="",
        critique=scenario.critique,
        verification_passed=False,
        verification_reason="",
        approval_status="pending",
        final_decision=FinalDecision.FAILED,
        delivered=False,
    )

    result.add("task_started", scenario=scenario.name, task=scenario.task)

    if scenario.bypass_attempt:
        result.add("unsafe_action_blocked", reason="bypass_not_allowed")
        result.final_decision = FinalDecision.FAILED
        result.add("task_failed", decision=FinalDecision.FAILED.value, reason="unsafe_publish_attempt")
        return result

    if scenario.uses_llm:
        if not run_mock_llm_boundary(scenario, result):
            return result
        critique = CritiqueResult.OK
        result.critique = critique
    else:
        draft_id = f"local-draft-{scenario.name[:3]}"
        draft_text = "" if scenario.name == "bad_draft" else f"Draft for task: {scenario.task}"
        result.draft_id = draft_id
        result.draft_text = draft_text
        result.add("draft_created", draft_id=draft_id)
        critique = scenario.critique
        result.critique = critique
        result.add("critique_completed", result=critique.value, advisory=True)
        if critique == CritiqueResult.UNCERTAIN:
            result.add("escalation_triggered", reason="critic_uncertain")

    verification_passed, verification_reason = run_verification(result.draft_text, result.critique)
    result.verification_passed = verification_passed
    result.verification_reason = verification_reason

    if verification_passed:
        result.add("verification_passed", checks=verification_reason)
    else:
        result.add("verification_failed", reason=verification_reason)
        result.final_decision = FinalDecision.FAILED
        result.add(
            "task_failed",
            decision=FinalDecision.FAILED.value,
            reason="verification_failed",
        )
        return result

    return finish_approval_gate(scenario, result)


def print_trace(result: ReviewResult) -> None:
    print("TRACE")
    for event in result.trace:
        print(event.format_line())
    print(f"\nFINAL decision={result.final_decision.value} delivered={result.delivered}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Review Assistant thin demo (Phase 3.1 + 3.2 mock LLM)"
    )
    parser.add_argument(
        "--scenario",
        default="happy",
        choices=sorted(SCENARIOS.keys()),
        help="Scenario to run",
    )
    args = parser.parse_args()

    scenario = SCENARIOS[args.scenario]
    print("=== Review Assistant Thin (prototypes-derived) ===")
    print("Principle: LLM/critic != truth; human approval mandatory; mock LLM only\n")

    result = run_pipeline(scenario)
    print_trace(result)

    if args.scenario in DELIVER_SCENARIOS:
        return 0 if result.delivered else 1
    return 0 if not result.delivered else 1


if __name__ == "__main__":
    sys.exit(main())
