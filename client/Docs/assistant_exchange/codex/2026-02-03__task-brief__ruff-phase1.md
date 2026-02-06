# Task Brief — Ruff Phase 1 cleanup

## Goal
Снять наиболее безопасные ruff‑нарушения (I001/F401/UP006/UP045).

## Changes
- Добавлены `__all__` для явных re-export в `modules/browser_progress` и `modules/messages`.
- Удалены неиспользуемые импорты `objc` и `Quartz`.
- Запущен ruff с авто‑фиксами для I001/F401/UP006/UP045.

## Files
- `modules/browser_progress/__init__.py`
- `modules/browser_progress/core/__init__.py`
- `modules/messages/__init__.py`
- `modules/permissions/v2/probers/contacts.py`
- `modules/permissions/v2/probers/input_monitoring.py`

## Commands
- `./.venv/bin/ruff check . --select I001,F401,UP006,UP045 --fix`

## Result
Ruff phase‑1 passed (no remaining issues in selected rules).
