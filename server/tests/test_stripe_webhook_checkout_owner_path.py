#!/usr/bin/env python3
import sys
from pathlib import Path

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from api.webhooks.stripe_webhook import _handle_event_type


class _RepoStub:
    def __init__(self):
        self.created = False

    def get_subscription(self, hardware_id):
        return {"hardware_id": hardware_id, "status": "limited_free_trial"}

    def create_or_update_subscription(self, **kwargs):  # legacy path should not be used
        self.created = True
        return True


class _ModuleStub:
    def __init__(self, result):
        self._result = result

    async def reconcile_checkout_success(self, session_id):
        return dict(self._result)


@pytest.mark.asyncio
async def test_checkout_completed_skips_when_reconcile_not_ok(monkeypatch):
    repo = _RepoStub()
    module = _ModuleStub({"ok": False, "reason": "session_not_paid"})

    monkeypatch.setattr("modules.subscription.get_subscription_module", lambda: module)

    result = await _handle_event_type(
        event_type="checkout.session.completed",
        event_data={"id": "cs_test_1", "customer": "cus_1", "subscription": "sub_1"},
        hardware_id="HW1",
        repo=repo,
        event_id="evt_1",
        stripe_created=None,
    )

    assert result["status"] == "skipped"
    assert result["reason"] == "reconcile_not_ok"
    assert repo.created is False


@pytest.mark.asyncio
async def test_checkout_completed_skips_when_subscription_module_unavailable(monkeypatch):
    repo = _RepoStub()
    monkeypatch.setattr("modules.subscription.get_subscription_module", lambda: None)

    result = await _handle_event_type(
        event_type="checkout.session.completed",
        event_data={"id": "cs_test_2", "customer": "cus_2", "subscription": "sub_2"},
        hardware_id="HW2",
        repo=repo,
        event_id="evt_2",
        stripe_created=None,
    )

    assert result["status"] == "skipped"
    assert result["reason"] == "reconcile_unavailable"
    assert repo.created is False


@pytest.mark.asyncio
async def test_subscription_updated_passes_cancel_scheduled_flag_to_state_machine(monkeypatch):
    repo = _RepoStub()
    captured = {}

    def _fake_transition(**kwargs):
        captured.update(kwargs)
        return {"success": True}

    monkeypatch.setattr(
        "modules.subscription.core.state_machine.SubscriptionStateMachine.transition",
        _fake_transition,
    )

    result = await _handle_event_type(
        event_type="customer.subscription.updated",
        event_data={
            "id": "sub_1",
            "status": "active",
            "cancel_at_period_end": False,
            "cancel_at": 1774239576,
            "current_period_end": 1775000000,
        },
        hardware_id="HW3",
        repo=repo,
        event_id="evt_3",
        stripe_created=None,
    )

    assert result["success"] is True
    assert captured.get("cancel_at_period_end") is True
