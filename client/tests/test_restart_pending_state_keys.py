from __future__ import annotations

import os
import sys
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch

import pytest

sys.path.insert(0, os.getcwd())

from integration.core.simple_module_coordinator import SimpleModuleCoordinator
from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.permission_restart_integration import PermissionRestartIntegration


@pytest.mark.asyncio
async def test_coordinator_requests_restart_via_permission_restart_in_restricted_mode() -> None:
    coordinator = SimpleModuleCoordinator()
    coordinator.state_manager = ApplicationStateManager()
    coordinator._permissions_restricted_startup = True
    coordinator.integrations = {
        "permission_restart": Mock(
            request_restart_after_first_run_completed=AsyncMock(return_value=True)
        )
    }

    await coordinator._on_permissions_completed(
        {
            "data": {
                "session_id": "sid-1",
                "all_granted": True,
                "missing": [],
            }
        }
    )

    coordinator.integrations["permission_restart"].request_restart_after_first_run_completed.assert_awaited_once_with(
        session_id="sid-1"
    )
    sm = coordinator.state_manager
    assert sm.get_state_data(StateKeys.FIRST_RUN_IN_PROGRESS, True) is False
    assert sm.get_state_data(StateKeys.FIRST_RUN_REQUIRED, True) is False
    assert sm.get_state_data(StateKeys.FIRST_RUN_COMPLETED, False) is True


@pytest.mark.asyncio
async def test_permission_restart_bypass_env_ignored_in_production() -> None:
    event_bus = Mock()
    event_bus.publish = AsyncMock()
    integration = PermissionRestartIntegration(
        event_bus=event_bus,
        state_manager=ApplicationStateManager(),
        error_handler=Mock(),
        config={},
    )
    integration._v2_enabled = False
    integration._ready_emitted = False
    integration._ready_pending_update = False

    with patch("integration.integrations.permission_restart_integration.is_production_env", return_value=True):
        with patch("integration.integrations.permission_restart_integration.get_bundle_id", return_value="com.nexy.assistant"):
            with patch.dict(os.environ, {"NEXY_BYPASS_PERMISSION_READY": "1"}, clear=False):
                await integration._publish_ready_if_applicable(source="test")

    event_bus.publish.assert_not_called()
    assert integration._ready_emitted is False


@pytest.mark.asyncio
async def test_permission_restart_publishes_only_permissions_ready_in_legacy_path() -> None:
    event_bus = Mock()
    event_bus.publish = AsyncMock()
    integration = PermissionRestartIntegration(
        event_bus=event_bus,
        state_manager=ApplicationStateManager(),
        error_handler=Mock(),
        config={},
    )
    integration._v2_enabled = False
    integration._ready_emitted = False
    integration._ready_pending_update = False

    with patch("integration.integrations.permission_restart_integration.get_bundle_id", return_value="com.nexy.assistant"):
        with patch.dict(os.environ, {"NEXY_BYPASS_PERMISSION_READY": "0"}, clear=False):
            await integration._publish_ready_if_applicable(source="test")

    calls = event_bus.publish.await_args_list
    assert len(calls) == 1
    assert calls[0].args[0] == "system.permissions_ready"


@pytest.mark.asyncio
async def test_permission_restart_skips_legacy_startup_detector_when_v2_enabled() -> None:
    event_bus = Mock()
    event_bus.publish = AsyncMock()
    integration = PermissionRestartIntegration(
        event_bus=event_bus,
        state_manager=ApplicationStateManager(),
        error_handler=Mock(),
        config={},
    )
    integration._v2_enabled = True
    integration._ready_emitted = False
    integration._ready_pending_update = False
    integration._detector.process_event = Mock()

    with patch("integration.integrations.permission_restart_integration.get_bundle_id", return_value="com.nexy.assistant"):
        with patch.dict(os.environ, {"NEXY_BYPASS_PERMISSION_READY": "0"}, clear=False):
            await integration._on_app_startup_event({})

    integration._detector.process_event.assert_not_called()
    event_bus.publish.assert_not_called()


