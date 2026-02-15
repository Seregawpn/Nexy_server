# Docs Conflicts Cleanup Pass 2

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-15
- ID (INS-###): N/A

## Diagnosis
В документации оставались битые ссылки и конфликтующие пути выполнения (root vs client vs server/server), из-за чего часть команд/ссылок не воспроизводилась.

## Root Cause
Наслоение legacy-доков + разные предположения о текущей рабочей директории для команд.

## Optimal Fix
- Root `Docs/PACKAGING_FINAL_GUIDE.md` переведён в index-only.
- Добавлены root redirect-файлы:
  - `Docs/CRM_CONSOLIDATED_RULES.md`
  - `Docs/CRM_ASSISTANT_INSTRUCTIONS.md`
- Исправлены пути:
  - `Docs/SYSTEM_CONCEPT.md` (proto path)
  - `Docs/PRODUCTION_CHECKLIST_SERVER.md` (pytest path)
- Нормализованы server docs:
  - `server/server/Docs/DB_BACKUP_AND_RESTORE_RUNBOOK.md`
  - `server/server/Docs/ARCHITECTURE_OVERVIEW.md`
  - `server/server/Docs/GRPC_PROTOCOL_AUDIT.md`
  - `server/server/Docs/SERVER_DEVELOPMENT_RULES.md`
  - `server/server/Docs/VERSION_MANAGEMENT.md`
  - `server/server/Docs/PRODUCT_CONCEPT.md`
  - `server/server/Docs/SERVER_PROTOBUF_SPECIFICATION.md`

## Verification
- `client/scripts/verify_doc_links.py` — passed.
- `pytest -q client/tests/test_gateways.py` — 13 passed.
- `server/.venv/bin/pytest -q server/server/tests/test_pr2_1_coordinator.py` — 15 passed.
- Повторный path-scan root/server docs больше не показывает критичных битых file-path refs.

## Запрос/цель
Исправить оставшиеся конфликты документации и валидацию тестовых инструкций.

## Контекст
- Root docs: `Docs/*.md`
- Client docs: `client/Docs/*.md`
- Server docs: `server/server/Docs/*.md`

## Решения/выводы
- Конфликт между root и каноническими client/server документами снижен.
- Server docs приведены к более единообразным путям скриптов/тестов.

## Открытые вопросы
- Нужен ли отдельный серверный линтер ссылок (по аналогии с client `verify_doc_links.py`) для CI.

## Следующие шаги
1. Добавить CI-проверку ссылок для root + server docs.
2. При необходимости унифицировать оставшиеся semantic refs (`VERSION`, endpoint refs) в отдельном проходе.
