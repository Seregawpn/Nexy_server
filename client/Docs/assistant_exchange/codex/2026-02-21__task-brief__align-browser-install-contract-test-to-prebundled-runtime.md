## Task
Привести `tests/test_browser_install_contracts.py` к актуальному контракту prebundled runtime (без install-start TTS/notification) и подтвердить зелёный прогон.

## Changes
- Обновлён тест:
  - Было: ожидал notification+deferred TTS для `status=started`.
  - Стало: проверяет, что для `status=started` нет notification и нет TTS.
- Файл:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_browser_install_contracts.py`

## Verification
1. `PYTHONPATH=. pytest -q tests/test_browser_install_contracts.py tests/test_browser_module_ready_bypass.py`
- Result: `15 passed`

2. `PYTHONPATH=. pytest -q tests/test_browser_action_race_condition.py tests/test_processing_workflow_session_guard.py tests/test_mode_management_mode_request_dedup.py`
- Result: `13 passed`

3. `python3 scripts/verify_architecture_guards.py`
- Result: `Architecture guards OK (no new violations beyond baseline).`

## Информация об изменениях
- Что изменено:
  - Тест-контракт синхронизирован с текущей продуктовой политикой prebundled browser runtime.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_browser_install_contracts.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-21__task-brief__align-browser-install-contract-test-to-prebundled-runtime.md`
- Причина/цель изменений:
  - Убрать ложное падение legacy-теста и закрепить актуальный runtime-контракт.
- Проверка:
  - Целевой pytest прогон + смежный regression набор + architecture guard.
