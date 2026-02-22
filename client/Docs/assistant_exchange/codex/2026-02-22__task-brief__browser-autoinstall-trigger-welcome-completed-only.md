# Browser Auto-Install Trigger: welcome.completed only

## Context
Уточнен startup trigger автозагрузки браузера: запуск только после успешного приветствия.

## Diagnosis
Был конфликт owner-path: `welcome.failed` тоже вызывал `_on_welcome_completed`, что нарушало контракт "после воспроизведенного приветствия".

## Implementation
- Удалена подписка:
  - `welcome.failed -> _on_welcome_completed`
- Оставлена только:
  - `welcome.completed -> _on_welcome_completed`

## Verification
- `python3 -m py_compile integration/integrations/browser_use_integration.py` -> OK
- grep:
  - `welcome.completed` есть
  - `welcome.failed` отсутствует в подписках BrowserUseIntegration

## Информация об изменениях
- Что изменено:
  - Убран конфликтный startup trigger автозагрузки браузера.
- Список файлов:
  - `integration/integrations/browser_use_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-22__task-brief__browser-autoinstall-trigger-welcome-completed-only.md`
- Причина/цель изменений:
  - Соблюсти требование запуска установки только после реального приветствия.
- Проверка:
  - Синтаксическая валидация и проверка подписок.
