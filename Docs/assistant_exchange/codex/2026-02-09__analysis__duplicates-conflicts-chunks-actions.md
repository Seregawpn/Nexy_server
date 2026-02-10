# Analysis: duplicates/conflicts in chunks/actions paths

## Scope
- chunk ingestion/playback path
- action extraction/execution path
- mode transition arbitration around playback/action completion

## Findings
1. grpc action can be dispatched from multiple sources in one response:
   - text_chunk command (`text_chunk_command`)
   - action_message (`action_message`)
   - combined text fallback (`text_combined_command`)
   - `action_message_sessions` is currently unused.

2. mode.request for SLEEPING is emitted from multiple parallel handlers on playback completion:
   - ProcessingWorkflow completion path
   - ModeManagementIntegration `_bridge_playback_done`
   - ModeManagementIntegration `_on_playback_finished` (fail-safe)

3. ModeManagementIntegration subscribes to both specific action events and lifecycle events:
   - `actions.open_app|close_app.*`
   - `actions.lifecycle.*`
   - For open/close actions this doubles start/finish accounting paths.

4. SpeechPlayback finalization guard map `_finalized_sessions` is not marked on normal `playback.completed` path, only on cancel/failed.

## Recommended centralization
- gRPC action owner: `action_message` as primary, text parsing as fallback only if action_message absent.
- mode transition owner: ModeManagementIntegration only; keep one publication path to `mode.request` after playback/action/browser quiescence.
- action activity owner in mode guard: `actions.lifecycle.*` only.
- playback terminal owner: SpeechPlaybackIntegration should mark finalized on every terminal publish path.
