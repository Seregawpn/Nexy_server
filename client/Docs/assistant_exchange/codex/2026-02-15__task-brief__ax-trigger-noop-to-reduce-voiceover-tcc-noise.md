# AX trigger no-op to reduce VoiceOver/TCC noise

## Context
При совместной работе Nexy и VoiceOver в unified log повторялись строки вида:
`attempted to call TCCAccessRequest for kTCCServiceAccessibility ...`.

## Root cause
В `AccessibilityProber.trigger()` вызывался `CGRequestPostEventAccess()`, который не дает надежного UX-результата, но может генерировать лишние TCC запросы/шум.

## Change
Файл: `modules/permissions/v2/probers/accessibility.py`

- Удален вызов `CGRequestPostEventAccess()` из `trigger()`.
- `trigger()` переведен в no-op с явным debug-логом.
- Источник истины для проверки Accessibility оставлен в `probe()` через `AXIsProcessTrusted()`.

## Architecture fit
- Централизация сохранена: permission status определяется только probe-контуром.
- Новые флаги/состояния не добавлены.
- Дубли путей TCC-запроса уменьшены.

## Verification
- `PYTHONPATH=. .venv/bin/python -m unittest discover -s tests -p 'test_quartz_monitor_chord_logic.py'` -> OK
- `test_permissions_v2_*` в текущем venv не запускается из-за отсутствия `pytest`.

## Expected impact
- Меньше лишних AX/TCC системных событий в логе.
- Ниже риск побочных эффектов при VoiceOver ON.
