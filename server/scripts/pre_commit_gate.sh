#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
POLICY_PATH="$ROOT_DIR/server/config/test_gate_policy.yaml"

STAGED_FILES="$(git -C "$ROOT_DIR" diff --cached --name-only --diff-filter=ACMR)"
STAGED_SERVER_PY="$(printf '%s\n' "$STAGED_FILES" | grep -E '^server/.*\.py$' || true)"

if [[ -z "$STAGED_SERVER_PY" ]]; then
  echo "[pre-commit] no staged Python files in server/, skipping gate"
  exit 0
fi

echo "[pre-commit] syntax check for staged server python files"
python3 - <<'PY' "$ROOT_DIR" "$STAGED_SERVER_PY"
import py_compile
import sys
from pathlib import Path

root = Path(sys.argv[1])
files = [line for line in sys.argv[2].splitlines() if line.strip()]

for rel in files:
    path = root / rel
    py_compile.compile(str(path), doraise=True)
    print(f"[pre-commit] ok: {rel}")
PY

if [[ -x "$ROOT_DIR/.venv/bin/basedpyright" ]]; then
  echo "[pre-commit] basedpyright on staged files"
  "$ROOT_DIR/.venv/bin/basedpyright" $(printf '%s\n' "$STAGED_SERVER_PY")
elif command -v basedpyright >/dev/null 2>&1; then
  echo "[pre-commit] basedpyright on staged files"
  basedpyright $(printf '%s\n' "$STAGED_SERVER_PY")
else
  echo "[pre-commit] basedpyright not found, skip type check"
fi

echo "[pre-commit] collecting relevant pytest targets"
PYTEST_TARGETS="$(python3 - <<'PY' "$ROOT_DIR" "$STAGED_SERVER_PY" "$POLICY_PATH"
from pathlib import Path
import sys
from typing import Any

root = Path(sys.argv[1])
staged = [line.strip() for line in sys.argv[2].splitlines() if line.strip()]
policy_path = Path(sys.argv[3])
tests_root = root / "server" / "tests"

selected: set[str] = set()
require_full_suite = False

critical_test_map: dict[str, list[str]] = {}
critical_full_suite_patterns: list[str] = []

def _load_policy(path: Path) -> tuple[dict[str, list[str]], list[str]]:
    if not path.exists():
        print(f"[pre-commit] policy not found: {path}, using defaults", file=sys.stderr)
        return {}, []
    try:
        import yaml
    except Exception:
        print("[pre-commit] PyYAML not available, using defaults", file=sys.stderr)
        return {}, []
    raw: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    raw_map = raw.get("critical_test_map", {})
    raw_full = raw.get("critical_full_suite_patterns", [])
    parsed_map: dict[str, list[str]] = {}
    if isinstance(raw_map, dict):
        for key, value in raw_map.items():
            if not isinstance(key, str) or not isinstance(value, list):
                continue
            parsed_map[key] = [item for item in value if isinstance(item, str)]
    parsed_full: list[str] = []
    if isinstance(raw_full, list):
        parsed_full = [item for item in raw_full if isinstance(item, str)]
    return parsed_map, parsed_full

critical_test_map, critical_full_suite_patterns = _load_policy(policy_path)

for rel in staged:
    if rel.startswith("server/tests/") and rel.endswith(".py"):
        selected.add(str(root / rel))

for rel in staged:
    if not rel.startswith("server/") or rel.startswith("server/tests/") or not rel.endswith(".py"):
        continue
    stem = Path(rel).stem
    direct = tests_root / f"test_{stem}.py"
    if direct.exists():
        selected.add(str(direct))
    for candidate in tests_root.glob(f"test_*{stem}*.py"):
        selected.add(str(candidate))

for rel in staged:
    for pattern, test_files in critical_test_map.items():
        if pattern in rel:
            for test_file in test_files:
                path = tests_root / test_file
                if path.exists():
                    selected.add(str(path))
    if any(pattern in rel for pattern in critical_full_suite_patterns):
        require_full_suite = True

if require_full_suite:
    print("__FULL_SUITE__")
elif selected:
    for path in sorted(selected):
        print(path)
PY
)"

if [[ "$PYTEST_TARGETS" == *"__FULL_SUITE__"* ]]; then
  echo "[pre-commit] critical path changed, running full server test suite"
  python3 -m pytest "$ROOT_DIR/server/tests" -q --maxfail=1
elif [[ -n "$PYTEST_TARGETS" ]]; then
  echo "[pre-commit] pytest targeted gate"
  python3 -m pytest -q --maxfail=1 $(printf '%s\n' "$PYTEST_TARGETS")
else
  echo "[pre-commit] no matched targeted tests, running full server test suite"
  python3 -m pytest "$ROOT_DIR/server/tests" -q --maxfail=1
fi

echo "[pre-commit] gate passed"
