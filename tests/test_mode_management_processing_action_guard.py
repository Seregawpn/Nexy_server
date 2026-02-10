import time

import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.mode_management_integration import ModeManagementIntegration
from modules.mode_management import AppMode


@pytest.mark.asyncio
async def test_action_intent_without_session_uses_active_processing_session():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler(event_bus))

    session_id = "11111111-1111-4111-8111-111111111111"
    state_manager.set_mode(AppMode.PROCESSING, session_id=session_id)

    await integration._on_action_intent({"data": {"source": "action_message"}})

    assert integration._has_pending_action_intent(session_id)


@pytest.mark.asyncio
async def test_sleeping_request_is_deferred_when_action_intent_is_pending_for_active_session():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler(event_bus))

    session_id = "22222222-2222-4222-8222-222222222222"
    state_manager.set_mode(AppMode.PROCESSING, session_id=session_id)
    integration._pending_action_intents[session_id] = time.monotonic()

    await integration._on_mode_request(
        {
            "data": {
                "target": AppMode.SLEEPING,
                "source": "playback.finished",
                "session_id": None,
            }
        }
    )

    assert state_manager.get_current_mode() == AppMode.PROCESSING
    assert session_id in integration.get_status()["deferred_sleep_sessions"]


@pytest.mark.asyncio
async def test_action_started_without_session_uses_active_processing_session():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler(event_bus))

    session_id = "33333333-3333-4333-8333-333333333333"
    state_manager.set_mode(AppMode.PROCESSING, session_id=session_id)

    await integration._on_action_started({"data": {"command": "send_message"}})

    assert integration.get_status()["active_action_sessions"].get(session_id) == 1


@pytest.mark.asyncio
async def test_sleeping_request_is_deferred_when_playback_active_even_without_session():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = ModeManagementIntegration(event_bus, state_manager, ErrorHandler(event_bus))

    session_id = "44444444-4444-4444-8444-444444444444"
    state_manager.set_mode(AppMode.PROCESSING, session_id=None)
    integration._active_playback_sessions.add(session_id)

    await integration._on_mode_request(
        {
            "data": {
                "target": AppMode.SLEEPING,
                "source": "playback.finished",
                "session_id": None,
            }
        }
    )

    assert state_manager.get_current_mode() == AppMode.PROCESSING
