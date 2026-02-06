# Disable Auto-Open Settings For Accessibility

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-05
- ID (INS-###): INS-005

## Diagnosis
Accessibility шаг в V2 permissions открывает System Settings автоматически при первом запуске.

## Root Cause
Конфиг `permissions_v2.steps.accessibility` задан как `mode: open_settings`, что приводит к автозапуску Settings в оркестраторе.

## Optimal Fix
Перевести accessibility в `auto_dialog` без `settings_target`, чтобы исключить автозапуск Settings.

## Verification
Проверить, что при первом запуске Settings не открывается на шаге Accessibility.

## Запрос/цель
Убрать автозапуск System Settings для Accessibility при первом запуске.

## Контекст
- Файлы: `config/unified_config.yaml`
- Документы: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`
- Ограничения: без изменения архитектуры и без новых источников истины

## Решения/выводы
- Изменен режим шага accessibility в конфиге.

## Открытые вопросы
- Нужно ли предусмотреть ручной триггер открытия Settings для Accessibility?

## Следующие шаги
- При необходимости добавить явный пользовательский триггер открытия Settings.
