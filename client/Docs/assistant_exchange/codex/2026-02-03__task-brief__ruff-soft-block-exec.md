# Task Brief — Ruff soft-block execution

## Goal
Сделать soft‑block для ruff реальным (gate не падает при lint‑debt).

## Changes
- Обернул запуск ruff в `set +e`/`set -e` и учёт `RUFF_STATUS`.
- При ошибках ruff увеличивается `SKIPPED`, gate продолжается.

## Files
- `scripts/pre_build_gate.sh`

## Notes
- Логика hard‑block остаётся доступной для будущего переключения.
