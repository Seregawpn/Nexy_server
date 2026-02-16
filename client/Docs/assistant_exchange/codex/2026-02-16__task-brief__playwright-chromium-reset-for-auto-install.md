# Task Brief: Playwright Chromium reset for auto-install

## Goal
Удалить локально установленный Playwright Chromium, чтобы приложение выполнило автоустановку при следующем browser-use запуске.

## Actions
- Удалены каталоги:
  - `~/Library/Application Support/Nexy/ms-playwright`
  - `~/Library/Application Support/Nexy-Dev/ms-playwright`
- Проверено после удаления:
  - `Nexy: missing`
  - `Nexy-Dev: missing`

## Architecture Gates
- Single Owner: браузерный runtime-owner не менялся (`BrowserUseModule`).
- Zero Duplication: новые пути/обходы не добавлялись.
- Anti-Race: текущий `single-flight` lock (`_install_lock`) сохранен.
- Flag Lifecycle: новые флаги не добавлялись.

## Expected Runtime
- При следующем `browser.use.request` приложение должно создать `ms-playwright` и установить Chromium автоматически.
