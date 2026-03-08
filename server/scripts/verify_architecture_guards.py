#!/usr/bin/env python3
"""Architecture guard rails for server CI."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

import yaml

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_DIRS = (
    ROOT / "server" / "modules",
    ROOT / "server" / "integrations",
    ROOT / "server" / "api",
)
RUNTIME_FILES = (ROOT / "server" / "main.py",)
FEATURE_FLAGS_MD = ROOT / "server" / "Docs" / "FEATURE_FLAGS.md"
UNIFIED_CONFIG_YAML = ROOT / "server" / "config" / "unified_config.yaml"

CRITICAL_EVENT_OWNERS = {
    "mcp.command_request": "server/integrations/core/assistant_response_parser.py",
}

EVENT_LITERAL_RE = re.compile(r"""["']event["']\s*:\s*["']([a-zA-Z0-9_.-]+)["']""")
FEATURE_ACCESS_RE = re.compile(r"""\b(?:[A-Za-z_][A-Za-z0-9_]*\.)*features\.([a-zA-Z_][a-zA-Z0-9_]*)\b""")
KILL_SWITCH_ACCESS_RE = re.compile(r"""\b(?:[A-Za-z_][A-Za-z0-9_]*\.)*kill_switches\.([a-zA-Z_][a-zA-Z0-9_]*)\b""")
IS_FEATURE_ENABLED_RE = re.compile(r"""is_feature_enabled\(\s*["']([a-zA-Z_][a-zA-Z0-9_]*)["']\s*\)""")
IS_KS_ACTIVE_RE = re.compile(r"""is_kill_switch_active\(\s*["']([a-zA-Z_][a-zA-Z0-9_]*)["']\s*\)""")


def _iter_runtime_py_files() -> Iterable[Path]:
    for runtime_dir in RUNTIME_DIRS:
        if runtime_dir.exists():
            yield from runtime_dir.rglob("*.py")
    for runtime_file in RUNTIME_FILES:
        if runtime_file.exists():
            yield runtime_file


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _parse_registry_flags() -> set[str]:
    if not FEATURE_FLAGS_MD.exists():
        return set()
    flags: set[str] = set()
    for line in FEATURE_FLAGS_MD.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        match = re.match(r"^\|\s*`?([A-Za-z_][A-Za-z0-9_]*)`?\s*\|", line)
        if match:
            flags.add(match.group(1))
    return flags


def _parse_declared_runtime_flags() -> tuple[set[str], set[str]]:
    if not UNIFIED_CONFIG_YAML.exists():
        return set(), set()
    data = yaml.safe_load(UNIFIED_CONFIG_YAML.read_text(encoding="utf-8")) or {}
    features = set((data.get("features") or {}).keys())
    kill_switches = set((data.get("kill_switches") or {}).keys())
    return features, kill_switches


def _read_event_payload() -> dict:
    event_path = os.getenv("GITHUB_EVENT_PATH", "")
    if not event_path:
        return {}
    path = Path(event_path)
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _resolve_diff_range() -> str:
    event_name = os.getenv("GITHUB_EVENT_NAME", "")
    if event_name == "pull_request":
        payload = _read_event_payload()
        pr = payload.get("pull_request") or {}
        base_sha = (pr.get("base") or {}).get("sha")
        head_sha = (pr.get("head") or {}).get("sha")
        if base_sha and head_sha:
            return f"{base_sha}..{head_sha}"
    return "HEAD~1..HEAD"


def _collect_added_lines() -> dict[str, list[tuple[int, str]]]:
    diff_range = _resolve_diff_range()
    cmd = ["git", "diff", "--unified=0", "--no-color", diff_range]
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if proc.returncode != 0:
        return {}

    added: dict[str, list[tuple[int, str]]] = {}
    current_file: str | None = None
    new_line_no = 0

    for raw_line in proc.stdout.splitlines():
        line = raw_line.rstrip("\n")
        if line.startswith("+++ b/"):
            current_file = line[len("+++ b/") :]
            continue
        if line.startswith("@@"):
            # Example: @@ -10,0 +11,4 @@
            match = re.search(r"\+(\d+)", line)
            if match:
                new_line_no = int(match.group(1))
            continue
        if current_file is None:
            continue
        if line.startswith("+") and not line.startswith("+++"):
            added.setdefault(current_file, []).append((new_line_no, line[1:]))
            new_line_no += 1
        elif line.startswith("-") and not line.startswith("---"):
            continue
        else:
            new_line_no += 1
    return added


def _is_runtime_python(path: str) -> bool:
    if not path.endswith(".py"):
        return False
    return (
        path.startswith("server/modules/")
        or path.startswith("server/integrations/")
        or path.startswith("server/api/")
        or path == "server/main.py"
    )


