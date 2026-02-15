#!/usr/bin/env bash
set -euo pipefail

echo "❌ server/scripts/sync_version_centralization.sh is deprecated and blocked."
echo "Use: python3 server/scripts/update_version.py X.Y.Z.W"
echo "Then: bash server/scripts/update_server_version.sh X.Y.Z.W"
exit 1
