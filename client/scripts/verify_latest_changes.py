#!/usr/bin/env python3
"""Enforce updates to Docs/LATEST_CHANGES.md for local client changes."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LATEST_CHANGES_PATH = ROOT / "Docs" / "LATEST_CHANGES.md"
CLIENT_PREFIX = "client/"

IGNORE_EXACT = {
    "Docs/LATEST_CHANGES.md",
    ".DS_Store",
}
IGNORE_PREFIXES = (
    "Docs/assistant_exchange/",
    "build_logs/",
)


def _run_git_status() -> list[str]:
    proc = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.rstrip("\n") for line in proc.stdout.splitlines() if line.strip()]


def _extract_path(status_line: str) -> str:
    # porcelain v1: "XY path" or "XY old -> new"
    raw = status_line[3:] if len(status_line) > 3 else ""
    if " -> " in raw:
        raw = raw.split(" -> ", 1)[1]
    return raw.strip()


def _is_relevant_client_path(path: str) -> bool:
    if not path or path.startswith("../"):
        return False
    if path in IGNORE_EXACT:
        return False
    if any(path.startswith(prefix) for prefix in IGNORE_PREFIXES):
        return False
    return True


def _normalize_repo_path(path: str) -> str:
    p = path.strip()
    if p.startswith(CLIENT_PREFIX):
        return p[len(CLIENT_PREFIX) :]
    return p


def _has_non_empty_latest_changes_entry(text: str) -> bool:
    section_match = re.search(
        r"## Изменения текущего цикла\s*(.*?)(?:\n## |\Z)",
        text,
        flags=re.DOTALL,
    )
    if not section_match:
        return False
    body = section_match.group(1)
    bullets = [line.strip() for line in body.splitlines() if line.strip().startswith("- ")]
    if not bullets:
        return False
    for bullet in bullets:
        normalized = bullet.lower()
        if "(пусто)" in normalized or "todo" in normalized:
            continue
        return True
    return False


def main() -> int:
    if not LATEST_CHANGES_PATH.exists():
        print("ERROR: Docs/LATEST_CHANGES.md не найден")
        return 1

    status_lines = _run_git_status()
    changed_paths_raw = [_extract_path(line) for line in status_lines]
    changed_paths = [_normalize_repo_path(p) for p in changed_paths_raw]
    relevant_paths = sorted({p for p in changed_paths if _is_relevant_client_path(p)})
    latest_changes_updated = "Docs/LATEST_CHANGES.md" in changed_paths

    text = LATEST_CHANGES_PATH.read_text(encoding="utf-8", errors="ignore")

    if relevant_paths and not latest_changes_updated:
        print("ERROR: Обнаружены изменения, но Docs/LATEST_CHANGES.md не обновлен.")
        print("Измененные пути (требуют запись в Latest Changes):")
        for path in relevant_paths[:30]:
            print(f"  - {path}")
        return 1

    if relevant_paths and not _has_non_empty_latest_changes_entry(text):
        print("ERROR: Docs/LATEST_CHANGES.md обновлен, но раздел изменений пуст.")
        print("Добавьте минимум одну запись в раздел 'Изменения текущего цикла'.")
        return 1

    print("Latest changes guard OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
