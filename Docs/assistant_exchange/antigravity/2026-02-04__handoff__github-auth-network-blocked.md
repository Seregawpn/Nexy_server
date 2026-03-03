## Автор
Codex

## Запрос / Цель
Продолжить и применить branch protection через `gh`.

## Контекст
- `server/scripts/enable_branch_protection.sh`

## Что сделано
1. Проверил, есть ли токен в окружении (`GH_TOKEN` / `GITHUB_TOKEN`) — не найден.
2. Попытался выполнить вход:
   - `gh auth login --hostname github.com --git-protocol https --web`

## Результат
Команда не выполнена из-за сетевого ограничения:
- `error connecting to github.com`

## Следующие шаги
1. Когда будет сетевой доступ:
   - `gh auth login`
2. Затем применить protection:
   - `bash server/scripts/enable_branch_protection.sh`
