#!/usr/bin/env bash
# Run Nexy client using .venv (arm64 dev). Use .venv_x86 only for x86_64 packaging.
set -e
CLIENT_DIR="${0%/*}"
cd "$CLIENT_DIR"

if [ -x "$CLIENT_DIR/.venv/bin/python" ]; then
  exec "$CLIENT_DIR/.venv/bin/python" main.py "$@"
elif [ -x "$CLIENT_DIR/.venv_x86/bin/python" ]; then
  ARCH=$(uname -m)
  if [ "$ARCH" = "arm64" ]; then
    echo "⚠ .venv not found; .venv_x86 is for x86_64. Create arm64 venv: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt"
    exit 1
  fi
  exec "$CLIENT_DIR/.venv_x86/bin/python" main.py "$@"
else
  echo "No .venv or .venv_x86 found. Create: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt"
  exit 1
fi
