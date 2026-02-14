# Task Brief: restore packaging Nexy.spec

Date: 2026-02-14
Branch: release/v1.6.1.35

## Goal
Restore missing packaging source-of-truth `packaging/Nexy.spec` and prevent false-positive preflight statuses.

## Changes made
1. Restored file:
   - `packaging/Nexy.spec` (restored from `main:client/packaging/Nexy.spec`)
2. Fixed preflight masking:
   - `packaging/build_final.sh`: added `set -o pipefail` right after `set -e`
3. Prevented future silent loss of spec:
   - `.gitignore`: added `!packaging/Nexy.spec` after `*.spec`

## Verification
- Ran: `./packaging/build_final.sh --speed-check`
- Result:
  - `verify_imports.py`: packaging files check now passes with `Nexy.spec` present.
  - `verify_pyinstaller.py`: validates spec successfully.
  - `verify_spec_dependencies.py`: 186/186 dependencies available.
  - Preflight now fails for a real blocking gate (`problem_scan_gate.sh` / basedpyright), not because of missing spec.

## Notes
Root issue was combination of:
- missing local file `packaging/Nexy.spec`, and
- `.gitignore` rule `*.spec` that hid this file from tracking.
