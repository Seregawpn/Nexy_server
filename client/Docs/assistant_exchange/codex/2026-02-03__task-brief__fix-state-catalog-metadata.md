# Task Brief — Fix state catalog + requirements metadata

## Goal
Разблокировать pre-build gate: 4‑артефактный инвариант и snapshot требований.

## Changes
- Привёл оси в `Docs/STATE_CATALOG.md` к именам из `interaction_matrix.yaml` (с alias для legacy).
- Исправил regex проверки версии в `scripts/update_requirements_snapshot.py`.

## Files
- `Docs/STATE_CATALOG.md`
- `scripts/update_requirements_snapshot.py`

## Verification
- `scripts/pre_build_gate.sh --skip-tests --skip-lint`

## Result
Gate passed (10 passed, 2 skipped).
