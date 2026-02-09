# Prod Ready Script

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Нет единого запускаемого скрипта, который подтверждает готовность сервера к продакшену.

## Root Cause
Проверки были распределены по документам и ручным шагам.

## Optimal Fix
Создать единый скрипт `prod_ready_check.sh`, объединяющий quick_check и проверки конфигов.

## Verification
Запуск скрипта завершается успехом и печатает READY при прохождении всех проверок.

## Запрос/цель
Собрать единый скрипт готовности сервера.

## Контекст
- Файлы: `server/server/scripts/quick_check.sh`, `server/server/config.env`
- Ограничения: без изменений API.

## Решения/выводы
- Добавлен скрипт `server/server/scripts/prod_ready_check.sh`.

## Открытые вопросы
- Нужен ли обязательный gRPC smoke‑test в CI.

## Следующие шаги
- При необходимости добавить smoke‑test в CI и сделать RUN_GRPC_SMOKE=true.
