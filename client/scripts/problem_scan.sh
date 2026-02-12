#!/bin/bash
set -euo pipefail

# Generates consolidated issue list (ruff + basedpyright if available).
BASELINE_ARG=""
if [ -f "problem_baseline.json" ]; then
    BASELINE_ARG="--baseline problem_baseline.json"
fi

./.venv/bin/python scripts/scan_problem_list.py --with-tests $BASELINE_ARG "$@"
./.venv/bin/python scripts/problem_scan_prioritize.py
