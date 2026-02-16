# Task Brief: Grandfather текущих пользователей в бесплатный статус

## Что сделано
- Добавлен one-time скрипт:
  - `server/grandfather_current_users.py`
  - режимы: dry-run (по умолчанию) и apply (`--apply`)
  - критерий: `created_at <= cutoff-date`, исключения: `grandfathered`, `admin_active`
- Выполнен dry-run:
  - `python3 server/grandfather_current_users.py --cutoff-date 2026-02-16`
  - кандидатов: `1`
- Выполнен apply:
  - `python3 server/grandfather_current_users.py --cutoff-date 2026-02-16 --apply`
  - обновлено: `1`

## Инцидент и исправление
- По ошибке был запущен `server/manual_activate_subscription.py`, что временно изменило статус/почту одного пользователя.
- Состояние исправлено вручную:
  - статус возвращен в `grandfathered`
  - email возвращен на исходный
- Финальная проверка:
  - `python3 server/grandfather_current_users.py --cutoff-date 2026-02-16`
  - кандидатов: `0`

## Итог
- Текущие пользователи (по срезу до 2026-02-16) переведены в бесплатный неограниченный статус `grandfathered`.
- Новые пользователи после даты среза продолжают идти по обычному платному/квотному флоу.
