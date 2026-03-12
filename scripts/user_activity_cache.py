#!/usr/bin/env python3
"""
Local cache for production user activity (requests + answers).

Why:
- Fetching from Azure VM with `az vm run-command` is slow.
- This script stores a local SQLite snapshot, then reads instantly.

Usage:
  python3 server/scripts/user_activity_cache.py refresh
  python3 server/scripts/user_activity_cache.py stats
  python3 server/scripts/user_activity_cache.py list --limit 50
  python3 server/scripts/user_activity_cache.py list --hardware-id <HWID> --limit 200
"""

from __future__ import annotations

import argparse
import datetime as dt
import sqlite3
import subprocess
import sys
from pathlib import Path
from typing import Iterable, List


DEFAULT_RG = "NexyNewRG"
DEFAULT_VM = "NexyNew"
DEFAULT_OUT = Path("monitor_inbox/user_activity_cache.sqlite")
CHUNK_SIZE = 10


def _run(cmd: List[str]) -> str:
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        raise RuntimeError(
            f"Command failed ({proc.returncode}): {' '.join(cmd)}\n"
            f"stdout:\n{proc.stdout}\n"
            f"stderr:\n{proc.stderr}"
        )
    return proc.stdout


def _az_run_sql(resource_group: str, vm_name: str, sql: str) -> str:
    remote_script = f"""set -eu
cd /home/azureuser/voice-assistant
if [ -f config.env ]; then set -a; . ./config.env; set +a; fi
export PGPASSWORD="${{DB_PASSWORD:-}}"
psql -h "${{DB_HOST:-localhost}}" -p "${{DB_PORT:-5432}}" -U "${{DB_USER:-voice_assistant}}" -d "${{DB_NAME:-voice_assistant_db}}" -At -F '|' -c "{sql}"
"""
    cmd = [
        "az",
        "vm",
        "run-command",
        "invoke",
        "--resource-group",
        resource_group,
        "--name",
        vm_name,
        "--command-id",
        "RunShellScript",
        "--query",
        "value[0].message",
        "-o",
        "tsv",
        "--scripts",
        remote_script,
    ]
    message = _run(cmd)
    lines = message.splitlines()
    out_lines: List[str] = []
    in_stdout = False
    for line in lines:
        if line.strip() == "[stdout]":
            in_stdout = True
            continue
        if line.strip() == "[stderr]":
            break
        if in_stdout:
            out_lines.append(line)
    return "\n".join(out_lines).strip()


def _parse_rows(raw: str) -> Iterable[List[str]]:
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 6:
            continue
        yield parts[:6]


