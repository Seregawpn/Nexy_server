# Task Brief — PROCESSING stuck after browser.done due playback no-audio race

## Symptom
После `browser.completed` режим оставался `PROCESSING` с blocker=`playback`.

## Root cause
`grpc.request_completed` мог приходить до первого audio chunk.
SpeechPlayback публиковал `playback.completed(no_audio)` и фиксировал terminal state.
Позже аудио приходило, но terminal уже был «закрыт», повторный `playback.completed` не публиковался.
ModeManagement видел активный playback blocker и не финализировал SLEEPING.

## Fix
Файл:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/speech_playback_integration.py`

Изменения:
1. Добавлен `self._no_audio_terminal_sessions`.
2. При `grpc_completed` без аудио: помечаем сессию как no-audio terminal.
3. При первом реальном `grpc_audio` chunk для такой сессии:
   - снимаем terminal markers (`_terminal_event_by_session`, `_finalized_sessions`),
   - удаляем из no-audio set,
   - логируем `AUDIO_RACE_RECOVER`.
4. Если `grpc_done` уже true и пришел аудио chunk — запускаем `_finalize_on_silence` чтобы гарантированно выпустить `playback.completed` после дренажа очереди.
5. На cancel cleanup удаляем sid из no-audio set.

## Tests
Файл:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_voice_audio_owner_guards.py`

Добавлен тест:
- `test_playback_reopens_no_audio_terminal_when_first_audio_arrives`

## Verification
- `pytest -q tests/test_voice_audio_owner_guards.py` → `10 passed`
- `pytest -q tests/test_grpc_client_interim_commit_gate.py` → `4 passed`
- `python3 -m py_compile ...` → OK

## Architectural gates
- Single Owner: playback terminal owner остаётся `SpeechPlaybackIntegration`.
- Zero Duplication: без новых owner-path, только race-recovery внутри текущего owner.
- Anti-Race: закрыт out-of-order `grpc_completed(no_audio) -> late audio`.
