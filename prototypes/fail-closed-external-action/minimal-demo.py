#!/usr/bin/env python3
"""Fail-closed external action: propose → verify → approve → execute OR deny."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prototypes.shared.audit import AuditLog  # noqa: E402
from prototypes.shared.gates import fail_closed, require_approval  # noqa: E402
from prototypes.shared.types import GateResult  # noqa: E402


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class ProposedAction:
    action_type: str
    payload: dict
    risk_level: RiskLevel

    @property
    def fingerprint(self) -> str:
        raw = json.dumps({"type": self.action_type, "payload": self.payload}, sort_keys=True)
        return hashlib.sha256(raw.encode()).hexdigest()[:16]


@dataclass
class ActionGate:
    approvals: dict[str, bool] = field(default_factory=dict)
    audit: AuditLog = field(default_factory=AuditLog)

    def propose(self, action: ProposedAction) -> None:
        self.audit.record(
            "agent",
            "proposed",
            action_type=action.action_type,
            risk=action.risk_level.value,
            fingerprint=action.fingerprint,
        )

    def verify(self, action: ProposedAction, scenario: str) -> GateResult:
        if scenario == "uncertain":
            result = GateResult.UNCERTAIN
        elif action.payload.get("invalid"):
            result = GateResult.FAIL
        else:
            result = GateResult.PASS
        self.audit.record("verifier", "verified", result=result.value)
        return result

    def request_approval(self, action: ProposedAction, approved: bool | None) -> None:
        if approved is not None:
            self.approvals[action.fingerprint] = approved
        self.audit.record(
            "human",
            "approval_recorded",
            fingerprint=action.fingerprint,
            approved=approved,
        )

    def execute(self, action: ProposedAction, verification: GateResult) -> tuple[bool, str]:
        allowed, reason = fail_closed(verification, "action verification")
        if not allowed:
            self.audit.record("gate", "denied", reason=reason)
            return False, reason

        approval = self.approvals.get(action.fingerprint)
        allowed, reason = require_approval(approval, action.action_type)
        if not allowed:
            self.audit.record("gate", "denied", reason=reason)
            if action.risk_level == RiskLevel.HIGH:
                self.audit.record("supervisor", "escalated", reason="high risk, no approval")
            return False, reason

        self.audit.record("executor", "executed", action_type=action.action_type)
        return True, f"executed {action.action_type} (mock — no real side effect)"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scenario",
        default="approved",
        choices=["approved", "no-approval", "uncertain", "rejected"],
    )
    args = parser.parse_args()

    print("=== Fail-Closed External Action (prototype) ===\n")
    gate = ActionGate()
    action = ProposedAction(
        action_type="send_email",
        payload={"to": "client@example.com", "subject": "Q1 report"},
        risk_level=RiskLevel.HIGH,
    )
    gate.propose(action)
    verification = gate.verify(action, args.scenario)

    if args.scenario == "approved":
        gate.request_approval(action, True)
    elif args.scenario == "rejected":
        gate.request_approval(action, False)
    # no-approval and uncertain: leave approval unset or uncertain path

    ok, msg = gate.execute(action, verification)
    print(f"Verification: {verification.value}")
    print(f"Execute: {msg}")
    print("\nAudit:")
    for row in gate.audit.dump():
        print(f"  {row}")


if __name__ == "__main__":
    main()
