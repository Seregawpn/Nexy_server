# Summary
- Добавлены guard’ы от повторной отмены и блокировка сигналов в окне cancel.
- Добавлен cooldown на CANCEL‑сигнал, чтобы не запускать playback сразу после отмены.

# Changes
- `integration/integrations/speech_playback_integration.py`: cancel dedup + signal block.
- `integration/integrations/signal_integration.py`: cooldown для CANCEL.

# Notes
- Не найдены обязательные документы: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.
