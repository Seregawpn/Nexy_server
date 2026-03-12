# Assistant Runtime V2 Owner Map

Цель этого документа: зафиксировать фактических владельцев текущей системы и целевой gap, который должен постепенно закрыть `assistant_runtime_v2`.

## Current Owners

### 1. Request Routing
- Owner: `server/server/modules/text_processing/core/text_processor.py`
- Responsibility:
  - route classification
  - classifier context assembly (`current_goal`, `short_term_memory`)
  - route flags for generation

### 2. Runtime Prompt Assembly
- Owner: `server/server/integrations/workflow_integrations/streaming_workflow_integration.py`
- Responsibility:
  - request-scoped orchestration
  - memory fetch on request path
  - runtime memory prompt assembly
  - LLM stream orchestration
  - current/v2 runtime switch

### 3. Memory Read/Write/Merge
- Owner: `server/server/modules/memory_management/core/memory_manager.py`
- Responsibility:
  - `current_goal`
  - short-term memory
  - medium-term memory
  - long-term memory
  - goal_state lifecycle inside memory snapshot

### 4. Memory Fetch / Cache / Refresh
- Owner: `server/server/integrations/workflow_integrations/memory_workflow_integration.py`
- Responsibility:
  - fetch memory context
  - cache memory context
  - background refresh/update

### 5. LLM Response Contract
- Owner: `server/server/integrations/core/assistant_response_parser.py`
- Responsibility:
  - parse model output
  - normalize command payload
  - normalize action args/text fallback

### 6. Client Action Dispatch
- Owner: `client/integration/integrations/action_execution_integration.py`
- Responsibility:
  - validate command
  - dedupe action execution
  - dispatch to domain executors
  - publish completion/failure feedback

### 7. Domain Execution Owners

#### Messages
- Owner: `client/modules/messages/send_message.py`
- Called through: `ActionExecutionIntegration`

#### WhatsApp
- Owner: WhatsApp client path via `ActionExecutionIntegration` -> WhatsApp integration/module

#### Browser
- Owner: `ActionExecutionIntegration` -> browser event path

#### Payment
- Owner: `ActionExecutionIntegration` -> payment event path

#### System Control
- Owner: `ActionExecutionIntegration` -> MCP app executor

## Main Architecture Gap

### Active Task Lifecycle
- Current state:
  - implicit/blurred
  - effectively driven through `current_goal` inside memory snapshot
- Problem:
  - runtime current task is mixed with user memory
  - continuation / cancel / pivot / topic-switch are not owned by a dedicated runtime layer
- Target owner:
  - `server/server/experimental/assistant_runtime_v2/`

## Rules For V2

1. `assistant_runtime_v2` owns only decision logic.
2. Existing parser remains response-contract owner.
3. Existing client action path remains execution owner.
4. `MemoryManager` remains long/short/medium memory owner until explicitly replaced.
5. New active-task lifecycle must not be re-added into parser or executor.

## Expansion Order

1. `messages`
2. `whatsapp`
3. `system_control`
4. `browser`
5. `payment`

Reason:
- `messages` and `whatsapp` stress continuation/clarification most strongly.
- `system_control` is simpler and can follow.
- `browser` and `payment` should reuse the same decision structure after the first domains are stable.

## First V2 Slice

The first explicit `v2` owner should be:

- domain: `messages`
- axis: `active task lifecycle`
- scope:
  - new request vs follow-up
  - recipient present/missing
  - message present/missing
  - cancel / pivot

Everything else stays on current owners.
