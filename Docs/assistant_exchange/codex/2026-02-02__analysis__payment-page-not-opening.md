# Payment Page Not Opening — Analysis

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-02
- ID (INS-###): N/A

## Diagnosis
Публикация `ui.action.buy_subscription` происходит, но подписчиков нет; PaymentIntegration не зарегистрирован. Дополнительно фиксируется дублирование обработчика `grpc.response.action` (двойной вызов одного и того же callback).

## Root Cause
PaymentIntegration отключён по умолчанию в IntegrationFactory (feature flag `payment.enabled=false`) → нет подписки на `ui.action.buy_subscription` → страница оплаты не открывается. Параллельно EventBus имеет два идентичных subscriber-а для `grpc.response.action`, что приводит к двойной публикации UI-события.

## Optimal Fix
Включить PaymentIntegration через config (`payment.enabled=true`) и добавить защиту от двойной подписки на `grpc.response.action` (idempotent subscribe или контроль единственного старта интеграции).

## Verification
1) После включения PaymentIntegration: `ui.action.buy_subscription` должен иметь ≥1 подписчик и приводить к открытию браузера. 2) `grpc.response.action` должен вызывать обработчик один раз.

## Запрос/цель
Разобрать, почему страница оплаты не открывается, и дать корректный фикс.

## Контекст
- Файлы: `client/integration/core/integration_factory.py`, `client/integration/integrations/payment_integration.py`, `client/integration/integrations/action_execution_integration.py`
- Документы: `Docs/PAYMENT_FLOW_EXPLAINED.md`

## Решения/выводы
- PaymentIntegration сейчас отключён и не подписан на UI-событие.
- Двойной callback на `grpc.response.action` указывает на дублирование подписки.

## Открытые вопросы
- Почему `grpc.response.action` имеет двух одинаковых подписчиков: двойной start или повторный create_all?

## Следующие шаги
- Включить payment feature в конфиге.
- Добавить дедуп/guard в EventBus.subscribe или в ActionExecutionIntegration.
