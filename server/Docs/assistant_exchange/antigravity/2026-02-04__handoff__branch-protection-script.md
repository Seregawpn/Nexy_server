## Автор
Codex

## Запрос / Цель
Включить branch protection с обязательным quality-статусом для `main/develop`.

## Контекст
- `server/scripts/enable_branch_protection.sh`
- `.github/workflows/server-quality.yml`

## Решение
Добавлен скрипт:
- `server/scripts/enable_branch_protection.sh`

Что делает:
1. Проверяет наличие `gh` и авторизацию.
2. Определяет `owner/repo` из `origin`.
3. Включает branch protection для `main` и `develop` (или переданных веток).
4. Устанавливает обязательный check:
- `Server Quality Gate / quality`
5. Дополнительно включает:
- PR review (минимум 1 approval)
- linear history
- запрет force-push/delete
- required conversation resolution

## Проверка
Локальный запуск:
- `bash server/scripts/enable_branch_protection.sh`
- Результат: остановка на проверке auth (`gh auth login` требуется).

## Следующие шаги
1. Выполнить `gh auth login`.
2. Запустить:
   - `bash server/scripts/enable_branch_protection.sh`
3. Проверить правила в GitHub: Settings -> Branches.
