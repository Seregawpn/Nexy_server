# Task Brief: Защита от случайной очистки данных подписок

## Контекст
Пользовательский риск: случайный запуск утилит очистки может удалить `subscriptions` и потерять grandfathered-статусы.

## Что изменено
1. `server/clear_user_data.py`
- Добавлен обязательный флаг `--allow-delete`.
- Добавлено обязательное подтверждение через env: `NEXY_CONFIRM_DESTRUCTIVE=YES`.
- Добавлен hard-block при `NEXY_ENV=production`.
- Добавлен параметр `--hardware-id` вместо захардкоженного-only сценария.

2. `server/verify_idempotency.py`
- Добавлен обязательный флаг `--allow-reset`.
- Добавлено обязательное подтверждение через env: `NEXY_CONFIRM_DESTRUCTIVE=YES`.
- Добавлен hard-block при `NEXY_ENV=production`.

## Проверка
- `python3 server/clear_user_data.py --help` — OK
- `python3 server/verify_idempotency.py --help` — OK

## Дополнительно по архитектуре
- Автоочистки `subscriptions` в runtime не обнаружено.
- В проекте есть DB hardening runbook и скрипт:
  - `server/server/Docs/DB_BACKUP_AND_RESTORE_RUNBOOK.md`
  - `server/server/scripts/harden_database_protection.sh`
  - В hardening включена trigger-защита от hard-delete для `subscriptions`, `subscription_events`, `payments`.
