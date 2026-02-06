# Analysis: PTT Interrupt Loop + Control Scope Fix

## Problem
1) quartz_monitor raised runtime error: cannot access local variable kCGEventFlagMaskControl.
2) LONG_PRESS triggered interrupt.request during active recording flow, causing mode fallback to SLEEPING while user still held PTT.

## Fixes
- quartz_monitor: removed local re-import of kCGEventFlagMaskControl in combo branch; use module-level constant.
- input_processing_integration: narrowed LONG_PRESS interrupt emission to real speech-stop cases only:
  - playback active OR grpc in-flight
  - and NOT mic_active
  - and NOT recording_started

## Effect
- No combo callback crash.
- No self-interrupt during active hold recording path.
- Mode no longer bounces to SLEEPING from LONG_PRESS in normal listening start.