def _check_diff_guards(added_lines: dict[str, list[tuple[int, str]]]) -> list[str]:
    errors: list[str] = []
    for rel_path, lines in added_lines.items():
        for line_no, line in lines:
            stripped = line.strip()
            if "sys.path.insert(" in line and _is_runtime_python(rel_path):
                errors.append(
                    f"{rel_path}:{line_no} запрещен новый sys.path.insert в runtime (entrypoint-only rule)"
                )

            lower = stripped.lower()
            if not _is_runtime_python(rel_path):
                continue
            if "legacy" in lower:
                if "legacy_remove_by:" not in lower:
                    errors.append(
                        f"{rel_path}:{line_no} legacy-path без срока удаления "
                        "(добавьте LEGACY_REMOVE_BY: YYYY-MM-DD)"
                    )
    return errors


def _collect_newly_declared_flags(
    added_lines: dict[str, list[tuple[int, str]]],
    declared_features: set[str],
    declared_kill_switches: set[str],
) -> tuple[set[str], set[str]]:
    new_features: set[str] = set()
    new_kill_switches: set[str] = set()
    for rel_path, lines in added_lines.items():
        if rel_path != "server/config/unified_config.yaml":
            continue
        for _line_no, line in lines:
            match = re.match(r"^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*", line)
            if not match:
                continue
            key = match.group(1)
            if key in declared_features:
                new_features.add(key)
            if key in declared_kill_switches:
                new_kill_switches.add(key)
    return new_features, new_kill_switches


def _check_flag_usage(added_lines: dict[str, list[tuple[int, str]]]) -> list[str]:
    errors: list[str] = []
    features, kill_switches = _parse_declared_runtime_flags()
    registry_flags = _parse_registry_flags()

    runtime_contents: dict[str, str] = {}
    for file_path in _iter_runtime_py_files():
        runtime_contents[_relative(file_path)] = file_path.read_text(encoding="utf-8")

    runtime_blob = "\n".join(runtime_contents.values())
    new_features, new_kill_switches = _collect_newly_declared_flags(
        added_lines, features, kill_switches
    )

    for feature in sorted(new_features):
        patterns = (
            rf"\bfeatures\.{re.escape(feature)}\b",
            rf"is_feature_enabled\(\s*['\"]{re.escape(feature)}['\"]\s*\)",
        )
        if not any(re.search(pattern, runtime_blob) for pattern in patterns):
            errors.append(f"dead flag: features.{feature} объявлен, но не используется в runtime")

    for kill_switch in sorted(new_kill_switches):
        patterns = (
            rf"\bkill_switches\.{re.escape(kill_switch)}\b",
            rf"is_kill_switch_active\(\s*['\"]{re.escape(kill_switch)}['\"]\s*\)",
        )
        if not any(re.search(pattern, runtime_blob) for pattern in patterns):
            errors.append(
                f"dead flag: kill_switches.{kill_switch} объявлен, но не используется в runtime"
            )

    used_runtime_flags: set[str] = set()
    for rel_path, lines in added_lines.items():
        if not _is_runtime_python(rel_path):
            continue
        for _line_no, line in lines:
            used_runtime_flags.update(FEATURE_ACCESS_RE.findall(line))
            used_runtime_flags.update(KILL_SWITCH_ACCESS_RE.findall(line))
            used_runtime_flags.update(IS_FEATURE_ENABLED_RE.findall(line))
            used_runtime_flags.update(IS_KS_ACTIVE_RE.findall(line))

    for flag_name in sorted(used_runtime_flags):
        if flag_name in features or flag_name in kill_switches:
            if flag_name not in registry_flags:
                errors.append(
                    f"undocumented runtime flag: {flag_name} используется в runtime, но отсутствует в FEATURE_FLAGS.md"
                )
        elif flag_name.startswith("use_") or flag_name.startswith("disable_"):
            errors.append(
                f"undocumented runtime flag: {flag_name} используется в runtime, но отсутствует в FEATURE_FLAGS.md"
            )
    return errors


def _check_event_owners() -> list[str]:
    errors: list[str] = []
    publishers: dict[str, set[str]] = {event: set() for event in CRITICAL_EVENT_OWNERS}

    for file_path in _iter_runtime_py_files():
        rel_path = _relative(file_path)
        for raw_line in file_path.read_text(encoding="utf-8").splitlines():
            stripped = raw_line.strip()
            if stripped.startswith("#"):
                continue
            for match in EVENT_LITERAL_RE.finditer(raw_line):
                event_name = match.group(1)
                if event_name in publishers:
                    publishers[event_name].add(rel_path)

    for event_name, owner_path in CRITICAL_EVENT_OWNERS.items():
        found = publishers.get(event_name, set())
        if not found:
            errors.append(f"critical event '{event_name}' не публикуется в runtime")
            continue
        if found != {owner_path}:
            offenders = ", ".join(sorted(found))
            errors.append(
                f"event-owner violation: '{event_name}' должен публиковаться только в {owner_path}, найдено: {offenders}"
            )
    return errors


def main() -> int:
    added_lines = _collect_added_lines()
    errors: list[str] = []
    errors.extend(_check_diff_guards(added_lines))
    errors.extend(_check_flag_usage(added_lines))
    errors.extend(_check_event_owners())

    if errors:
        print("[arch-guards] FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("[arch-guards] OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
