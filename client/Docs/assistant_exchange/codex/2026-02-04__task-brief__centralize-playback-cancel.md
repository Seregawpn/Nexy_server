# Summary
- Централизована публикация `playback.cancelled` в SpeechPlaybackIntegration.
- Убраны прямые публикации cancel из InterruptManagement и ActionExecution, заменены на `grpc.request_cancel`.

# Changes
- `integration/integrations/interrupt_management_integration.py`
- `integration/integrations/action_execution_integration.py`

# Notes
- Не найдены обязательные документы: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.
