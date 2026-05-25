#!/usr/bin/env python3
"""GUI safe action: observe → verify → approve → execute OR reject."""

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
from prototypes.shared.gates import fail_closed, require_approval
from prototypes.shared.types import GateResult, VisualOutcome

SCREENS = {
    "checkout": {"title": "Checkout", "total": 99.0},
    "checkout_confirmed": {"title": "Checkout", "toast": "Paid"},
    "wrong_modal": {"title": "Error", "message": "Card declined"},
    "unchanged": {"title": "Checkout", "total": 99.0},
}


class RiskLevel(str, Enum):
    LOW = "low"
    HIGH = "high"


@dataclass
class SafeActionWorkflow:
    screen: str = "checkout"
    c_strikes: int = 0
    audit: AuditLog = field(default_factory=AuditLog)

    def observe(self) -> dict:
        state = SCREENS[self.screen]
        self.audit.record("perception", "observe", screen=self.screen)
        return state

    def propose(self) -> tuple[str, str, RiskLevel]:
        return "click:confirm_payment", "checkout_confirmed", RiskLevel.HIGH

    def simulate_post_state(self, scenario: str) -> str:
        if scenario == "mismatch":
            return "wrong_modal"
        if scenario == "uncertain":
            return "unchanged"
        return "checkout_confirmed"

    def visual_verify(self, expected: str, actual: str) -> VisualOutcome:
        if actual == expected:
            return VisualOutcome.A
        if actual != self.screen:
            return VisualOutcome.B
        return VisualOutcome.C

    def run(self, scenario: str, approval: bool | None) -> tuple[bool, str]:
        self.observe()
        click, expected, risk = self.propose()
        self.audit.record("planner", "proposed", click=click, expected=expected, risk=risk.value)

        actual = self.simulate_post_state(scenario)
        outcome = self.visual_verify(expected, actual)
        self.audit.record("verifier", "visual", outcome=outcome.value, actual=actual)

        if outcome == VisualOutcome.C:
            self.c_strikes += 1
            if self.c_strikes >= 2:
                self.audit.record("system", "circuit_breaker")
                return False, "fail-closed: circuit breaker after C outcomes"

        if outcome != VisualOutcome.A:
            if scenario == "uncertain":
                gate = GateResult.UNCERTAIN
            else:
                gate = GateResult.FAIL
            allowed, reason = fail_closed(gate, f"visual {outcome.value}")
            self.audit.record("gate", "rejected", reason=reason)
            return False, reason

        if risk == RiskLevel.HIGH:
            allowed, reason = require_approval(approval, click)
            if not allowed:
                self.audit.record("gate", "denied", reason=reason)
                return False, reason

        self.screen = actual
        self.audit.record("actuator", "executed", click=click)
        return True, f"executed {click} (mock)"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="happy", choices=["happy", "mismatch", "no-approval", "uncertain"])
    args = parser.parse_args()

    approval = True if args.scenario == "happy" else None
    if args.scenario == "no-approval":
        approval = None

    print("=== GUI Safe Action Workflow (integration) ===")
    print("Mock screens only\n")

    wf = SafeActionWorkflow()
    ok, msg = wf.run(args.scenario, approval)
    print(f"Result: {msg}")
    print("\nAudit:")
    for row in wf.audit.dump():
        print(f"  {row}")


if __name__ == "__main__":
    main()
