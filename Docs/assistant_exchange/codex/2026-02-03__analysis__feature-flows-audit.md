# Feature flows audit (payments/whatsapp/messages/browser/app)

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Серьёзных гонок не обнаружено, но есть 2 логических конфликта и 2 потенциальных риска в платежной цепочке и правилах команд.

## Root Cause
Командные правила формируются в разных местах (prompt vs validator), а платёжная цепочка допускает fail‑open при неинициализированном модуле.

## Optimal Fix
Синхронизировать allowed_commands в prompt и валидаторе, и принять решение по fail‑open в payment‑модуле.

## Verification
Проверить, что buy_subscription присутствует в allowed_commands при включённой подписке; проверить поведение при enabled+not_initialized.

## Запрос/цель
Аудит функционала payment/whatsapp/messages/browser/open/close app на конфликты/дубли/гонки.

## Контекст
- Файлы: `server/config/prompts.py`, `server/config/unified_config.py`, `server/integrations/core/response_models.py`, `server/integrations/workflow_integrations/streaming_workflow_integration.py`, `server/modules/subscription/subscription_module.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: аудит без изменений

## Решения/выводы
- Конфликт: `build_system_prompt()` добавляет только `manage_subscription`, но **не** добавляет `buy_subscription`, тогда как `streaming_workflow_integration` требует `buy_subscription` и валидатор разрешает её. Это рассинхрон prompt ↔ validator.
- Риск: `SubscriptionModule.can_process()` при `enabled=True` и `initialized=False` делает **fail‑open** (разрешает доступ). Это осознанно, но критично для безопасности/платежей.
- WhatsApp/Messages/Browser/Open/Close App: на сервере нет локального исполнения, только валидация и forward — конфликтов с флагами не обнаружено.

## Открытые вопросы
- Должен ли prompt включать `buy_subscription` при включенной подписке?
- Нужно ли менять fail‑open на fail‑closed для платежей?

## Следующие шаги
- Синхронизировать allowed_commands в prompt и валидаторе.
- Принять решение по fail‑open и зафиксировать в документе/коде.
