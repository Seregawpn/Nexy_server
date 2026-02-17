## Task
Стабилизировать запуск browser automation после полной очистки Chrome/Chromium, устранить ложный bypass `Local chromium ready`.

## Actions
- Ужесточена проверка локальной готовности Chromium в `modules/browser_automation/module.py`:
  - добавлен метод `_resolve_local_chromium_executable()`;
  - `_is_local_chromium_ready()` теперь требует одновременно:
    - `INSTALLATION_COMPLETE` marker,
    - реально существующий исполняемый Chromium в `ms-playwright/chromium-*`.
- Добавлена post-install валидация:
  - после `playwright install chromium` успех фиксируется только если `_is_local_chromium_ready()==True`;
  - иначе выбрасывается ошибка `install_completed_but_chromium_not_ready` и статус `failed`.
- Добавлен guard против stale cache:
  - в `process()` если `_browser_installed=True`, но Chromium фактически отсутствует, кэш сбрасывается и принудительно используется путь переустановки.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py` — OK.
- Проверено присутствие новых точек:
  - `_resolve_local_chromium_executable`
  - `install_completed_but_chromium_not_ready`
  - лог stale-cache guard.

## Информация об изменениях
- Что изменено:
  - Усилен runtime-контроль готовности браузера и устранён ложный "ready" путь.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__browser-readiness-hardening-and-stale-cache-guard.md`
- Причина/цель изменений:
  - После удаления браузеров система могла сообщать "Local chromium ready" без реального исполняемого Chromium, что приводило к нерабочему browser flow.
- Проверка:
  - Выполнена компиляционная проверка и точечная валидация новых guard-блоков.
