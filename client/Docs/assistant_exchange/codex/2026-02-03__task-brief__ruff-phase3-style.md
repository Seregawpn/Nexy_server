# Task Brief — Ruff Phase 3 (style policy)

## Goal
Снять PLR2004/PLW1510/B904 как optional‑style debt без массовых правок в коде.

## Changes
- Расширены per‑file ignores для style‑правил в `pyproject.toml`:
  - `integration/**/*.py`: PLR2004, PLW1510 (E501 already)
  - `modules/**/*.py`: PLR2004, PLW1510, B904 (E501 already)
  - `scripts/**/*.py`, `tests/**/*.py`, `mcp_servers/**`, `config/tests/**`, `packaging/*.py`, `check_version.py`
- Починена B904 chaining в `config/server_manager.py`, `config/updater_manager.py`, `modules/whatsapp/mcp_client.py`.

## Files
- `pyproject.toml`
- `config/server_manager.py`
- `config/updater_manager.py`
- `modules/whatsapp/mcp_client.py`

## Verification
- `./.venv/bin/ruff check . --select B904,PLR2004,PLW1510`

## Result
All checks passed.
