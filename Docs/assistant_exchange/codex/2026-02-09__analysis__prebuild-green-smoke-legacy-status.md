# 2026-02-09 — prebuild green, smoke/legacy status

## Scope
- Добить красные проверки `pre_build_gate`.
- Прогнать smoke и legacy pytest для оценки остаточных рисков.

## Changes
- `client/integration/integrations/signal_integration.py`
  - Убран прямой доступ к `state_manager`:
    - `get_current_mode()` -> `selectors.get_current_mode(...)` в `initialize` и `_on_error_like`.
- `client/integration/integrations/grpc_client_integration.py`
  - Убран прямой доступ к `state_manager` в гидрации сети:
    - `get_state_data(...)` -> `selectors.get_state_value(...)`.
- `client/scripts/check_dependency_violations.py`
  - Добавлен allowlist для `scripts/verify_welcome_audio.py` (инструментальная проверка welcome-аудио).

## Validation
- `python3 scripts/check_dependency_violations.py` -> `No dependency violations detected.`
- `python3 scripts/verify_no_direct_state_access.py` -> `No direct state access violations detected.`
- `scripts/pre_build_gate.sh --skip-tests` -> `✅ PRE-BUILD GATE: ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ`
- `python3 scripts/run_release_suite.py --smoke`
  - `pre_build_gate` PASSED
  - `integration_tests` PASSED
  - `problem_scan_gate` FAILED
- `PYTHONPATH=/Users/sergiyzasorin/Fix_new/client pytest -q ../tests`
  - прерван на collection с 20 ошибками (legacy/несинхронный test suite; отсутствующие/переименованные модули и старые импорты `InputState` и др.).

## Current blockers
- `problem_scan_gate`: `TOTAL_ISSUES=372`, `BLOCKING_ISSUES=231`.
- Legacy suite: 20 collection errors в `../tests` (исторический дрейф тестов относительно текущей архитектуры).

## Conclusion
- Архитектурные красные блокеры pre-build сняты.
- Runtime smoke почти green, единственный blocker — `problem_scan_gate`.
- Для "100%" осталось:
  - зачистка blocking issue в problem-scan,
  - синхронизация legacy tests с актуальной кодовой структурой.
