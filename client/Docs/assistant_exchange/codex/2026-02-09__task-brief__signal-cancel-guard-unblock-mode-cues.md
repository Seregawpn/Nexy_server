# Task Brief: Signal reliability after interrupt

## Goal
Убрать пропадание UX-сигналов (`listen_start/done/error`) сразу после interrupt/cancel.

## Root cause
В `SpeechPlaybackIntegration._on_playback_signal` guard `cancel_in_flight` блокировал ВСЕ `playback.signal` в окне cancel, включая mode cues.

## Fix
Файл: `integration/integrations/speech_playback_integration.py`
- Изменен guard:
  - раньше: блокировал любой `playback.signal` в cancel-окне;
  - теперь: блокирует только `pattern == "cancel"` в cancel-окне.
- `listen_start/done/error` больше не подавляются после interrupt.

## Architecture fit
- Source of Truth сигналов не менялся (`SignalIntegration` по `app.mode_changed`/error/cancel).
- Изменен только playback-guard (anti-race), без новых состояний.

## Verification
- `python3 -m py_compile integration/integrations/speech_playback_integration.py` — OK.

## Expected behavior
- После interrupt mode cues воспроизводятся стабильно.
- Дублирующий late-cancel cue по-прежнему подавляется.
