# Analysis: Multi-activation / multiple Nexy instances on first launch

## Context
- User symptom: after install + first launch, many activations and many Nexy icons/processes appear.
- Evidence source: `log.md`.

## Findings
1. Log shows repeated app check-ins with new PIDs every few seconds:
   - `CHECKIN: pid=13419`, then `13429`, `13440`, `13444`, ...
2. `runningboardd` reports identity conflicts:
   - `Two equal instances have unequal identities...`
3. This indicates duplicate instance guard is not correctly recognizing the already-running packaged process.

## Root cause
In `modules/instance_manager/core/instance_manager.py`, method `_is_lock_valid()`:
- It correctly identifies packaged process by name `Nexy`.
- But then applies an extra `cmdline_check` requiring `com.nexy.assistant` or `main.py` in cmdline.
- For packaged app, cmdline often does not contain those markers.
- Result: valid lock is treated as invalid, lock file gets removed, and next process starts as "single".

## Implemented fix
- Removed the extra `cmdline_check` gate that invalidated real packaged Nexy processes.
- Added robust packaged detection via `process.exe()` and bundle binary path match.
- Preserved dev/debug script detection.

Changed file:
- `modules/instance_manager/core/instance_manager.py` (duplicate detection block in `_is_lock_valid`)

## Validation
- Syntax check passed:
  - `python3 -m py_compile modules/instance_manager/core/instance_manager.py`

## Expected outcome
- Second and subsequent launches detect active Nexy instance as duplicate.
- New duplicate processes should exit early instead of creating repeated activations/icons.
