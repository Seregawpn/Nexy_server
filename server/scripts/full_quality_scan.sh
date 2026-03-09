#!/usr/bin/env bash
set -u

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
TARGET_DIR="${1:-server}"
REPORT_DIR="$ROOT_DIR/server/.reports"
TIMESTAMP="$(date +"%Y%m%d_%H%M%S")"
PYRIGHT_JSON="$REPORT_DIR/basedpyright_${TIMESTAMP}.json"
STATUS=0

mkdir -p "$REPORT_DIR"

step() {
  local title="$1"
  echo
  echo "[quality] $title"
}

fail_step() {
  local message="$1"
  echo "[quality][FAIL] $message"
  STATUS=1
}

step "Syntax check (compileall) for '$TARGET_DIR'"
if ! python3 -m compileall -q "$ROOT_DIR/$TARGET_DIR"; then
  fail_step "compileall reported syntax/import-bytecode errors"
fi

if [[ -x "$ROOT_DIR/.venv/bin/basedpyright" ]]; then
  step "Type check (basedpyright)"
  if ! "$ROOT_DIR/.venv/bin/basedpyright" --outputjson "$ROOT_DIR/$TARGET_DIR" > "$PYRIGHT_JSON"; then
    STATUS=1
  fi
elif command -v basedpyright >/dev/null 2>&1; then
  step "Type check (basedpyright)"
  if ! basedpyright --outputjson "$ROOT_DIR/$TARGET_DIR" > "$PYRIGHT_JSON"; then
    STATUS=1
  fi
else
  step "Type check (basedpyright)"
  echo "[quality] basedpyright not found, skipping type check"
  echo "[quality] install: pip install basedpyright"
fi

if [[ -f "$PYRIGHT_JSON" ]]; then
  step "Type-check summary"
  python3 "$ROOT_DIR/server/scripts/type_error_report.py" "$PYRIGHT_JSON" || STATUS=1
  echo "[quality] full json report: $PYRIGHT_JSON"
fi

step "Tests (pytest server/tests)"
if ! python3 -m pytest "$ROOT_DIR/server/tests" -q; then
  fail_step "pytest failed"
fi

echo
if [[ $STATUS -eq 0 ]]; then
  echo "[quality] All checks passed"
else
  echo "[quality] Checks completed with failures"
fi

exit "$STATUS"
