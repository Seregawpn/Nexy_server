from __future__ import annotations

import os
import sys

import pytest

sys.path.insert(0, os.getcwd())

from integration.core.simple_module_coordinator import SimpleModuleCoordinator
from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager


@pytest.mark.asyncio
async def test_permissions_completed_sets_completed_true_only_when_all_granted() -> None:
    coordinator = SimpleModuleCoordinator()
    coordinator.state_manager = ApplicationStateManager()
    coordinator.state_manager.set_first_run_state(in_progress=True, required=True, completed=False)

    await coordinator._on_permissions_completed(
        {"data": {"session_id": "s1", "all_granted": True, "missing": []}}
    )

    assert coordinator.state_manager.get_state_data(StateKeys.FIRST_RUN_IN_PROGRESS, True) is False
    assert coordinator.state_manager.get_state_data(StateKeys.FIRST_RUN_REQUIRED, True) is False
    assert coordinator.state_manager.get_state_data(StateKeys.FIRST_RUN_COMPLETED, False) is True


@pytest.mark.asyncio
async def test_permissions_completed_keeps_required_when_not_all_granted() -> None:
    coordinator = SimpleModuleCoordinator()
    coordinator.state_manager = ApplicationStateManager()
    coordinator.state_manager.set_first_run_state(in_progress=True, required=True, completed=False)

    await coordinator._on_permissions_completed(
        {"data": {"session_id": "s2", "all_granted": False, "missing": ["contacts"]}}
    )

    assert coordinator.state_manager.get_state_data(StateKeys.FIRST_RUN_IN_PROGRESS, True) is False
    assert coordinator.state_manager.get_state_data(StateKeys.FIRST_RUN_REQUIRED, False) is True
    assert coordinator.state_manager.get_state_data(StateKeys.FIRST_RUN_COMPLETED, True) is False
