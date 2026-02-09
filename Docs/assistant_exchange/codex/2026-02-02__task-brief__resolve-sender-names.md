# Resolve sender names in read_messages

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-02
- ID (INS-###): N/A

## Diagnosis
read_messages озвучивал номер/handle в sender без резолвинга имени.

## Root Cause
formatted_messages.sender формировался без contact_resolver.

## Optimal Fix
Добавлен resolve_contact для sender (кроме from_me), чтобы озвучивать display_label при наличии.

## Verification
read_messages должен возвращать sender с именем контакта, если оно есть в адресной книге.

## Запрос/цель
Озвучивать имя контакта вместо номера телефона.

## Контекст
- Файл: client/integration/integrations/action_execution_integration.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md

## Решения/выводы
- Sender label резолвится через contact_resolver.

## Открытые вопросы
- Нужно ли кэшировать резолвинг sender для больших выборок.

## Следующие шаги
- Проверить read_messages на контактах с именем и без имени.
