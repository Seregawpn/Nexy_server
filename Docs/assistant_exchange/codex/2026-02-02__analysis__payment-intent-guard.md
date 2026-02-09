# Payment Intent Guard

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-02
- ID (INS-###): N/A

## Diagnosis
LLM вернул команду manage_subscription на smalltalk ("как дела"), из-за чего открылся платежный менеджмент.

## Root Cause
Команда из LLM валидируется только по схеме, без проверки явного пользовательского намерения → команда пробрасывается в клиент.

## Optimal Fix
Добавить серверный guard: разрешать payment-команды только при явном intent в исходном тексте запроса.

## Verification
Запросы без explicit payment intent не должны порождать manage_subscription/buy_subscription.

## Запрос/цель
Исключить автоматическое открытие платежного менеджмента без явного запроса пользователя.

## Контекст
- Файлы: server/server/integrations/workflow_integrations/streaming_workflow_integration.py, server/server/config/prompts.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: без новых источников истины и без реархитектуры

## Решения/выводы
- Добавлен явный intent-guard на сервере перед форвардом payment-команд.

## Открытые вопросы
- Нужны ли дополнительные фразы/локализации для intent-детектора?

## Следующие шаги
- Проверить логи на кейсах smalltalk и явных запросов оплаты.
