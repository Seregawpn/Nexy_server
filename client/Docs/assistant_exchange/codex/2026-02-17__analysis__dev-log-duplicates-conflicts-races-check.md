# Analysis

## Summary
Проверен свежий `nexy-dev.log` и прогон тестов на признаки дублей, конфликтов и гонок условий.

## Findings
- Тесты стабильны:
  - `32 passed` для набора browser/audio/input/interrupt.
- Архитектурные dedup/guards активно работают (это ожидаемо, не ошибка):
  - `Terminal playback event dedup`
  - `VOICE: terminal STT dedup`
  - `cancel dedup`
  - `Mode request ignored (same mode)`
  - `press_stale_session_clear`
- Конфликт/гонка, влияющая на UX озвучки browser-step, **остается**:
  - `BROWSER_TTS suppressed ... playback_active_* queue_len=...`
  - `BROWSER_TTS watchdog timeout: queue_len=... playback_active=True`
  Это означает, что при длительном активном playback browser runtime TTS продолжает откладываться и не проигрывается вовремя.
- Дополнительные нестабильности в логе (не критично для core flow):
  - `Page readiness timeout` (browser page readiness)
  - `Finalize timeout waiting idle ...` в speech playback (редко, но повторяется)
  - `Health check неудачен (1/3)` одиночные предупреждения

## Verification
- Лог:
  - `/Users/sergiyzasorin/Library/Logs/Nexy/nexy-dev.log`
- Команды:
  - поиск dedup/race/suppress/timeout маркеров
  - хвост последнего участка лога
- Тесты:
  - `pytest -q tests/test_browser_install_contracts.py tests/test_voice_audio_owner_guards.py tests/test_interrupt_playback.py tests/test_quartz_monitor_chord_logic.py tests/test_input_secure_input_healthcheck.py`
  - результат: `32 passed in 11.04s`

## Информация об изменениях
- Изменения не вносились.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__analysis__dev-log-duplicates-conflicts-races-check.md`
- Причина/цель изменений:
  - Подтвердить наличие/отсутствие дублей, конфликтов и гонок условий на актуальном Dev логе.
- Проверка (что выполнено для валидации):
  - Анализ runtime-логов + целевой тестовый прогон.
