# Analysis: Legacy Ops Artifacts Cleanup Pass 4

## Scope
Client workspace: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client`

## Objective
Убрать из корня проекта артефакты, не участвующие в runtime/CI/release, без потери истории.

## Applied changes
1. Перенесен root cleanup script:
- from: `clean.sh`
- to: `scripts/_legacy/ops_tools/clean.sh`

2. Перенесен legacy packaging artifact:
- from: `components.plist`
- to: `_Docs_ARCHIVED/legacy_artifacts/components.plist`

3. Добавлен навигационный файл:
- `scripts/_legacy/ops_tools/README.md`

## Validation
- `clean.sh` не участвует в CI/preflight/release контурах.
- `components.plist` не используется текущим `packaging/build_final.sh` (PKG собирается через `pkgbuild` + `productbuild` с `distribution.xml`).

## Result
- Root проекта очищен от legacy-артефактов.
- История сохранена через перенос в legacy зоны.
- Риск поломки pipeline: низкий.
