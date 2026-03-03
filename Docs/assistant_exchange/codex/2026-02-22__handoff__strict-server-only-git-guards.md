# Handoff — Strict server-only git guards

## Goal
Зафиксировать режим: из данного workspace разрешён только server-срез и только remote `Seregawpn/Nexy`.

## Applied Guards
1. Удалены нецелевые remotes:
   - `origin` удалён
   - `client_test` удалён
2. Оставлен только remote:
   - `origin -> https://github.com/Seregawpn/Nexy.git`
3. Установлен локальный hook:
   - `../.git/hooks/pre-push`
   - Блокирует любой push, если remote != `origin`.
   - Блокирует push, если commit не содержит `server/main.py` (защита от root-history push).
4. Добавлен алиас безопасного пуша:
   - `git push-server` = `git subtree push --prefix=server origin`

## Verification
- `git push --dry-run origin HEAD:refs/heads/_guard_test_block` -> BLOCKED.
- `git subtree split --prefix=server ...` + dry-run push -> ALLOWED.

## Result
На локальной машине установлен жёсткий guardrail: обычный ошибочный push root-истории и push в любой другой GitHub remote технически блокируются.
