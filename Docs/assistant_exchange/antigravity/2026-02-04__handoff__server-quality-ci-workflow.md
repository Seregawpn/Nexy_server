## Автор
Codex

## Запрос / Цель
Добавить CI workflow, который запускает серверный quality gate в PR/push.

## Контекст
- `.github/workflows/server-quality.yml`
- `server/scripts/full_quality_scan.sh`

## Решение
Добавлен workflow `Server Quality Gate`:
1. Триггеры:
- `push` в `main/develop` (только при изменениях в `server/**`)
- `pull_request` в `main/develop` (только при изменениях в `server/**`)
- `workflow_dispatch`

2. Шаги job:
- checkout
- setup Python 3.13 + pip cache
- install dependencies (`server/requirements.txt`)
- install `basedpyright`
- запуск `bash server/scripts/full_quality_scan.sh`

## Проверка
- Локально `bash server/scripts/full_quality_scan.sh` проходит (`74 passed`).

## Следующие шаги
1. Открыть PR с изменениями и убедиться, что новый workflow запускается в GitHub Actions.
2. При необходимости добавить branch protection rule: merge только при green `Server Quality Gate`.
