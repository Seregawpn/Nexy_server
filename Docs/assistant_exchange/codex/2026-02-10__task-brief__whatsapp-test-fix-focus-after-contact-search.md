# Whatsapp_test fix: focus message input after contact search

Date: 2026-02-10
Type: task-brief

## Problem
When running with `--contact`, WhatsApp search was performed, but paste could land in search field instead of chat composer.

## Fix
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/whatsapp_adapter.py`
  - added `focus_message_input()`
    - attempts to focus the last text area in front WhatsApp window
    - fallback nudge: `Esc + Tab + Tab`
  - `paste_message()` now always calls `focus_message_input()` before paste
  - increased post-chat-select delay for stability

## Validation
- Syntax check passed:
  - `python3 -m py_compile /Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/whatsapp_adapter.py`

