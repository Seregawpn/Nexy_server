import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from integration.core.event_bus import EventBus
from integration.workflows.base_workflow import WorkflowState
from integration.workflows.processing_workflow import ProcessingStage, ProcessingWorkflow


@pytest.mark.asyncio
async def test_processing_mode_without_session_id_does_not_start_chain() -> None:
    workflow = ProcessingWorkflow(EventBus())

    await workflow._on_mode_changed(
        {
            "data": {
                "mode": "processing",
                "session_id": None,
                "source": "welcome_message",
            }
        }
    )

    assert workflow.state == WorkflowState.IDLE
    assert workflow.current_session_id is None


@pytest.mark.asyncio
async def test_processing_mode_with_session_id_starts_chain() -> None:
    workflow = ProcessingWorkflow(EventBus())

    await workflow._on_mode_changed(
        {
            "data": {
                "mode": "processing",
                "session_id": "sid-1",
                "source": "input_processing",
            }
        }
    )

    assert workflow.state == WorkflowState.ACTIVE
    assert workflow.current_session_id == "sid-1"


@pytest.mark.asyncio
async def test_early_screenshot_is_buffered_and_consumed_on_processing_start() -> None:
    workflow = ProcessingWorkflow(EventBus())

    await workflow._on_screenshot_captured(
        {"data": {"session_id": "sid-1", "path": "/tmp/shot.webp"}}
    )

    assert workflow.state == WorkflowState.IDLE
    assert "sid-1" in workflow._pending_screenshot_by_session

    await workflow._on_mode_changed(
        {
            "data": {
                "mode": "processing",
                "session_id": "sid-1",
                "source": "input_processing",
            }
        }
    )

    assert workflow.state == WorkflowState.ACTIVE
    assert workflow.current_session_id == "sid-1"
    assert workflow.screenshot_captured is True
    assert workflow.current_stage == ProcessingStage.SENDING_GRPC
    assert "sid-1" not in workflow._pending_screenshot_by_session
