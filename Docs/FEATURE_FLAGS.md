# Feature Flags Guide

Nexy supports granular control over major capabilities through Feature Flags. You can completely disable specific subsystems (Messages, Browser Automation, Payment) to reduce resource usage or for testing purposes.

## Architecture

When a feature is disabled:
1. **Prompt Engineering:** The LLM system prompt is rebuilt to exclude all instructions, examples, and commands related to that feature. The AI literally "forgets" how to use it.
2. **Command Validation:** The server rejects any commands related to the disabled feature (protecting against hallucinations).
3. **Client Resources:** The client does not initialize heavy integrations (like Chrome orchestration) for disabled features.
4. **UI Guards:** Action executors prevent accidental dispatch of disabled commands.
5. **Tray Menu:** Menu items for disabled features are hidden.

---

## 1. Messages Integration (iMessage)

Controls: `read_messages`, `send_message`, `find_contact`.

### How to Disable

**Server (`server/server/config.env`):**
```bash
MESSAGES_ENABLED=false
```

**Client (`client/config/unified_config.yaml`):**
```yaml
messages:
  enabled: false
```

### Effect
- User queries "Read my messages" will be answered with a text response instead of action.
- LLM will not see any iMessage-related instructions.

---

## 2. Browser Automation (Browser Use)

Controls: `browser_use` (complex web tasks), `close_browser`.
*Note: This does not affect simple Google Search (WebSearch tool).*

### How to Disable

**Server (`server/server/config.env`):**
```bash
BROWSER_USE_ENABLED=false
```

**Client (`client/config/unified_config.yaml`):**
```yaml
browser_use:
  enabled: false
```

*Note: `features.browser_use.enabled` может использоваться как rollout/legacy, но канонический флаг — `browser_use.enabled`.*

### Effect
- "Open YouTube" will likely be handled as `open_app` (Safari app) or WebSearch, but NOT as an autonomous browser agent.
- `BrowserUseIntegration` and `BrowserProgressIntegration` will not start on client.

---

## 3. Payment System (Stripe)

Controls: `buy_subscription`, `manage_subscription`, Quota checks.

### How to Disable

**Server (`server/server/config.env`):**
```bash
SUBSCRIPTION_ENABLED=false
```
```bash
SUBSCRIPTION_KILL_SWITCH=true
```

**Client (`client/config/unified_config.yaml`):**
```yaml
payment_use:
  enabled: false
```

### Effect
- Subscription checks are bypassed (Unlimited access).
- Prompt does not contain "User needs to subscribe" instructions.
- `PaymentIntegration` is not initialized on client.
- "Manage Subscription" menu item hidden in Tray.

---

## Synchronization

Ideally, flags should be synchronized between Server and Client for consistent behavior.
- If **Server=False**, **Client=True**: Client is ready, but Server never sends the command. (Safe)
- If **Server=True**, **Client=False**: Server sends command, Client rejects it with "Feature disabled" error. (Safe, but user gets an error message).

**Recommendation:** Always update both configs when toggling features.

---

## Quick Reference

| Feature | Server Variable | Client YAML Path |
|---------|-----------------|------------------|
| Messages | `MESSAGES_ENABLED` | `messages.enabled` |
| Browser | `BROWSER_USE_ENABLED` | `browser_use.enabled` |
| Payment | `SUBSCRIPTION_ENABLED` | `payment_use.enabled` |
| WhatsApp | `WHATSAPP_ENABLED` | `whatsapp.enabled` |
| Web Search | `WEB_SEARCH_ENABLED` | n/a (server-only) |
| MCP Action Forwarding | `FORWARD_ASSISTANT_ACTIONS` | n/a (server-only) |
| Payment Automation | `PAYMENT_USE_ENABLED` | n/a (server-only) |
| Subscription Kill Switch | `SUBSCRIPTION_KILL_SWITCH` | n/a (server-only) |

---

## 4. WhatsApp Integration

Controls: `send_whatsapp_message`, `read_whatsapp_messages`.
*Note: Requires a separate persistent Node.js service.*

### How to Disable

**Server (`server/server/config.env`):**
```bash
WHATSAPP_ENABLED=false
```

**Client (`client/config/unified_config.yaml`):**
```yaml
whatsapp:
  enabled: false
```

### Effect
- "Send WhatsApp message" commands will be rejected by the server if disabled.
- Client will not start the `whatsapp-mcp-ready` Node.js service.
- Prompts related to WhatsApp are removed from LLM context.

---

## 5. Web Search (Server)

Controls: `web_search` tool exposure in the server prompt and validator.

### How to Disable

**Server (`server/server/config.env`):**
```bash
WEB_SEARCH_ENABLED=false
```

### Effect
- Web search instructions/tools are excluded from the system prompt.
- Any web_search command is rejected server-side.

---

## 6. MCP Action Forwarding (Server)

Controls: forwarding of MCP `command_payload` to the client.

### How to Disable

**Server (`server/server/config.env`):**
```bash
FORWARD_ASSISTANT_ACTIONS=false
```

### Effect
- LLM can still return action JSON, but the server will not forward commands.

---

## 7. Payment Automation (Server)

Controls: payment automation workflow (separate from subscription checks).

### How to Disable

**Server (`server/server/config.env`):**
```bash
PAYMENT_USE_ENABLED=false
```

### Effect
- Payment automation workflow is disabled regardless of subscription system.

---

## 8. Subscription Kill Switch (Server)

Controls: emergency disable of subscription checks.

### How to Disable

**Server (`server/server/config.env`):**
```bash
SUBSCRIPTION_KILL_SWITCH=true
```

### Effect
- Subscription checks are bypassed even if `SUBSCRIPTION_ENABLED=true`.
