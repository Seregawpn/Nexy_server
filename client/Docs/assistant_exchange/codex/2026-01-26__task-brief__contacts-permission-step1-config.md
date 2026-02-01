# Contacts Permission Step 1 — Config Check

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-26
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Контакты должны быть включены в `permissions_v2.order` и иметь шаг `steps.contacts` в конфиге.

## Root Cause
Без этих записей Contacts шаг не запускается и диалог не появляется.

## Optimal Fix
Проверить, что `config/unified_config.yaml` содержит корректный порядок и шаг для contacts.

## Verification
- `permissions_v2.order` включает `contacts`.
- `permissions_v2.steps.contacts` = `mode: auto_dialog`.

## Запрос/цель
Начать с первого этапа — проверка конфигурации.

## Контекст
- Файлы: config/unified_config.yaml

## Решения/выводы
- `permissions_v2.order` содержит `contacts`.
- `steps.contacts` задан, `mode: auto_dialog`, `criticality: hard`.

## Открытые вопросы
- Нет.

## Следующие шаги
- Перейти к проверке Info.plist (`NSContactsUsageDescription`).
