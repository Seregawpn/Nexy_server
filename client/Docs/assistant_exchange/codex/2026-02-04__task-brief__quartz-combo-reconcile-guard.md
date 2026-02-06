# Task Brief: Quartz Combo Reconcile Guard

## Goal
Eliminate false combo deactivation by preventing watchdog reconcile during active Ctrl+N hold.

## Changes
- Added guard in modules/input_processing/keyboard/mac/quartz_monitor.py:_reconcile_combo_state to skip CGEventSource* sync when combo is active and key is held.

## Rationale
CGEventSource* is unreliable when events are suppressed, causing false release and mic stop. Guard keeps single source of truth in event-path; timeouts remain as fallback.

## Files
- modules/input_processing/keyboard/mac/quartz_monitor.py

## Verification
- Hold Ctrl+N for >5s: no DEACTIVATION TRIGGERED, mic stays active.
- Release Ctrl+N: single RELEASE, recording stops normally.
