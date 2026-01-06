# Pre-build Gate GUI Skip Guard

- Date: 2026-01-05
- Scope: scripts/pre_build_gate.sh
- Goal: Avoid Abort trap 6 when GUI/AppKit tests run in headless/sandbox environments.

## Changes
- Added --skip-gui flag.
- GUI-dependent checks (test_critical_paths.py, test_tray_termination.py) now skip when --skip-gui or --skip-tests is set.

## Notes
- GUI tests pass when run unsandboxed:
  - python3 scripts/test_critical_paths.py
  - python3 scripts/test_tray_termination.py
