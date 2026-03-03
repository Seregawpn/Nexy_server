## Автор
Codex

## Запрос / Цель
Включить `basedpyright`, запустить полный скан и исправить найденные проблемы.

## Что сделано
1. Установлен `basedpyright` в `.venv`:
- `./.venv/bin/pip install basedpyright`

2. Выполнен полный прогон:
- `bash server/scripts/full_quality_scan.sh`

3. Исправлены ошибки в production-коде:
- `server/config/prompts.py`
- `server/api/webhooks/stripe_webhook.py`
- `server/modules/subscription/providers/stripe_service.py`
- `server/modules/subscription/subscription_module.py`
- `server/modules/subscription/core/quota_checker.py`
- `server/modules/subscription/repository/subscription_repository.py`
- `server/integrations/core/response_models.py`
- `server/modules/update/config.py`
- `server/modules/interrupt_handling/adapter.py`
- `server/modules/interrupt_handling/core/interrupt_manager.py`
- `server/updates/scripts/sign_file.py`

## Результат
После фиксов:
- `pytest`: `74 passed`
- basedpyright diagnostics: `159 -> 97`
- Важное: **в production-коде (`server/` без `server/scripts/`) ошибок basedpyright больше нет**
- Остаток диагностик целиком в `server/scripts/*` (вспомогательные/диагностические скрипты)

## Следующие шаги
1. Решить стратегию для `server/scripts/*`:
   - либо довести их типизацию до чистого basedpyright,
   - либо явно исключить ad-hoc скрипты из строгого type-check policy.
