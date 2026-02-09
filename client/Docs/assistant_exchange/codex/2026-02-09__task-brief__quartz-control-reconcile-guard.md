# Task Brief: Quartz Control Reconcile Guard

## Context
- Симптом: во время удержания `ctrl+n` происходил ложный `DEACTIVATION TRIGGERED`, после чего шёл `RELEASE` и цепочка перехода в `PROCESSING -> SLEEPING`.
- Логи показывали рассинхронизацию: `Control: local=True, actual=False` из watchdog reconcile.

## Root Cause
- В `QuartzKeyboardMonitor._reconcile_combo_state` состояние `Control` синхронизировалось через `CGEventSourceFlagsState` даже при активной подавляемой комбинации.
- При подавлении событий этот источник временами даёт ложный `False`, что форсирует локальный `control_pressed=False` и деактивацию combo.

## Change
- Файл: `/Users/sergiyzasorin/Fix_new/client/modules/input_processing/keyboard/mac/quartz_monitor.py`
- Добавлен guard: при `self._combo_active and self._control_pressed` синхронизация `Control` через flags state пропускается (аналогично уже существующему правилу для `N`).
- Сохранена обычная reconcile-логика для неактивной комбинации и остальных случаев.

## Expected Effect
- Watchdog перестаёт ронять активную `ctrl+n` из-за ложного `Control up`.
- Уменьшаются ложные `RELEASE` и преждевременные переходы режима.

## Verification
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py integration/integrations/input_processing_integration.py integration/integrations/signal_integration.py integration/integrations/speech_playback_integration.py` — OK.
