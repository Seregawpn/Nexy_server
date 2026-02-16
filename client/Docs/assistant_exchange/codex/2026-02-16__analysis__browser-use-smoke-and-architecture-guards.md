# Analysis: browser-use smoke and architecture guards

## Scope
Проверить, есть ли конфликты в логике browser-use после удаления `ms-playwright`, и подтвердить корректность owner-пути.

## What was checked
- Статическая проверка `BrowserUseModule`:
  - owner установки: `_ensure_browser_installed`
  - guard: `_install_lock` (single-flight)
  - явные terminal fail events: `BROWSER_TASK_FAILED`
- Поиск fallback-путей в browser-use цепочке:
  - в `modules/browser_automation` и `integration/integrations/browser_use_integration.py` не найдено `webbrowser/open/xdg-open/startfile`.
- Runtime smoke test:
  - вызов `BrowserUseModule.process(...)` и получение terminal события.
- Архитектурный baseline gate:
  - `python3 scripts/verify_architecture_guards.py` -> OK.

## Results
- Runtime behavior подтвержден: при недоступности browser runtime возвращается корректный terminal fail (`BROWSER_TASK_FAILED`) через owner-модуль.
- Конфликтов по architecture guard не обнаружено (`no new violations beyond baseline`).
- Дублирующего fallback-пути на системный браузер в browser-use цепочке не обнаружено.

## Limitation
- В текущем CLI-окружении отсутствует пакет `browser_use` (`No module named 'browser_use'`), поэтому auto-install Chromium из этого окружения не проверялся end-to-end. Для полного e2e подтверждения нужен запуск именно packaged `.app`.
