#!/usr/bin/env bash
set -euo pipefail

echo "❌ server/scripts/fix_version_mismatch.sh is deprecated and blocked."
echo "Use canonical flow:"
echo "  1) python3 server/scripts/update_version.py X.Y.Z.W"
echo "  2) python3 server/scripts/publish_assets_and_sync.py"
echo "  3) bash server/scripts/update_server_version.sh X.Y.Z.W"
exit 1
