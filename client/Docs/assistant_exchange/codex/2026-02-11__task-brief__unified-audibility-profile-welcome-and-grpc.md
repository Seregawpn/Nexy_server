# Unified Audibility Profile Welcome And Grpc

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): n/a

## Diagnosis
Welcome (`playback.raw_audio`) и command (`grpc.response.audio`) шли через разные пути предобработки громкости, из-за чего при успешном playback команды могли восприниматься значительно тише.

## Root Cause
Разные входы в playback owner без единого loudness-профиля -> неодинаковый peak/RMS перед AVFoundation -> разная слышимость при одном route.

## Optimal Fix
В `SpeechPlaybackIntegration` добавлен единый owner-метод `_apply_audibility_profile(...)` и применён в обоих путях:
- `_on_audio_chunk` (grpc stream)
- `_on_raw_audio` (welcome/raw)

Профиль:
- включается через `auto_gain_enabled` (default `true`)
- использует пороги `auto_gain_min_peak_int16`, `auto_gain_target_peak_int16`, `auto_gain_max_gain`
- поддерживает both `int16` и `float32` вход

## Verification
- `python3 -m py_compile integration/integrations/speech_playback_integration.py modules/speech_playback/core/avf_player.py`
- Runtime DoD:
  - welcome слышен
  - command response слышен на том же output route
  - в логах есть `playback.started` и `playback.completed` для command session

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `/Users/sergiyzasorin/Fix_new/client/Docs/DOCS_INDEX.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/PRE_CHANGE_CHECKLIST.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/PROJECT_REQUIREMENTS.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/ARCHITECTURE_OVERVIEW.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/FEATURE_FLAGS.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/CODEX_PROMPT.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/ANTIGRAVITY_PROMPT.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/PRE_CHANGE_CHECKLIST.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/assistant_exchange/TEMPLATE.md`
- Source of Truth: `SpeechPlaybackIntegration` (audibility profile owner).
- Дублирование: разрозненные пути громкости объединены в общий метод.
- Feature Flags check: новых флагов не добавлено.
- Race check: новых shared-state/locks не добавлено.

## Запрос/цель
Сделать одинаковую слышимость welcome и command при одном output.

## Контекст
- Файлы: `integration/integrations/speech_playback_integration.py`, `modules/speech_playback/core/avf_player.py`

## Решения/выводы
- Разные пути доставки оставлены, но loudness-профиль централизован.

## Открытые вопросы
- При сохранении проблемы проверить системный output profile (Bluetooth route) отдельно от playback pipeline.

## Следующие шаги
1. Прогнать 3 последовательных command-ответа после welcome.
2. При необходимости включить `audio_diag_verbose=true` и сравнить peak до/после профиля.
