# Task Brief

## Summary
Закреплена логика озвучки browser-step без немого режима при активном playback и добавлены тест-контракты, чтобы поведение не откатывалось.

## Scope
- `BrowserUseIntegration` runtime TTS policy.
- Контрактные тесты browser install/runtime TTS.

## Changes
- В `BrowserUseIntegration._queue_or_publish_runtime_tts`:
  - для `missing_session_id` теперь явный `drop` (без queue/flush в `system`), чтобы убрать неявную переозвучку без сессии;
  - поведение для валидной `session_id` остаётся publish-through (без suppress) и сериализуется `SpeechPlaybackIntegration`.
- Добавлены тесты:
  - runtime TTS **не suppress** при `playback_active` и валидном `session_id`;
  - runtime TTS с `missing_session_id` не публикуется и не попадает в queue.

## Verification
- Прогон:
  - `pytest -q tests/test_browser_install_contracts.py tests/test_voice_audio_owner_guards.py tests/test_interrupt_playback.py tests/test_quartz_monitor_chord_logic.py tests/test_input_secure_input_healthcheck.py`
- Результат:
  - `34 passed in 9.87s`

## Информация об изменениях
- Что изменено:
  - Устранена неоднозначность suppress-пути для отсутствующего `session_id`.
  - Зафиксирован контракт unsuppress для browser-step TTS при валидной сессии.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/browser_use_integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_browser_install_contracts.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__browser-runtime-tts-unsuppress-contract-hardening.md`
- Причина/цель изменений:
  - Убрать повторяющуюся тишину во время browser steps и исключить потенциальные дубли из path `missing_session_id -> queue -> system`.
- Проверка (что выполнено для валидации):
  - Полный целевой прогон тестов, все зелёные.
