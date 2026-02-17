from unittest.mock import AsyncMock, Mock

import pytest

from integration.integrations.interrupt_management_integration import (
    InterruptManagementIntegration,
)
from modules.interrupt_management.core.types import (
    InterruptEvent,
    InterruptPriority,
    InterruptType,
)
from modules.mode_management import AppMode


def _make_interrupt_event(source: str) -> InterruptEvent:
    return InterruptEvent(
        type=InterruptType.SPEECH_STOP,
        priority=InterruptPriority.NORMAL,
        source=source,
        timestamp=0.0,
        data={},
    )


@pytest.mark.asyncio
async def test_speech_stop_preempt_source_publishes_sleep_mode_request():
    event_bus = Mock()
    event_bus.publish = AsyncMock()
    integration = InterruptManagementIntegration(event_bus, Mock(), Mock())

    event = _make_interrupt_event("keyboard.press_preempt")
    ok = await integration._handle_speech_stop(event)

    assert ok is True
    published = [call.args for call in event_bus.publish.await_args_list]
    assert ("speech.stop_requested",) == published[0][:1]
    assert any(
        args[0] == "mode.request"
        and args[1]["target"] == AppMode.SLEEPING
        and args[1]["source"] == "interrupt_management"
        and "request_id" in args[1]
        for args in published
    )


@pytest.mark.asyncio
async def test_speech_stop_regular_source_publishes_sleep_mode_request():
    event_bus = Mock()
    event_bus.publish = AsyncMock()
    integration = InterruptManagementIntegration(event_bus, Mock(), Mock())

    event = _make_interrupt_event("interrupt_management")
    ok = await integration._handle_speech_stop(event)

    assert ok is True
    published = [call.args for call in event_bus.publish.await_args_list]
    assert any(
        args[0] == "mode.request"
        and args[1]["target"] == AppMode.SLEEPING
        and args[1]["source"] == "interrupt_management"
        for args in published
    )


@pytest.mark.asyncio
async def test_interrupt_request_preempt_sets_cancel_cue_suppression_flag():
    event_bus = Mock()
    event_bus.publish = AsyncMock()
    integration = InterruptManagementIntegration(event_bus, Mock(), Mock())
    integration._coordinator = Mock()
    integration._coordinator.trigger_interrupt = AsyncMock()

    await integration._on_interrupt_request(
        {
            "data": {
                "type": "speech_stop",
                "source": "keyboard.press_preempt",
                "session_id": "11111111-1111-4111-8111-111111111111",
                "event_id": "evt-preempt-1",
            }
        }
    )

    grpc_cancel_payloads = [
        call.args[1]
        for call in event_bus.publish.await_args_list
        if call.args and call.args[0] == "grpc.request_cancel"
    ]
    assert grpc_cancel_payloads
    payload = grpc_cancel_payloads[0]
    assert payload["interrupt_source"] == "keyboard.press_preempt"
    assert payload["suppress_cancel_cue"] is True
