#!/usr/bin/env bash
set -euo pipefail

echo "❌ scripts/deploy.sh is deprecated and blocked."
echo "Use canonical flow instead:"
echo "  1) python3 scripts/update_version.py X.Y.Z.W"
echo "  2) python3 scripts/publish_assets_and_sync.py"
echo "  3) bash scripts/update_server_version.sh X.Y.Z.W"
exit 1
