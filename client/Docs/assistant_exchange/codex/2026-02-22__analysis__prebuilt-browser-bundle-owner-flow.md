## Task
Перевести packaging на owner-flow: использовать только заранее подготовленный Playwright browser bundle, без скачивания в `build_final.sh`.

## Diagnosis
`build_final.sh` скачивал/устанавливал Chromium во время сборки, что создавало второй runtime-path и нестабильный release flow.

## Root Cause
Подготовка browser runtime была встроена в production build script вместо отдельного pre-step.

## Changes
1. `packaging/build_final.sh`
- функция `prepare_playwright_browser_bundle()` теперь только валидирует существующий bundle;
- auto-install/merge логика удалена;
- при отсутствии/неполном bundle сборка падает с инструкцией: `scripts/prepare_playwright_browser_bundle.sh`.

2. `scripts/prepare_playwright_browser_bundle.sh` (новый)
- отдельный pre-step подготовки bundle;
- ставит arm64 Chromium и x64 Chromium (через temp bundle + merge в основной);
- проверяет universal-ready структуру (`chrome-mac-arm64` + `chrome-mac`/`chrome-mac-x64`).

## Verification
- `bash -n packaging/build_final.sh` — OK
- `bash -n scripts/prepare_playwright_browser_bundle.sh` — OK

## Информация об изменениях
- Что изменено:
  - Удалён runtime download из production build.
  - Добавлен явный pre-step подготовки Playwright bundle.
- Список файлов:
  - `packaging/build_final.sh`
  - `scripts/prepare_playwright_browser_bundle.sh`
  - `Docs/assistant_exchange/codex/2026-02-22__analysis__prebuilt-browser-bundle-owner-flow.md`
- Причина/цель изменений:
  - Стабильный, предсказуемый release flow: сначала подготовка артефактов, потом упаковка/подпись/нотаризация.
- Проверка:
  - синтаксическая валидация скриптов и проверка owner-message в build_final.
