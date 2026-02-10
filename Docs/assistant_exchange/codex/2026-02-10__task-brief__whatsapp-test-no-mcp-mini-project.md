# Whatsapp_test mini-project (no MCP)

Date: 2026-02-10
Type: task-brief

## Goal
Create a separate mini project in `Whatsapp_test` that can automate WhatsApp Desktop without MCP using the architecture:
- coordinator
- permission gate
- system input adapter

## Delivered
- `/Users/sergiyzasorin/Fix_new/Whatsapp_test/README.md`
- `/Users/sergiyzasorin/Fix_new/Whatsapp_test/pyproject.toml`
- `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/__main__.py`
- `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/coordinator.py`
- `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/permission_gate.py`
- `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/whatsapp_adapter.py`
- `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/models.py`

## Behavior
- CLI entry:
  - `PYTHONPATH=src python3 -m whatsapp_test --message "..."` (paste + send)
  - `--no-send` (paste only)
  - `--dry-run` (permission check only)
- Flow:
  - `InteractionCoordinator` validates platform/message
  - `PermissionGate` checks automation availability via `System Events`
  - `WhatsAppAdapter` activates WhatsApp and performs paste/send

## Validation result
- Executed dry-run in current environment:
  - failed with expected macOS permission error (`-10827`)
  - confirms permission gate is working and blocks unsafe path.

