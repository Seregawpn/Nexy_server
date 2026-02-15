# CI Docs Link Gate Enable

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-15
- ID (INS-###): N/A

## Diagnosis
После централизации docs отсутствовал обязательный CI-gate для root/server ссылок, поэтому риск повторного дрейфа оставался.

## Root Cause
Проверка ссылок существовала только для client docs (`client/scripts/verify_doc_links.py`), но не покрывала root и server/server docs.

## Optimal Fix
- Добавлен скрипт: `scripts/verify_docs_root_server_links.py`.
- Подключен в CI:
  - `client/.github/workflows/ci.yml` (job `pre-build-gate`)
  - `server/.github/workflows/server-quality.yml` (job `quality`)

## Verification
- `python3 scripts/verify_docs_root_server_links.py` → passed.
- Workflow-файлы содержат шаг `Docs link gate (root + server)`.

## Контекст
- CI workflows:
  - `client/.github/workflows/ci.yml`
  - `server/.github/workflows/server-quality.yml`
- Script:
  - `scripts/verify_docs_root_server_links.py`

## Следующие шаги
1. Зафиксировать branch protection, что CI jobs с docs-gate обязательны.
2. При необходимости добавить этот gate в pre-commit.
