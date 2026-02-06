# Task Brief — Ruff Phase 2 (E501 integration)

## Goal
Снять E501 в integration‑слое без массового форматирования логов.

## Changes
- Добавлен per‑file ignore для `E501` на `integration/**/*.py`.

## Files
- `pyproject.toml`

## Verification
- `./.venv/bin/ruff check integration --select E501`

## Result
All checks passed for E501 in integration layer.
