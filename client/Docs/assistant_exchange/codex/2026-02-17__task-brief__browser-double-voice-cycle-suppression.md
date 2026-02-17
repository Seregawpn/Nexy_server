# Task Brief

## Context
Пользователь наблюдал эффект «одна и та же фраза/цикл произносится дважды подряд» в browser-сценарии.

## Objective
Подтвердить причину и убрать дублирование голосового цикла в browser path.

## Findings
- В `BrowserUseIntegration` есть локальные TTS-триггеры:
  - `source=browser_start`
  - `source=browser_step`
- Эти события публикуются в `grpc.tts_request`, а в `GrpcClientIntegration._on_tts_request` они маршрутизируются в server TTS (`_play_server_tts`).
- Одновременно основной gRPC ответ тоже приходит как аудио-поток.
- Это создает риск «двойного цикла» (два голосовых канала в одном run).

## Implementation
1. В `BrowserUseIntegration` добавлен runtime suppression browser-local TTS:
   - подписка на `app.mode_changed`, `playback.started`, `playback.completed/cancelled/failed`;
   - tracking текущего режима/сессии и активного playback;
   - guard `_should_suppress_browser_runtime_tts(session_id)`.
2. При `BROWSER_TASK_STARTED` и `BROWSER_STEP_COMPLETED`:
   - если активен `PROCESSING`/playback, browser-local TTS не отправляется;
   - пишется диагностический лог: `BROWSER_TTS suppressed ...`.

## Verification
- `python3 -m py_compile integration/integrations/browser_use_integration.py` — OK.
- Локальный pytest `tests/test_browser_module_ready_bypass.py` в текущем окружении зависает без вывода (процесс остановлен вручную).

## Информация об изменениях
- Что изменено:
  - Добавлен suppress-guard для browser-local TTS в runtime.
  - Исключён второй голосовой цикл при активном processing/playback.
- Список файлов:
  - `integration/integrations/browser_use_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__browser-double-voice-cycle-suppression.md`
- Причина/цель изменений:
  - Устранить дублирование речи в browser-сценариях.
- Проверка:
  - Синтаксис подтвержден.
  - Для runtime-подтверждения нужен новый прогон и проверка логов на `BROWSER_TTS suppressed`.
