# Analysis/Fix: STT snapshot terminal race on release

## Symptom
User says query like sports news gets generic response and seems incomplete.

## Evidence from logs
Session: `88a8d141-91fb-4265-9fa6-1abd2cf6a4d0` in `~/Library/Logs/Nexy/nexy-dev.log`.
- `20:06:36.788` STT interim-like text: `can you find me`.
- `20:06:37.732` gRPC COMMIT started with prompt `can you find me...`.
- `20:06:38.738` later STT result appears: `Kingsport`.
- `20:06:38.740` this late result was dropped by terminal dedup.

## Root cause
`voice.recording_stop` path published stop snapshot terminal too early while controller still had pending final recognition.
This reserved terminal dedup slot and blocked later real `v2_completed` terminal text.

## Fix
File: `client/integration/integrations/voice_recognition_integration.py`
- In `_publish_stop_snapshot_terminal`:
  - if `_has_pending_stop_recognition()` is true, skip snapshot terminal publication (both text and error paths).
  - keep fallback mechanism to avoid hangs.

## Tests
- Added test in `client/tests/test_voice_audio_owner_guards.py`:
  - `test_stop_snapshot_terminal_is_skipped_while_pending_recognition`.
- Ran:
  - `pytest -q tests/test_voice_audio_owner_guards.py tests/test_grpc_client_interim_commit_gate.py`
  - Result: `16 passed`.
