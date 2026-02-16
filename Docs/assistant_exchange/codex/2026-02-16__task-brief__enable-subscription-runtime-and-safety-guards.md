# Task Brief: Enable subscription runtime + safety guards

## Выполнено
1. Включен subscription runtime:
- `server/config.env`:
  - `SUBSCRIPTION_ENABLED=true`
  - `SUBSCRIPTION_TRIAL_DAYS=0`
  - `SUBSCRIPTION_PENDING_TTL=30`
  - `SUBSCRIPTION_QUOTA_DAILY=25`
  - `SUBSCRIPTION_QUOTA_WEEKLY=125`
  - `SUBSCRIPTION_QUOTA_MONTHLY=500`

2. Закрыт конфиг-дефект, который ломал инициализацию subscription модуля:
- `server/server/config/unified_config.py`:
  - добавлено поле `pending_ttl_seconds: int = 30`
  - добавлен env mapping `SUBSCRIPTION_PENDING_TTL`

3. Дозащищен destructive admin script:
- `server/manual_activate_subscription.py`:
  - обязательный флаг `--allow-update`
  - обязательный confirm token: `NEXY_CONFIRM_DESTRUCTIVE=YES`
  - блокировка при `NEXY_ENV=production`
  - параметры `--hardware-id`, `--email`

## Проверки
- `python3 server/manual_activate_subscription.py --help` — OK
- Проверка значений в `config.env` и `unified_config.py` — OK

## Эффект
- Монетизация активируется в runtime.
- Убрана точка падения на `pending_ttl_seconds`.
- Снижен риск случайной ручной мутации подписок.
