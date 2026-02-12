# Speech Playback Dead Code Cleanup

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): n/a

## Diagnosis
В `SpeechPlaybackIntegration` оставались no-op/unused части, не влияющие на поведение playback, но усложняющие сопровождение.

## Root Cause
Исторические хвосты после предыдущих итераций (resync placeholders, no-op WAV block, пустая подписка mic_closed) не были удалены.

## Optimal Fix
Удалены безопасные неиспользуемые части:
1. Поля `_needs_output_resync` и `_pending_resync_task`.
2. no-op `WAV header skip logic` и связанный state `_wav_header_skipped`.
3. Пустая подписка `voice.mic_closed` и no-op handler `_on_voice_mic_closed`.

## Verification
- `python3 -m py_compile integration/integrations/speech_playback_integration.py modules/speech_playback/core/avf_player.py`
- Поведение playback pipeline не изменено: transport/terminal events остаются теми же.

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
- Source of Truth: `SpeechPlaybackIntegration`.
- Дублирование: удалены неиспользуемые ветки и поля.
- Feature Flags check: не менялись.
- Race check: новых shared-state/lock не добавлено.

## Запрос/цель
Удалить дубли/мертвые части, которые больше не нужны.

## Контекст
- Файл: `integration/integrations/speech_playback_integration.py`

## Решения/выводы
- Cleanup проведён без функциональных изменений и без новых флагов/состояний.

## Открытые вопросы
- none

## Следующие шаги
1. Наблюдать 2-3 обычных сессии по логам `playback.started/completed`.
