#!/usr/bin/env bash
set -euo pipefail

echo "❌ scripts/sync_version_centralization.sh is deprecated and blocked."
echo "Use: python3 scripts/update_version.py X.Y.Z.W"
echo "Then: bash scripts/update_server_version.sh X.Y.Z.W"
exit 1
