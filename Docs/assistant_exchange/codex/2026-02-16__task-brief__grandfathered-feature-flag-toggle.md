# Task Brief: Feature flag для grandfathered free-usage

## Что добавлено
- Новый env flag: `SUBSCRIPTION_GRANDFATHERED_ENABLED`
  - `true` (default): `grandfathered` => unlimited access
  - `false`: `grandfathered` больше не unlimited, работает как limited tier (квоты)

## Измененные файлы
- `server/server/config/unified_config.py`
  - `SubscriptionConfig.grandfathered_enabled: bool = True`
  - env mapping из `SUBSCRIPTION_GRANDFATHERED_ENABLED`
- `server/server/modules/subscription/core/subscription_types.py`
  - `map_status_to_tier(status, grandfathered_enabled=True)`
  - special-case для `grandfathered` при `flag=false` -> `LIMITED`
- `server/server/modules/subscription/core/quota_checker.py`
  - оба вызова `map_status_to_tier(...)` теперь с `grandfathered_enabled=self.config.grandfathered_enabled`
- `server/server/modules/subscription/subscription_module.py`
  - tier mapping в `get_subscription_status` и `get_context_for_prompt` теперь учитывает флаг
- `server/server/integrations/workflow_integrations/streaming_workflow_integration.py`
  - выбор `manage_subscription` vs `buy_subscription` теперь через tier mapping с флагом
- `server/config.env`
  - добавлено: `SUBSCRIPTION_GRANDFATHERED_ENABLED=true`

## Проверка
- `FLAG_ON` => `allowed=True`, `reason=unlimited_access`, `status=grandfathered`
- `FLAG_OFF` => `allowed=True`, `reason=within_quota`, `status=grandfathered`

## Использование
- Включить бесплатный grandfathered:
  - `SUBSCRIPTION_GRANDFATHERED_ENABLED=true`
- Выключить бесплатный grandfathered:
  - `SUBSCRIPTION_GRANDFATHERED_ENABLED=false`
- После изменения env требуется перезапуск сервера.
