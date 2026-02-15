# Task Brief: Problem scan blocking Ruff fixes

## Context
- Build pipeline failed at `scripts/problem_scan_gate.sh`.
- Blocking issues were only Ruff errors (`I001`, `B018`, `F821`).

## Diagnosis
- `main.py` contained a stray symbol `т` near the PyObjC comment, causing `F821` + `B018`.
- Import blocks in `main.py` and `integration/integrations/welcome_message_integration.py` were unsorted (`I001`).

## Changes
- Removed stray `т` from `main.py` comment line before `_apply_pyobjc_fix_early`.
- Normalized imports in:
  - `main.py`
  - `integration/integrations/welcome_message_integration.py`

## Verification
- Ran:
  - `.venv/bin/ruff check --fix main.py integration/integrations/welcome_message_integration.py`
  - `.venv/bin/ruff check main.py integration/integrations/welcome_message_integration.py`
  - `scripts/problem_scan_gate.sh`
- Result:
  - `BLOCKING_ISSUES=0`
  - gate passed

## Architecture impact
- No behavior change.
- No new state.
- No ownership changes; only lint/syntax hygiene in existing modules.
