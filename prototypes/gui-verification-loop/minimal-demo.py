#!/usr/bin/env python3
"""GUI verification loop with mocked screens and A/B/C outcomes."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prototypes.shared.audit import AuditLog  # noqa: E402
from prototypes.shared.types import VisualOutcome  # noqa: E402

# Mock screen registry — synthetic, not real screenshots
SCREENS = {
    "home": {"title": "Home", "buttons": ["settings", "profile"]},
    "settings": {"title": "Settings", "buttons": ["back", "save"]},
    "settings_saved": {"title": "Settings", "toast": "Saved"},
    "profile": {"title": "Profile", "buttons": ["back"]},
    "unchanged": {"title": "Home", "buttons": ["settings", "profile"]},
}

MAX_C_RETRIES = 2


@dataclass
class GuiLoop:
    current_screen: str = "home"
    c_strikes: int = 0
    audit: AuditLog = field(default_factory=AuditLog)

    def observe(self) -> dict:
        state = SCREENS[self.current_screen]
        self.audit.record("perception", "observe", screen=self.current_screen)
        return state

    def plan(self, goal: str) -> tuple[str, str]:
        """Return (action, expected_next_screen)."""
        if goal == "save_settings" and self.current_screen == "home":
            return "click:settings", "settings"
        if goal == "save_settings" and self.current_screen == "settings":
            return "click:save", "settings_saved"
        return "click:unknown", self.current_screen

    def simulate_click(self, action: str, scenario: str) -> str:
        """Mock action result — returns resulting screen id."""
        if scenario == "outcome-b" and action == "click:save":
            return "profile"  # wrong screen
        if scenario == "outcome-c":
            return "unchanged"  # no change
        if action == "click:settings":
            return "settings"
        if action == "click:save":
            return "settings_saved"
        return self.current_screen

    def visual_verify(self, expected: str, actual: str) -> VisualOutcome:
        if actual == expected:
            return VisualOutcome.A
        if actual != self.current_screen and actual != expected:
            return VisualOutcome.B
        return VisualOutcome.C

    def run_step(self, goal: str, scenario: str = "happy") -> bool:
        self.observe()
        action, expected = self.plan(goal)
        self.audit.record("planner", "proposed_click", click=action, expected=expected)

        # Verify BEFORE treating click as successful (simulate post-state)
        actual = self.simulate_click(action, scenario)
        outcome = self.visual_verify(expected, actual)
        self.audit.record(
            "verifier",
            "visual_verify",
            outcome=outcome.value,
            expected=expected,
            actual=actual,
        )

        if outcome != VisualOutcome.A:
            if outcome == VisualOutcome.C:
                self.c_strikes += 1
                if self.c_strikes >= MAX_C_RETRIES:
                    self.audit.record("system", "circuit_breaker", strikes=self.c_strikes)
            self.audit.record("gate", "click_rejected", reason=outcome.value)
            print(f"  Click REJECTED — outcome {outcome.name}: expected {expected}, got {actual}")
            return False

        self.current_screen = actual
        self.audit.record("actuator", "click_executed", screen=actual)
        print(f"  Click EXECUTED — outcome A: now on {actual}")
        return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scenario",
        default="happy",
        choices=["happy", "outcome-b", "outcome-c"],
    )
    args = parser.parse_args()

    print("=== GUI Verification Loop (prototype) ===")
    print("Mock screens only — no ADB/emulator\n")

    loop = GuiLoop()
    for step in ["navigate", "save"]:
        goal = "save_settings"
        if step == "navigate" and args.scenario == "happy":
            ok = loop.run_step(goal, "happy")
            if ok:
                continue
        ok = loop.run_step(goal, args.scenario)
        if not ok and args.scenario != "happy":
            break

    print(f"\nFinal screen: {loop.current_screen}")
    print("Audit:")
    for row in loop.audit.dump():
        print(f"  {row}")


if __name__ == "__main__":
    main()
