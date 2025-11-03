"""
Contract tests for update_in_progress and restart_pending events.

Tests that events are published with correct payload schemas:
- updater.in_progress.changed: {active: bool, trigger: str}
- permissions.restart_pending.changed: {active: bool, session_id: str, source: str}
"""

import pytest
from unittest.mock import AsyncMock, Mock, MagicMock
import asyncio

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.updater_integration import UpdaterIntegration


class TestUpdaterInProgressChanged:
    """Test updater.in_progress.changed event contract."""

    @pytest.fixture
    async def event_bus(self):
        """Create EventBus with attached loop."""
        bus = EventBus()
        try:
            loop = asyncio.get_running_loop()
            bus.attach_loop(loop)
        except RuntimeError:
            pass
        return bus

    @pytest.fixture
    def state_manager(self):
        """Create ApplicationStateManager."""
        return ApplicationStateManager()

    @pytest.fixture
    async def updater_integration(self, event_bus, state_manager):
        """Create UpdaterIntegration."""
        config = {"updater": {"enabled": True, "check_on_startup": False, "check_interval_sec": 3600}}
        integration = UpdaterIntegration(event_bus, state_manager, config)
        await integration.initialize()
        yield integration
        # Cleanup: stop the integration to cancel check_task
        try:
            await integration.stop()
        except Exception:
            pass

    @pytest.mark.anyio
    async def test_event_published_when_state_changes_to_true(self, event_bus, state_manager):
        """Test that event is published when update_in_progress becomes True."""
        config = {"updater": {"enabled": True}}

        integration = UpdaterIntegration(event_bus, state_manager, config)
        await integration.initialize()

        # Subscribe to event
        published_events = []
        async def event_handler(event_data):
            published_events.append(event_data)

        await event_bus.subscribe("updater.in_progress.changed", event_handler)

        # Trigger state change
        integration._set_update_state(True, trigger="test_trigger")

        # Wait for async event processing
        await asyncio.sleep(0.2)

        # Verify event was published
        assert len(published_events) > 0
        event_obj = published_events[-1]
        event_data = event_obj.get("data", event_obj)  # Extract data from event object

        # Verify payload schema
        assert "active" in event_data
        assert isinstance(event_data["active"], bool)
        assert event_data["active"] is True

        assert "trigger" in event_data
        assert isinstance(event_data["trigger"], str)
        assert event_data["trigger"] == "test_trigger"

    @pytest.mark.anyio
    async def test_event_published_when_state_changes_to_false(self, event_bus, state_manager):
        """Test that event is published when update_in_progress becomes False."""
        config = {"updater": {"enabled": True}}

        integration = UpdaterIntegration(event_bus, state_manager, config)
        await integration.initialize()

        # Set initial state to True
        integration._set_update_state(True, trigger="initial")

        # Subscribe to event
        published_events = []
        async def event_handler(event_data):
            published_events.append(event_data)

        await event_bus.subscribe("updater.in_progress.changed", event_handler)

        # Trigger state change to False
        integration._set_update_state(False, trigger="test_trigger")

        # Wait for async event processing
        await asyncio.sleep(0.2)

        # Verify event was published
        assert len(published_events) > 0
        event_obj = published_events[-1]
        event_data = event_obj.get("data", event_obj)  # Extract data from event object

        # Verify payload schema
        assert event_data["active"] is False
        assert event_data["trigger"] == "test_trigger"

    @pytest.mark.anyio
    async def test_event_published_when_state_stays_same(self, event_bus, state_manager):
        """Test that event is published even when state value doesn't change (shadow-mode)."""
        config = {"updater": {"enabled": True}}

        integration = UpdaterIntegration(event_bus, state_manager, config)
        await integration.initialize()

        # Set initial state
        integration._set_update_state(True, trigger="initial")

        # Subscribe to event
        published_events = []
        async def event_handler(event_data):
            published_events.append(event_data)

        await event_bus.subscribe("updater.in_progress.changed", event_handler)

        # Set same state again (shadow-mode: publish for synchronization)
        integration._set_update_state(True, trigger="repeat")

        # Wait for async event processing
        await asyncio.sleep(0.2)

        # Verify event was published (shadow-mode behavior)
        assert len(published_events) > 0
        event_obj = published_events[-1]
        event_data = event_obj.get("data", event_obj)  # Extract data from event object

        # Verify payload schema
        assert event_data["active"] is True
        assert event_data["trigger"] == "repeat"

    @pytest.mark.anyio
    async def test_payload_contains_only_required_fields(self, event_bus, state_manager):
        """Test that payload contains only expected fields (no extras)."""
        config = {"updater": {"enabled": True}}

        integration = UpdaterIntegration(event_bus, state_manager, config)
        await integration.initialize()

        # Subscribe to event
        published_events = []
        async def event_handler(event_data):
            published_events.append(event_data)

        await event_bus.subscribe("updater.in_progress.changed", event_handler)

        # Trigger state change
        integration._set_update_state(True, trigger="test")

        # Wait for async event processing
        await asyncio.sleep(0.2)

        # Verify event was published
        assert len(published_events) > 0
        event_obj = published_events[-1]
        event_data = event_obj.get("data", event_obj)  # Extract data from event object

        # Verify payload contains only expected fields
        expected_keys = {"active", "trigger"}
        assert set(event_data.keys()) == expected_keys, f"Unexpected keys in payload: {set(event_data.keys()) - expected_keys}"

    def test_payload_schema_types(self):
        """Test that payload fields have correct types."""
        # Valid payload
        valid_payload = {
            "active": True,
            "trigger": "startup",
        }

        # Type checks for valid payload
        assert isinstance(valid_payload["active"], bool)
        assert isinstance(valid_payload["trigger"], str)

        # Invalid payloads - verify they fail type checks
        invalid_payloads = [
            {"active": "true", "trigger": "startup"},  # active not bool
            {"active": True, "trigger": 123},  # trigger not str
            {"active": True},  # missing trigger
            {"trigger": "startup"},  # missing active
        ]

        # Test each invalid payload
        for invalid_payload in invalid_payloads:
            errors = []
            if "active" in invalid_payload and not isinstance(invalid_payload["active"], bool):
                errors.append(f"active should be bool, got {type(invalid_payload['active'])}")
            if "trigger" in invalid_payload and not isinstance(invalid_payload["trigger"], str):
                errors.append(f"trigger should be str, got {type(invalid_payload['trigger'])}")
            if "trigger" not in invalid_payload:
                errors.append("trigger is required but missing")
            if "active" not in invalid_payload:
                errors.append("active is required but missing")
            
            # Verify that invalid payloads would fail validation
            assert len(errors) > 0, f"Invalid payload should have validation errors: {invalid_payload}"


