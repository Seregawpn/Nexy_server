# Analysis: quartz release scheduled but recording not finalized

## Context
По логу 2026-02-17 11:30:24 видно `combo release ... RELEASE scheduled`, но отсутствует owner-цепочка `InputProcessingIntegration` для `voice.recording_stop` и `mode.request(PROCESSING)`. В результате микрофон остается в continuous listening-loop и пользователь не может штатно завершить цикл.

## Root cause
Практический race на границе low-level combo release и lifecycle owner:
- release фиксируется в `QuartzKeyboardMonitor`;
- но terminal path в `InputProcessingIntegration` иногда не выполняется;
- следствие: `recording` не закрывается, STT цикл остается активным.

## Fix
Добавлен owner-compatible watchdog в `InputProcessingIntegration._run_health_check`:
- если state=`RECORDING`, combo физически уже отпущен (`combo_active/control_pressed/n_pressed=false`) два тика подряд,
- выполняется terminal stop через существующий owner path,
- публикуется `mode.request(PROCESSING)` и lifecycle переводится в `WAITING_GRPC`.

Это не добавляет второй owner принятия решений: используется тот же `InputProcessingIntegration` terminal path.

## Verification
- `pytest -q tests/test_input_secure_input_healthcheck.py -k "watchdog" -vv` ✅
- `pytest -q tests/test_input_secure_input_healthcheck.py -k "cooldown_and_restore or attempts_monitor_recovery" -vv` ✅

Примечание: полный запуск `tests/test_browser_module_ready_bypass.py` в текущей среде флакал/висел на старом stale-install сценарии; к исправлению release-race не относится.

## Информация об изменениях
- Что изменено:
  - Добавлен watchdog release-missed для quartz combo в input owner.
  - Добавлен тест на принудительный terminal stop по watchdog.
- Список файлов:
  - `integration/integrations/input_processing_integration.py`
  - `tests/test_input_secure_input_healthcheck.py`
  - `Docs/assistant_exchange/codex/2026-02-17__analysis__quartz-release-missed-watchdog.md`
- Причина/цель изменений:
  - Устранить зависание микрофона в `RECORDING/LISTENING` при пропуске terminal release path.
- Проверка (что выполнено для валидации):
  - Пройдены целевые pytest сценарии для watchdog и secure-input recovery.
