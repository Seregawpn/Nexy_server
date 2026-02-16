# Review: Subscription runtime smoke после включения

## Проверки
1. Проверен процесс сервера:
- `server/server/main.py` запущен и слушает `:8080`, `:8081`, `:50051`.

2. Проверены HTTP endpoints (через локальный запрос):
- `GET /health` -> `{"status":"OK", ...}`
- `GET /api/subscription/status?hardware_id=<grandfathered>` -> статус `grandfathered`
- `GET /api/subscription/status?hardware_id=NEW_HW_TEST_001` -> `status=none`

3. Проверен runtime gate через модуль подписки:
- `grandfathered` -> `can_process.allowed=True`, reason=`unlimited_access`
- новый `hardware_id`:
  - первые 25 запросов проходят
  - 26-й запрос: `allowed=False`, reason=`daily_limit_exceeded`

## Найдено и исправлено
- Дефект в `get_subscription_status`: для `grandfathered` возвращалось `active=false`.
- Исправлено в:
  - `server/server/modules/subscription/subscription_module.py`
  - логика `active` теперь основана на tier mapping (`UNLIMITED`/`LIMITED`).
- Локальная проверка после правки:
  - `{'status': 'grandfathered', ..., 'active': True}`

## Важно
- Чтобы HTTP endpoint `/api/subscription/status` начал отдавать исправленное `active=true` в уже запущенном процессе, нужен перезапуск сервера (или hot-reload, если включен).
