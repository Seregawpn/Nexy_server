## Автор
Codex

## Запрос / Цель
Продолжить автоматизацию и добавить быстрый gate до коммита.

## Контекст
- `server/scripts/pre_commit_gate.sh`
- `server/scripts/install_pre_commit_hook.sh`
- `.git/hooks/pre-commit`

## Решение
1. Добавлен быстрый pre-commit gate:
- `server/scripts/pre_commit_gate.sh`
- Логика:
  - берет staged файлы
  - если нет staged `server/*.py` — пропускает
  - проверяет синтаксис staged Python-файлов
  - запускает basedpyright по staged файлам (если доступен)
  - запускает `pytest server/tests -q --maxfail=1`

2. Добавлен установщик pre-commit hook:
- `server/scripts/install_pre_commit_hook.sh`
- Ставит `.git/hooks/pre-commit` и подключает `pre_commit_gate.sh`.

3. Хук установлен:
- `.git/hooks/pre-commit`

## Проверка
- `bash server/scripts/pre_commit_gate.sh` (сценарий без staged Python) — корректно skip.
- `bash server/scripts/full_quality_scan.sh` — `74 passed`.

## Следующие шаги
1. Работать через обычный `git commit` — gate запускается автоматически.
2. После появления basedpyright pre-commit начнет проверять типы staged-файлов без доп. изменений.
