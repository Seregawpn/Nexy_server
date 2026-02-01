# Task
- Add guard around asyncio Future set_result in NSAlert helper.

# Changes
- Added future.done() check before set_result in success and error paths.

# Files
- integration/integrations/first_run_permissions_integration.py

# Notes
- Prevents InvalidStateError if wait_for timed out or future already completed.
