# Task Brief

## Context
Следующим приоритетным файлом в warning backlog был `modules/screenshot_capture/macos/simple_bridge.py` (24 warning basedpyright).

## Changes
- Централизован импорт pyobjc-символов в верхней части файла через `getattr(...)`:
  - `AppKit`/`Quartz` грузятся как модули,
  - runtime-символы (`CGDisplayCreateImage`, `NSBitmapImageRep` и т.д.) извлекаются безопасно,
  - убран constant redefinition (`_COREGRAPHICS_AVAILABLE` -> `_coregraphics_available`).
- Добавлены guard-условия перед CoreGraphics-путем:
  - fallback на `screencapture` при недоступных нативных символах.
- Убран локальный импорт Quartz внутри `_resize_cgimage_if_needed`, использованы централизованные символы.
- Убран локальный импорт AppKit-констант в энкодерах, добавлены проверки доступности.
- Исправлены optional-операции в `_resize_if_needed` через нормализацию:
  - `max_width = int(config.max_width or 0)`
  - `max_height = int(config.max_height or 0)`.
- Добавлен helper `_require_nsbitmap_rep()` для строгого доступа к `NSBitmapImageRep`.

## Verification
- `./.venv/bin/ruff check modules/screenshot_capture/macos/simple_bridge.py` → OK
- `../server/.venv/bin/basedpyright modules/screenshot_capture/macos/simple_bridge.py --outputjson` → 0 diagnostics
- `./scripts/problem_scan.sh` → `TOTAL_ISSUES=391`
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh` → PASSED

## Impact
- Для `simple_bridge.py`: warning reduced `24 -> 0`.
- Общий backlog reduced: `415 -> 391`.
- Логика нативных импортов стала централизованной и предсказуемой (меньше дублирования и optional-risk).
