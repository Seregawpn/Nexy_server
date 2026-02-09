## Task
Нестабильные сигналы при `shortcut` и отсутствие сигнала при переходе в `SLEEPING`.

## Diagnosis
- `SignalIntegration` не использовал `app.mode_changed` как источник истины для UI-cues.
- `_on_mode_changed` был пустым.
- `CANCEL` часто подавлялся (`cooldown` + reason-filter), поэтому reset не всегда давал звук.

## Implemented Fix
1. Централизация на mode transitions:
   - Подписка на `app.mode_changed` в `SignalIntegration`.
   - `LISTENING` -> emit `LISTEN_START`.
   - Переход в `SLEEPING` из любого не-sleeping -> emit `DONE`.

2. Устойчивый reset-cue:
   - Подписка на `keyboard.short_press`.
   - Прямой emit `CANCEL` c локальным cooldown-guard.

3. Снижен риск "не всегда слышно" из-за длинных cooldown:
   - `LISTEN_START`: 600ms -> 250ms
   - `DONE`: 2000ms -> 400ms
   - `CANCEL`: 150ms -> 200ms

4. Убран reason-based skip в `playback.cancelled` для `CANCEL`, оставлен только cooldown guard.

## Files
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/signal_integration.py`

## Architecture Fit
- Source of Truth для переходов режимов: `app.mode_changed` (ModeManagement/StateManager).
- Сигналы теперь следуют централизованному маршруту режимов, без локального "второго пути".

## Validation
- `python3 -m py_compile integration/integrations/signal_integration.py` — успешно.
