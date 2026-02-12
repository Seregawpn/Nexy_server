# Pytest Warning Cleanup

Date: 2026-02-11
Assistant: codex
Type: task-brief

## Done
- Registered `integration` marker in `pyproject.toml` (`[tool.pytest.ini_options].markers`).
- Fixed potential coroutine leak in tray quit callback path:
  - `modules/tray_controller/core/tray_controller.py`
  - replaced `asyncio.create_task(...)` call with explicit running-loop lookup + `loop.create_task(...)`.
- Removed pytest class-collection warning source in manual script-like test file:
  - `tests/test_ctrl_n_combo.py`
  - renamed class `TestCtrlNCombo` -> `CtrlNComboTester`.

## Verification
- Command: `PYTHONPATH=. pytest -q`
- Result: `242 passed, 16 skipped`.
- Warnings: none.
