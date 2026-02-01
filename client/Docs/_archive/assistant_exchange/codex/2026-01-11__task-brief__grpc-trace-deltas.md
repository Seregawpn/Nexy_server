# Author
Codex

# Request/Goal
Добавить минимальные логи/тайминги, чтобы измерять задержку между `recording.stop` → `grpc.start` → `grpc.response`.

# Context
- `integration/integrations/grpc_client_integration.py`
- Архитектура: `_Docs_ARCHIVED/ARCHITECTURE_OVERVIEW.md`
- Требования: `_Docs_ARCHIVED/PROJECT_REQUIREMENTS.md`

# Decisions/Findings
- Добавлена подписка на `voice.recording_stop` для фиксации ts по session_id.
- В `grpc.start` лог добавлена дельта от `recording.stop`.
- В `grpc.response` (первый chunk) лог добавлена дельта от `grpc.start`.

# Open Questions
- Нужны ли дельты до `playback.start` для полной цепочки?

# Next Steps
- Запустить одну сессию и проверить дельты по TRACE в логе.
