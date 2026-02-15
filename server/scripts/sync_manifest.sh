#!/usr/bin/env bash
set -euo pipefail

echo "❌ server/scripts/sync_manifest.sh is deprecated and blocked."
echo "Use canonical owner scripts only:"
echo "  - python3 server/scripts/publish_assets_and_sync.py"
echo "  - bash server/scripts/update_manifest_remote_locked.sh [options]"
exit 1
