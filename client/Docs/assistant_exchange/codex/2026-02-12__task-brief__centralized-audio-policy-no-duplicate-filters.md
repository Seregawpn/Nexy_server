# Task Brief: Centralized audio policy (remove duplicate audibility filters)

## Goal
Убрать дубли и конфликтующие решения по "слышимости" между grpc ingress и playback owner, оставив централизованную политику в SpeechPlaybackIntegration.

## Changes
1. `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/grpc_client_integration.py`
   - Удалены duplicate audibility/noise-floor gates на ingress уровне:
     - `_min_audible_peak_int16`
     - `_min_audible_rms_int16`
     - `_noise_floor_peak_int16`
     - `_noise_floor_rms_int16`
   - grpc layer теперь выполняет transport-only роль:
     - валидация протокола (`sample_rate/channels`)
     - drop только пустых/полностью нулевых чанков
     - публикация всех non-zero чанков дальше в playback owner

2. `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/config/unified_config_loader.py`
   - Добавлен централизованный проброс флагов `speech_playback`:
     - `audio_diag_verbose`
     - `audio_diag_log_every`
     - `tts_auto_gain_enabled`
     - `tts_target_peak`
     - `tts_max_gain`
     - `tts_min_peak_for_gain`

3. `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/config/unified_config.yaml`
   - Добавлены соответствующие ключи в секцию `speech_playback`.

4. `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/speech_playback_integration.py`
   - Ранее выполненный фикс закреплён: near-silent первый чанк не пинит gain=1.0 на всю сессию.

## Validation
- `python3 -m py_compile integration/integrations/grpc_client_integration.py config/unified_config_loader.py integration/integrations/speech_playback_integration.py` -> OK
- `PYTHONPATH=. pytest -q tests/test_speech_playback_grpc_audio_format.py tests/test_interrupt_playback.py tests/test_speech_playback_session_id.py -q` -> PASS

## Result
- Удален архитектурный дубль audibility-логики на ingress слое.
- Единый owner audible policy: `SpeechPlaybackIntegration`.
- Конфигурация loudness/diag теперь централизованно управляется через `speech_playback`.
