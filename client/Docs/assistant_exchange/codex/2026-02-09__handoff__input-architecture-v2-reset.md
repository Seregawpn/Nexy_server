# Handoff: Input Architecture V2 reset

## Done

1. Archived legacy/conflicting input files:
- `Docs/_archive/input_arch/input_processing_integration__legacy_2026-02-09.py`
- `Docs/_archive/input_arch/quartz_monitor__snapshot_2026-02-09.py`

2. Replaced input coordinator with V2 implementation:
- `integration/integrations/input_processing_integration.py`

3. Documented canonical architecture and interaction contract:
- `Docs/INPUT_ARCHITECTURE_V2.md`

## Key architecture changes

- Single Source of Truth for input lifecycle moved to `InputProcessingIntegration`.
- Keyboard monitor remains low-level adapter (edge events only).
- Unified terminal path: `voice.recording_stop` -> wait `voice.mic_closed` -> `mode.request`.
- `press_id` idempotency guard for terminal stop.
- Secure Input fallback force-stops current cycle and returns to `SLEEPING`.

## Validation

- Compile check passed:
  - `python3 -m py_compile integration/integrations/input_processing_integration.py`
  - `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py`

## Next expected checks (runtime)

1. Hold/release (normal): `LISTENING -> PROCESSING -> SLEEPING` without sticky mic.
2. Short tap: cancel to `SLEEPING`.
3. Secure Input during hold: forced stop and reset to `SLEEPING`.
4. `grpc.request_failed` during active cycle: forced stop and reset.

