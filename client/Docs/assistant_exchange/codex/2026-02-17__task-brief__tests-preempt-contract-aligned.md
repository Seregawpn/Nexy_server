# Task Brief

## Summary
Приведен в соответствие тестовый контракт `interrupt` с текущей централизованной preempt-логикой (preempt только при реальных in-flight сигналах).

## Scope
- Обновлены 3 теста в `tests/test_interrupt_playback.py`.
- Выполнен повторный прогон целевого набора тестов.

## Changes
- В `test_short_press_publishes_interrupt_request_in_processing` заменено legacy-ожидание mode-only на `input_integration._playback_active = True`.
- В `test_press_publishes_interrupt_request_in_processing_without_playback_flag` обновлен сценарий на preempt через активный playback.
- В `test_press_and_long_press_same_press_id_publish_single_interrupt_request` обновлен контракт dedup для playback-preempt пути.

## Verification
- Запуск: `pytest -q tests/test_browser_install_contracts.py tests/test_voice_audio_owner_guards.py tests/test_quartz_monitor_chord_logic.py tests/test_input_secure_input_healthcheck.py tests/test_interrupt_playback.py`
- Результат: `32 passed in 9.93s`.

## Информация об изменениях
- Что изменено:
  - Актуализированы ожидания трех interrupt-тестов под owner-guard preempt (`playback_active`).
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_interrupt_playback.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__tests-preempt-contract-aligned.md`
- Причина/цель изменений:
  - Убрать конфликт между runtime-централизацией preempt и устаревшим test-contract mode-only.
- Проверка (что выполнено для валидации):
  - Повторный прогон целевого набора тестов, зеленый результат.
