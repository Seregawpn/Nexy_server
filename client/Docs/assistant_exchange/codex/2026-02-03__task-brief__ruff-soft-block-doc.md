# Task Brief — Ruff soft-block policy

## Goal
Зафиксировать в архитектурной документации, что `ruff` работает в soft‑block режиме до снижения lint‑debt.

## Changes
- Добавлен раздел про Quality Gates в `Docs/ARCHITECTURE_OVERVIEW.md`.

## Files
- `Docs/ARCHITECTURE_OVERVIEW.md`

## Notes
- Режим `ruff` в `scripts/pre_build_gate.sh` уже soft‑block; документируем политику перехода на hard‑block.
