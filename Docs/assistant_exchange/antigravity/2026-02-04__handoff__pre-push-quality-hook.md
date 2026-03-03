## Автор
Codex

## Запрос / Цель
Продолжить автоматизацию quality-процесса, чтобы проверки запускались перед каждым push.

## Контекст
- `server/scripts/install_quality_hook.sh`
- `.git/hooks/pre-push`
- `server/scripts/full_quality_scan.sh`

## Решение
1. Добавлен установщик git-хука:
- `server/scripts/install_quality_hook.sh`
- Скрипт ставит `.git/hooks/pre-push` и делает его исполняемым.

2. Хук `pre-push`:
- Автоматически запускает `bash server/scripts/full_quality_scan.sh`
- Блокирует push при ошибках syntax/tests/type-check (если basedpyright доступен).

## Проверка
- Хук успешно установлен:
  - `.git/hooks/pre-push`
- Содержимое хука проверено (`cat .git/hooks/pre-push`).

## Следующие шаги
1. Работать в обычном режиме `git push` — quality-gate будет запускаться автоматически.
2. Когда появится basedpyright, hook автоматически начнет включать type-check без дополнительных изменений.
