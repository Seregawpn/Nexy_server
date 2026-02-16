#!/usr/bin/env python3
"""
One-time admin script: mark existing users as grandfathered (free unlimited).

Default mode is dry-run. Use --apply to execute updates.
"""

import argparse
import os
import sys
from datetime import datetime
from typing import List, Dict

from psycopg2.extras import RealDictCursor


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Grant 'grandfathered' status to existing users up to a cutoff date."
    )
    parser.add_argument(
        "--cutoff-date",
        required=True,
        help="Cutoff date in YYYY-MM-DD format (inclusive).",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply changes. Without this flag script only prints dry-run preview.",
    )
    parser.add_argument(
        "--limit-preview",
        type=int,
        default=20,
        help="How many rows to print in preview (default: 20).",
    )
    return parser.parse_args()


def _bootstrap_imports() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    server_pkg_dir = os.path.join(current_dir, "server")
    if server_pkg_dir not in sys.path:
        sys.path.append(server_pkg_dir)


def _parse_cutoff(cutoff_date: str) -> datetime:
    try:
        day = datetime.strptime(cutoff_date, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("Invalid --cutoff-date. Use YYYY-MM-DD.") from exc

    # Inclusive end-of-day cutoff
    return day.replace(hour=23, minute=59, second=59, microsecond=999999)


def _fetch_candidates(conn, cutoff_dt: datetime, preview_limit: int) -> List[Dict]:
    query = """
        SELECT hardware_id, status, created_at
        FROM subscriptions
        WHERE created_at <= %s
          AND status NOT IN ('grandfathered', 'admin_active')
        ORDER BY created_at ASC
        LIMIT %s
    """
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(query, (cutoff_dt, preview_limit))
        rows = cur.fetchall() or []
    return [dict(r) for r in rows]


def _count_candidates(conn, cutoff_dt: datetime) -> int:
    query = """
        SELECT COUNT(*) AS cnt
        FROM subscriptions
        WHERE created_at <= %s
          AND status NOT IN ('grandfathered', 'admin_active')
    """
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(query, (cutoff_dt,))
        row = cur.fetchone() or {"cnt": 0}
    return int(row["cnt"])


def _apply_updates(conn, cutoff_dt: datetime) -> int:
    query = """
        UPDATE subscriptions
        SET status = 'grandfathered',
            updated_at = CURRENT_TIMESTAMP
        WHERE created_at <= %s
          AND status NOT IN ('grandfathered', 'admin_active')
    """
    with conn.cursor() as cur:
        cur.execute(query, (cutoff_dt,))
        updated = cur.rowcount
    conn.commit()
    return int(updated)


def main() -> int:
    args = _parse_args()
    cutoff_dt = _parse_cutoff(args.cutoff_date)
    _bootstrap_imports()

    from server.modules.subscription.repository.subscription_repository import SubscriptionRepository

    repo = SubscriptionRepository()
    conn = repo._get_connection()
    try:
        total = _count_candidates(conn, cutoff_dt)
        preview = _fetch_candidates(conn, cutoff_dt, args.limit_preview)

        print(f"Cutoff (inclusive): {cutoff_dt.isoformat()}")
        print(f"Candidates to grandfather: {total}")
        print("Preview:")
        for row in preview:
            hid = row.get("hardware_id", "")
            status = row.get("status")
            created_at = row.get("created_at")
            print(f"  - hardware_id={hid} status={status} created_at={created_at}")

        if not args.apply:
            print("\nDry-run mode. No changes were made.")
            print("Run with --apply to execute.")
            return 0

        updated = _apply_updates(conn, cutoff_dt)
        print(f"\nApplied: updated {updated} subscription(s) to status='grandfathered'.")
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
