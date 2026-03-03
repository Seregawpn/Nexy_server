# Task Brief: Server Architecture PR Gates

## Scope
- Внедрены обязательные архитектурные гейты в server CI без реархитектуры runtime.

## Implemented
- Добавлен PR gate `server/scripts/verify_pr_single_owner_check.py`:
  - Проверяет обязательный блок Single Owner Check в PR body:
    - `Owner (SoT):`
    - `Duplicate Removed:`
    - `No Second Path Rationale:`
    - `Legacy Removal Date:`
- Добавлен архитектурный gate `server/scripts/verify_architecture_guards.py`:
  - Блокирует добавление `sys.path.insert(...)` в runtime-слоях.
  - Блокирует новые `legacy`-ветки без `LEGACY_REMOVE_BY: YYYY-MM-DD`.
  - Проверяет dead-flag сценарий для **новых** флагов из `unified_config.yaml` (если флаг добавлен, но не используется в runtime).
  - Проверяет runtime-ветки для флагов в изменениях: `use_*` / `disable_*` должны быть зарегистрированы в `FEATURE_FLAGS.md`.
  - Проверяет правило `one event, one owner` для `mcp.command_request` (owner: `server/integrations/core/assistant_response_parser.py`).
- Добавлен docs gate script `scripts/verify_docs_root_server_links.py`.
- Обновлен workflow `.github/workflows/server-quality.yml`:
  - `Docs link gate`
  - `PR Single Owner Check`
  - `Feature flags registry gate`
  - `Architecture guard rails`
  - `Run server quality scan`
- Обновлен PR template `.github/pull_request_template.md`:
  - Добавлен обязательный блок `Single Owner Check (Required)`.

## Validation
- Локально выполнено:
  - `python3 scripts/verify_docs_root_server_links.py` -> OK
  - `python3 server/scripts/verify_pr_single_owner_check.py` -> skip вне PR контекста
  - `python3 server/scripts/verify_architecture_guards.py` -> OK
  - `python3 server/scripts/verify_feature_flags.py` -> OK

## Notes
- Проверка `dead flag` и `runtime branch undocumented` реализована по изменениям (diff-based), чтобы не блокировать исторический технический долг и фокусироваться на новых PR.
