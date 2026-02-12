from __future__ import annotations

from pathlib import Path
import sys
from unittest.mock import AsyncMock

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import integration.integrations.autostart_manager_integration as autostart_module
from integration.integrations.autostart_manager_integration import AutostartManagerIntegration
from modules.autostart_manager.core.types import AutostartStatus
import pytest


class _FakeStateManager:
    def __init__(self, *, user_quit_intent: bool = False) -> None:
        self._state = {"user_quit_intent": user_quit_intent}

    def get_state_data(self, key: str, default=None):
        return self._state.get(key, default)


def _make_integration(*, auto_repair: bool = True, user_quit_intent: bool = False) -> AutostartManagerIntegration:
    return AutostartManagerIntegration(
        event_bus=None,  # type: ignore[arg-type]
        state_manager=_FakeStateManager(user_quit_intent=user_quit_intent),  # type: ignore[arg-type]
        error_handler=None,  # type: ignore[arg-type]
        config={"auto_repair": auto_repair},
    )


def test_should_repair_when_enabled_and_missing_agent(monkeypatch) -> None:
    integration = _make_integration(auto_repair=True)
    monkeypatch.setattr(autostart_module, "is_update_in_progress", lambda _sm: False)
    monkeypatch.setattr(autostart_module, "is_first_run_in_progress", lambda _sm: False)

    should_repair, reason = integration._should_repair_autostart(launch_agent_exists=False)
    assert should_repair is True
    assert reason == ""


def test_should_not_repair_when_user_quit_intent(monkeypatch) -> None:
    integration = _make_integration(auto_repair=True, user_quit_intent=True)
    monkeypatch.setattr(autostart_module, "is_update_in_progress", lambda _sm: False)
    monkeypatch.setattr(autostart_module, "is_first_run_in_progress", lambda _sm: False)

    should_repair, reason = integration._should_repair_autostart(launch_agent_exists=False)
    assert should_repair is False
    assert reason == "user_quit_intent_active"


def test_should_not_repair_when_update_in_progress(monkeypatch) -> None:
    integration = _make_integration(auto_repair=True)
    monkeypatch.setattr(autostart_module, "is_update_in_progress", lambda _sm: True)
    monkeypatch.setattr(autostart_module, "is_first_run_in_progress", lambda _sm: False)

    should_repair, reason = integration._should_repair_autostart(launch_agent_exists=False)
    assert should_repair is False
    assert reason == "update_in_progress"


def test_should_not_repair_when_user_opt_out(monkeypatch) -> None:
    integration = _make_integration(auto_repair=True)
    monkeypatch.setattr(autostart_module, "is_update_in_progress", lambda _sm: False)
    monkeypatch.setattr(autostart_module, "is_first_run_in_progress", lambda _sm: False)
    monkeypatch.setattr(integration, "_is_autostart_opted_out", lambda: True)

    should_repair, reason = integration._should_repair_autostart(launch_agent_exists=False)
    assert should_repair is False
    assert reason == "user_opt_out"


def test_user_quit_intent_accessor_prefers_event_payload() -> None:
    integration = _make_integration(auto_repair=True, user_quit_intent=False)
    assert integration._is_user_quit_intent({"user_initiated": True}) is True


@pytest.mark.asyncio
async def test_enable_requested_clears_opt_out_and_enables_autostart(monkeypatch) -> None:
    event_bus = type("Bus", (), {"publish": AsyncMock()})()
    integration = AutostartManagerIntegration(
        event_bus=event_bus,  # type: ignore[arg-type]
        state_manager=_FakeStateManager(),  # type: ignore[arg-type]
        error_handler=None,  # type: ignore[arg-type]
        config={"auto_repair": True},
    )
    integration._autostart_manager.enable_autostart = AsyncMock(return_value=AutostartStatus.ENABLED)  # type: ignore[method-assign]
    calls: list[bool] = []
    monkeypatch.setattr(integration, "_set_user_opt_out", lambda enabled: calls.append(enabled))

    await integration._on_enable_requested({})

    assert calls == [False]
    integration._autostart_manager.enable_autostart.assert_awaited_once()  # type: ignore[attr-defined]
    event_bus.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_disable_requested_sets_opt_out_and_disables_autostart(monkeypatch) -> None:
    event_bus = type("Bus", (), {"publish": AsyncMock()})()
    integration = AutostartManagerIntegration(
        event_bus=event_bus,  # type: ignore[arg-type]
        state_manager=_FakeStateManager(),  # type: ignore[arg-type]
        error_handler=None,  # type: ignore[arg-type]
        config={"auto_repair": True},
    )
    integration._autostart_manager.disable_autostart = AsyncMock(return_value=AutostartStatus.DISABLED)  # type: ignore[method-assign]
    calls: list[bool] = []
    monkeypatch.setattr(integration, "_set_user_opt_out", lambda enabled: calls.append(enabled))

    await integration._on_disable_requested({})

    assert calls == [True]
    integration._autostart_manager.disable_autostart.assert_awaited_once()  # type: ignore[attr-defined]
    event_bus.publish.assert_awaited_once()


def test_should_not_repair_when_first_run_restart_scheduled(monkeypatch) -> None:
    integration = _make_integration(auto_repair=True)
    integration.state_manager._state["first_run_restart_scheduled"] = True
    monkeypatch.setattr(autostart_module, "is_update_in_progress", lambda _sm: False)
    monkeypatch.setattr(autostart_module, "is_first_run_in_progress", lambda _sm: False)

    should_repair, reason = integration._should_repair_autostart(launch_agent_exists=False)
    assert should_repair is False
    assert reason == "first_run_restart_scheduled"
