# Browser Install Skip: Root Cause + Runtime Path Fix

## Diagnosis
Установка Chromium не запускалась, потому что модуль определял браузер как уже готовый из bundled-пути внутри `.app`, и install-flow пропускался.

## Root Cause
`_resolve_browser_runtime_base_dir()` в frozen-режиме приоритетно возвращал `Contents/Resources/playwright-browsers`, если директория существовала. Это конфликтовало с новой целевой моделью runtime-install на машине пользователя.

## Fix
- Удален fallback на bundled browser runtime в frozen-режиме.
- Теперь runtime browser path всегда user-level (`Application Support/.../chrome-nexy`), если нет явного override через config/env.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py` -> OK
- Проверка функции `_resolve_browser_runtime_base_dir` подтверждает отсутствие bundled fallback.

## Информация об изменениях
- Что изменено:
  - Убран bundled runtime fallback из резолва пути Chromium.
- Список файлов:
  - `modules/browser_automation/module.py`
  - `Docs/assistant_exchange/codex/2026-02-22__analysis__browser-install-skip-root-cause-and-runtime-path-fix.md`
- Причина/цель изменений:
  - Обеспечить единый owner-path runtime установки Chromium на клиентской машине и исключить silent skip из-за старого bundled каталога.
- Проверка:
  - Синтаксическая валидация и точечная проверка обновленного path-resolver.
