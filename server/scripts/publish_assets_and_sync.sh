#!/bin/bash
# Публикация DMG/PKG в фиксированные GitHub release теги и параллельная синхронизация версии на Azure.
#
# Usage:
#   ./server/scripts/publish_assets_and_sync.sh --dmg /path/Nexy.dmg --pkg /path/Nexy.pkg
#   ./server/scripts/publish_assets_and_sync.sh --dmg /path/Nexy.dmg --version 1.6.1.34

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO] $1${NC}"; }
log_warn() { echo -e "${YELLOW}[WARN] $1${NC}"; }
log_err() { echo -e "${RED}[ERR ] $1${NC}"; }
log_step() { echo -e "${BLUE}[STEP] $1${NC}"; }

usage() {
  cat <<USAGE
Usage: $0 [--dmg /abs/path/Nexy.dmg] [--pkg /abs/path/Nexy.pkg] [--version X.Y.Z.W] [--repo OWNER/REPO]
USAGE
}

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VERSION_FILE="$PROJECT_ROOT/VERSION"

DMG_PATH=""
PKG_PATH=""
REPO="Seregawpn/Nexy_production"
PUBLIC_HOST="nexy-server.canadacentral.cloudapp.azure.com"
AZURE_RESOURCE_GROUP="Nexy"
AZURE_VM_NAME="nexy-regular"
OVERRIDE_VERSION=""

while [ $# -gt 0 ]; do
  case "$1" in
    --dmg) DMG_PATH="${2:-}"; shift 2 ;;
    --pkg) PKG_PATH="${2:-}"; shift 2 ;;
    --version) OVERRIDE_VERSION="${2:-}"; shift 2 ;;
    --repo) REPO="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) log_err "Unknown argument: $1"; usage; exit 1 ;;
  esac
done

if [ -z "$DMG_PATH" ] && [ -z "$PKG_PATH" ]; then
  log_err "At least one asset must be provided: --dmg or --pkg"
  exit 1
fi

if [ -n "$DMG_PATH" ] && [ ! -f "$DMG_PATH" ]; then
  log_err "DMG not found: $DMG_PATH"
  exit 1
fi
if [ -n "$PKG_PATH" ] && [ ! -f "$PKG_PATH" ]; then
  log_err "PKG not found: $PKG_PATH"
  exit 1
fi

if [ -n "$OVERRIDE_VERSION" ]; then
  VERSION="$OVERRIDE_VERSION"
elif [ -f "$VERSION_FILE" ]; then
  VERSION="$(tr -d '\n\r ' < "$VERSION_FILE")"
else
  log_err "VERSION file not found: $VERSION_FILE"
  exit 1
fi

if ! echo "$VERSION" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$'; then
  log_err "Invalid version format: $VERSION (expected X.Y.Z.W)"
  exit 1
fi

command -v gh >/dev/null 2>&1 || { log_err "gh CLI not found"; exit 1; }
command -v az >/dev/null 2>&1 || { log_err "az CLI not found"; exit 1; }

if ! gh auth status >/dev/null 2>&1; then
  log_err "GitHub CLI is not authenticated (run: gh auth login)"
  exit 1
fi
if ! az account show >/dev/null 2>&1; then
  log_err "Azure CLI is not authenticated (run: az login)"
  exit 1
fi

ensure_release() {
  local tag="$1"
  local title="$2"
  if gh release view "$tag" --repo "$REPO" >/dev/null 2>&1; then
    return 0
  fi
  gh release create "$tag" --repo "$REPO" --title "$title" --notes "Managed by release automation"
}

upload_asset() {
  local tag="$1"
  local path="$2"
  ensure_release "$tag" "Nexy ${tag}"
  gh release upload "$tag" "$path" --repo "$REPO" --clobber
}

DMG_URL=""
DMG_SHA=""
DMG_SIZE=""

if [ -n "$DMG_PATH" ]; then
  if command -v sha256sum >/dev/null 2>&1; then
    DMG_SHA="$(sha256sum "$DMG_PATH" | awk '{print $1}')"
  else
    DMG_SHA="$(shasum -a 256 "$DMG_PATH" | awk '{print $1}')"
  fi
fi

log_info "Version source of truth: $VERSION"
log_info "Repo: $REPO"

log_step "Start Azure version sync in parallel"
"$SCRIPT_DIR/update_server_version.sh" "$VERSION" "$VERSION" > /tmp/nexy_publish_update_server_version.log 2>&1 &
SYNC_PID=$!

