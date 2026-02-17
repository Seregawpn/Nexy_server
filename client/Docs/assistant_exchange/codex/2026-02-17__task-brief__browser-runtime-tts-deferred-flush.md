# Task Brief: Browser runtime TTS deferred flush

## Context
Браузерные шаги выполнялись, но озвучка (`browser_start`/`browser_step`) часто отсутствовала. В логах фиксировалось: `BROWSER_TTS suppressed ... reason=playback_active_other_session`.

## Diagnosis
В `BrowserUseIntegration` suppression runtime TTS работал как hard-drop: при активном playback сообщение отбрасывалось и не воспроизводилось позже.

## Architecture Fit
- Owner: `BrowserUseIntegration` (browser-runtime narration policy)
- Source of truth: playback activity state внутри интеграции (`_playback_active`, `_active_playback_sessions`)
- Централизация сохранена: не добавлен второй путь в Speech/Mode owners.

## Implementation
В `integration/integrations/browser_use_integration.py`:
1. Добавлена deferred очередь runtime TTS:
   - `_pending_runtime_tts`, `_pending_runtime_tts_set`.
2. Добавлен единый метод `_queue_or_publish_runtime_tts(...)`:
   - при `playback_active*` не дропает, а откладывает сообщение.
3. В `_on_playback_terminal(...)` добавлен `_flush_pending_runtime_tts()` когда playback idle.
4. `browser_start` и `browser_step` переведены на новый единый owner-метод.

## Concurrency / Race Guard
- Дедуп отложенных сообщений по `(session_id, text)`.
- Flush только при `not _playback_active`.

## Verification
- `python3 -m py_compile integration/integrations/browser_use_integration.py` — OK.
- По логике: suppression больше не приводит к потере текста, а к deferred воспроизведению.

## Информация об изменениях
- Что изменено:
  - Устранена потеря браузерной озвучки при active playback другого session.
  - Введена отложенная доставка runtime TTS после завершения playback.
- Список файлов:
  - `integration/integrations/browser_use_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__browser-runtime-tts-deferred-flush.md`
- Причина/цель изменений:
  - Браузер выполняется, но пользователь не слышит прогресс/подтверждение из-за suppression-дропа.
- Проверка:
  - Синтаксис проверен (`py_compile`), owner suppression-path теперь с deferred flush.
