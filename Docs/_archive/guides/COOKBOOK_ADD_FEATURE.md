# 🍳 Cookbook: How to Add a New Feature (15 mins)

> **Goal**: Add a new feature safely using the standardized routes for Client, Server, and End-to-End flows.
> **Time**: 10-15 minutes.
> **Prerequisites**: VS Code, Terminal.

---

## 🚫 Critical Rules (DO NOT IGNORE)
1.  **NO Direct Communication**: Modules must NEVER import other modules or integrations. Use `EventBus`.
2.  **Config Safety**: Always use `UnifiedConfigLoader`.
3.  **Error Safety**: Always use `ErrorHandler`.
4.  **Event Contract**: All events MUST include `session_id`.

---

## 📝 Step-by-Step Checklist (Client)

### Phase 1: Create the Module (5 mins)

1.  [ ] **Copy Template**
    Copy `client/modules/_module_template` to `client/modules/your_feature_name`.

2.  [ ] **Rename & Customize**
    - Rename classes in `core/logic.py` and `core/types.py`.
    - UPDATE `__init__.py` to export your new classes.

3.  [ ] **Define Events**
    In `core/types.py`, define your events.
    > **IMPORTANT**: Ensure your payload types support `session_id`.

4.  [ ] **Implement Logic**
    Write your business logic in `core/logic.py`. Keep it pure!

### Phase 2: Create the Integration (5 mins)

5.  [ ] **Copy Integration Template**
    Copy `integration/integrations/_template_integration.py` to `integration/integrations/your_feature_integration.py`.

6.  [ ] **Bind to EventBus**
    - Update `initialize()` to subscribe explicitly awaiting `event_bus.subscribe`.
    - Use `UnifiedConfigLoader.get_instance().get_feature_config("your_feature_name")`.
    - Ensure `_handle_...` methods are wrapped in `try/except` using `error_handler`.

### Phase 3: Register & Config (5 mins)

7.  [ ] **Register Feature Flag**
    - Add to `Docs/FEATURE_FLAGS.md`.
    - Add to `config/unified_config.yaml`:
      ```yaml
      features:
        your_feature:
          enabled: true
      ```

8.  [ ] **Register Integration**
    In `integration/core/simple_module_coordinator.py`:
    ```python
    from integration.integrations.your_feature_integration import YourFeatureIntegration
    # ...
    # Inside setup_integrations:
    self.your_feature = YourFeatureIntegration(self.event_bus, self.error_handler)
    await self.your_feature.initialize()
    ```

---

## 🧩 Server Feature Route (Server)

Use this section only when the feature requires server-side changes.

### Phase 4: Create Server Module (5 mins)

1.  [ ] **Add Module**
    Create `server/server/modules/your_feature/` with pure business logic.
    - No direct imports from other modules.
    - Implement or adapt to `UniversalModuleInterface` (use adapter if needed).

2.  [ ] **Register in ModuleFactory**
    Update `server/server/integrations/core/module_factory.py`:
    ```python
    ModuleFactory.register("your_feature", "modules.your_feature.adapter:YourFeatureAdapter")
    ```

### Phase 5: Integrate & Configure (5 mins)

3.  [ ] **Coordinator Registration**
    Register capability in server coordinator flow (ModuleCoordinator):
    - Ensure the capability is registered/initialized in the server startup path.

4.  [ ] **Server Config**
    Add config in `server/server/config/unified_config.yaml`.
    - If feature flags are used, register in `server/server/Docs/FEATURE_FLAGS.md`.

---

## 🔗 End-to-End (Client ↔ Server)

Use this when feature spans both sides.

1.  [ ] **Contract**
    Define the event ↔ gRPC contract and payload (include `session_id`).
2.  [ ] **Client Integration**
    Publish/subscribe via EventBus using the client template.
3.  [ ] **Server Module**
    Implement capability and register via ModuleFactory.
4.  [ ] **Server Coordinator**
    Ensure the capability is initialized and accessed via ModuleCoordinator.
4.  [ ] **Config + Flags**
    Add both client and server configs and flags (if needed).
5.  [ ] **E2E Contract Check**
    Confirm `session_id` is present in all client events and server responses.

---

## ✅ Verification (Automated)

We have an automated script to verify that the template architecture works correctly. You can run this script to ensure your environment is set up correctly for new features.

1.  **Run the POC Verifier**:
    ```bash
    python3 scripts/verify_cookbook_poc.py
    ```

2.  **Expected Output**:
    ```text
    POC_VERIFIER - 🚀 Starting POC Verification...
    ...
    poc_integration - [PocIntegration] Subscribed to events
    POC_VERIFIER - [Test] Publishing Trigger Event...
    client.modules.poc_feature.core.logic - [template_module] Processing data: ...
    POC_VERIFIER - ✅ [Test] Success! Received result: ...
    POC_VERIFIED
    ```

**🎉 You are done!**
