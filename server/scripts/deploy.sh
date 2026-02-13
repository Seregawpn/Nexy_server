#!/bin/bash
# Единый деплой обновления: GitHub release + синхронизация версии на Azure.
# Источник версии по умолчанию: VERSION файл в корне проекта.
#
# Использование:
#   ./server/scripts/deploy.sh <FILE> [--channel stable|beta] [--version X.Y.Z.W] [--repo OWNER/REPO]
#
# Примеры:
#   ./server/scripts/deploy.sh Nexy.dmg
#   ./server/scripts/deploy.sh Nexy.dmg --channel beta
#   ./server/scripts/deploy.sh Nexy.dmg --version 1.6.1.34 --channel stable

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
Usage: $0 <FILE> [--channel stable|beta] [--version X.Y.Z.W] [--repo OWNER/REPO]
USAGE
}

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VERSION_FILE="$PROJECT_ROOT/VERSION"

FILE="${1:-}"
if [ -z "$FILE" ]; then
  usage
  exit 1
fi
shift || true

CHANNEL="stable"
OVERRIDE_VERSION=""
REPO="Seregawpn/Nexy_production"
PUBLIC_HOST="nexy-server.canadacentral.cloudapp.azure.com"
AZURE_RESOURCE_GROUP="Nexy"
AZURE_VM_NAME="nexy-regular"

while [ $# -gt 0 ]; do
  case "$1" in
    --channel)
      CHANNEL="${2:-}"
      shift 2
      ;;
    --version)
      OVERRIDE_VERSION="${2:-}"
      shift 2
      ;;
    --repo)
      REPO="${2:-}"
      shift 2
      ;;
    *)
      log_err "Unknown argument: $1"
      usage
      exit 1
      ;;
  esac
done

if [ "$CHANNEL" != "stable" ] && [ "$CHANNEL" != "beta" ]; then
  log_err "--channel must be stable or beta"
  exit 1
fi

if [ ! -f "$FILE" ]; then
  log_err "File not found: $FILE"
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

if [ "$CHANNEL" = "beta" ]; then
  TAG="beta-v${VERSION}"
  RELEASE_TITLE="Nexy Beta ${VERSION}"
  PRERELEASE_FLAG="--prerelease"
else
  TAG="v${VERSION}"
  RELEASE_TITLE="Nexy ${VERSION}"
  PRERELEASE_FLAG=""
fi

FILE_NAME="$(basename "$FILE")"
LOCAL_FILE_SIZE="$(wc -c < "$FILE" | tr -d ' ')"
if command -v sha256sum >/dev/null 2>&1; then
  FILE_SHA256="$(sha256sum "$FILE" | awk '{print $1}')"
else
  FILE_SHA256="$(shasum -a 256 "$FILE" | awk '{print $1}')"
fi

DOWNLOAD_URL="https://github.com/${REPO}/releases/download/${TAG}/${FILE_NAME}"

log_info "File: $FILE_NAME"
log_info "Version (source of truth): $VERSION"
log_info "Channel: $CHANNEL"
log_info "Tag: $TAG"
log_info "Repo: $REPO"

log_step "Check CLI dependencies"
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

log_step "Start Azure version sync in parallel"
"$SCRIPT_DIR/update_server_version.sh" "$VERSION" "$VERSION" > /tmp/nexy_update_server_version.log 2>&1 &
SYNC_PID=$!

log_step "Publish artifact to GitHub release"
if gh release view "$TAG" --repo "$REPO" >/dev/null 2>&1; then
  log_warn "Release $TAG already exists, uploading asset with --clobber"
  gh release upload "$TAG" "$FILE" --repo "$REPO" --clobber
else
  gh release create "$TAG" \
    --repo "$REPO" \
    --title "$RELEASE_TITLE" \
    --notes "Automated ${CHANNEL} release ${VERSION}" \
    $PRERELEASE_FLAG \
    "$FILE"
fi

log_step "Wait for Azure version sync"
if ! wait "$SYNC_PID"; then
  log_err "Azure version sync failed"
  cat /tmp/nexy_update_server_version.log || true
  exit 1
fi

log_step "Fetch actual GitHub CDN size"
sleep 5
ACTUAL_FILE_SIZE="$(curl -sSLI "$DOWNLOAD_URL" | awk '/[Cc]ontent-[Ll]ength:/ {gsub("\r", "", $2); print $2}' | tail -1)"
if [ -z "$ACTUAL_FILE_SIZE" ] || [ "$ACTUAL_FILE_SIZE" = "0" ]; then
  log_err "Failed to fetch GitHub content-length for $DOWNLOAD_URL"
  exit 1
fi

if [ "$ACTUAL_FILE_SIZE" != "$LOCAL_FILE_SIZE" ]; then
  log_warn "Local size ($LOCAL_FILE_SIZE) differs from GitHub size ($ACTUAL_FILE_SIZE); GitHub size will be used"
fi

FILE_SIZE="$ACTUAL_FILE_SIZE"

log_step "Update remote manifests (manifest.json + manifest_${VERSION}.json)"
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
download_url = '${DOWNLOAD_URL}'
size = int('${FILE_SIZE}')
sha256 = '${FILE_SHA256}'
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
manifest_current.write_text(txt + '\n', encoding='utf-8')
manifest_versioned.write_text(txt + '\n', encoding='utf-8')

print(f'updated: {manifest_current}')
print(f'updated: {manifest_versioned}')
PYEOF" >/tmp/nexy_remote_manifest_update.log

log_step "Validate remote endpoints"
sleep 3
HEALTH_JSON="$(curl -sk "https://${PUBLIC_HOST}/updates/health" || true)"
if [ -z "$HEALTH_JSON" ]; then
  log_err "No response from /updates/health"
  exit 1
fi

HEALTH_VERSION="$(printf '%s' "$HEALTH_JSON" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('latest_version',''))" 2>/dev/null || true)"
HEALTH_BUILD="$(printf '%s' "$HEALTH_JSON" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('latest_build',''))" 2>/dev/null || true)"

APPCAST_XML="$(curl -sk "https://${PUBLIC_HOST}/updates/appcast.xml" || true)"
APPCAST_VERSION="$(printf '%s' "$APPCAST_XML" | grep -o 'sparkle:version="[^"]*"' | head -1 | cut -d'"' -f2)"
APPCAST_SIZE="$(printf '%s' "$APPCAST_XML" | grep -o 'length="[^"]*"' | head -1 | cut -d'"' -f2)"

if [ "$HEALTH_VERSION" != "$VERSION" ] || [ "$HEALTH_BUILD" != "$VERSION" ]; then
  log_err "Version mismatch on /updates/health: got ${HEALTH_VERSION}/${HEALTH_BUILD}, expected ${VERSION}/${VERSION}"
  exit 1
fi
if [ "$APPCAST_VERSION" != "$VERSION" ]; then
  log_err "Version mismatch in appcast: got ${APPCAST_VERSION}, expected ${VERSION}"
  exit 1
fi
if [ "$APPCAST_SIZE" != "$FILE_SIZE" ]; then
  log_err "Size mismatch in appcast: got ${APPCAST_SIZE}, expected ${FILE_SIZE}"
  exit 1
fi

echo
log_info "Release completed"
log_info "Tag: $TAG"
log_info "Download: $DOWNLOAD_URL"
log_info "Health: https://${PUBLIC_HOST}/updates/health"
log_info "Appcast: https://${PUBLIC_HOST}/updates/appcast.xml"
