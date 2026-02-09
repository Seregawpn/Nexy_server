## Автор
Codex

## Запрос / Цель
Сделать обязательную проверку перед продакшеном и зафиксировать это в документации.

## Что изменено
1. Усилен pre-production gate:
- `server/scripts/prod_ready_check.sh`
- Теперь включает:
  - `full_quality_scan.sh` (syntax + basedpyright + pytest),
  - `verify_feature_flags.py`,
  - sanity-check `config.env`.

2. Добавлена отдельная документация:
- `server/Docs/PRE_PRODUCTION_TESTING.md`
- Описывает обязательный запуск, опциональные smoke-проверки и критерии готовности.

3. Обновлены каноничные документы:
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md` — добавлен обязательный шаг 0 (pre-production gate).
- `server/Docs/ARCHITECTURE_OVERVIEW.md` — добавлен обязательный quality gate перед продом.

4. Доведена регистрация feature flags:
- `server/Docs/FEATURE_FLAGS.md`
- Добавлены `messages_enabled` и `web_search_enabled` (требовались `verify_feature_flags.py`).

## Проверка
- `bash server/scripts/full_quality_scan.sh` → passed (`basedpyright diagnostics: 0`, `pytest: 74 passed`)
- `bash server/scripts/prod_ready_check.sh` → passed (READY)

## Следующие шаги
1. Использовать `bash server/scripts/prod_ready_check.sh` как mandatory gate перед любым production deploy.
2. Для релизов с сетевыми изменениями запускать расширенный режим:
   - `RUN_GRPC_SMOKE=true ...`
   - `RUN_WEB_SEARCH_SMOKE=true ...`
