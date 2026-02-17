## Task
Разобрать причину постоянной переустановки браузера в Dev и устранить цикл переустановки.

## Findings
- В `Nexy-Dev/ms-playwright/chromium-1208` присутствует `INSTALLATION_COMPLETE` и фактический бинарник браузера.
- Фактический путь бинарника:
  - `.../chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing`
- Ранее runtime-проверка искала только старые пути (`chrome-mac/Chromium.app/...`) и не учитывала `chrome-mac-arm64/Google Chrome for Testing.app/...`.
- Из-за этого readiness возвращал `False`, запускался install path и происходил reinstall-loop.

## Actions
- Обновлен список candidate-путей в `_resolve_local_chromium_executable()`:
  - добавлены `chrome-mac-arm64/Google Chrome for Testing.app/...`
  - добавлены дополнительные mac/linux варианты.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py` — OK.
- Runtime-проверка через `.venv/bin/python`:
  - `_is_local_chromium_ready()` -> `True`
  - `_resolve_local_chromium_executable()` -> корректный путь к `Google Chrome for Testing`.

## Информация об изменениях
- Что изменено:
  - Исправлена детекция локального Chromium под актуционный layout Playwright (mac-arm64).
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__analysis__dev-browser-reinstall-loop-root-cause-and-path-fix.md`
- Причина/цель изменений:
  - Убрать постоянную переустановку браузера в Dev при уже установленном локальном браузере.
- Проверка:
  - Компиляция и прямой runtime вызов readiness/executable resolvers.