if [ -n "$DMG_PATH" ]; then
  log_step "Upload DMG to release tag Update"
  upload_asset "Update" "$DMG_PATH"
  DMG_FILE="$(basename "$DMG_PATH")"
  DMG_URL="https://github.com/${REPO}/releases/download/Update/${DMG_FILE}"
fi

if [ -n "$PKG_PATH" ]; then
  log_step "Upload PKG to release tag App"
  upload_asset "App" "$PKG_PATH"
fi

log_step "Wait for Azure version sync"
if ! wait "$SYNC_PID"; then
  log_err "Azure version sync failed"
  cat /tmp/nexy_publish_update_server_version.log || true
  exit 1
fi

if [ -n "$DMG_URL" ]; then
  log_step "Fetch actual GitHub CDN size for DMG"
  sleep 5
  DMG_SIZE="$(curl -sSLI "$DMG_URL" | awk '/[Cc]ontent-[Ll]ength:/ {gsub("\r", "", $2); print $2}' | tail -1)"
  if [ -z "$DMG_SIZE" ] || [ "$DMG_SIZE" = "0" ]; then
    log_err "Failed to fetch DMG content-length from GitHub CDN"
    exit 1
  fi

  log_step "Update remote manifests for DMG URL/version"
  az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "cd /home/azureuser/voice-assistant/server && python3 <<'PYEOF'
import json
from datetime import datetime, timezone
from pathlib import Path

manifests_dir = Path('updates/manifests')
manifests_dir.mkdir(parents=True, exist_ok=True)
manifest_current = manifests_dir / 'manifest.json'
manifest_versioned = manifests_dir / 'manifest_${VERSION}.json'

version = '${VERSION}'
download_url = '${DMG_URL}'
size = int('${DMG_SIZE}')
sha256 = '${DMG_SHA}'
now = datetime.now(timezone.utc).isoformat()

if manifest_current.exists():
    data = json.loads(manifest_current.read_text(encoding='utf-8'))
else:
    data = {
        'version': version,
        'build': version,
        'artifact': {
            'type': 'dmg',
            'url': download_url,
            'size': size,
            'sha256': sha256,
            'arch': 'universal2',
            'min_os': '11.0',
            'ed25519': ''
        },
        'critical': False,
        'auto_install': True,
        'notes_url': download_url,
    }

artifact = data.setdefault('artifact', {})
artifact['type'] = 'dmg'
artifact['url'] = download_url
artifact['size'] = size
artifact['sha256'] = sha256
artifact.setdefault('arch', 'universal2')
artifact.setdefault('min_os', '11.0')
artifact.setdefault('ed25519', '')

data['version'] = version
data['build'] = version
data['release_date'] = now
data['notes_url'] = download_url

txt = json.dumps(data, indent=2, ensure_ascii=False)
manifest_current.write_text(txt + '\\n', encoding='utf-8')
manifest_versioned.write_text(txt + '\\n', encoding='utf-8')
print('manifest synced')
PYEOF" >/tmp/nexy_publish_remote_manifest.log
fi

log_step "Validate update endpoints"
HEALTH_JSON="$(curl -sk "https://${PUBLIC_HOST}/updates/health" || true)"
APPCAST_XML="$(curl -sk "https://${PUBLIC_HOST}/updates/appcast.xml" || true)"

if [ -z "$HEALTH_JSON" ] || [ -z "$APPCAST_XML" ]; then
  log_err "Failed to fetch update endpoints"
  exit 1
fi

HEALTH_VERSION="$(printf '%s' "$HEALTH_JSON" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('latest_version',''))" 2>/dev/null || true)"
HEALTH_BUILD="$(printf '%s' "$HEALTH_JSON" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('latest_build',''))" 2>/dev/null || true)"
APPCAST_VERSION="$(printf '%s' "$APPCAST_XML" | grep -o 'sparkle:version=\"[^\"]*\"' | head -1 | cut -d'\"' -f2)"

if [ "$HEALTH_VERSION" != "$VERSION" ] || [ "$HEALTH_BUILD" != "$VERSION" ] || [ "$APPCAST_VERSION" != "$VERSION" ]; then
  log_err "Version mismatch after publish (health/appcast != VERSION)"
  exit 1
fi

echo
log_info "Publish completed"
if [ -n "$DMG_PATH" ]; then
  log_info "DMG: https://github.com/${REPO}/releases/download/Update/$(basename "$DMG_PATH")"
fi
if [ -n "$PKG_PATH" ]; then
  log_info "PKG: https://github.com/${REPO}/releases/download/App/$(basename "$PKG_PATH")"
fi
log_info "Version on server: $VERSION"

