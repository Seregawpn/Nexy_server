# Task Brief — Ruff Phase 2 (E501 MCP)

## Goal
Снять E501 в MCP‑серверных файлах без ломки длинных help/regex строк.

## Changes
- Добавлены per‑file ignores для `E501` в `mcp_servers/messages/*.py` и `mcp_servers/telegram/*.py`.

## Files
- `pyproject.toml`

## Verification
- `./.venv/bin/ruff check mcp_servers --select E501`

## Result
All checks passed for E501 in MCP servers.
