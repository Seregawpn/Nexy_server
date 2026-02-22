# Packaging Gates: Browser Runtime + Gemini API

## Task
Добавить обязательные проверки при старте упаковки и после сборки .app:
- наличие браузера и его компонентов,
- наличие API,
- проверка работоспособности API.

## Architecture Fit
- Owner packaging gate: `packaging/build_final.sh`.
- Runtime owner-цепочки не затронуты.

## Implementation
1. Добавлен preflight `Gemini API` в `build_final.sh`:
- проверка наличия `gemini_api_key` из env/credentials/config,
- fallback на embedded key (`EMBEDDED_GEMINI_API_KEY`) для тестового режима,
- live-check вызов к Gemini через `langchain_google_genai`.
- Fail блокирует packaging.
- Для оффлайн-режима добавлен явный bypass: `NEXY_SKIP_GEMINI_API_LIVE_CHECK=1`.

2. Добавлена функция `verify_packaged_browser_runtime()` и вызов после сборки `dist/Nexy.app`:
- проверяет `Contents/Resources/playwright-browsers`,
- проверяет `Contents/Resources/playwright/driver`,
- проверяет `chromium-*`, `INSTALLATION_COMPLETE`, executable,
- проверяет driver-компоненты (`playwright.sh/cmd` или `node + cli.js`).
- Любой fail блокирует packaging.

## Verification
- `bash -n packaging/build_final.sh` — OK
- Поиск новых gate-блоков в скрипте — OK

## Информация об изменениях
- что изменено:
  - Добавлен блокирующий preflight Gemini API (наличие + live health-check).
  - Добавлена блокирующая проверка packaged browser runtime внутри `.app`.
  - Добавлен управляемый bypass live API check для оффлайн-случаев.
- список файлов:
  - `packaging/build_final.sh`
  - `Docs/assistant_exchange/codex/2026-02-21__task-brief__packaging-gates-browser-and-gemini-api.md`
- причина/цель изменений:
  - Гарантировать, что при упаковке DMG браузерный runtime реально упакован и API реально доступен/работает до релиза.
- проверка (что выполнено для валидации):
  - Bash syntax check и проверка наличия новых gate-секций.
