# Whatsapp_test contact selection hardening

Date: 2026-02-10
Type: task-brief

## Problem
`--contact` selected search, but message still did not land in chat composer reliably.

## Fix
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/whatsapp_adapter.py`
  - hardened `select_chat(contact)`:
    - primary flow: `Cmd+K -> paste contact -> Down -> Enter -> Esc`
    - fallback flow: `Cmd+F -> paste contact -> Down -> Enter -> Esc`
  - increased stabilization delay after chat open
  - kept `focus_message_input()` call before paste

## Validation
- Syntax check passed:
  - `python3 -m py_compile /Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/whatsapp_adapter.py`

