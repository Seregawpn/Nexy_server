# Analysis: Input architecture race and duplication

## Key findings
- Core race: keyboard lifecycle events (`PRESS/LONG/RELEASE`) are not correlated by a single `press_id`.
- Delayed `RELEASE` callback can arrive after a new `LONG_PRESS`/session start and stop the wrong recording.
- InputProcessingIntegration currently publishes cancel/stop/mode events from several branches, creating overlapping paths.

## Architecture fit (current SoT)
- Mode SoT is correct: `mode.request` -> `ModeManagementIntegration` -> `ApplicationStateManager.set_mode`.
- Weak SoT area: input gesture lifecycle; ownership is split between Quartz state and InputProcessing session logic without strict event correlation.

## Duplications/conflicts
- Multiple cancel paths publish similar effects (`interrupt.request`, `grpc.request_cancel`, `voice.recording_stop`, `mode.request`).
- Signals consume both `app.mode_changed` and playback events, increasing duplicate cue chances.
- Old-session `app.mode_changed` can still be observed by integrations without strict session guard.

## Primary fix direction
1. Introduce `press_id` in keyboard events (generated in Quartz at combo activation).
2. Propagate `press_id` in all `KeyEvent.data` for PRESS/LONG/RELEASE.
3. InputProcessingIntegration keeps `active_press_id` and ignores stale LONG/RELEASE with mismatched `press_id`.
4. Centralize cancel path into one method and call it from short/interrupt branches.
5. Keep signals sourced primarily from `app.mode_changed`; keep playback hooks only for explicit cancel/error fallback with dedup.

## Expected effect
- Removes cross-session RELEASE races.
- Reduces duplicate transitions/cues.
- Keeps architecture boundaries intact (no rearchitecture).

