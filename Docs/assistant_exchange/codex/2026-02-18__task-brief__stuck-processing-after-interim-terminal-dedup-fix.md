# Task Brief — Fix stuck processing after interim terminal dedup

## Симптом
В hold-сценарии `voice.recognition_completed(interim=true)` мог помечать сессию как terminal. После release финальный completed (`interim=false`) отбрасывался dedup-логикой, COMMIT не запускался, UI зависал в processing/waiting_grpc.

## Root cause
`_publish_v2_completed()` вызывал `_try_mark_terminal_recognition()` для любого `result.text`, включая interim while listening.

## Fix
Файл:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/voice_recognition_integration.py`

Изменение:
- terminal mark + cancel fallback выполняются только при `is_still_listening == False`.
- interim completed продолжает публиковаться, но не маркирует terminal.

## Tests
Файл:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_voice_audio_owner_guards.py`

Добавлен тест:
- `test_v2_completed_does_not_mark_terminal_while_listening`
  - несколько interim completed проходят;
  - terminal dedup не ставится до release;
  - после release final completed становится terminal ровно один раз.

## Verification
- `pytest -q tests/test_voice_audio_owner_guards.py` → `9 passed`
- `pytest -q tests/test_grpc_client_interim_commit_gate.py` → `4 passed`
- `python3 -m py_compile ...` → OK

## Архитектурные гейты
- Single Owner: terminal owner остается release/final path.
- Zero Duplication: убран конфликт interim-vs-terminal в одном методе.
- Anti-Race: устранен out-of-order dedup drop финального completed.
