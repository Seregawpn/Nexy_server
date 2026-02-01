# Payment 404 Fallback Plan

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-31
- ID (INS-###): INS-008

## Diagnosis
Клиент при 404 на portal сообщает “No Subscription” и не запускает buy flow, теряя ожидаемый UX редиректа.

## Root Cause
Fallback в PaymentIntegration ограничен уведомлением, без маршрутизации в buy flow.

## Optimal Fix
Добавить централизованный fallback в client/integration/integrations/payment_integration.py: при 404 логировать редирект, показывать уведомление и вызывать open_buy_subscription().

## Verification
Проверить два сценария: без подписки (лог + редирект на checkout + уведомление), с подпиской (портал открывается).

## Запрос/цель
Сформировать корректный план изменения обработки 404 для manage subscription.

## Контекст
- Файлы: client/integration/integrations/payment_integration.py
- Документы: Docs/PAYMENT_FLOW_EXPLAINED.md, Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: без новой архитектуры, только в рамках интеграции.

## Решения/выводы
- Fallback остается в PaymentIntegration как UI-уровень реакции, Source of Truth остается сервер.

## Открытые вопросы
- Нужен ли дополнительный telemetry event при редиректе (если уже есть стандарты событий для платежей).

## Следующие шаги
- Обновить open_manage_subscription() и проверить вручную сценарии 404/200.
