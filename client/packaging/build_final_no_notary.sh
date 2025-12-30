#!/bin/bash

# Явный сценарий: финальная упаковка БЕЗ нотарификации (локальные тесты).
set -e

export NEXY_SKIP_NOTARIZATION=1

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "$SCRIPT_DIR/build_final.sh"
