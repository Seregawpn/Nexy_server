# Task Brief: CUE_TRACE end-to-end observability

## Problem
Сигнал мог "теряться" субъективно, но в логах не было единого сквозного идентификатора и явных причин drop по всем guard-веткам.

## Change
- Введен `cue_id` в сигнал-контракты:
  - `SignalRequest.cue_id`
  - `AudioSink.play_pcm(..., cue_id=...)`
- Добавлен сквозной `CUE_TRACE`:
  - `SignalIntegration`: `signal.emit` (pattern/profile/session/reason/cue_id)
  - `EventBusAudioSink`: `sink.publish` (cue_id + bytes/sr/ch)
  - `SpeechPlaybackIntegration`: `playback_signal.received`, `playback_signal.dropped(drop_reason=...)`, `playback_signal.queued`
  - `AVFoundationPlayer`: `avf.queue_push`, `avf.render_start`
  - `ModeManagementIntegration`: `mode_request.rejected/dedup/ignored`

## Why
- Теперь каждая попытка cue имеет трассу: emit -> publish -> receive/drop -> queue -> render.
- Любой "не услышал" можно привязать к конкретной причине (`shutdown`, `stale`, `cancel_in_flight`, `player_not_ready`, и т.д.).

## Validation
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py tests/test_processing_workflow_session_guard.py`
- `22 passed`

