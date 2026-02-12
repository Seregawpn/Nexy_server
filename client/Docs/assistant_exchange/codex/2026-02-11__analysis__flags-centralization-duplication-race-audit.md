# Flags Centralization / Duplication / Race Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11

## Scope
- Централизация флагов состояния (first_run/restart_pending/update_in_progress/user_quit_intent)
- Дубли/конфликты в логике gateway/interaction_matrix/selectors
- Потенциальные гонки в restart/autostart flows

## Findings
1. **High**: `restart_pending` ось в `Snapshot` всегда `False` (`integration/core/selectors.py`), при этом `interaction_matrix.yaml` и gateway-предикаты содержат правила `app.restart_pending` / `app.first_run_restart_pending`.
2. **Medium**: Дублирование модели конфигурации автозапуска (`modules/autostart_manager/core/types.py::AutostartConfig` и `modules/autostart_manager/core/config.py::AutostartConfig`).
3. **Medium**: Матрица содержит оси/правила, частично отключенные или не реализованные в Snapshot (например, часть комментариев про disabled rules), что увеличивает риск рассинхронизации SoT.
4. **Low**: В `PermissionRestartIntegration` есть локальные флаги (`_ready_emitted`, `_ready_pending_update`, `_was_restarted_this_session`), но они являются внутренним state owner интеграции и не создают второй глобальный SoT.

## Risk summary
- Duplication risk: medium
- Conflict risk: medium
- Race risk: low-to-medium (основная гонка в autostart уже закрыта lock-guard)

## Recommended next change
- Вернуть централизованную ось `restart_pending` в Snapshot из V2 ledger (`permission_ledger.json`) через selector-функцию; убрать мертвые правила в матрице, если ось сознательно не используется.
