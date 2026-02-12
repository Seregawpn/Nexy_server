# Messages Centralization Audit (2026-02-11)

## Scope
- User ask: analyze whether message interaction has conflicts/duplication/lack of centralization.
- Workspace: `/Users/sergiyzasorin/Fix_new/client`.

## Pre-Change Gate Evidence
Reviewed canonical docs:
- `AGENTS.md`
- `Docs/DOCS_INDEX.md`
- `Docs/PRE_CHANGE_CHECKLIST.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `Docs/ARCHITECTURE_OVERVIEW.md`
- `Docs/FLOW_INTERACTION_SPEC.md`
- `Docs/STATE_CATALOG.md`
- `Docs/FEATURE_FLAGS.md`

Note:
- `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/CODEX_PROMPT.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md` are referenced by policy text, but not present in this workspace.

## Findings
1. Contract drift for messages events:
   - Spec defines `messages.read_request`, `messages.send_request`, `messages.contact_search` (`Docs/FLOW_INTERACTION_SPEC.md:563,572,581`).
   - No implementation references these event names in runtime code (`rg` over `integration/ modules/ tests/ config` returns no matches).

2. Message execution path is coupled to `ActionExecutionIntegration`:
   - `grpc.response.action` handler parses commands and directly executes messages logic (`integration/integrations/action_execution_integration.py:314,452,463,1202,1507`).
   - This creates a mixed owner (MCP dispatch + business logic + user feedback in one integration).

3. Parallel action intent tracking exists in mode layer:
   - `ModeManagementIntegration` separately tracks action intent via `grpc.response.action` (`integration/integrations/mode_management_integration.py:148,607,612`).
   - This is acceptable for mode-guarding, but increases coupling to transport event and should not own message business flow.

4. Event constants gap:
   - `EventTypes` lacks message event constants (`integration/core/event_types.py` has no `MESSAGES_*` constants).
   - Increases typo risk and weakens contract enforcement for message flows.

## Source of Truth (current)
- Runtime owner for message actions in current code: `ActionExecutionIntegration`.
- Canonical contract owner in docs: `FLOW_INTERACTION_SPEC` events (`messages.*`) + EventBus architecture.

## Recommended change set (minimal, architecture-fit)
1. Keep `ActionExecutionIntegration` as MCP ingress only.
2. Add message-domain event routing:
   - `read_messages` -> publish `messages.read_request`
   - `send_message` -> publish `messages.send_request`
   - `find_contact` -> publish `messages.contact_search`
3. Introduce dedicated `MessagesIntegration` as single owner for message business logic and terminal events.
4. Add `EventTypes` constants for `messages.*`.
5. Keep mode guard subscription to lifecycle/intent, but bind to domain lifecycle events (avoid business logic duplication in mode layer).

## Risks
- Medium migration risk if done in one PR (touches integration factory + action flow + tests).
- Low runtime risk with phased migration (dual publish + cutover + cleanup).

## Verification targets
- Contract tests for `grpc.response.action` -> `messages.*` routing.
- Unit tests for `MessagesIntegration` success/failure/duplicate handling.
- Regression: no direct message business logic remains in `ActionExecutionIntegration`.
