# Task Brief: browser install jitless fix for frozen Playwright node

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-16
- ID (INS-###): N/A

## Diagnosis
В `.app` режиме установка Chromium падала на этапе запуска bundled Playwright `node` с ошибкой `Failed to reserve virtual memory for CodeRange`.

## Root Cause
Hardened-runtime + V8 JIT в bundled `node` → падение инициализации Isolate (CodeRange) → browser setup fail до установки Chromium.

## Optimal Fix
- Source of Truth: `modules/browser_automation/module.py` (`BrowserUseModule._ensure_browser_installed`).
- Изменение:
  - Для frozen install-команды вида `.../playwright/driver/node .../cli.js install chromium` добавлен `NODE_OPTIONS=--jitless` (с сохранением существующих `NODE_OPTIONS`).
  - Применяется только на install-path браузера в `.app`, не затрагивает остальной runtime.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py` -> OK
- Ручная валидация причины:
  - Без `--jitless`: `node cli.js --version` падает с `Failed to reserve virtual memory for CodeRange`.
  - С `--jitless`: `node --jitless cli.js --version` работает.

## Информация об изменениях
- Что изменено:
  - Добавлен guarded runtime workaround (`NODE_OPTIONS=--jitless`) для frozen Playwright install.
- Файлы:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`
- Причина/цель:
  - Устранить падение browser setup на macOS packaged build при старте browser-use.
- Проверка:
  - Компиляция модуля + воспроизведение/подтверждение ошибки и успешного запуска с `--jitless`.

