# Task Brief: Grandfathered limited mode usage tracking fix

## Context
- `SUBSCRIPTION_GRANDFATHERED_ENABLED=false` переводит `grandfathered` в limited tier.
- Логи показывали `Failed to increment usage`, из-за чего счетчики не росли и payment-flow не триггерился по лимиту.

## What was wrong
- `QuotaChecker` считал `grandfathered` лимитным (при флаге OFF).
- `SubscriptionRepository.increment_usage()` и reset queries работали только для `status='limited_free_trial'`.
- Итог: отказ инкремента + потенциальная рассинхронизация reset для grandfathered в limited-режиме.

## Changes
1. `server/server/modules/subscription/core/quota_checker.py`
- Добавлен единый owner-метод `_limited_statuses_for_usage_tracking()`:
  - `['limited_free_trial']`
  - + `grandfathered` при `grandfathered_enabled=false`.
- Этот список теперь используется в:
  - `increment_usage(...)`
  - `reset_daily_counters(...)`
  - `reset_weekly_counters(...)`
  - `reset_monthly_counters(...)`

2. `server/server/modules/subscription/repository/subscription_repository.py`
- Расширены методы параметром статусов:
  - `increment_usage(..., allowed_statuses=None)`
  - `get_subscriptions_for_daily_reset(..., limited_statuses=None)`
  - `get_subscriptions_for_weekly_reset(..., limited_statuses=None)`
  - `get_subscriptions_for_monthly_reset(..., limited_statuses=None)`
- SQL переведен на `status = ANY(%s)` вместо жесткого `status='limited_free_trial'`.
- Значение по умолчанию сохранено как `['limited_free_trial']` (backward compatible).

## Validation
- `python3 -m py_compile` для измененных файлов: OK.
- Mock smoke (PYTHONPATH=server/server):
  - при `grandfathered_enabled=false` вызовы идут с `['limited_free_trial', 'grandfathered']`;
  - при `grandfathered_enabled=true` — только `['limited_free_trial']`.

## Risks
- Низкий: поведение для legacy limited_free_trial не изменено.
- Средний: интеграционный runtime test не выполнен в `verify_payment_scenarios.py`, т.к. в текущем окружении модуль подписок выключен.
