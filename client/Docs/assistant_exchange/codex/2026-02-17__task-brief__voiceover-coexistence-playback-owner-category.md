# Task Brief: VoiceOver Coexistence - Playback Owner Category (2026-02-17)

## Goal
Снизить конфликты VoiceOver/Nexy за счет устранения input-ownership из playback path.

## Changes
1. `AVFoundationPlayer` playback profile policy:
- В `modules/speech_playback/core/avf_player.py::_ensure_playback_audio_session`
  удалена Bluetooth-ветка, переводившая playback в `PlayAndRecord`.
- Playback path теперь всегда удерживает `AVAudioSessionCategoryPlayback`.
- Лог обновлен: на Bluetooth фиксируется, что сохраняется `Playback` category.

2. Safety alignment with previous fix:
- Логика explicit reassert через owner recovery path сохранена (`start_playback(reassert_session=...)`).
- Безусловный no-op reassert остается отключенным.

## Why
`PlayAndRecord` в playback-owner path создает конкуренцию за input ownership с VoiceOver.
Для accessibility-coexistence playback не должен захватывать input category.

## Verification
- `PYTHONPATH=. pytest -q tests/test_voice_audio_owner_guards.py tests/test_interrupt_playback.py tests/test_speech_playback_session_id.py tests/test_speech_playback_pipeline_diagnostic.py`
  - Result: `23 passed`
- `python3 scripts/verify_architecture_guards.py`
  - Result: `Architecture guards OK`
- `python3 scripts/verify_feature_flags.py`
  - Result: `Feature flags registry OK`

## Информация об изменениях
- Что изменено:
  - Убрано использование `PlayAndRecord` в playback audio profile path.
  - Playback owner теперь не претендует на input ownership даже на Bluetooth route.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/speech_playback/core/avf_player.py`
- Причина/цель изменений:
  - Устранить класс конфликтов с VoiceOver (`session=(null)`) за счет строгого разделения ownership.
- Проверка (что выполнено для валидации):
  - Прогнаны целевые тесты (23 passed), architecture guards и feature flags проверки успешны.
