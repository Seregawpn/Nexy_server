# Task Brief: Quartz combo stale-N guard against ghost press

## Context
- Incident from runtime log: mode jumped to `SLEEPING` and then `LISTENING` without intentional user press.
- Sequence shows `PRESS_PREEMPT ... sid=None state=idle` followed by `interrupt.request`, then new `PTT_STATE: idle -> armed`.

## Diagnosis
- `QuartzKeyboardMonitor` could activate combo in `flagsChanged` branch when `_n_pressed=True` stayed stale after missed/lost `N keyup`.
- That generated synthetic `PRESS` path in input integration (`press_preempt`) and caused unintended interrupt/mode transition.

## Changes
- File: `modules/input_processing/keyboard/mac/quartz_monitor.py`
1. Added stale-N tracking fields:
   - `_last_n_keydown_ts`
   - `_stale_n_pressed_reset_sec`
2. In `flagsChanged` control branch:
   - Added stale-state healing: reset `_n_pressed` when no recent real `N keydown`.
   - Removed combo activation from control `flagsChanged` path.
3. Kept combo activation only on real `N keydown` while Control is pressed.
4. Updated `N keydown` branch to refresh `_last_n_keydown_ts`.

## Architecture fit
- Logic remains in keyboard adapter (`QuartzKeyboardMonitor`) where low-level key edge normalization belongs.
- No new mode owner/state owner introduced; `mode.request` centralization unchanged.

## Verification
- Syntax check: `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py`
- Runtime expectation:
  - No unexpected `PRESS_PREEMPT` after `grpc_completed` without real key press.
  - No unintended `interrupt.request` caused by stale combo state.

## Risk
- Behavior change: combo no longer activates from `control flagsChanged` alone; activation is now tied to real `N keydown` edge.
- This reduces false positives from stale `n_pressed` and should not affect standard `Ctrl+N` sequence.
