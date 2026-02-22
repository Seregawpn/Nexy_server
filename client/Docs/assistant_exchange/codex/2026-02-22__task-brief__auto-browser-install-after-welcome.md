# Auto Browser Install After Welcome

## Context
Требование: установка браузера должна стартовать автоматически после приветствия, без первого browser-запроса пользователя.

## Diagnosis
Текущий install-flow запускался только из `browser.use.request`, поэтому при простом старте приложения и приветствии установка не начиналась.

## Root Cause
Отсутствовал startup trigger на уровне интеграции браузера после `welcome.completed`.

## Implementation
1. Добавлен публичный owner-метод в модуль браузера:
- `BrowserUseModule.ensure_runtime_browser_ready(reason=...)`
- Использует существующий single-flight install-task (`_get_or_start_install_task`) и возвращает `ready`.

2. Добавлен post-welcome startup trigger в integration:
- В `BrowserUseIntegration._on_welcome_completed()` запускается одноразовая background-задача
  `self._run_startup_browser_prepare()`.
- Задача вызывает `module.ensure_runtime_browser_ready(reason="post_welcome_startup")`.

3. Защита от дублей:
- `_startup_browser_prepare_started` исключает повторный запуск за одну сессию.
- На `stop()` задача корректно отменяется.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py integration/integrations/browser_use_integration.py` -> OK
- grep-проверка новых точек входа/логов -> OK

## Информация об изменениях
- Что изменено:
  - Добавлен автоматический запуск установки Chromium после приветствия.
  - Сохранен единый owner и single-flight конкурентная защита.
- Список файлов:
  - `modules/browser_automation/module.py`
  - `integration/integrations/browser_use_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-22__task-brief__auto-browser-install-after-welcome.md`
- Причина/цель изменений:
  - Соответствие требованию product UX: install начинается сразу после старта/приветствия, без первого запроса.
- Проверка:
  - Синтаксическая валидация Python и структурная проверка новых startup hooks.
