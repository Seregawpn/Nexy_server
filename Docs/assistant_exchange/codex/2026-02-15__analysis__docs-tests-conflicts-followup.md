# Docs & Tests Follow-up Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-15
- ID (INS-###): N/A

## Diagnosis
После выравнивания root-архитектуры остаются конфликтующие документы/ссылки: часть root и server-документов указывает на несуществующие пути или неправильный workspace-root для команд.

## Root Cause
Главная причина — смешение двух контекстов путей:
1) запуск из репо-root,
2) запуск из `server/server` или `client`.
При этом в документах зафиксированы команды/пути без единых правил относительности.

## Optimal Fix
1. Root `Docs/PACKAGING_FINAL_GUIDE.md` перевести в index-only (ссылка на `client/Docs/PACKAGING_FINAL_GUIDE.md`) или полностью синхронизировать пути на `client/...`.
2. Root prompts (`Docs/CODEX_PROMPT.md`, `Docs/ANTIGRAVITY_PROMPT.md`) обновить ссылки на CRM документы (сейчас target-файлы отсутствуют в root).
3. `Docs/SYSTEM_CONCEPT.md` заменить `modules/grpc_service/streaming.proto` на реальный путь `server/server/modules/grpc_service/streaming.proto`.
4. `Docs/PRODUCTION_CHECKLIST_SERVER.md` исправить тест-команду: `pytest server/server/tests -q`.
5. В `server/server/Docs/*` унифицировать скриптовые пути:
   - либо все команды относительно `server/server` (`scripts/...`),
   - либо все относительно repo-root (`server/server/scripts/...`).
   Сейчас встречается смесь `server/scripts/...` и `scripts/...`, что конфликтует с реальными файлами.

## Verification
### Что проверено фактически
- `client/scripts/verify_doc_links.py` — **passed**.
- Тесты:
  - `pytest -q client/tests/test_gateways.py` → **13 passed**.
  - `server/.venv/bin/pytest -q server/server/tests/test_pr2_1_coordinator.py` → **15 passed**.
- Выявлены битые root-ссылки:
  - `Docs/CRM_CONSOLIDATED_RULES.md` (нет файла)
  - `Docs/CRM_ASSISTANT_INSTRUCTIONS.md` (нет файла)
  - `modules/grpc_service/streaming.proto` (нет такого пути в repo-root)
  - `scripts/prepare_release.sh` (нет в repo-root)
  - `scripts/validate_release_bundle.py` (нет в repo-root)
  - `packaging/build_final.sh` (в repo-root нет, фактически `client/packaging/build_final.sh`)
- Выявлен конфликт серверных script-paths:
  - Файлы реально лежат в `server/server/scripts/*`
  - Документация местами ссылается на `server/scripts/*` (для ряда скриптов путь не существует).

## Запрос/цель
Повторно проверить, соответствует ли документация тестам и есть ли дополнительные конфликтующие документы.

## Контекст
- Root docs: `Docs/*.md`
- Client docs: `client/Docs/*.md`
- Server docs: `server/server/Docs/*.md`

## Решения/выводы
- Клиентский docs-контур в целом консистентен (link-check passed).
- Основные проблемы остались в root docs (legacy ссылки) и в server docs (неконсистентные пути к скриптам/тестам).

## Открытые вопросы
- Выбрать единый стиль для server docs: команды от `repo-root` или от `server/server`.

## Следующие шаги
1. Применить пакет правок по 5 пунктам выше.
2. Добавить автопроверку path-refs для root и `server/server/Docs` (аналог client `verify_doc_links.py`).
