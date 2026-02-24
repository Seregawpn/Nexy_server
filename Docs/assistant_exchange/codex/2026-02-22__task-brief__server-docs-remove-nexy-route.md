# Task Brief — Remove `Seregawpn/Nexy` Route From Server Workspace Docs

## Context
Пользователь зафиксировал правило: из текущей директории `server` не использовать `Seregawpn/Nexy`; использовать только `Seregawpn/Nexy`.

## Changes
1. Обновлены Git Routing Rules в `AGENTS.md`:
   - удалены упоминания `Seregawpn/Nexy` как рабочего push-path;
   - зафиксирован единственный допустимый remote: `Seregawpn/Nexy`.
2. Обновлены Git Routing Rules в `server/AGENTS.md`:
   - удалён блок `Seregawpn/Nexy`;
   - оставлен только `Seregawpn/Nexy` и запрет на push в другие GitHub-репозитории.
3. Обновлён `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`:
   - в разделе Repo Responsibilities оставлен только `Seregawpn/Nexy`;
   - добавлен явный запрет push в другие репозитории из этой директории.

## Verification
- Поиск `Seregawpn/Nexy` в активных документах (без `_archive` и `assistant_exchange`) возвращает 0 совпадений.

## Result
Source of truth для server Git routing в этой директории централизован: только `Seregawpn/Nexy`.
