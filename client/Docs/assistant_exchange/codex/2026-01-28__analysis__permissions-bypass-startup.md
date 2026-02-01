# Analysis: permissions bypass startup

## Context
- User question: почему приложение стартует без запроса разрешений.
- Files reviewed: `main.py`, `integration/integrations/first_run_permissions_integration.py`, `log.md`.

## Findings
- В `main.py` включается автоматический dev-bypass при запуске из терминала, выставляя `NEXY_TEST_SKIP_PERMISSIONS=1` и `NEXY_DEV_FORCE_PERMISSIONS=1`.
- В `integration/integrations/first_run_permissions_integration.py` при `NEXY_TEST_SKIP_PERMISSIONS=1` pipeline пропускается и сразу публикуются `permissions.first_run_completed` и `system.ready_to_greet`.
- Второй путь обхода: при наличии флага `permissions_first_run_completed.flag` pipeline также пропускается.
- Логи в `log.md` — системные (runningboardd/WindowServer) без Nexy-логов, поэтому запросы/skip из Nexy там не видны.

## Notes
- Required docs referenced in AGENTS instructions are missing in this workspace: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.

## Next checks (5–10 min)
- Запустить без bypass: `NEXY_DISABLE_TERMINAL_PERMISSIONS_BYPASS=1 python main.py`.
- Очистить first-run флаги: `python scripts/clear_first_run_flags.py`.