def _connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS cache_meta (
          key TEXT PRIMARY KEY,
          value TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS activity (
          rn INTEGER PRIMARY KEY,
          hardware_id_hash TEXT NOT NULL,
          request_created_at TEXT NOT NULL,
          prompt TEXT NOT NULL,
          answer_created_at TEXT,
          answer TEXT
        )
        """
    )
    return conn


def refresh_cache(resource_group: str, vm_name: str, db_path: Path) -> None:
    total_sql = (
        "SELECT COUNT(*) "
        "FROM commands c "
        "JOIN sessions s ON s.id = c.session_id "
        "JOIN users u ON u.id = s.user_id"
    )
    total_raw = _az_run_sql(resource_group, vm_name, total_sql)
    if not total_raw.strip().isdigit():
        raise RuntimeError(f"Cannot parse total rows from remote output: {total_raw!r}")
    total = int(total_raw.strip())

    conn = _connect(db_path)
    with conn:
        conn.execute("DELETE FROM activity")

    for start in range(1, total + 1, CHUNK_SIZE):
        end = min(start + CHUNK_SIZE - 1, total)
        sql = f"""
WITH ordered AS (
  SELECT
    row_number() OVER (ORDER BY c.created_at, c.id) AS rn,
    c.id AS command_id,
    u.hardware_id_hash,
    c.created_at,
    regexp_replace(c.prompt, E'[\\n\\r\\t]+', ' ', 'g') AS prompt
  FROM commands c
  JOIN sessions s ON s.id = c.session_id
  JOIN users u ON u.id = s.user_id
),
joined AS (
  SELECT
    o.rn,
    o.hardware_id_hash,
    o.created_at,
    o.prompt,
    COALESCE(a.created_at::text, '') AS answer_created_at,
    COALESCE(regexp_replace(a.response, E'[\\n\\r\\t]+', ' ', 'g'), '') AS answer
  FROM ordered o
  LEFT JOIN LATERAL (
    SELECT response, created_at
    FROM llm_answers la
    WHERE la.command_id = o.command_id
    ORDER BY la.created_at DESC
    LIMIT 1
  ) a ON true
  WHERE o.rn BETWEEN {start} AND {end}
)
SELECT
  rn::text,
  hardware_id_hash,
  created_at::text,
  prompt,
  answer_created_at,
  answer
FROM joined
ORDER BY rn
"""
        raw = _az_run_sql(resource_group, vm_name, " ".join(sql.split()))
        rows = list(_parse_rows(raw))
        with conn:
            conn.executemany(
                """
                INSERT OR REPLACE INTO activity
                (rn, hardware_id_hash, request_created_at, prompt, answer_created_at, answer)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                rows,
            )
        print(f"cached rows {start}-{end}")

    now = dt.datetime.now(dt.timezone.utc).isoformat()
    with conn:
        conn.execute(
            "INSERT OR REPLACE INTO cache_meta(key, value) VALUES ('last_refresh_utc', ?)",
            (now,),
        )
        conn.execute(
            "INSERT OR REPLACE INTO cache_meta(key, value) VALUES ('total_rows', ?)",
            (str(total),),
        )
    conn.close()
    print(f"refresh complete: total_rows={total}, cache={db_path}")


def print_stats(db_path: Path) -> None:
    conn = _connect(db_path)
    row_count = conn.execute("SELECT COUNT(*) FROM activity").fetchone()[0]
    last_refresh = conn.execute(
        "SELECT value FROM cache_meta WHERE key='last_refresh_utc'"
    ).fetchone()
    print(f"cache={db_path}")
    print(f"rows={row_count}")
    print(f"last_refresh_utc={last_refresh[0] if last_refresh else 'never'}")
    conn.close()


def list_rows(db_path: Path, limit: int, hardware_id: str | None) -> None:
    conn = _connect(db_path)
    if hardware_id:
        rows = conn.execute(
            """
            SELECT rn, hardware_id_hash, request_created_at, prompt, answer_created_at, answer
            FROM activity
            WHERE hardware_id_hash = ?
            ORDER BY rn DESC
            LIMIT ?
            """,
            (hardware_id, limit),
        ).fetchall()
    else:
        rows = conn.execute(
            """
            SELECT rn, hardware_id_hash, request_created_at, prompt, answer_created_at, answer
            FROM activity
            ORDER BY rn DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    conn.close()

    print("rn | hardware_id_hash | request_created_at | prompt | answer_created_at | answer")
    for r in rows:
        print(" | ".join(str(x or "") for x in r))


def main() -> int:
    parser = argparse.ArgumentParser(description="Cache and query user requests+answers fast.")
    parser.add_argument("--resource-group", default=DEFAULT_RG)
    parser.add_argument("--vm-name", default=DEFAULT_VM)
    parser.add_argument("--db-path", default=str(DEFAULT_OUT))
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("refresh")
    sub.add_parser("stats")

    list_parser = sub.add_parser("list")
    list_parser.add_argument("--limit", type=int, default=100)
    list_parser.add_argument("--hardware-id", default=None)

    args = parser.parse_args()
    db_path = Path(args.db_path)

    if args.cmd == "refresh":
        refresh_cache(args.resource_group, args.vm_name, db_path)
    elif args.cmd == "stats":
        print_stats(db_path)
    elif args.cmd == "list":
        list_rows(db_path, args.limit, args.hardware_id)
    else:
        parser.print_help()
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
