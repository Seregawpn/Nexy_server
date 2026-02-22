# Browser Install UX: Start + Complete Only

## Context
Уточнен UX установки браузера: сообщать только о начале и завершении скачивания, без промежуточных сообщений и без "ready" в сценарии, когда браузер уже установлен.

## Implementation
- Обновлен обработчик install-status в `BrowserUseIntegration`:
  - `started` -> `Browser download started.`
  - `downloading` -> без пользовательских уведомлений/озвучки
  - `completed` -> `Browser download complete. You can use browser now.` только если ранее был `started`
  - `already_installed` -> молчаливо (без "ready" сообщения)
  - `failed` -> ошибка установки
- Добавлен локальный guard-флаг `_browser_install_started_announced` для исключения ложных "complete" без реального старта скачивания.

## Verification
- `python3 -m py_compile integration/integrations/browser_use_integration.py` -> OK
- grep-проверка строк сообщений -> только start/complete для download UX.

## Информация об изменениях
- Что изменено:
  - Упрощен UX до двух событий: старт и завершение скачивания.
  - Убраны промежуточные прогресс-фразы и уведомление "готов" для already-installed.
- Список файлов:
  - `integration/integrations/browser_use_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-22__task-brief__browser-install-ux-start-complete-only.md`
- Причина/цель изменений:
  - Соответствие продукт-требованию: минимальный и недвусмысленный install UX.
- Проверка:
  - Синтаксическая валидация Python и проверка текстов уведомлений.
