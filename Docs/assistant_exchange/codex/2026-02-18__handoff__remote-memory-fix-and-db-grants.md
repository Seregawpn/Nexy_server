# Remote Memory Fix and DB Grants

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-18
- ID (INS-###): N/A

## Diagnosis
На удалённом сервере memory pipeline падал из-за двух причин: async mismatch в `memory_analyzer` и DB drift (отсутствующие таблицы/права runtime-role).

## Root Cause
- Код: `await` над sync `TokenUsageTracker.record_usage()` → `object bool can't be used in 'await' expression`.
- Инфраструктура: отсутствовали `token_usage`/`subscriptions` и не были выданы корректные grants runtime-role `voice_assistant_user`.

## Optimal Fix
- В коде убран `await` в вызове `token_tracker.record_usage`.
- На VM созданы/проверены таблицы `token_usage`, `subscriptions`.
- Для `voice_assistant_user` применены grants `SELECT/INSERT/UPDATE` + sequence/function privileges.
- Сервис `voice-assistant` перезапущен.

## Verification
- Локально: `python3 -m py_compile server/modules/memory_management/providers/memory_analyzer.py`.
- VM:
  - Проверены таблицы: `users`, `token_usage`, `subscriptions` существуют.
  - Проверены права: `users_select=true`, `users_update=true`, `token_usage_insert=true`, `subscriptions_select=true`.
  - `systemctl is-active voice-assistant` => `active`.
  - `/health` => `{"status":"OK"...}`.
  - `bash server/scripts/publish_server_incident_local.sh` => `NO_NEW_INCIDENT`.
  - Журнал после restart не содержит memory/db ошибок из инцидента.

## Информация об изменениях
- Что изменено:
  - Исправлен async mismatch в memory analyzer.
  - На удалённой VM применён SQL fix для schema + grants (runtime).
- Файлы:
  - `server/modules/memory_management/providers/memory_analyzer.py`
  - `Docs/assistant_exchange/codex/2026-02-18__handoff__remote-memory-fix-and-db-grants.md`
- Причина/цель:
  - Восстановить корректную работу памяти на удалённом сервере без second-path.
- Проверка:
  - Локальная компиляция Python файла.
  - Remote health/log/incident проверки через Azure Run Command.

## Запрос/цель
Исправить некорректную работу памяти на удалённом сервере.

## Контекст
- `monitor_inbox/2026-02-18__23-35-56__incident__server-monitor.md`
- `server/modules/memory_management/providers/memory_analyzer.py`
- `server/integrations/core/token_usage_tracker.py`
- `server/modules/database/providers/postgresql_provider.py`

## Решения/выводы
- Память восстановлена на runtime уровне: критичные причины инцидента закрыты.

## Открытые вопросы
- Желательно синхронизировать `/home/azureuser/voice-assistant/config.env` с systemd env, чтобы убрать drift `DB_USER` (`nexy_user` vs `voice_assistant_user`).

## Следующие шаги
- Деплойнуть коммит с кодовым фиксом в `Nexy`, чтобы правка на VM не была только hotfix.
