"""
Regression test for browser action race condition.

The bug: when gRPC responds with both TTS audio and a browser_use action,
playback.completed can fire before browser.started (because Chromium takes
time to initialize). ProcessingWorkflow would then see
  grpc_completed=True, playback_completed=True, browser_active=False
and prematurely complete the chain → SLEEPING → cancel browser task.

The fix: ProcessingWorkflow now tracks `action_dispatched` flag set by
`actions.browser_use.started` and blocks chain completion until
`browser.started` arrives.
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from integration.core.event_bus import EventBus
from integration.workflows.base_workflow import WorkflowState
from integration.workflows.processing_workflow import ProcessingWorkflow


async def _start_workflow(event_bus: EventBus) -> ProcessingWorkflow:
    """Helper: create and start a ProcessingWorkflow with an active session."""
    wf = ProcessingWorkflow(event_bus)
    await wf._setup_subscriptions()
    await wf._on_mode_changed(
        {"data": {"mode": "processing", "session_id": "sid-race", "source": "input_processing"}}
    )
    assert wf.state == WorkflowState.ACTIVE
    assert wf.current_session_id == "sid-race"
    return wf


@pytest.mark.asyncio
async def test_chain_NOT_completed_when_browser_action_dispatched_but_not_started() -> None:
    """
    Simulate the race condition:
    1. gRPC completed
    2. Browser action dispatched (actions.browser_use.started)
    3. Playback completed
    => chain must NOT complete because browser hasn't started yet.
    """
    bus = EventBus()
    terminal_events: list[dict] = []

    async def capture_terminal(event):
        terminal_events.append(event)

    await bus.subscribe("processing.terminal", capture_terminal)

    wf = await _start_workflow(bus)

    # 1. gRPC request completed
    wf.grpc_completed = True
    wf.grpc_started = True

    # 2. Browser action dispatched (but Chromium not started)
    await bus.publish(
        "actions.browser_use.started",
        {"session_id": "sid-race", "command": "browser_use"},
    )
    assert wf.action_dispatched is True
    assert wf.browser_active is False

    # 3. Playback completed (TTS finished quickly)
    wf.playback_completed = True
    await wf._complete_processing_chain()

    # Chain must NOT have completed — action_dispatched blocks it
    assert wf.state == WorkflowState.ACTIVE
    assert len(terminal_events) == 0, "processing.terminal must NOT fire while action_dispatched"


@pytest.mark.asyncio
async def test_chain_completes_after_browser_started_and_completed() -> None:
    """
    Full happy path:
    1. gRPC completed
    2. Browser action dispatched
    3. Playback completed
    4. Browser started (action_dispatched cleared)
    5. Browser completed
    => chain completes normally.
    """
    bus = EventBus()
    terminal_events: list[dict] = []

    async def capture_terminal(event):
        terminal_events.append(event)

    await bus.subscribe("processing.terminal", capture_terminal)

    wf = await _start_workflow(bus)

    # 1-3: Same setup as above
    wf.grpc_completed = True
    wf.grpc_started = True
    await bus.publish(
        "actions.browser_use.started",
        {"session_id": "sid-race", "command": "browser_use"},
    )
    wf.playback_completed = True

    # 4. Browser started
    await bus.publish(
        "browser.started",
        {"session_id": "sid-race", "task_id": "t1"},
    )
    assert wf.action_dispatched is False  # Cleared by browser.started
    assert wf.browser_active is True

    # Chain still blocked because browser_active is True
    await wf._complete_processing_chain()
    assert len(terminal_events) == 0

    # 5. Browser completed
    await bus.publish(
        "browser.completed",
        {"session_id": "sid-race", "task_id": "t1"},
    )
    assert wf.browser_active is False

    # Now chain should complete
    await wf._complete_processing_chain()
    assert len(terminal_events) == 1


@pytest.mark.asyncio
async def test_chain_completes_normally_without_browser_action() -> None:
    """
    Regular flow without browser actions:
    gRPC completed + playback completed => chain completes (as before fix).
    """
    bus = EventBus()
    terminal_events: list[dict] = []

    async def capture_terminal(event):
        terminal_events.append(event)

    await bus.subscribe("processing.terminal", capture_terminal)

    wf = await _start_workflow(bus)

    wf.grpc_completed = True
    wf.grpc_started = True
    wf.playback_completed = True

    # No browser action dispatched => chain should complete
    assert wf.action_dispatched is False
    await wf._complete_processing_chain()

    assert len(terminal_events) == 1
