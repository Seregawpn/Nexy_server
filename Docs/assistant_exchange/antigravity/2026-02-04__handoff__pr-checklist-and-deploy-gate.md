## Автор
Codex

## Запрос / Цель
Сделать процесс устойчивее: добавить PR checklist и гарантировать, что deploy выполняется только после quality gate.

## Что сделано
1. Добавлен PR template:
- `.github/pull_request_template.md`
- Включает обязательные пункты:
  - `full_quality_scan.sh`
  - `prod_ready_check.sh`
  - `verify_feature_flags.py` (если меняли флаги)
  - обновление документации и регрессионных тестов

2. Обновлены deploy workflows:
- `.github/workflows/deploy-to-azure.yml`
- `.github/workflows/deploy.yml`

В оба workflow добавлен job `quality` (server quality scan), а `deploy` теперь имеет `needs: [quality]`.

## Проверка
- YAML workflows валидны (успешный `yaml.safe_load` для всех workflow файлов).
- `bash server/scripts/full_quality_scan.sh` проходит:
  - basedpyright diagnostics: 0
  - pytest: 74 passed

## Следующие шаги
1. Включить branch protection rule с обязательным статусом `Server Quality Gate / quality`.
2. Использовать PR checklist как обязательный gate в code review.
