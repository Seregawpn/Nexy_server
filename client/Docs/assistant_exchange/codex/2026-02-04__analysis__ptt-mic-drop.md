# Summary
- Диагностика: PTT long-press запускает запись в PROCESSING, но режим не переводится в LISTENING; затем SLEEPING от playback/processing гасит микрофон.
- Предложен фикс: отложить voice.recording_start до выхода из PROCESSING (app.mode_changed=SLEEPING) при удержании PTT.

# Key Files
- integration/integrations/input_processing_integration.py
- integration/integrations/mode_management_integration.py
- integration/workflows/listening_workflow.py

# Notes
- Не найдено: Docs/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/ANTIGRAVITY_PROMPT.md, Docs/CODEX_PROMPT.md, Docs/assistant_exchange/TEMPLATE.md (assumption logged в ответе).
