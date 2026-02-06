#!/bin/bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_PYTHON="$PROJECT_ROOT/.venv/bin/python"

if [ ! -x "$VENV_PYTHON" ]; then
    echo "[ERROR] .venv не найден. Создайте окружение: python3 -m venv .venv"
    exit 1
fi

echo "[INFO] Installing dev dependencies from requirements-dev.txt"
if "$VENV_PYTHON" -m pip install -r "$PROJECT_ROOT/requirements-dev.txt"; then
    echo "[INFO] Dev environment is ready"
    exit 0
fi

echo "[WARN] Failed to install all dev dependencies from index"
if [ -n "${BASEDPYRIGHT_WHEEL:-}" ]; then
    echo "[INFO] Installing basedpyright from wheel: $BASEDPYRIGHT_WHEEL"
    "$VENV_PYTHON" -m pip install "$BASEDPYRIGHT_WHEEL"
    echo "[INFO] Dev environment is ready (wheel fallback)"
    exit 0
fi

echo "[ERROR] basedpyright install failed."
echo "[ERROR] Set BASEDPYRIGHT_WHEEL=/absolute/path/to/basedpyright-*.whl and rerun."
exit 1
