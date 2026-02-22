# Remote Memory Health Check

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-19
- ID (INS-###): N/A

## Diagnosis
Память на удалённом сервере работает некорректно: чтение/запись user memory падает в runtime. Есть архитектурный дрейф между runtime owner памяти и состоянием PostgreSQL (права/схема).

## Root Cause
1) Кодовая причина: `MemoryAnalyzer` делает `await token_tracker.record_usage(...)`, но `TokenUsageTracker.record_usage()` синхронный и возвращает `bool` → `object bool can't be used in 'await' expression`.
2) Инфраструктурная причина: runtime DB user не имеет корректных прав на `users`, а часть таблиц отсутствует (`token_usage`, `subscriptions`) → `permission denied` и `relation does not exist`.

## Optimal Fix
Цель: восстановить стабильную работу memory pipeline без второго owner-path и локальных обходов.

Architecture Fit:
- Логика памяти остаётся в `memory_management` + `database` через `ModuleCoordinator`.
- Source of Truth по flow: `server/Docs/FLOW_INTERACTION_SPEC.md`.

Where it belongs:
- Код: `server/modules/memory_management/providers/memory_analyzer.py`
- Инфраструктура БД: миграции и grants через существующие server scripts/runbook.

Source of Truth:
- Runtime flow owner: `grpc_service/core/grpc_server.py` + `ModuleCoordinator`
- Memory owner: `MemoryManager`
- DB policy owner: `server/Docs/ARCHITECTURE_OVERVIEW.md` + `server/scripts/harden_database_protection.sh`

Breaks architecture: no

Implementation Plan:
1. Исправить вызов token tracking в `MemoryAnalyzer`: убрать `await` для sync-метода или централизованно сделать async-wrapper в одном owner.
2. На VM проверить текущего DB пользователя сервиса (`config.env`) и фактические grants на таблицы `users`, `token_usage`, `subscriptions`.
3. Применить missing migrations (`token_usage`/payment schema) и затем re-apply least-privilege/grants для app-role.
4. Перезапустить `voice-assistant`, собрать новый incident (`server/scripts/publish_server_incident_local.sh`) и сверить отсутствие memory/db ошибок за 70 минут.

Code Touchpoints:
- `server/modules/memory_management/providers/memory_analyzer.py::analyze_conversation`
- `server/integrations/core/token_usage_tracker.py::record_usage`
- `server/modules/database/providers/postgresql_provider.py::get_user_memory`
- `server/modules/database/providers/postgresql_provider.py::update_user_memory`
- `server/scripts/harden_database_protection.sh`
- `server/scripts/apply_payment_migrations.py`

Concurrency Guard (if needed):
- state-guard через существующий `MemoryWorkflowIntegration._memory_tasks` (single-flight per hardware_id), без добавления новых runtime-флагов.

What to remove / merge:
- Убрать дублирующий async-ожидатель (`await`) для sync token-tracker вызова в memory analyzer.
- Не вводить второй путь записи памяти; оставить единый owner в `MemoryManager`.

## Verification
- Шаги проверки:
  1) Запустить `server/scripts/publish_server_incident_local.sh`.
  2) Проверить latest incident в `monitor_inbox/`.
  3) Убедиться, что нет строк:
     - `Error updating user memory (upsert): permission denied for table users`
     - `Error reading records from users: permission denied for table users`
     - `Error recording token usage: relation "token_usage" does not exist`
     - `object bool can't be used in 'await' expression`

- Ожидаемое поведение:
  - memory context читается/обновляется без ошибок,
  - token usage пишется без WARN/ERROR,
  - `service_status=active`, `health_ok=yes`.

- Регрессионные проверки:
  - StreamAudio/Interrupt flow без изменений контракта (`streaming.proto` untouched),
  - нет новых флагов `use_*`/`disable_*`,
  - single owner по памяти не изменён.

## Информация об изменениях
- Что изменено:
  - Добавлен анализ текущего состояния памяти на удалённом сервере.
- Файлы:
  - `Docs/assistant_exchange/codex/2026-02-19__analysis__remote-memory-health-check.md`
- Причина/цель:
  - Зафиксировать root cause и архитектурно-совместимый plan восстановления памяти.
- Проверка:
  - Проанализированы свежие инциденты и кодовые точки памяти/БД.
  - Изменения не вносились.

## Запрос/цель
Проверить, корректно ли работает память на удалённом сервере.

## Контекст
- Файлы:
  - `monitor_inbox/2026-02-18__23-35-56__incident__server-monitor.md`
  - `server/modules/memory_management/providers/memory_analyzer.py`
  - `server/integrations/core/token_usage_tracker.py`
  - `server/modules/database/providers/postgresql_provider.py`
- Документы:
  - `server/Docs/ARCHITECTURE_OVERVIEW.md`
  - `server/Docs/FLOW_INTERACTION_SPEC.md`
  - `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
- Ограничения:
  - Без second-path и без реархитектуры.

## Решения/выводы
- Память на удалённом сервере сейчас некорректна.
- Есть 2 независимых root cause: кодовый async mismatch и DB schema/permission drift.

## Открытые вопросы
- Нет.

## Следующие шаги
- Выполнить кодовый фикс `await` mismatch.
- Привести БД VM к каноничной схеме/правам и повторить incident-check.
