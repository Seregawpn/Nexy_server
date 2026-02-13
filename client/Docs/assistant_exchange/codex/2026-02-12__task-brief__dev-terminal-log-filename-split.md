# Dev terminal log filename split

## Goal
Separate dev launch logs (from terminal) from default runtime logs to avoid mixed sessions in one file.

## Changes
1. `integration/utils/logging_setup.py`
- Added centralized detection for terminal dev launch (`_is_terminal_dev_launch`).
- Added centralized path resolver (`_resolve_log_file_path`).
- Rule: if non-frozen launch from interactive terminal, use sibling file `nexy-dev.log`; otherwise keep configured path.
- Added `get_effective_log_file_path()` for single source of truth in startup reporting.

2. `main.py`
- Replaced ad-hoc raw config path read with `get_effective_log_file_path()`.
- Unified final path normalization with `expanduser + abspath`.

## Verification
- `python3 -m py_compile integration/utils/logging_setup.py main.py` passed.

## Notes
- In non-interactive runners (CI/tool exec), path remains default `nexy.log` by design.
- In interactive terminal `python3 main.py`, logs go to `~/Library/Logs/Nexy/nexy-dev.log`.
