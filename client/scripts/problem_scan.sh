#!/bin/bash
set -euo pipefail

# Generates consolidated issue list (ruff + basedpyright if available).
./.venv/bin/python scripts/scan_problem_list.py --with-tests "$@"
./.venv/bin/python scripts/problem_scan_prioritize.py
