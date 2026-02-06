# Analysis: False Control Release During Combo Hold

## Symptom
During Ctrl+N hold, mic starts then stops unexpectedly with DEACTIVATION TRIGGERED.

## Root Cause
flagsChanged sometimes reports Control=False while combo is still physically held (event suppression side effect). This false edge deactivates combo and emits RELEASE.

## Fix
Added guard in modules/input_processing/keyboard/mac/quartz_monitor.py:
- When combo is active and N is held, a Control=False from flagsChanged is accepted only if CGEventSourceFlagsState also confirms Control is not pressed.
- If system flags still show Control pressed, release is ignored.

## Expected Result
No false combo deactivation during active hold; RELEASE should happen only on real key release.