@pytest.mark.asyncio
async def test_permission_restart_aborts_if_first_run_active_without_restart_pending_before_trigger() -> None:
    state_manager = ApplicationStateManager()
    state_manager.set_first_run_state(in_progress=True, required=True, completed=False)

    integration = PermissionRestartIntegration(
        event_bus=Mock(),
        state_manager=state_manager,
        error_handler=Mock(),
        config={},
    )
    integration._config = SimpleNamespace(restart_delay_sec=0.0)
    integration._restart_handler = Mock()
    integration._restart_handler.trigger_restart = AsyncMock()
    integration._restart_handler.get_recent_restart_flag = Mock(return_value=None)

    await integration._execute_scheduled_restart("test_reason", ["microphone"])

    integration._restart_handler.trigger_restart.assert_not_called()


@pytest.mark.asyncio
async def test_permission_restart_aborts_if_recent_restart_flag_detected_before_trigger() -> None:
    integration = PermissionRestartIntegration(
        event_bus=Mock(),
        state_manager=ApplicationStateManager(),
        error_handler=Mock(),
        config={},
    )
    integration._config = SimpleNamespace(restart_delay_sec=0.0)
    integration._restart_handler = Mock()
    integration._restart_handler.trigger_restart = AsyncMock()
    integration._restart_handler.get_recent_restart_flag = Mock(return_value={"timestamp": 123.0})

    await integration._execute_scheduled_restart("test_reason", ["screen_capture"])

    integration._restart_handler.trigger_restart.assert_not_called()


@pytest.mark.asyncio
async def test_permission_restart_aborts_if_user_quit_intent_is_set_before_trigger() -> None:
    state_manager = ApplicationStateManager()
    state_manager.set_state_data(StateKeys.USER_QUIT_INTENT, True)

    integration = PermissionRestartIntegration(
        event_bus=Mock(),
        state_manager=state_manager,
        error_handler=Mock(),
        config={},
    )
    integration._config = SimpleNamespace(restart_delay_sec=0.0)
    integration._restart_handler = Mock()
    integration._restart_handler.trigger_restart = AsyncMock()
    integration._restart_handler.get_recent_restart_flag = Mock(return_value=None)

    await integration._execute_scheduled_restart("test_reason", ["accessibility"])

    integration._restart_handler.trigger_restart.assert_not_called()


@pytest.mark.asyncio
async def test_permission_restart_aborts_if_updater_is_busy_before_trigger() -> None:
    integration = PermissionRestartIntegration(
        event_bus=Mock(),
        state_manager=ApplicationStateManager(),
        error_handler=Mock(),
        config={},
        updater_integration=Mock(is_update_in_progress=Mock(return_value=True)),
    )
    integration._config = SimpleNamespace(restart_delay_sec=0.0)
    integration._restart_handler = Mock()
    integration._restart_handler.trigger_restart = AsyncMock()
    integration._restart_handler.get_recent_restart_flag = Mock(return_value=None)

    await integration._execute_scheduled_restart("test_reason", ["input_monitoring"])

    integration._restart_handler.trigger_restart.assert_not_called()


@pytest.mark.asyncio
async def test_permission_restart_marks_first_run_restart_scheduled_state() -> None:
    state_manager = ApplicationStateManager()
    integration = PermissionRestartIntegration(
        event_bus=Mock(),
        state_manager=state_manager,
        error_handler=Mock(),
        config={},
    )
    integration._config = SimpleNamespace(enabled=True, restart_delay_sec=1.0)
    integration._restart_handler = Mock()
    integration._restart_handler.get_recent_restart_flag = Mock(return_value=None)

    fake_task = Mock()
    fake_task.done.return_value = False
    fake_task.add_done_callback = Mock()

    def _fake_create_task(coro):
        coro.close()
        return fake_task

    with patch("integration.integrations.permission_restart_integration.asyncio.create_task", side_effect=_fake_create_task):
        scheduled = await integration.request_restart_after_first_run_completed(session_id="s-final")

    assert scheduled is True
    assert state_manager.get_state_data(StateKeys.FIRST_RUN_RESTART_SCHEDULED, False) is True
