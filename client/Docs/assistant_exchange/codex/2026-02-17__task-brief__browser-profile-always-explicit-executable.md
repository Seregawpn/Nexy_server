## Task
Исправить повторяющийся `uvx` fallback при запуске browser task.

## Actions
- Обновлен `modules/browser_automation/module.py`:
  - `BrowserProfile` теперь создается всегда, когда нет `browser_session` (не только при `keep_browser_open=true`).
  - `BrowserProfile` всегда получает:
    - `is_local=True`
    - `executable_path=chromium_executable`
  - `keep_alive` переключается через `bool(self._keep_browser_open)`.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py` — OK.
- Проверка блоков через `rg` — новые условия на месте.

## Информация об изменениях
- Что изменено:
  - Устранен путь, где Agent мог стартовать без browser profile и уходить в внутренний install через `uvx`.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__browser-profile-always-explicit-executable.md`
- Причина/цель изменений:
  - Повторная ошибка `FileNotFoundError: 'uvx'` при режиме без keep-alive.
- Проверка:
  - Выполнена компиляция и проверка целевых строк.
