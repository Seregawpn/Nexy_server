# Task Brief: VoiceOver Route Stabilization for Mic-Recovery Guard (2026-02-17)

## Goal
Убрать остаточные конфликты audio ownership в окне `mic_closed -> playback recovery` при route churn (VoiceOver/Bluetooth).

## Changes
1. `SpeechPlaybackIntegration` route-aware recovery:
- В `integration/integrations/speech_playback_integration.py` добавлены:
  - post-stop cooldown перед recovery reassert (`_mic_recovery_post_stop_cooldown_sec`)
  - ожидание стабилизации route (`_wait_for_player_route_stable`)
  - проверка in-flight route transition (`_player_route_transition_in_flight`)
- `AUDIO_MIC_RECOVERY` теперь:
  - ждёт короткий cooldown после `recording_stop`/terminal sources,
  - не выполняет reassert, если route transition не стабилизировался в timeout,
  - сохраняет existing dedup/reassert guards.

2. `AVFoundationPlayer` route state exposure:
- В `modules/speech_playback/core/avf_player.py` добавлен метод:
  - `is_route_transition_in_flight()`
- Метод возвращает `True`, если:
  - recreate route в процессе,
  - либо активен debounce window route change.

3. Tests:
- `tests/test_voice_audio_owner_guards.py`:
  - обновлены моки route-transition статуса,
  - добавлен тест `test_playback_mic_recovery_skips_during_route_transition`.

## Why
Конфликтный burst происходил в коротком окне, когда input owner уже отпускается, а playback owner reassert выполняется слишком рано/параллельно с route recreate. Новый guard делает recovery route-aware и снижает вероятность `session=(null)`.

## Verification
- `PYTHONPATH=. pytest -q tests/test_voice_audio_owner_guards.py tests/test_interrupt_playback.py tests/test_speech_playback_session_id.py tests/test_speech_playback_pipeline_diagnostic.py`
  - Result: `24 passed`
- `python3 scripts/verify_architecture_guards.py`
  - Result: `Architecture guards OK`
- `python3 scripts/verify_feature_flags.py`
  - Result: `Feature flags registry OK`

## Информация об изменениях
- Что изменено:
  - Добавлен route-stable wait/cooldown для post-mic playback recovery.
  - Добавлен API проверки route transition in-flight в AVF player.
  - Добавлены/обновлены unit tests под новый guard.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/speech_playback_integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/speech_playback/core/avf_player.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_voice_audio_owner_guards.py`
- Причина/цель изменений:
  - Устранить race в окне route transition, снижающую стабильность VoiceOver co-existence.
- Проверка (что выполнено для валидации):
  - Прогнаны целевые тесты (24 passed), архитектурные и флаговые гейты проходят.
