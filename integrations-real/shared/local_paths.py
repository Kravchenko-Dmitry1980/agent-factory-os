"""Local data directory for Phase 2.2 adapters. Not a framework."""

from __future__ import annotations

from pathlib import Path


def data_dir() -> Path:
    root = Path(__file__).resolve().parents[1]
    path = root / ".data"
    path.mkdir(parents=True, exist_ok=True)
    return path


def adapter_dir(name: str) -> Path:
    path = data_dir() / name
    path.mkdir(parents=True, exist_ok=True)
    return path
