# Task Brief — Processing stuck: sessionless cancel vs silence finalize

Date: 2026-02-18
Assistant: Codex
Type: task-brief

## Goal
Убрать race, при котором `session=None` cancel мог отменять все `silence_finalize` задачи и оставлять `ModeManagement` с вечным `blocker=playback` (оранжевая иконка/PROCESSING).

## Changes

1) Sessionless cancel guard in playback owner
- File: `client/integration/integrations/speech_playback_integration.py`
- `_apply_cancel_state` changed:
  - `session=None` больше не вызывает глобальный cancel всех silence-задач
  - сначала резолвит активную session (`_current_session_id` / `_active_output_session_id`)
  - отменяет finalize только для резолвленной session
  - cleanup/finalized/cancelled тоже применяются только к резолвленной session

2) Regression test for race
- File: `client/tests/test_speech_playback_pipeline_diagnostic.py`
- Added: `test_sessionless_cancel_does_not_cancel_foreign_silence_finalize`
  - проверяет, что sessionless cancel не сносит чужую pending finalize-задачу.

## Verification
- `pytest -q tests/test_speech_playback_pipeline_diagnostic.py tests/test_mode_management_mode_request_dedup.py` -> 9 passed
- `python3 -m py_compile integration/integrations/speech_playback_integration.py tests/test_speech_playback_pipeline_diagnostic.py` -> OK

## Architecture gates
- Single Owner: playback terminal/cancel owner остался `SpeechPlaybackIntegration`.
- Zero Duplication: не добавлены обходы в `ModeManagement`/workflow.
- Anti-Race: убран глобальный side-effect от sessionless cancel.
- Flag lifecycle: без новых флагов.