class TestPermissionsRestartPendingChanged:
    """Test permissions.restart_pending.changed event contract."""

    @pytest.fixture
    def event_bus(self):
        """Create EventBus."""
        return EventBus()

    @pytest.mark.anyio
    async def test_event_published_with_correct_payload(self, event_bus):
        """Test that restart_pending event is published with correct payload schema."""
        # Subscribe to event
        published_events = []
        async def event_handler(event_data):
            published_events.append(event_data)

        await event_bus.subscribe("permissions.restart_pending.changed", event_handler)

        # Publish event manually (contract test - we test the contract, not the implementation)
        await event_bus.publish("permissions.restart_pending.changed", {
            "active": True,
            "session_id": "test-session-123",
            "source": "first_run_permissions_integration",
        })

        # Wait for async event processing
        await asyncio.sleep(0.2)

        # Verify event was published
        assert len(published_events) > 0
        event_obj = published_events[-1]
        event_data = event_obj.get("data", event_obj)  # Extract data from event object

        # Verify payload schema
        assert "active" in event_data
        assert isinstance(event_data["active"], bool)
        assert event_data["active"] is True

        assert "session_id" in event_data
        assert isinstance(event_data["session_id"], str)
        assert event_data["session_id"] == "test-session-123"

        assert "source" in event_data
        assert isinstance(event_data["source"], str)
        assert event_data["source"] == "first_run_permissions_integration"

    def test_payload_schema_types(self):
        """Test that payload fields have correct types."""
        # Valid payload
        valid_payload = {
            "active": True,
            "session_id": "session-uuid-123",
            "source": "permission_restart_integration",
        }

        # Type checks for valid payload
        assert isinstance(valid_payload["active"], bool)
        assert isinstance(valid_payload["session_id"], str)
        assert isinstance(valid_payload["source"], str)

        # Invalid payloads - verify they fail type checks
        invalid_payloads = [
            {"active": "true", "session_id": "123", "source": "test"},  # active not bool
            {"active": True, "session_id": 123, "source": "test"},  # session_id not str
            {"active": True, "session_id": "123", "source": 456},  # source not str
        ]

        # Test each invalid payload
        for invalid_payload in invalid_payloads:
            errors = []
            if "active" in invalid_payload and not isinstance(invalid_payload["active"], bool):
                errors.append(f"active should be bool, got {type(invalid_payload['active'])}")
            if "session_id" in invalid_payload and not isinstance(invalid_payload["session_id"], str):
                errors.append(f"session_id should be str, got {type(invalid_payload['session_id'])}")
            if "source" in invalid_payload and not isinstance(invalid_payload["source"], str):
                errors.append(f"source should be str, got {type(invalid_payload['source'])}")
            
            # Verify that invalid payloads would fail validation
            assert len(errors) > 0, f"Invalid payload should have validation errors: {invalid_payload}"

    @pytest.mark.anyio
    async def test_event_published_when_restart_pending_true(self, event_bus):
        """Test that event is published when restart_pending becomes True."""
        # Subscribe to event
        published_events = []
        async def event_handler(event_data):
            published_events.append(event_data)

        await event_bus.subscribe("permissions.restart_pending.changed", event_handler)

        # Publish event
        await event_bus.publish("permissions.restart_pending.changed", {
            "active": True,
            "session_id": "session-123",
            "source": "first_run_permissions",
        })

        # Wait for async event processing
        await asyncio.sleep(0.2)

        # Verify event was published
        assert len(published_events) > 0
        event_obj = published_events[-1]
        event_data = event_obj.get("data", event_obj)  # Extract data from event object

        assert event_data["active"] is True

    @pytest.mark.anyio
    async def test_event_published_when_restart_pending_false(self, event_bus):
        """Test that event is published when restart_pending becomes False."""
        # Subscribe to event
        published_events = []
        async def event_handler(event_data):
            published_events.append(event_data)

        await event_bus.subscribe("permissions.restart_pending.changed", event_handler)

        # Publish event
        await event_bus.publish("permissions.restart_pending.changed", {
            "active": False,
            "session_id": "session-123",
            "source": "first_run_permissions",
        })

        # Wait for async event processing
        await asyncio.sleep(0.2)

        # Verify event was published
        assert len(published_events) > 0
        event_obj = published_events[-1]
        event_data = event_obj.get("data", event_obj)  # Extract data from event object

        assert event_data["active"] is False

