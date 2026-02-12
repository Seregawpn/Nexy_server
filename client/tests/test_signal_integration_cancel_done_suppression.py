from unittest.mock import AsyncMock

import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.signal_integration import SignalIntegration
from modules.mode_management import AppMode
from modules.signals.core.interfaces import SignalPattern


@pytest.mark.asyncio
async def test_done_emitted_from_processing_terminal_success():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = SignalIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    integration._service.emit = AsyncMock(return_value=True)

    await integration._on_processing_terminal(
        {"data": {"session_id": "sid-1", "result": "success", "reason": "completed"}}
    )

    patterns = [call.args[0].pattern for call in integration._service.emit.await_args_list]
    assert SignalPattern.DONE in patterns


@pytest.mark.asyncio
async def test_done_emitted_from_processing_terminal_failed_recognition():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = SignalIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    integration._service.emit = AsyncMock(return_value=True)

    await integration._on_processing_terminal(
        {"data": {"session_id": "sid-2", "result": "failed", "reason": "failed_recognition"}}
    )

    patterns = [call.args[0].pattern for call in integration._service.emit.await_args_list]
    assert SignalPattern.DONE in patterns


@pytest.mark.asyncio
async def test_terminal_dedup_same_session():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = SignalIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    integration._service.emit = AsyncMock(return_value=True)

    event = {"data": {"session_id": "sid-3", "result": "success", "reason": "completed"}}
    await integration._on_processing_terminal(event)
    await integration._on_processing_terminal(event)

    patterns = [call.args[0].pattern for call in integration._service.emit.await_args_list]
    assert patterns.count(SignalPattern.DONE) == 1


@pytest.mark.asyncio
async def test_shutdown_suppresses_followup_terminal():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = SignalIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    integration._service.emit = AsyncMock(return_value=True)

    await integration._on_app_shutdown({"data": {"reason": "user_quit"}})
    await integration._on_processing_terminal(
        {"data": {"session_id": "sid-4", "result": "success", "reason": "completed"}}
    )

    assert integration._service.emit.await_count == 0


@pytest.mark.asyncio
async def test_listen_start_still_emitted_on_mode_changed():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = SignalIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    integration._service.emit = AsyncMock(return_value=True)

    await integration._on_mode_changed(
        {"data": {"mode": AppMode.LISTENING, "session_id": "sid-listen"}}
    )

    patterns = [call.args[0].pattern for call in integration._service.emit.await_args_list]
    assert SignalPattern.LISTEN_START in patterns
