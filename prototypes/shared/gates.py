"""Fail-closed gate helpers. Deny by default on uncertainty."""

from __future__ import annotations

from prototypes.shared.types import GateResult


def fail_closed(result: GateResult, reason: str) -> tuple[bool, str]:
    """Return (allowed, reason). Uncertain always denies."""
    if result == GateResult.PASS:
        return True, reason
    if result == GateResult.UNCERTAIN:
        return False, f"fail-closed: uncertain — {reason}"
    return False, f"fail-closed: rejected — {reason}"


def require_approval(approved: bool | None, action: str) -> tuple[bool, str]:
    """External actions require explicit True approval. None = not reviewed."""
    if approved is True:
        return True, f"approved: {action}"
    if approved is None:
        return False, f"deny-by-default: no approval for {action}"
    return False, f"denied: {action}"
