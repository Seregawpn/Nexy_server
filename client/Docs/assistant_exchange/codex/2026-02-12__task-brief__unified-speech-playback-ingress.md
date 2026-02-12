# Task Brief: Unified speech playback ingress (grpc + welcome)

## Goal
Свести gRPC-аудио и приветствие к единому внутреннему пути постановки аудио в AVF плеер, чтобы убрать расхождения в поведении.

## Changes
1. `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/speech_playback_integration.py`
   - Добавлен единый helper `_queue_session_audio(...)`:
     - централизует `ensure_player_ready`,
     - единообразно публикует `playback.started`,
     - единообразно ставит аудио в очередь плеера,
     - обновляет playback timestamp/state.
   - `grpc.response.audio` (`_on_audio_chunk`) переведен на этот helper.
   - `playback.raw_audio` / welcome path (`_on_raw_audio`) переведен на этот же helper.
   - Добавлена очистка `self._tts_gain_by_session` в терминальных точках (cancel/failed/completed).

## Validation
- `python3 -m py_compile integration/integrations/speech_playback_integration.py` -> OK

## Result
- Оба входных потока речи (welcome и gRPC) используют единый внутренний runtime-путь.
- Уменьшен риск расхождения поведения между приветствием и основной речью.
- Логика стала проще для дальнейшей калибровки громкости/диагностики.
