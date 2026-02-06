#!/bin/bash
set -euo pipefail

# Unified strict quality gate alias.
# Enforces basedpyright presence and runs the full pre-build gate.
./scripts/pre_build_gate.sh --require-basedpyright "$@"
