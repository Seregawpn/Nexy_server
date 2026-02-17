from unittest.mock import AsyncMock, Mock

import pytest

from integration.integrations.mode_management_integration import ModeManagementIntegration
from modules.mode_management import AppMode


def _build_integration(current_mode: AppMode, current_session_id: str | None):
    state_manager = Mock()
    state_manager.get_current_mode.return_value = current_mode
    state_manager.get_current_session_id.return_value = current_session_id

    integration = ModeManagementIntegration(
        event_bus=Mock(),
        state_manager=state_manager,
        error_handler=Mock(),
    )
    integration._apply_mode = AsyncMock()
    return integration, state_manager


def test_collect_blockers_does_not_use_global_any_with_session():
    integration, _ = _build_integration(AppMode.PROCESSING, None)
    integration._active_playback_sessions.add("foreign-session")

    blockers = integration._collect_blockers_for_sleep_guard(
        "3f92511e-5c82-41e5-aae4-38a9ebb8d1ee"
    )

    assert blockers == []


@pytest.mark.asyncio
async def test_mode_request_sleeping_not_deferred_by_foreign_playback_any():
    session_id = "3f92511e-5c82-41e5-aae4-38a9ebb8d1ee"
    integration, _ = _build_integration(AppMode.PROCESSING, session_id)
    integration._active_playback_sessions.add("foreign-playback-session")

    await integration._on_mode_request(
        {
            "data": {
                "target": AppMode.SLEEPING,
                "source": "ProcessingWorkflow.processing_failed_recognition",
                "session_id": session_id,
                "priority": 90,
            }
        }
    )

    integration._apply_mode.assert_awaited_once_with(
        AppMode.SLEEPING,
        source="interrupt",
        session_id=session_id,
    )


def test_normalize_session_id_rejects_non_uuid_values():
    assert (
        ModeManagementIntegration._normalize_session_id("system") is None
    )
    assert (
        ModeManagementIntegration._normalize_session_id(
            "3f92511e-5c82-41e5-aae4-38a9ebb8d1ee"
        )
        == "3f92511e-5c82-41e5-aae4-38a9ebb8d1ee"
    )
