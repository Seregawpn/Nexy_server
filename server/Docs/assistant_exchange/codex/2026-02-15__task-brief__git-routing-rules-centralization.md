# Task Brief: Git Routing Rules Centralization

## Context
Уточнены обязательные правила маршрутизации между `Seregawpn/Nexy`, `Seregawpn/Nexy_server` и `Seregawpn/Nexy_production`, чтобы исключить путаницу ассистентов при push/deploy/release.

## What Was Updated
- `AGENTS.md`
  - Убрана привязка к конкретной версии в путях.
  - Зафиксированы роли 3 репозиториев и запрет смешивания code/asset pipeline.
  - Сохранена каноничная команда `git subtree push --prefix=server server_repo <branch>`.
- `server/AGENTS.md`
  - Добавлен раздел `Git Routing Rules (обязательно)` для server-scope.
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
  - Раздел `Two Pipelines` заменен на `Repo Responsibilities`.
  - Явно зафиксировано: Azure deploy только из `Nexy_server`, обновление через subtree.
- `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
  - Раздел `Two Pipelines` заменен на `Repo Responsibilities`.
  - Явно зафиксировано: DMG/PKG только в `Nexy_production`.

## Result
Единый и непротиворечивый набор правил:
- `Nexy` = корневой workspace.
- `Nexy_server` = server deploy source.
- `Nexy_production` = client release assets/update URLs.

## Risk Notes
- При существующих ветках в `Nexy_server` может потребоваться выравнивание через `subtree split` + `push --force` (документировано в правилах).
