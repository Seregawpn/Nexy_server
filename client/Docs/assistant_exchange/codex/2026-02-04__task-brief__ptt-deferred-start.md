# Summary
- Исправлен конфликт PTT с режимом PROCESSING: старт записи откладывается до SLEEPING при удержании.
- Добавлен отложенный старт записи по `app.mode_changed` при удержанном PTT.

# Changes
- `integration/integrations/input_processing_integration.py`: подписка на `app.mode_changed`, отложенный старт записи, defer при PROCESSING.

# Notes
- Не найдены обязательные документы: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.
