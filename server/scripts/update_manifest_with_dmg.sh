#!/usr/bin/env bash
set -euo pipefail

echo "❌ scripts/update_manifest_with_dmg.sh is deprecated and blocked."
echo "Use canonical flow:"
echo "  1) Place artifacts in release_inbox/"
echo "  2) python3 scripts/publish_assets_and_sync.py"
exit 1
