# Analysis: Текущее состояние квот подписки и целевой режим

## Что проверено
- Конфиг owner: `server/server/config/unified_config.py`
- Runtime gate: `server/server/integrations/workflow_integrations/streaming_workflow_integration.py`
- Subscription owner: `server/server/modules/subscription/subscription_module.py`
- Quota policy: `server/server/modules/subscription/core/quota_checker.py`
- Локальные env: `server/config.env`

## Фактическое состояние
1. По коду default лимиты:
   - daily=5, weekly=25, monthly=50 (`SubscriptionConfig`).
2. В локальном env переопределено:
   - `SUBSCRIPTION_QUOTA_DAILY=1`.
3. Но одновременно:
   - `SUBSCRIPTION_ENABLED=false`, значит модуль подписки выключен.
4. При выключенном модуле gate в workflow не применяется (`get_subscription_module() -> None`), поэтому запросы фактически не ограничиваются подпиской.

## Критический дефект
- В `SubscriptionModule.__init__` используется `self.config.pending_ttl_seconds`, но такого поля нет в `SubscriptionConfig`.
- При включении подписки это может ломать инициализацию модуля и приводить к деградации gate.

## Рекомендуемый target (минимальные изменения)
1. Исправить конфиг-модель:
   - добавить `pending_ttl_seconds` в `SubscriptionConfig` + env override.
2. Включить подписку в env:
   - `SUBSCRIPTION_ENABLED=true`
3. Установить стартовые лимиты:
   - `SUBSCRIPTION_QUOTA_DAILY=25`
   - `SUBSCRIPTION_QUOTA_WEEKLY=120`
   - `SUBSCRIPTION_QUOTA_MONTHLY=300`
4. Сохранить единый owner:
   - только `SubscriptionModule.can_process()` + `increment_usage()`.

## Проверка после правок
- Логи старта: модуль подписки initialized, scheduler started.
- На 26-м запросе за день должен приходить deny c `daily_limit_exceeded`.
- После полуночи daily counter сбрасывается по scheduler.
