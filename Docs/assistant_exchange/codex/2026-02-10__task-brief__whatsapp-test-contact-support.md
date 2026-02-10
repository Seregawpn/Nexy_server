# Whatsapp_test contact support

Date: 2026-02-10
Type: task-brief

## Goal
Add support for selecting a WhatsApp chat by contact name or phone number before pasting/sending a message.

## Changes
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/models.py`
  - `RunRequest` now includes optional `contact`.
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/__main__.py`
  - added CLI argument `--contact`.
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/coordinator.py`
  - if `contact` is provided, calls adapter chat selection before message paste/send.
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/whatsapp_adapter.py`
  - added `select_chat(contact)` flow:
    - activate WhatsApp
    - `Cmd+F`
    - paste contact
    - `Enter`
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/README.md`
  - added contact-based run examples.

## Validation
- Ran: `python3 main.py --help`
- Result: CLI exposes `--contact CONTACT` argument correctly.

