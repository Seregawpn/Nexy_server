# Analysis: startup stuck in PROCESSING after welcome playback

## Context
После старта приложение переходило в `PROCESSING` для приветствия и не возвращалось в `SLEEPING`.

## Diagnosis
Проблема состояла из двух частей:
1) `WelcomeMessageIntegration` не отправлял `mode.request -> SLEEPING` в success/failed ветках.
2) `SpeechPlaybackIntegration._on_raw_audio` не запускал финализацию для UUID-сессий raw_audio, из-за чего `playback.completed` часто не приходил для welcome.

## Root Cause
- Welcome flow переводил в `PROCESSING`, но обратный переход был только в exception-path.
- Raw-audio finalize запускался только для `raw_session=True`; welcome передавал валидный UUID (`raw_session=False`), и terminal playback event не эмитился.

## Architecture Fit
- Owner mode transitions: `ModeManagementIntegration` через `mode.request` (сохранено).
- Owner playback terminal events: `SpeechPlaybackIntegration` (сохранено).

## Changes
1) `integration/integrations/welcome_message_integration.py`
- Добавлен явный `mode.request` в `SLEEPING` после:
  - `welcome.completed` (`reason=welcome_completed`)
  - `welcome.failed` (`reason=welcome_failed`)

2) `integration/integrations/speech_playback_integration.py`
- В `_on_raw_audio` raw clip теперь всегда помечается как завершённый по gRPC (`_grpc_done_sessions[session_id] = True`).
- Финализация `_finalize_on_silence(session_id, timeout=1.0)` запускается всегда для raw audio, не только для `raw_session`.

## Verification
- `python3 -m py_compile integration/integrations/welcome_message_integration.py integration/integrations/speech_playback_integration.py` — OK.
- Проверка наличия новых веток:
  - `reason=welcome_completed`
  - `reason=welcome_failed`
  - unconditional raw finalize in `_on_raw_audio`

## Информация об изменениях
- Что изменено:
  - Исправлен возврат режима после welcome.
  - Исправлена финализация raw-audio welcome playback.
- Список файлов:
  - `integration/integrations/welcome_message_integration.py`
  - `integration/integrations/speech_playback_integration.py`
- Причина/цель изменений:
  - Убрать зависание в `PROCESSING` после старта и стабилизировать terminal playback события.
- Проверка:
  - Синтаксическая проверка пройдена.
