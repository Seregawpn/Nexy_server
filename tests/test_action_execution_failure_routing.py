import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.action_execution_integration import ActionExecutionIntegration


@pytest.mark.asyncio
async def test_send_message_failure_uses_messages_event_and_no_interrupt_when_suppressed():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = ActionExecutionIntegration(event_bus, state_manager, ErrorHandler(event_bus))
    integration._open_app_config.speak_errors = False

    failed_events: list[dict] = []
    interrupt_events: list[dict] = []
    wrong_domain_events: list[dict] = []

    async def on_failed(event):
        failed_events.append(event)

    async def on_interrupt(event):
        interrupt_events.append(event)

    async def on_wrong_domain(event):
        wrong_domain_events.append(event)

    await event_bus.subscribe("actions.send_message.failed", on_failed)
    await event_bus.subscribe("interrupt.request", on_interrupt)
    await event_bus.subscribe("actions.open_app.failed", on_wrong_domain)

    await integration._publish_failure(
        session_id="sid-1",
        feature_id="F-2025-016-messages",
        error_code="similar_contacts_found",
        message="Contact not found",
        app_name="Messages",
        command="send_message",
        suppress_playback_cancel=True,
    )

    assert len(failed_events) == 1
    assert failed_events[0]["type"] == "actions.send_message.failed"
    assert len(interrupt_events) == 0
    assert len(wrong_domain_events) == 0


@pytest.mark.asyncio
async def test_open_app_failure_keeps_interrupt_cancel_flow():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = ActionExecutionIntegration(event_bus, state_manager, ErrorHandler(event_bus))
    integration._open_app_config.speak_errors = False

    failed_events: list[dict] = []
    interrupt_events: list[dict] = []

    async def on_failed(event):
        failed_events.append(event)

    async def on_interrupt(event):
        interrupt_events.append(event)

    await event_bus.subscribe("actions.open_app.failed", on_failed)
    await event_bus.subscribe("interrupt.request", on_interrupt)

    await integration._publish_failure(
        session_id="sid-2",
        feature_id="F-2025-013-open-app",
        error_code="app_not_found",
        message="App not found",
        app_name="FakeApp",
        command="open_app",
        suppress_playback_cancel=False,
    )

    assert len(failed_events) == 1
    assert failed_events[0]["type"] == "actions.open_app.failed"
    assert len(interrupt_events) == 1
    assert interrupt_events[0]["type"] == "interrupt.request"

