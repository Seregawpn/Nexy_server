# Task Brief — Ruff Phase 2 (E501 modules)

## Goal
Снять E501 в `modules/**` без массового форматирования длинных строк/логов.

## Changes
- Добавлен per‑file ignore для `E501` на `modules/**/*.py`.

## Files
- `pyproject.toml`

## Verification
- `./.venv/bin/ruff check modules --select E501`

## Result
All checks passed for E501 in modules.
