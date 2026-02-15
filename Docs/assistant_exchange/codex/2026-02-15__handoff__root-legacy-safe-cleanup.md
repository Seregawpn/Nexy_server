# Root Legacy Safe Cleanup

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-15
- ID (INS-###): N/A

## Diagnosis
В root оставались legacy markdown/python/test файлы без использования в активных канонах, скриптах и CI.

## Root Cause
Исторические артефакты не были удалены после миграции к канонам `client/Docs` и `server/server/Docs`.

## Optimal Fix
Удалён safe-list неиспользуемых root-файлов:
- `CHECK_STATUS.md`
- `CLEANUP_ANALYSIS.md`
- `CLIENT_SERVER_CLEANUP_PLAN.md`
- `PROBLEM_ANALYSIS.md`
- `test_client_server_full.py`
- `test_production_server.py`
- `test_server_quick.py`
- `verify_browser_config.py`
- `verify_fix.py`
- `check_my_location.py`
- `debug_whatsapp_config.py`

## Verification
- `python3 scripts/verify_docs_root_server_links.py` → passed
- `client/.venv/bin/python client/scripts/verify_doc_links.py` → passed
- `pytest -q client/tests/test_gateways.py` → 13 passed
- `server/.venv/bin/pytest -q server/server/tests/test_pr2_1_coordinator.py` → 15 passed

## Запрос/цель
Очистить лишние root-файлы, не участвующие в текущем процессе.

## Контекст
- Root docs/scripts/tests
- Каноны: `client/Docs/*`, `server/server/Docs/*`

## Решения/выводы
Удалённые файлы не влияли на текущий CI/tests/docs-gates.

## Открытые вопросы
Следующий этап: решить судьбу legacy `server/Docs` после полной миграции ссылок из `server/server/Docs`.

## Следующие шаги
1. Отдельным проходом мигрировать все `server/Docs/...` алиасы в `server/server/Docs/...`.
2. После миграции удалить legacy `server/Docs` (кроме нужных workflow-артефактов).
