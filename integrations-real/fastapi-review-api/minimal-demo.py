#!/usr/bin/env python3
"""FastAPI review API: submit → pending → approve/reject → immutable audit."""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHARED = ROOT / "integrations-real" / "shared"
sys.path.insert(0, str(SHARED))
import local_paths  # noqa: E402


class ReviewStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


def _db_path() -> Path:
    return local_paths.adapter_dir("fastapi-review-api") / "reviews.db"


def init_db() -> None:
    conn = sqlite3.connect(_db_path())
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS reviews (
            id TEXT PRIMARY KEY,
            content TEXT NOT NULL,
            source TEXT NOT NULL,
            status TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS audit (
            audit_id TEXT PRIMARY KEY,
            review_id TEXT NOT NULL,
            event TEXT NOT NULL,
            detail TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def _audit(conn: sqlite3.Connection, review_id: str, event: str, detail: dict) -> str:
    audit_id = str(uuid.uuid4())[:8]
    conn.execute(
        "INSERT INTO audit (audit_id, review_id, event, detail, created_at) VALUES (?,?,?,?,?)",
        (
            audit_id,
            review_id,
            event,
            json.dumps(detail),
            datetime.now(timezone.utc).isoformat(),
        ),
    )
    return audit_id


class ReviewStore:
    def __init__(self) -> None:
        init_db()

    def _conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(_db_path())
        conn.row_factory = sqlite3.Row
        return conn

    def submit(self, content: str, source: str) -> dict:
        if not content.strip():
            raise ValueError("empty content")
        rid = str(uuid.uuid4())[:8]
        conn = self._conn()
        try:
            conn.execute(
                "INSERT INTO reviews (id, content, source, status) VALUES (?,?,?,?)",
                (rid, content, source, ReviewStatus.PENDING.value),
            )
            _audit(conn, rid, "submitted", {"source": source})
            conn.commit()
        finally:
            conn.close()
        return {"id": rid, "status": ReviewStatus.PENDING.value}

    def approve(self, rid: str) -> dict:
        conn = self._conn()
        try:
            row = conn.execute("SELECT status FROM reviews WHERE id=?", (rid,)).fetchone()
            if row is None:
                raise KeyError("not found")
            if row["status"] != ReviewStatus.PENDING.value:
                _audit(conn, rid, "invalid_transition", {"attempt": "approve", "was": row["status"]})
                conn.commit()
                raise RuntimeError("invalid transition")
            conn.execute("UPDATE reviews SET status=? WHERE id=?", (ReviewStatus.APPROVED.value, rid))
            aid = _audit(conn, rid, "approved", {})
            conn.commit()
            return {"id": rid, "status": ReviewStatus.APPROVED.value, "audit_id": aid}
        finally:
            conn.close()

    def reject(self, rid: str, reason: str) -> dict:
        conn = self._conn()
        try:
            row = conn.execute("SELECT status FROM reviews WHERE id=?", (rid,)).fetchone()
            if row is None:
                raise KeyError("not found")
            if row["status"] != ReviewStatus.PENDING.value:
                _audit(conn, rid, "invalid_transition", {"attempt": "reject", "was": row["status"]})
                conn.commit()
                raise RuntimeError("invalid transition")
            conn.execute("UPDATE reviews SET status=? WHERE id=?", (ReviewStatus.REJECTED.value, rid))
            aid = _audit(conn, rid, "rejected", {"reason": reason})
            conn.commit()
            return {"id": rid, "status": ReviewStatus.REJECTED.value, "audit_id": aid}
        finally:
            conn.close()


def run_demo(scenario: str) -> None:
    store = ReviewStore()
    item = store.submit("Curated pattern draft", "experiments/review")
    print(f"  submitted: {item}")
    if scenario == "happy":
        result = store.approve(item["id"])
        print(f"  approved: {result}")
    elif scenario == "invalid-transition":
        store.approve(item["id"])
        try:
            store.approve(item["id"])
        except RuntimeError as exc:
            print(f"  fail-closed: {exc}")
    else:
        result = store.reject(item["id"], reason="quality insufficient")
        print(f"  rejected: {result}")


def run_fastapi_client(scenario: str) -> None:
    try:
        from fastapi import FastAPI, HTTPException
        import httpx
    except ImportError:
        print("  fastapi/httpx not installed — store demo validates governance")
        return

    store = ReviewStore()
    app = FastAPI(title="Review API (prototype)")

    @app.post("/submit")
    def submit(content: str, source: str) -> dict:
        try:
            return store.submit(content, source)
        except ValueError as exc:
            raise HTTPException(400, str(exc)) from exc

    @app.post("/review/{rid}/approve")
    def approve(rid: str) -> dict:
        try:
            return store.approve(rid)
        except KeyError:
            raise HTTPException(404, "not found") from None
        except RuntimeError as exc:
            raise HTTPException(409, str(exc)) from exc

    @app.post("/review/{rid}/reject")
    def reject(rid: str, reason: str = "unspecified") -> dict:
        try:
            return store.reject(rid, reason)
        except KeyError:
            raise HTTPException(404, "not found") from None
        except RuntimeError as exc:
            raise HTTPException(409, str(exc)) from exc

    import asyncio

    transport = httpx.ASGITransport(app=app)

    async def _http_demo() -> None:
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.post("/submit", params={"content": "API draft", "source": "http"})
            if r.status_code != 200:
                print(f"  POST /submit failed: {r.status_code} {r.text}")
                return
            print(f"  POST /submit -> {r.status_code} {r.json()}")
            rid = r.json()["id"]
            if scenario == "invalid-transition":
                await client.post(f"/review/{rid}/approve")
                r2 = await client.post(f"/review/{rid}/approve")
                print(f"  double approve -> {r2.status_code} {r2.json()}")
            else:
                r2 = await client.post(f"/review/{rid}/approve")
                print(f"  POST /approve -> {r2.status_code} {r2.json()}")

    asyncio.run(_http_demo())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="happy", choices=["happy", "reject", "invalid-transition"])
    parser.add_argument("--serve", action="store_true")
    args = parser.parse_args()

    print("=== FastAPI Review API (Phase 2.2) ===\n")

    if args.serve:
        try:
            import uvicorn
            from fastapi import FastAPI
        except ImportError:
            print("Install: pip install fastapi uvicorn")
            sys.exit(1)
        # Minimal serve uses same store — import app from inline build
        run_fastapi_client(args.scenario)
        print("\nFor --serve, use minimal-demo without --serve first to validate store.")
        return

    run_demo(args.scenario)
    print()
    run_fastapi_client(args.scenario)


if __name__ == "__main__":
    main()
