from unittest.mock import AsyncMock

import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.signal_integration import SignalIntegration, SignalsIntegrationConfig
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

    await integration._on_mode_changed({"data": {"mode": "listening", "session_id": "sid-listen"}})

    patterns = [call.args[0].pattern for call in integration._service.emit.await_args_list]
    assert SignalPattern.LISTEN_START in patterns


@pytest.mark.asyncio
async def test_sleep_done_emitted_on_mode_changed_without_processing_terminal():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = SignalIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    integration._service.emit = AsyncMock(return_value=True)

    await integration._on_mode_changed(
        {
            "data": {
                "mode": "sleeping",
                "old_mode": "listening",
                "session_id": "sid-sleep-1",
            }
        }
    )

    patterns = [call.args[0].pattern for call in integration._service.emit.await_args_list]
    assert SignalPattern.DONE in patterns


@pytest.mark.asyncio
async def test_sleep_done_dedup_after_terminal_for_same_session():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = SignalIntegration(event_bus, state_manager, ErrorHandler())
    await integration.initialize()

    integration._service.emit = AsyncMock(return_value=True)

    sid = "sid-sleep-dedup-1"
    await integration._on_processing_terminal(
        {"data": {"session_id": sid, "result": "success", "reason": "completed"}}
    )
    await integration._on_mode_changed(
        {
            "data": {
                "mode": "sleeping",
                "old_mode": "processing",
                "session_id": sid,
            }
        }
    )

    patterns = [call.args[0].pattern for call in integration._service.emit.await_args_list]
    assert patterns.count(SignalPattern.DONE) == 1


@pytest.mark.asyncio
async def test_listen_start_suppressed_for_ptt_session_when_enabled():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = SignalIntegration(
        event_bus,
        state_manager,
        ErrorHandler(),
        SignalsIntegrationConfig(suppress_listen_start_for_ptt=True),
    )
    await integration.initialize()
    integration._service.emit = AsyncMock(return_value=True)

    sid = "sid-ptt-1"
    await integration._on_mode_request({"data": {"target": "listening", "source": "input_processing", "session_id": sid}})
    await integration._on_mode_changed({"data": {"mode": "listening", "session_id": sid}})

    assert integration._service.emit.await_count == 0


@pytest.mark.asyncio
async def test_cancel_suppressed_for_keyboard_interrupt_window_when_enabled():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = SignalIntegration(
        event_bus,
        state_manager,
        ErrorHandler(),
        SignalsIntegrationConfig(
            suppress_cancel_for_keyboard_interrupt=True,
        ),
    )
    await integration.initialize()
    integration._service.emit = AsyncMock(return_value=True)

    sid = "sid-cancel-1"
    await integration._on_playback_cancelled(
        {
            "data": {
                "session_id": sid,
                "source": "keyboard.press_preempt",
                "initiator": "keyboard",
                "reason": "user_interrupt",
            }
        }
    )

    assert integration._service.emit.await_count == 0
