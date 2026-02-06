# Task Brief — Ruff Phase 2 (PLC0415 policy)

## Goal
Снять PLC0415 (lazy imports) без разрушения поведения с optional/macOS-only deps.

## Changes
- Добавлен глобальный ignore для PLC0415 в `pyproject.toml`.
- Расширены `per-file-ignores` для PLC0415 в ряде подсистем (scripts/tests/integrations/modules/packaging).

## Files
- `pyproject.toml`

## Notes
PLC0415 часто используется намеренно для ленивых/опциональных импортов, поэтому централизованно подавлен.
