## Task
Устранить падение browser automation с ошибкой `FileNotFoundError: 'uvx'`.

## Actions
- В `modules/browser_automation/module.py` изменен поток `process()`:
  - если браузер не готов, теперь **дожидаемся** завершения install task (`await install_task`) до старта Agent;
  - добавлена обязательная проверка наличия executable после setup (`chromium_executable_not_found_after_setup`).
- В создание `BrowserProfile` добавлен явный путь к локальному Chromium:
  - `BrowserProfile(..., is_local=True, executable_path=chromium_executable)`.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py` — OK.
- Проверены точки в коде:
  - `await install_task`
  - `chromium_executable_not_found_after_setup`
  - `executable_path=chromium_executable`.

## Информация об изменениях
- Что изменено:
  - Убран путь, при котором `browser_use` мог запускать внутренний install через `uvx`.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__browser-uvx-failure-guard-and-explicit-executable.md`
- Причина/цель изменений:
  - В runtime отсутствует `uvx`, из-за чего browser launch падал при внутреннем install watchdog.
- Проверка:
  - Выполнена компиляционная проверка и валидация новых guard-блоков.
