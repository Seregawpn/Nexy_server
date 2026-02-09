# Handoff: Input Lifecycle State Machine (Phase 1)

## What changed

### 1) Unified lifecycle state in Input coordinator
- File: `integration/integrations/input_processing_integration.py`
- Added `PTTLifecycleState`:
  - `IDLE`, `ARMED`, `RECORDING`, `STOPPING`, `PROCESSING`
- Added `self._lifecycle_state` and `_transition_lifecycle(...)` with structured transition logs.

### 2) Lifecycle transitions wired into key handlers
- `PRESS` -> `ARMED`
- `LONG_PRESS` -> `RECORDING`
- `RELEASE` stop path -> `STOPPING`
- `RELEASE` processing path -> `PROCESSING`
- Cancel/reset paths -> `IDLE`

### 3) Recognition failure guard during active press lifecycle
- `_on_recognition_failed` now skips fallback-to-sleeping while active input lifecycle is in:
  - `ARMED`, `RECORDING`, `STOPPING`
- Prevents mode flapping while release/stop is still being resolved.

### 4) Quartz pending-release correlation hardening (continued cleanup)
- File: `modules/input_processing/keyboard/mac/quartz_monitor.py`
- `pending release Control` requires correlated `pending release N`.
- Removed early clearing of `pending_n_release_at` on `Control up`.
- Added stale/pair-gap guards for pending release correlation.

## Why this is architectural (not patch-on-patch)
- Input lifecycle now has one explicit coordinator state in integration layer.
- Error fallback (`recognition_failed`) no longer overrides active input lifecycle.
- Quartz confirms releases only with correlated key evidence.

## Remaining work (Phase 2)
1. Move all terminal stop publication ownership (`voice.recording_stop` / `voice.mic_closed`) to one place.
2. Remove duplicate mode transition publishing outside coordinator-owned transitions.
3. Consolidate `session=None` stop path into explicit emergency-only branch with dedicated reason code.
