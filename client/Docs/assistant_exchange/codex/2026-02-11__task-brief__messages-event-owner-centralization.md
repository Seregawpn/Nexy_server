# Task Brief: Messages Event Owner Centralization

## What changed
- Added `MessagesIntegration` as a single owner for messages domain execution.
- Switched `ActionExecutionIntegration` from direct messages execution to canonical event routing:
  - `read_messages` -> `messages.read_request`
  - `send_message` -> `messages.send_request`
  - `find_contact` -> `messages.contact_search`
- Registered `MessagesIntegration` in `IntegrationFactory` and startup order.
- Added EventTypes constants for messages events and `grpc.response.action`.
- Added tests for routing and owner lifecycle publishing.

## Source of Truth
- Messages domain execution owner: `integration/integrations/messages_integration.py`
- Transport ingress owner: `integration/integrations/action_execution_integration.py`

## Verification
- `PYTHONPATH=. pytest -q tests/test_client_server_flow_contracts.py`
- Result: `6 passed`

## Touched files
- `integration/integrations/messages_integration.py` (new)
- `integration/integrations/action_execution_integration.py`
- `integration/core/integration_factory.py`
- `integration/core/event_types.py`
- `tests/test_client_server_flow_contracts.py`
