from unittest.mock import AsyncMock

import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.integrations.mode_management_integration import ModeManagementIntegration


@pytest.mark.asyncio
async def test_mode_request_dedup_by_request_id():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    integration._apply_mode = AsyncMock(return_value=None)  # type: ignore[method-assign]

    payload = {
        "target": "listening",
        "source": "input_processing",
        "session_id": "sid-1",
        "request_id": "req-1",
    }

    await integration._on_mode_request({"data": payload})
    await integration._on_mode_request({"data": payload})

    assert integration._apply_mode.await_count == 1


@pytest.mark.asyncio
async def test_mode_request_different_request_id_not_deduped():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    integration._apply_mode = AsyncMock(return_value=None)  # type: ignore[method-assign]

    await integration._on_mode_request(
        {
            "data": {
                "target": "listening",
                "source": "input_processing",
                "session_id": "sid-2",
                "request_id": "req-1",
            }
        }
    )
    await integration._on_mode_request(
        {
            "data": {
                "target": "listening",
                "source": "input_processing",
                "session_id": "sid-2",
                "request_id": "req-2",
            }
        }
    )

    assert integration._apply_mode.await_count == 2


@pytest.mark.asyncio
async def test_mode_request_processing_without_session_id_rejected():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    integration._apply_mode = AsyncMock(return_value=None)  # type: ignore[method-assign]

    await integration._on_mode_request(
        {
            "data": {
                "target": "processing",
                "source": "welcome_message",
                "session_id": None,
            }
        }
    )

    assert integration._apply_mode.await_count == 0


@pytest.mark.asyncio
async def test_mode_request_interrupt_management_source_bypasses_processing_session_mismatch():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    state_manager.set_mode(AppMode.PROCESSING, session_id="active-sid")
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    integration._apply_mode = AsyncMock(return_value=None)  # type: ignore[method-assign]

    await integration._on_mode_request(
        {
            "data": {
                "target": "sleeping",
                "source": "interrupt_management",
                "session_id": "other-sid",
                "priority": 10,
            }
        }
    )

    assert integration._apply_mode.await_count == 1
    call = integration._apply_mode.await_args
    assert call.kwargs["source"] == "interrupt"
    assert call.kwargs["session_id"] == "other-sid"
    mode_arg = call.args[0]
    assert getattr(mode_arg, "value", str(mode_arg)) == "sleeping"
