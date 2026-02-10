"""
Поведенческие тесты ModeManagementIntegration для переходов в LISTENING/PROCESSING.
"""

from unittest.mock import AsyncMock

import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.mode_management_integration import ModeManagementIntegration
from modules.mode_management import AppMode


@pytest.mark.asyncio
async def test_listening_request_from_processing_without_session_is_applied():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler(event_bus))
    integration._apply_mode = AsyncMock()

    state_manager.set_mode(AppMode.PROCESSING, session_id="11111111-1111-4111-8111-111111111111")

    await integration._on_mode_request(
        {
            "data": {
                "target": AppMode.LISTENING,
                "source": "input_processing",
                "session_id": None,
            }
        }
    )

    integration._apply_mode.assert_awaited_once()
    args, kwargs = integration._apply_mode.await_args
    assert args[0] == AppMode.LISTENING


@pytest.mark.asyncio
async def test_request_with_mismatched_session_in_processing_is_ignored():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler(event_bus))
    integration._apply_mode = AsyncMock()

    state_manager.set_mode(AppMode.PROCESSING, session_id="22222222-2222-4222-8222-222222222222")

    await integration._on_mode_request(
        {
            "data": {
                "target": AppMode.SLEEPING,
                "source": "playback.finished",
                "session_id": "33333333-3333-4333-8333-333333333333",
            }
        }
    )

    integration._apply_mode.assert_not_awaited()


@pytest.mark.asyncio
async def test_interrupt_request_bypasses_session_guard():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler(event_bus))
    integration._apply_mode = AsyncMock()

    state_manager.set_mode(AppMode.PROCESSING, session_id="44444444-4444-4444-8444-444444444444")

    await integration._on_mode_request(
        {
            "data": {
                "target": AppMode.SLEEPING,
                "source": "interrupt",
                "priority": 100,
                "session_id": "55555555-5555-4555-8555-555555555555",
            }
        }
    )

    integration._apply_mode.assert_awaited_once()
    args, kwargs = integration._apply_mode.await_args
    assert args[0] == AppMode.SLEEPING
    assert kwargs.get("source") == "interrupt"
