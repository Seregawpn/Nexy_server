from unittest.mock import AsyncMock

import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.mode_management_integration import ModeManagementIntegration
from modules.mode_management import AppMode


@pytest.mark.asyncio
async def test_mode_request_dedup_by_request_id():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    integration._apply_mode = AsyncMock(return_value=None)  # type: ignore[method-assign]

    payload = {
        "target": AppMode.LISTENING,
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
                "target": AppMode.LISTENING,
                "source": "input_processing",
                "session_id": "sid-2",
                "request_id": "req-1",
            }
        }
    )
    await integration._on_mode_request(
        {
            "data": {
                "target": AppMode.LISTENING,
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
                "target": AppMode.PROCESSING,
                "source": "welcome_message",
                "session_id": None,
            }
        }
    )

    assert integration._apply_mode.await_count == 0


@pytest.mark.asyncio
async def test_processing_terminal_bridged_to_mode_request_sleeping():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    state_manager.set_mode(AppMode.PROCESSING, session_id="sid-terminal")
    integration._apply_mode = AsyncMock(return_value=None)  # type: ignore[method-assign]

    await integration._on_processing_terminal(
        {
            "data": {
                "session_id": "sid-terminal",
                "reason": "completed",
            }
        }
    )

    assert integration._apply_mode.await_count == 1
    args, kwargs = integration._apply_mode.await_args
    assert args[0] == AppMode.SLEEPING
    assert kwargs["source"] == "interrupt"
    assert kwargs["session_id"] == "sid-terminal"


@pytest.mark.asyncio
async def test_processing_terminal_without_session_id_ignored():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    state_manager.set_mode(AppMode.PROCESSING, session_id="sid-terminal")
    integration._apply_mode = AsyncMock(return_value=None)  # type: ignore[method-assign]

    await integration._on_processing_terminal({"data": {"reason": "completed"}})

    assert integration._apply_mode.await_count == 0
