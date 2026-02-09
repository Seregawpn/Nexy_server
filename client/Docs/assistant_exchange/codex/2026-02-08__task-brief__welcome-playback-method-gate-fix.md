# Task Brief: Welcome Playback Method Gate Fix

## Context
- Симптом: на старте welcome-цепочка доходила до серверной генерации аудио, но звук часто не воспроизводился.
- Логи показывали старт `welcome_player.play_welcome()` и gRPC-аудио диагностику, но не всегда был переход в `playback.raw_audio`.

## Root Cause
- В `WelcomeMessageIntegration` отправка аудио в `SpeechPlaybackIntegration` выполнялась только при `result.method == "server"`.
- При других валидных серверных значениях `method` (например `edge_tts`/`tts`) результат считался успешным, но аудио не отправлялось в playback.
- Дополнительно `_welcome_played` в callback завершения выставлялся в `True` даже при неуспехе, что создавало риск ложного “уже проиграно”.

## Changes
- Файл: `integration/integrations/welcome_message_integration.py`
  - Убрал жёсткий gate `result.method == "server"`.
  - Теперь аудио отправляется в playback при `result.success` и наличии `audio_data` (кроме `local_fallback`, где звук уже воспроизведён через `say`).
  - Добавил диагностический warning для случая `success=True`, но `audio_data is None`.
  - Исправил установку `_welcome_played` в `_on_welcome_completed`: теперь зависит от `result.success`.

## Verification
- `python3 -m py_compile integration/integrations/welcome_message_integration.py` — OK.

## Expected Outcome
- Приветствие не зависит от конкретной строковой метки `method` в серверном ответе.
- Если сервер вернул валидное аудио, оно всегда уходит в единый playback-пайплайн.
- Меньше ложных состояний “приветствие уже проиграно”.
