# Task Brief: Quality gate stabilized by excluding generated dist/build trees

## Diagnosis
- `problem_scan_gate.sh` failed with `basedpyright_status=failed` and dependency violations even when source code checks were green.
- Root cause: scanners analyzed generated artifacts (`dist-arm64`, `dist-x86_64`, `build-*`) and reported third-party/copied code issues as blocking.

## Changes
1. `scripts/check_dependency_violations.py`
   - Hardened file traversal filter:
     - skip top-level `.venv`, `.venv_x86`
     - skip top-level `dist`, `build`, `dist-*`, `build-*`

2. `scripts/scan_problem_list.py`
   - Expanded global path exclusions:
     - `/dist/`, `/build/`, `/dist-`, `/build-`
     - `/.venv/`, `/.venv_x86/`
     - kept existing `/Docs/_archive/`

## Verification
- `python .venv/bin/python scripts/check_dependency_violations.py` -> `No dependency violations detected.`
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh` -> passed:
  - `TOTAL_ISSUES=0`
  - `BLOCKING_ISSUES=0`
  - `[INFO] problem scan gate passed`
- `./packaging/build_final.sh --speed-check` -> full preflight passed.

## Result
- Quality gate now reflects source tree quality only.
- Generated packaging outputs no longer create false blocking issues.
