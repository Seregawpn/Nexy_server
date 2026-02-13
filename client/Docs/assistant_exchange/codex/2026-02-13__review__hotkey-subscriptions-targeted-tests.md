# Review — hotkey/subscriptions targeted tests

## Scope
Проверка после правок в VoiceOver keyboard subscription path:
- dedup subscriptions;
- safe default `engage_on_keyboard_events=false`;
- отсутствие регрессии в hotkey combo contract.

## Executed
1. `PYTHONPATH=. pytest -q tests/test_quartz_monitor_chord_logic.py tests/test_coordinator_critical_subscriptions.py`

## Result
- `7 passed in 2.56s`

## Coverage notes
- Покрыто:
  - strict combo suppression contract (`Ctrl+N` owner path),
  - критичные coordinator subscriptions (регрессии после dedup правок не выявлены).
- Не покрыто этим прогоном:
  - GUI/runtime smoke для `Cmd+Space`/Alfred/VoiceOver ON/OFF (требует ручного системного теста на macOS UI).
