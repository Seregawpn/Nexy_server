# Pre-Build Gate Run

Goal: run full pre_build_gate after adding state catalog check and fixing Ruff warning.

## Result
- `scripts/pre_build_gate.sh` PASSED.
- Ruff: PASSED.
- Warnings: DeprecationWarning (is_first_run_restart_pending), PytestUnknownMarkWarning (smoke), and log config permissions warning.

## Files touched
- `scripts/verify_state_catalog.py`
