# Browser Directory Single Owner Overrides

## Task
Централизовать настройку директорий browser runtime/driver, чтобы убрать расхождения между dev и пользовательской средой.

## Architecture Fit
- Владелец резолва директорий: `BrowserUseModule`.
- Второй owner-path не добавлен.

## Implementation
1. В `BrowserUseModule` добавлены single-owner резолверы:
- `_resolve_browser_runtime_base_dir()`
- `_resolve_playwright_driver_override_dir()`
2. Добавлены override-механизмы (в порядке приоритета):
- config: `browser_use.runtime_browser_dir`, `browser_use.playwright_driver_dir`
- env: `NEXY_BROWSER_RUNTIME_DIR`, `NEXY_PLAYWRIGHT_DRIVER_DIR`
- fallback: текущий app-support path.
3. `_resolve_frozen_playwright_install_cmd()` теперь сначала проверяет explicit driver dir.
4. Добавлен диагностический лог с финальными путями при каждом browser request.
5. В `config/unified_config.yaml` добавлены ключи:
- `runtime_browser_dir`
- `playwright_driver_dir`

## Verification
- `python3 -m py_compile modules/browser_automation/module.py` — OK
- YAML parse `config/unified_config.yaml` — OK

## Информация об изменениях
- что изменено:
  - Централизован owner-резолв директорий browser runtime и playwright driver.
  - Добавлены конфигурационные override-пути для user-машины.
  - Добавлен runtime-лог финальной path-конфигурации.
- список файлов:
  - `modules/browser_automation/module.py`
  - `config/unified_config.yaml`
  - `Docs/assistant_exchange/codex/2026-02-21__task-brief__browser-directory-single-owner-overrides.md`
- причина/цель изменений:
  - Убрать недетерминированный path-selection и дать управляемую настройку директорий в проде.
- проверка (что выполнено для валидации):
  - Синтаксическая проверка Python-модуля и валидность YAML-конфига.
