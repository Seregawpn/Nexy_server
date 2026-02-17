# Task Brief

## Summary
Устранена блокировка/потеря озвучки browser-step при Dev запуске через централизацию deferred runtime TTS в `BrowserUseIntegration`.

## Scope
- Один owner-path для browser runtime TTS: `suppress -> queue -> flush`.
- Без изменения общей архитектуры mode/playback owners.

## Changes
- В `BrowserUseIntegration` добавлен единый deferred-queue путь для **всех** suppress-reason (включая `mode_processing*`, не только `playback_active*`).
- Добавлен watchdog `runtime_tts_flush_task` для безопасного idle-flush при пропущенном terminal callback.
- Добавлены диагностические логи:
  - `BROWSER_TTS suppressed ... queue_len=...`
  - `BROWSER_TTS flush: queued_count=...`
  - timeout warning watchdog.
- Добавлен корректный cancel cleanup для `runtime_tts_flush_task` в `stop()`.

## Verification
- Команда:
  - `pytest -q tests/test_browser_install_contracts.py tests/test_voice_audio_owner_guards.py tests/test_interrupt_playback.py`
- Результат:
  - `27 passed in 9.94s`

## Информация об изменениях
- Что изменено:
  - Централизован runtime suppress/queue/flush в `BrowserUseIntegration`.
  - Исключен путь suppress без deferred queue для browser-step TTS.
  - Добавлен idle watchdog flush как anti-race safety-net.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/browser_use_integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__browser-runtime-tts-centralized-deferred-flush.md`
- Причина/цель изменений:
  - Убрать ситуацию, когда browser steps выполняются, но их озвучка подавляется и не доходит до воспроизведения.
- Проверка (что выполнено для валидации):
  - Прогон целевых тестов: 27/27 passed.
