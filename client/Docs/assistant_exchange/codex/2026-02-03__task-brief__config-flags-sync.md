# Task Brief: Config Feature/Kill-Switch Sync

## Scope
Синхронизация `features.*` и `ks_*` из `config/unified_config.yaml` с `Docs/FEATURE_FLAGS.md`.

## Changes
- Приведены имена фич к `features.*` (use_events_for_update_status, use_events_for_restart_pending, critical_subscriptions_fix, serial_tcc_prompts, ks_first_run_normalization).
- Добавлены `features.actions`, `features.browser_use`, `features.template_feature`, `features.ks_template_feature`.
- Добавлены `ks_avfoundation_*`, `ks_first_run_normalization`, `ks_serial_tcc`, `ks_template_feature`.
- Добавлен `NEXY_INIT` и убраны ссылочные kill-switches в V2 permission flags.

## Verification
Сверка с `unified_config.yaml`:
- MISSING_FEATURES_IN_REGISTRY: none
- MISSING_KS_IN_REGISTRY: none

## Notes
Env-флаги и config-флаги теперь синхронизированы с реестром.
