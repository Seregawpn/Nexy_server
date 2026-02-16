# Task Brief: browser setup TTS status messages

## Context
User requested clear assistant voice feedback when browser installation starts and when it finishes.

## Changes
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/browser_use_integration.py`.

### Added voice prompts
1. On transient setup state (`browser_setup_in_progress`):
   - TTS once per request cycle:
   - "Браузер сейчас устанавливается. Пожалуйста, подождите немного. Запросы браузерного поиска временно недоступны."
2. On first real browser start after setup was pending:
   - TTS:
   - "Браузер установился. Теперь можно использовать браузерный поиск."

## Architecture Gates
- Single Owner: install owner unchanged (`BrowserUseModule`).
- Zero Duplication: used existing `grpc.tts_request` event channel.
- Anti-Race: one-time announce flag per processing cycle (`setup_wait_announced`).
- Flag Lifecycle: no new feature flags.

## Verification
- `python3 -m py_compile integration/integrations/browser_use_integration.py` passed.
