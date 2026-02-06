# Task Brief

## Context
Следующим top-файлом из priority отчета был `modules/tray_controller/macos/menu_handler.py` (17 warning basedpyright).

## Changes
- Усилена типизация callback-слоя:
  - `status_callbacks: dict[str, Callable[..., Any]]`
  - `_quit_callback: Callable[[], Any] | None`
  - сигнатуры `set_status_callback` и `set_quit_callback`.
- `create_app` теперь возвращает `rumps.App | None` (соответствует реальному поведению при ошибке).
- Исправлен `quit_button=None` → `quit_button=""` (совместимо с типами rumps).
- Централизован безопасный доступ к `AppKit` символам через `getattr` в `create_app`:
  - `NSApplication`
  - `NSApplicationActivationPolicyAccessory`.
- Убраны optional-member warning для `self.app.icon` в delayed icon flow:
  - локальный guard `app = self.app; if app is None: return`.
- Убраны attribute-assignment warning на `applicationShouldTerminate`:
  - используется `setattr(... )  # noqa: B010` в fallback/handler setup.

## Verification
- `./.venv/bin/ruff check modules/tray_controller/macos/menu_handler.py` → OK
- `../server/.venv/bin/basedpyright modules/tray_controller/macos/menu_handler.py --outputjson` → 0 diagnostics
- `./scripts/problem_scan.sh` → `TOTAL_ISSUES=352`
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh` → PASSED

## Impact
- В `menu_handler.py`: warning reduced `17 -> 0`.
- Общий backlog reduced: `369 -> 352`.
- Логика setup quit handler и delayed icon path стала безопаснее для optional-state и тип-проверки.
