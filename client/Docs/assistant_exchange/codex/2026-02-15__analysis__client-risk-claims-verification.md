# Проверка заявленных рисков (client)

Дата: 2026-02-15

## Scope
Проверены утверждения по файлам:
- main.py
- integration/core/event_bus.py
- integration/integrations/mode_management_integration.py
- integration/workflows/processing_workflow.py
- integration/integrations/grpc_client_integration.py
- integration/core/gateways/common.py
- integration/core/gateways/permission_gateways.py
- integration/integrations/permission_restart_integration.py

## Вердикт по пунктам

1. Два entrypoint с разной логикой путей (`main.py` 16-23 и 57-66)
- Частично некорректно сформулировано.
- 16-23: это ранний PyObjC fix (не path/entrypoint ветка).
- 57-66: реальная path-инициализация и приоритеты `sys.path`.
- Два реальных runtime-entry режима есть в `__main__`: diagnostics и обычный запуск (`main.py` 423-441), но path-логика задается единоразово до этого.

2. Недетерминированная обработка `app.mode_changed`
- Подтверждено.
- `EventBus._fast_events` включает `app.mode_changed` (`event_bus.py` 31-33).
- Для fast events async callback’и запускаются fire-and-forget через `create_task`/`run_coroutine_threadsafe` без `await` (`event_bus.py` 203-231).
- При этом подписчики содержат предположение о последовательности (`mode_management_integration.py` 247, `processing_workflow.py` 154).

3. Дубли управления processing lifecycle между ModeManagement и ProcessingWorkflow
- Подтверждено (частично архитектурно осознанно, но риск есть).
- ModeManagement ведет runtime-карты lifecycle (`_active_*`, `_deferred_sleep_sessions`) и публикует `mode.request` на sleeping (`mode_management_integration.py` 92-102, 640-747).
- ProcessingWorkflow параллельно ведет собственный lifecycle state/flags/stage и тоже публикует `mode.request` на sleeping (`processing_workflow.py` 51-71, 727-771).
- Есть дедуп-гарды, но два владельца финализации остаются.

4. Legacy/fallback runtime пути
- Подтверждено, но риск разной степени:
  - `grpc_client_integration.py` содержит compatibility путь для action через `text_chunk_legacy` (1006-1039).
  - `gateways/common.py` и `permission_gateways.py` имеют fallback_to=legacy при exception в engine (common.py 83-88 и др.; permission_gateways.py 213-218 и др.).
  - `permission_restart_integration.py` держит legacy ветки под freeze-гейтом `_legacy_restart_paths_frozen()` (например 108-112, 128-142, 223-251, 836-838).
- Важная оговорка: часть legacy путей уже заморожена при V2 и не активна одновременно в нормальном happy-path.

## Дополнительно
- Из обязательных для сверки документов в этом workspace отсутствуют:
  - Docs/ASSISTANT_COORDINATION_PROTOCOL.md
  - Docs/CODEX_PROMPT.md
  - Docs/ANTIGRAVITY_PROMPT.md
  - Docs/assistant_exchange/TEMPLATE.md
- Использованы доступные: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md.
