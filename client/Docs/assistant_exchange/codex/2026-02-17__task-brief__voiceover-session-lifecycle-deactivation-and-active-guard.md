# Task Brief: VoiceOver Session Lifecycle Deactivation and Active Guard (2026-02-17)

## Goal
Снизить session churn между Nexy и VoiceOver: деактивировать playback-сессию в idle и не вызывать лишний `setActive(True)` при уже активной корректной сессии.

## Changes
1. Session lifecycle в `AVFoundationPlayer`:
- Добавлено поле `self._session_active` в `__init__`.
- Добавлен метод `_deactivate_audio_session(reason=...)`:
  - вызывает `AVAudioSession.sharedInstance().setActive_error_(False, None)`
  - сбрасывает `self._session_active=False`
  - сбрасывает `self._last_audio_session_signature=None`
  - логирует `AUDIO_SESSION_DEACTIVATE`.

2. Деактивация при остановке playback:
- `stop_playback()` теперь вызывает `_deactivate_audio_session(reason="stop_playback")` после остановки нити/узла.
- `shutdown()` теперь вызывает `_deactivate_audio_session(reason="shutdown")` при завершении движка.

3. Guard от лишнего `setActive(True)`:
- В `_ensure_playback_audio_session()` добавлена проверка:
  - если `self._session_active` и `already_on_target`, то `setActive(True)` пропускается (`AUDIO_SESSION_ALREADY_ACTIVE`).
- При реальном activate-path после retry выставляется `self._session_active` по результату активации.

4. Unit tests:
- Добавлен файл `tests/test_avf_player_audio_session_lifecycle.py`:
  - проверка skip redundant activation,
  - проверка активации при неактивной сессии,
  - проверка reset состояния при deactivation,
  - проверка вызова deactivation из `stop_playback()` и `shutdown()`.

## Why
Текущая проблема вызвана тем, что playback-сессия держится активной весь lifecycle приложения и repeatedly re-activates. Это провоцирует лишние HAL-переговоры и шум в VoiceOver-логах. Новая схема делает owner lifecycle явным: activate на входе в playback, deactivate на выходе в idle.

## Verification
- `python3 -m pytest tests/test_avf_player_audio_session_lifecycle.py -q`
  - Result: `4 passed`
- `python3 -m pytest tests/test_speech_playback_grpc_audio_format.py tests/test_speech_playback_pipeline_diagnostic.py tests/test_speech_playback_session_id.py -v`
  - Result: `6 passed`
- `python3 scripts/verify_architecture_guards.py`
  - Result: `Architecture guards OK`
- `python3 scripts/verify_feature_flags.py`
  - Result: `Feature flags registry OK`

## Информация об изменениях
- Что изменено:
  - Добавлен lifecycle-control playback audio session (deactivate on stop/shutdown).
  - Добавлен runtime guard от redundant `setActive(True)`.
  - Добавлены unit tests на lifecycle и guard.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/speech_playback/core/avf_player.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_avf_player_audio_session_lifecycle.py`
- Причина/цель изменений:
  - Уменьшить VoiceOver session churn и HAL contention без изменения центра управления playback owner.
- Проверка (что выполнено для валидации):
  - Прогнаны целевые unit/integration тесты и архитектурные/флаговые гейты.
