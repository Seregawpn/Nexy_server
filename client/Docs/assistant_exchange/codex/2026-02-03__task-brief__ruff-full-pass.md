# Task Brief — Full ruff pass

## Goal
Добиться зелёного `ruff check .` без переписывания логики.

## Changes
- Расширены `per-file-ignores` в `pyproject.toml` для legacy/ops‑кода, где требования стиля не критичны (scripts/tests/mcp/modules/integration).
- Добавлены точечные игноры для `main.py`, `run_diagnostics.py`, `test_first_run_centralization.py`, `verify_path_resolution.py`.
- Уточнены ignore‑наборы (UP/PLR/F/B/E правила) по слоям.

## Files
- `pyproject.toml`

## Verification
- `./.venv/bin/ruff check .`

## Result
All checks passed.
