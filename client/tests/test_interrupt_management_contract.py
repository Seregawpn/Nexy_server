import asyncio

import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.interrupt_management_integration import (
    InterruptManagementIntegration,
)
from modules.interrupt_management.core.types import (
    InterruptEvent,
    InterruptPriority,
    InterruptType,
)


@pytest.mark.asyncio
async def test_recording_stop_mode_request_contains_session_id():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = InterruptManagementIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
    )

    published_events = []

    async def capture_event(event):
        event_type = event.get("type") if isinstance(event, dict) else None
        payload = event.get("data") if isinstance(event, dict) else event
        published_events.append((event_type, payload))

    await event_bus.subscribe("mode.request", capture_event)

    sid = "11db9f42-c560-4d93-8db4-e75470f82ce9"
    interrupt_event = InterruptEvent(
        type=InterruptType.RECORDING_STOP,
        priority=InterruptPriority.NORMAL,
        source="interrupt_management",
        timestamp=0.0,
        data={"session_id": sid},
    )

    ok = await integration._handle_recording_stop(interrupt_event)
    await asyncio.sleep(0.05)

    assert ok is True
    mode_requests = [
        payload
        for event_type, payload in published_events
        if event_type == "mode.request" and isinstance(payload, dict)
    ]
    assert len(mode_requests) == 1
    assert mode_requests[0].get("target").value == "processing"
    assert mode_requests[0].get("source") == "interrupt_management"
    assert mode_requests[0].get("session_id") == sid


@pytest.mark.asyncio
async def test_interrupt_request_without_session_id_does_not_publish_grpc_cancel():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = InterruptManagementIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
    )

    captured: list[dict] = []

    async def _capture(event):
        payload = event.get("data") if isinstance(event, dict) else {}
        captured.append(payload or {})

    await event_bus.subscribe("grpc.request_cancel", _capture)

    await integration._on_interrupt_request(
        {
            "data": {
                "type": "speech_stop",
                "source": "keyboard.short_press",
                "timestamp": 0.0,
            }
        }
    )
    await asyncio.sleep(0.05)

    assert captured == []
