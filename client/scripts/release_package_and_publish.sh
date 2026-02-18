#!/usr/bin/env bash

set -euo pipefail

CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT_DIR="$(cd "$CLIENT_DIR/.." && pwd)"
OWNER_SCRIPT="$ROOT_DIR/scripts/release_package_and_publish.sh"
FIX_SCRIPT="$CLIENT_DIR/scripts/fix_dist_release_artifact.sh"
SHOW_HELP=0

for arg in "$@"; do
    if [ "$arg" = "-h" ] || [ "$arg" = "--help" ]; then
        SHOW_HELP=1
        break
    fi
done

if [ ! -x "$OWNER_SCRIPT" ]; then
    echo "ERROR: missing executable owner script: $OWNER_SCRIPT" >&2
    exit 1
fi

if [ ! -x "$FIX_SCRIPT" ]; then
    echo "ERROR: missing executable fix script: $FIX_SCRIPT" >&2
    exit 1
fi

if [ "$SHOW_HELP" -eq 0 ]; then
    if [ "${NEXY_WIPE_ACTIVATION:-0}" = "1" ]; then
        bash "$FIX_SCRIPT" --wipe-activation
    else
        bash "$FIX_SCRIPT"
    fi
fi

exec "$OWNER_SCRIPT" "$@"
