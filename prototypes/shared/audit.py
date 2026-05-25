"""Append-only audit log for prototype demos."""

from __future__ import annotations

from dataclasses import dataclass, field

from prototypes.shared.types import AuditEvent


@dataclass
class AuditLog:
    events: list[AuditEvent] = field(default_factory=list)

    def record(self, actor: str, action: str, **detail: object) -> None:
        self.events.append(AuditEvent.now(actor, action, **detail))

    def dump(self) -> list[dict[str, object]]:
        return [
            {
                "timestamp": e.timestamp,
                "actor": e.actor,
                "action": e.action,
                **e.detail,
            }
            for e in self.events
        ]
