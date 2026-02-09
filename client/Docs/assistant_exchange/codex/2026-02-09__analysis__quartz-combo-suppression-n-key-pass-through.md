# Quartz combo suppression: allow standalone N input

## Симптом
При включенном hotkey `Ctrl+N` клавиша `N` не вводилась как обычный символ.

## Root Cause
`QuartzKeyboardMonitor._handle_combo_event()` подавлял (`return None`) события:
- `flagsChanged` для `Control`,
- `N keydown/up` почти безусловно.

Это блокировало обычный ввод `N` и часть системных shortcuts.

## Изменение
- Файл: `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Новая политика suppression:
  - `Control flagsChanged` больше не блокируется (всегда пропускается),
  - `N` блокируется только если реально активируется/идет `Ctrl+N` combo,
  - одиночная `N` (`keydown/keyup` вне combo) всегда пропускается.

## Architecture Fit
- Quartz monitor остается thin low-level adapter.
- Lifecycle решений (PTT start/stop) по-прежнему в `InputProcessingIntegration`.

## Verification
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py` ✅
- `pytest -q tests/test_processing_workflow_session_guard.py` ✅
- `pytest -q tests/test_welcome_startup_sequence.py` ✅

## Expected Effect
- `N` как обычный ввод работает.
- `Ctrl+N` как PTT combo продолжает работать.
