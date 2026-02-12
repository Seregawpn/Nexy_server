#!/bin/bash
set -euo pipefail

# Run consolidated scan and fail if at least one issue is found.
./scripts/problem_scan.sh "$@"

SCAN_SUMMARY="$(./.venv/bin/python - <<'PY'
import json
from pathlib import Path

path = Path("build_logs/problem_scan_latest.json")
if not path.exists():
    print("-1|-1|missing")
    raise SystemExit(0)

data = json.loads(path.read_text(encoding="utf-8"))
summary = data.get("summary", {})
total = int(summary.get("total_issues", 0))
blocking = int(summary.get("blocking_issues", total))
basedpyright_status = str(summary.get("basedpyright_status", "unknown"))
print(f"{total}|{blocking}|{basedpyright_status}")
PY
)"

TOTAL_ISSUES="$(echo "$SCAN_SUMMARY" | cut -d'|' -f1)"
BLOCKING_ISSUES="$(echo "$SCAN_SUMMARY" | cut -d'|' -f2)"
BASEDPYRIGHT_STATUS="$(echo "$SCAN_SUMMARY" | cut -d'|' -f3)"

if [ "$TOTAL_ISSUES" -lt 0 ] || [ "$BLOCKING_ISSUES" -lt 0 ]; then
  echo "[ERROR] problem scan report not found"
  exit 1
fi

REQUIRE_BASEDPYRIGHT_IN_SCAN="${REQUIRE_BASEDPYRIGHT_IN_SCAN:-true}"
if [ "$REQUIRE_BASEDPYRIGHT_IN_SCAN" = "true" ] && [ "$BASEDPYRIGHT_STATUS" != "ok" ]; then
  echo "[ERROR] basedpyright scan is required but status is '$BASEDPYRIGHT_STATUS'"
  exit 1
fi

if [ "$BLOCKING_ISSUES" -gt 0 ]; then
  echo "[ERROR] problem scan found $BLOCKING_ISSUES blocking issue(s) (total: $TOTAL_ISSUES)"
  exit 1
fi

echo "[INFO] problem scan gate passed (blocking: 0, total: $TOTAL_ISSUES)"
