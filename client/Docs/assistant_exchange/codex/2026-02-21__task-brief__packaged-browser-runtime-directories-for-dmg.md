# Packaged Browser Runtime Directories for DMG

## Task
Настроить канонические директории и упаковку browser runtime/driver для macOS DMG, чтобы убрать runtime path-расхождения на пользовательских машинах.

## Architecture Fit
- Single owner для runtime path: `BrowserUseModule`.
- Single owner для packaging browser bundle: `packaging/build_final.sh` + `packaging/Nexy.spec`.
- Mode/session owner-path не изменён.

## Implementation
1. `BrowserUseModule`:
- Для frozen runtime добавлен канонический default path:
  - `Contents/Resources/playwright-browsers` (browser runtime)
  - `Contents/Resources/playwright/driver` (driver)
- Сохранены explicit overrides через config/env.

2. `Nexy.spec`:
- Добавлено bundling браузерного runtime из `NEXY_PLAYWRIGHT_BROWSERS_BUNDLE_DIR` в `playwright-browsers` внутри `.app`.
- Добавлены явные логи при отсутствии переменной/директории.

3. `build_final.sh`:
- Добавлена подготовка bundled Chromium runtime перед PyInstaller:
  - ставит Chromium в единый staging dir;
  - прогоняет install для native + x86_64 env (если доступен);
  - валидирует `chromium-*`, `INSTALLATION_COMPLETE` и executable;
  - экспортирует `NEXY_PLAYWRIGHT_BROWSERS_BUNDLE_DIR` для `Nexy.spec`.
- Добавлен guard `NEXY_SKIP_PLAYWRIGHT_BROWSERS_BUNDLE=1` (только для осознанного bypass).

## Verification
- `python3 -m py_compile modules/browser_automation/module.py` — OK
- `python3 -m py_compile packaging/Nexy.spec` — OK
- `bash -n packaging/build_final.sh` — OK
- YAML parse `config/unified_config.yaml` — OK

## Информация об изменениях
- что изменено:
  - В frozen runtime добавлены канонические bundled директории browser runtime/driver.
  - Добавлен deterministic packaging browser runtime в `.app` через build pipeline.
  - Добавлен preflight bundled Chromium runtime до PyInstaller.
- список файлов:
  - `modules/browser_automation/module.py`
  - `packaging/Nexy.spec`
  - `packaging/build_final.sh`
  - `Docs/assistant_exchange/codex/2026-02-21__task-brief__packaged-browser-runtime-directories-for-dmg.md`
- причина/цель изменений:
  - Обеспечить одинаковые директории и полную упаковку browser runtime для пользовательских DMG сборок.
- проверка (что выполнено для валидации):
  - Синтаксические проверки Python/Bash и валидность YAML.
