#!/usr/bin/env bash
set -euo pipefail

# Fast one-VM runtime cutover for production ingress (:443):
# - target=staging: route :443 -> staging local ports (50061/8082/8083)
# - target=prod:    route :443 -> prod local ports (50051/8080/8081)
#
# The script is fail-closed:
# - validates target backend health before switch
# - applies nginx config change only inside listen 443 server block
# - runs nginx -t and reload
# - rolls back config on failure
#
# Usage:
#   bash server/server/scripts/cutover_runtime_backend.sh --to staging
#   bash server/server/scripts/cutover_runtime_backend.sh --to prod

RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
VM_NAME="${AZURE_VM_NAME:-NexyNew}"
PUBLIC_HOST="${PUBLIC_HOST:-nexy-prod-sergiy.canadacentral.cloudapp.azure.com}"
NGINX_FILE="${NGINX_FILE:-/etc/nginx/sites-enabled/nexy}"
TARGET=""
DRY_RUN=0

usage() {
  cat <<USAGE
Usage:
  $(basename "$0") --to <staging|prod> [options]

Options:
  --to TARGET           Required: staging|prod
  --resource-group RG   Azure resource group (default: NexyNewRG)
  --vm NAME             Azure VM name (default: NexyNew)
  --host HOST           Public host for post-check (default: nexy-prod-sergiy.canadacentral.cloudapp.azure.com)
  --nginx-file PATH     Remote nginx site file (default: /etc/nginx/sites-enabled/nexy)
  --dry-run             Validate flow without writing config/reloading nginx
  -h, --help            Show this help
USAGE
}

log() {
  printf '\n[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$1"
}

fail() {
  printf '\nERROR: %s\n' "$1" >&2
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --to)
      TARGET="${2:-}"
      shift 2
      ;;
    --resource-group)
      RESOURCE_GROUP="${2:-}"
      shift 2
      ;;
    --vm)
      VM_NAME="${2:-}"
      shift 2
      ;;
    --host)
      PUBLIC_HOST="${2:-}"
      shift 2
      ;;
    --nginx-file)
      NGINX_FILE="${2:-}"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      fail "Unknown argument: $1"
      ;;
  esac
done

case "$TARGET" in
  staging|prod) ;;
  *)
    fail "--to must be staging or prod"
    ;;
esac

if ! command -v az >/dev/null 2>&1; then
  fail "az CLI not found"
fi

az account show >/dev/null
az vm show --resource-group "$RESOURCE_GROUP" --name "$VM_NAME" -o table >/dev/null

log "Cutover request: target=$TARGET rg=$RESOURCE_GROUP vm=$VM_NAME host=$PUBLIC_HOST"

