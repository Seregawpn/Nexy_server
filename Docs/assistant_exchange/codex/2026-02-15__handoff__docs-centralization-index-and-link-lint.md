# Docs Centralization: Index + Link Lint

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-15
- ID (INS-###): N/A

## Diagnosis
В root оставались дубли канонов (requirements/flags/server checklist), что создавало риск документного рассинхрона.

## Root Cause
Несколько источников истины для одних и тех же осей (root и профильные docs), плюс отсутствие единой проверки ссылок для root/server документации.

## Optimal Fix
- Root docs переведены в index-only:
  - `Docs/FEATURE_FLAGS.md`
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/PRODUCTION_CHECKLIST_SERVER.md`
- Добавлен doc-link lint для root + server docs:
  - `scripts/verify_docs_root_server_links.py`
- Для обратной совместимости добавлены redirect docs:
  - `Docs/CRM_CONSOLIDATED_RULES.md`
  - `Docs/CRM_ASSISTANT_INSTRUCTIONS.md`

## Verification
- `python3 scripts/verify_docs_root_server_links.py` → passed.
- `client/.venv/bin/python client/scripts/verify_doc_links.py` → passed.
- `pytest -q client/tests/test_gateways.py` → 13 passed.
- `server/.venv/bin/pytest -q server/server/tests/test_pr2_1_coordinator.py` → 15 passed.

## Запрос/цель
Довести централизацию документации и убрать оставшиеся конфликты/дубли.

## Контекст
- Root docs: `Docs/*.md`
- Client docs: `client/Docs/*.md`
- Server docs: `server/server/Docs/*.md`

## Решения/выводы
- Root больше не хранит дубли runtime-канонов.
- Добавлен автоматический guard на битые file-path refs для root/server docs.

## Открытые вопросы
- Нужно ли добавить вызов `scripts/verify_docs_root_server_links.py` в CI-пайплайн как обязательный gate.

## Следующие шаги
1. Подключить `scripts/verify_docs_root_server_links.py` в CI.
2. При необходимости добавить pre-commit hook для doc refs.
