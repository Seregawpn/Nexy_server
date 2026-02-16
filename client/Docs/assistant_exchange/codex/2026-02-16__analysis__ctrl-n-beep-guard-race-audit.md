# Ctrl+N beep guard race audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-16
- ID (INS-###): N/A

## Diagnosis
В guard lifecycle был race: `stop()` мог выполниться до `setup_on_main`, после чего отложенный setup потенциально устанавливал handler уже после остановки.

## Root Cause
Асинхронная установка через main queue без поколений состояния (`epoch`) -> out-of-order execution между install/remove -> риск "висячего" hidden item.

## Optimal Fix
Добавлен state-guard в owner-слое `InputProcessingIntegration`:
- `_ctrl_n_beep_guard_desired`
- `_ctrl_n_beep_guard_epoch`
- install block применяет изменения только если `desired=true` и `epoch` совпал.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py`
- `PYTHONPATH=. pytest -q tests/test_quartz_monitor_chord_logic.py`
- Результат: `2 passed`.

## Architecture Gates
- Single Owner Gate: owner hotkey decision не изменен.
- Zero Duplication Gate: без нового дублирующего пути.
- Anti-Race Gate: добавлен explicit state-guard (epoch).
- Flag Lifecycle Gate: runtime-флаги только локального lifecycle, без config/dead flags.