REMOTE_SCRIPT=$(cat <<EOF
set -euo pipefail

TARGET="$TARGET"
PUBLIC_HOST="$PUBLIC_HOST"
NGINX_FILE="$NGINX_FILE"
DRY_RUN="$DRY_RUN"
LOCK_DIR="/tmp/nexy-cutover.lockdir"
BACKUP_FILE=""

cleanup() {
  rm -rf "\$LOCK_DIR" >/dev/null 2>&1 || true
}
trap cleanup EXIT INT TERM

if ! mkdir "\$LOCK_DIR" 2>/dev/null; then
  echo "ERROR: another cutover is in progress (\$LOCK_DIR)" >&2
  exit 41
fi

if [ ! -f "\$NGINX_FILE" ]; then
  echo "ERROR: nginx file not found: \$NGINX_FILE" >&2
  exit 42
fi

if [ "\$TARGET" = "staging" ]; then
  systemctl is-active --quiet voice-assistant-staging || {
    echo "ERROR: voice-assistant-staging is not active" >&2
    exit 43
  }
  curl -fsS http://127.0.0.1:8082/health >/dev/null
  curl -fsS http://127.0.0.1:8083/health >/dev/null
else
  systemctl is-active --quiet voice-assistant || {
    echo "ERROR: voice-assistant is not active" >&2
    exit 44
  }
  curl -fsS http://127.0.0.1:8080/health >/dev/null
  curl -fsS http://127.0.0.1:8081/health >/dev/null
fi

if [ "\$DRY_RUN" = "1" ]; then
  echo "CUTOVER_DRY_RUN_OK target=\$TARGET"
  exit 0
fi

TS=\$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="\${NGINX_FILE}.cutover.\${TS}.bak"
cp "\$NGINX_FILE" "\$BACKUP_FILE"

rollback() {
  if [ -n "\$BACKUP_FILE" ] && [ -f "\$BACKUP_FILE" ]; then
    cp "\$BACKUP_FILE" "\$NGINX_FILE"
    nginx -t >/dev/null 2>&1 && systemctl reload nginx >/dev/null 2>&1 || true
  fi
}

python3 - "\$NGINX_FILE" "\$TARGET" <<'PY'
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
target = sys.argv[2]
text = path.read_text(encoding="utf-8")
lines = text.splitlines(keepends=True)

if target == "staging":
    mapping = {
        "127.0.0.1:50051": "127.0.0.1:50061",
        "127.0.0.1:8080": "127.0.0.1:8082",
        "127.0.0.1:8081": "127.0.0.1:8083",
    }
elif target == "prod":
    mapping = {
        "127.0.0.1:50061": "127.0.0.1:50051",
        "127.0.0.1:8082": "127.0.0.1:8080",
        "127.0.0.1:8083": "127.0.0.1:8081",
    }
else:
    raise SystemExit(f"unsupported target: {target}")

blocks: list[tuple[int, int]] = []
depth = 0
in_server = False
start = -1
contains_443 = False

for i, line in enumerate(lines):
    if not in_server and re.match(r"^\s*server\s*\{", line):
        in_server = True
        start = i
        depth = line.count("{") - line.count("}")
        contains_443 = bool(re.search(r"\blisten\s+443\b", line))
        if depth == 0:
            in_server = False
            if contains_443:
                blocks.append((start, i))
        continue
    if in_server:
        if re.search(r"\blisten\s+443\b", line):
            contains_443 = True
        depth += line.count("{") - line.count("}")
        if depth == 0:
            in_server = False
            if contains_443:
                blocks.append((start, i))

if not blocks:
    raise SystemExit("listen 443 server block not found")

changed = False
for start_i, end_i in blocks:
    segment = lines[start_i:end_i + 1]
    patched: list[str] = []
    for ln in segment:
        updated = ln
        for old, new in mapping.items():
            updated = updated.replace(old, new)
        patched.append(updated)
    if patched != segment:
        lines[start_i:end_i + 1] = patched
        changed = True

if changed:
    path.write_text("".join(lines), encoding="utf-8")
    print(f"PATCHED target={target}")
else:
    print(f"NOOP target={target}")
PY

if ! nginx -t; then
  echo "ERROR: nginx -t failed, rollback" >&2
  rollback
  exit 45
fi

if ! systemctl reload nginx; then
  echo "ERROR: nginx reload failed, rollback" >&2
  rollback
  exit 46
fi

if ! curl -kfsS https://127.0.0.1/health -H "Host: \$PUBLIC_HOST" >/dev/null; then
  echo "ERROR: post-check /health failed, rollback" >&2
  rollback
  exit 47
fi

if ! curl -kfsS https://127.0.0.1/updates/health -H "Host: \$PUBLIC_HOST" >/dev/null; then
  echo "ERROR: post-check /updates/health failed, rollback" >&2
  rollback
  exit 48
fi

echo "CUTOVER_OK target=\$TARGET backup=\$BACKUP_FILE"
EOF
)

az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "$REMOTE_SCRIPT" >/dev/null

if [[ "$DRY_RUN" -eq 1 ]]; then
  log "Remote dry-run completed"
  exit 0
fi

log "Running external post-checks on https://$PUBLIC_HOST"
curl -fsS "https://$PUBLIC_HOST/health" >/dev/null
curl -fsS "https://$PUBLIC_HOST/updates/health" >/dev/null
python3 server/server/scripts/grpc_smoke.py "$PUBLIC_HOST" 443 >/dev/null

log "CUTOVER COMPLETE target=$TARGET"

