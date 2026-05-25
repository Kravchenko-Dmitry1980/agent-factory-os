"""Shared types for Phase 2.0 prototypes. Not a runtime framework."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class GateResult(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    UNCERTAIN = "uncertain"


class VisualOutcome(str, Enum):
    """A/B/C taxonomy from agent-os visual-verification."""

    A = "expected_transition"
    B = "wrong_screen"
    C = "no_change"


@dataclass
class AuditEvent:
    timestamp: str
    actor: str
    action: str
    detail: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def now(cls, actor: str, action: str, **detail: Any) -> AuditEvent:
        return cls(
            timestamp=datetime.now(timezone.utc).isoformat(),
            actor=actor,
            action=action,
            detail=dict(detail),
        )
