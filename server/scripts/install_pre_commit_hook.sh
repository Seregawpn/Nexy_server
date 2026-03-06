#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
HOOK_PATH="$ROOT_DIR/.git/hooks/pre-commit"

if [[ ! -d "$ROOT_DIR/.git/hooks" ]]; then
  echo "[hook] .git/hooks not found at $ROOT_DIR"
  exit 1
fi

cat > "$HOOK_PATH" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
echo "[pre-commit] running server pre-commit gate..."
bash "$ROOT_DIR/server/scripts/pre_commit_gate.sh"
EOF

chmod +x "$HOOK_PATH"
echo "[hook] installed: $HOOK_PATH"
