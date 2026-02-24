#!/usr/bin/env python3
import sys
from pathlib import Path
from datetime import datetime, timezone

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.subscription.subscription_module import SubscriptionModule


class _ConfigStub:
    grandfathered_enabled = True

    @staticmethod
    def is_active() -> bool:
        return True


class _QuotaCheckerStub:
    def __init__(self, result):
        self._result = result

    def check_quota(self, hardware_id: str):
        return dict(self._result)


class _RepoStub:
    def __init__(self, by_hw):
        self._by_hw = by_hw
        self.updated = []

    def get_subscription(self, hardware_id: str):
        return self._by_hw.get(hardware_id)

    def update_subscription(self, hardware_id: str, **kwargs):
        current = self._by_hw.get(hardware_id)
        if not current:
            return False
        current.update(kwargs)
        self.updated.append((hardware_id, dict(kwargs)))
        return True


def _make_module(*, quota_result, subscriptions):
    module = SubscriptionModule()
    module.config = _ConfigStub()
    module._initialized = True
    module._quota_checker = _QuotaCheckerStub(quota_result)
    module._repository = _RepoStub(subscriptions)
    module.invalidate_all_cache()
    return module


@pytest.mark.asyncio
async def test_can_process_allows_paid_user():
    module = _make_module(
        quota_result={
            "allowed": True,
            "reason": "paid_unlimited",
            "status": "paid",
            "limits": {},
        },
        subscriptions={},
    )

    result = await module.can_process("HW_PAID")
    assert result.allowed is True
    assert result.status == "paid"
    assert result.reason == "paid_unlimited"


@pytest.mark.asyncio
async def test_status_none_returns_checkout_action():
    module = _make_module(
        quota_result={
            "allowed": True,
            "reason": "new_user",
            "status": "none",
            "limits": {},
        },
        subscriptions={},
    )

    status = await module.get_subscription_status("HW_NEW")
    assert status["status"] == "none"
    assert status["billing_action"] == "checkout"
    assert status["recommended_billing_route"] == "checkout"


@pytest.mark.asyncio
async def test_cancel_at_period_end_user_stays_active_until_period_end():
    module = _make_module(
        quota_result={
            "allowed": True,
            "reason": "paid_unlimited",
            "status": "paid",
            "limits": {},
        },
        subscriptions={
            "HW_CANCELLED_BUT_ACTIVE": {
                "status": "paid",
                "stripe_status": "active",
                "stripe_customer_id": "cus_123",
                "cancel_at_period_end": True,
                "current_period_end": 1798041600,  # deterministic timestamp
            }
        },
    )

    status = await module.get_subscription_status("HW_CANCELLED_BUT_ACTIVE")
    assert status["status"] == "paid"
    assert status["active"] is True
    assert status["billing_active"] is True
    assert status["recommended_billing_route"] == "manage"
    assert status["billing_action"] == "none"


@pytest.mark.asyncio
async def test_cancel_at_period_end_user_still_allowed_by_gate():
    module = _make_module(
        quota_result={
            "allowed": True,
            "reason": "paid_unlimited",
            "status": "paid",
            "limits": {},
        },
        subscriptions={
            "HW_CANCELLED_BUT_NOT_EXPIRED": {
                "status": "paid",
                "stripe_status": "active",
                "stripe_customer_id": "cus_123",
                "cancel_at_period_end": True,
                "current_period_end": 1798041600,
            }
        },
    )

    gate = await module.can_process("HW_CANCELLED_BUT_NOT_EXPIRED")
    assert gate.allowed is True
    assert gate.status == "paid"
    assert gate.reason == "paid_unlimited"


@pytest.mark.asyncio
async def test_paid_trial_user_is_active_until_trial_end():
    module = _make_module(
        quota_result={
            "allowed": True,
            "reason": "paid_trial_active",
            "status": "paid_trial",
            "limits": {},
        },
        subscriptions={
            "HW_TRIALING": {
                "status": "paid_trial",
                "stripe_status": "trialing",
                "stripe_customer_id": "cus_trial",
                "cancel_at_period_end": False,
                "current_period_end": 1798041600,
            }
        },
    )

    gate = await module.can_process("HW_TRIALING")
    assert gate.allowed is True
    assert gate.status == "paid_trial"

    status = await module.get_subscription_status("HW_TRIALING")
    assert status["active"] is True
    assert status["billing_active"] is True
    assert status["recommended_billing_route"] == "manage"
    assert status["billing_action"] == "none"


@pytest.mark.asyncio
async def test_re_subscribe_flow_prefers_checkout_for_limited_tier_even_with_customer():
    module = _make_module(
        quota_result={
            "allowed": True,
            "reason": "limited_tier",
            "status": "limited_free_trial",
            "limits": {"daily": {"used": 0, "limit": 2}},
        },
        subscriptions={
            "HW_WANTS_RESUBSCRIBE": {
                "status": "limited_free_trial",
                "stripe_status": "canceled",
                "stripe_customer_id": "cus_existing",
                "current_period_end": None,
            }
        },
    )

    status = await module.get_subscription_status("HW_WANTS_RESUBSCRIBE")
    assert status["status"] == "limited_free_trial"
    assert status["recommended_billing_route"] == "checkout"
    assert status["billing_action"] == "checkout"


@pytest.mark.asyncio
async def test_cancelled_and_period_ended_user_is_limited_even_with_customer():
    module = _make_module(
        quota_result={
            "allowed": False,
            "reason": "daily_limit_exceeded",
            "status": "limited_free_trial",
            "message": "Daily limit exceeded. You have 0 daily requests remaining.",
            "limits": {"daily": {"used": 2, "limit": 2}},
        },
        subscriptions={
            "HW_PERIOD_ENDED": {
                "status": "limited_free_trial",
                "stripe_status": "canceled",
                "stripe_customer_id": "cus_keep_for_resubscribe",
                "cancel_at_period_end": True,
                "current_period_end": 1700000000,  # already ended in scenario setup
            }
        },
    )

    gate = await module.can_process("HW_PERIOD_ENDED")
    assert gate.allowed is False
    assert gate.status == "limited_free_trial"
    assert gate.reason == "daily_limit_exceeded"

    status = await module.get_subscription_status("HW_PERIOD_ENDED")
    # project canon: active=True means user can still use limited tier
    assert status["active"] is True
    assert status["billing_active"] is False
    # limited tier should direct to fresh checkout flow
    assert status["recommended_billing_route"] == "checkout"
    assert status["billing_action"] == "checkout"


@pytest.mark.asyncio
async def test_expired_user_with_no_customer_gets_checkout_and_deny():
    module = _make_module(
        quota_result={
            "allowed": False,
            "reason": "daily_limit_exceeded",
            "status": "limited_free_trial",
            "message": "Daily limit exceeded. You have 0 daily requests remaining.",
            "limits": {"daily": {"used": 2, "limit": 2}},
        },
        subscriptions={
            "HW_EXPIRED": {
                "status": "limited_free_trial",
                "stripe_status": None,
                "stripe_customer_id": None,
                "current_period_end": None,
            }
        },
    )

    gate = await module.can_process("HW_EXPIRED")
    assert gate.allowed is False
    assert gate.reason == "daily_limit_exceeded"
    assert gate.status == "limited_free_trial"

    status = await module.get_subscription_status("HW_EXPIRED")
    assert status["recommended_billing_route"] == "checkout"
    assert status["billing_active"] is False
    assert status["billing_action"] == "checkout"


@pytest.mark.asyncio
async def test_status_serializes_datetime_current_period_end_to_iso():
    module = _make_module(
        quota_result={
            "allowed": True,
            "reason": "paid_unlimited",
            "status": "paid",
            "limits": {},
        },
        subscriptions={
            "HW_DATETIME": {
                "status": "paid",
                "stripe_status": "active",
                "stripe_customer_id": "cus_dt",
                "current_period_end": datetime(2026, 3, 31, 12, 30, tzinfo=timezone.utc),
            }
        },
    )

    status = await module.get_subscription_status("HW_DATETIME")
    assert status["status"] == "paid"
    assert status["current_period_end"] == "2026-03-31T12:30:00+00:00"


@pytest.mark.asyncio
async def test_context_marks_cancelled_but_active_until_period_end():
    module = _make_module(
        quota_result={
            "allowed": True,
            "reason": "paid_unlimited",
            "status": "paid",
            "limits": {},
        },
        subscriptions={
            "HW_CANCEL_CONTEXT": {
                "status": "paid",
                "stripe_status": "active",
                "stripe_customer_id": "cus_ctx",
                "cancel_at_period_end": True,
                "current_period_end": 1798041600,
            }
        },
    )

    ctx = await module.get_context_for_prompt("HW_CANCEL_CONTEXT")
    assert "Cancelled" in ctx
    assert "Active until period end" in ctx


class _StripeStub:
    def __init__(self, payload):
        self.payload = payload
        self.calls = 0

    def get_subscription(self, subscription_id: str):
        self.calls += 1
        return dict(self.payload)


@pytest.mark.asyncio
async def test_status_lazy_sync_updates_cancel_flag_without_webhook():
    module = _make_module(
        quota_result={
            "allowed": True,
            "reason": "paid_unlimited",
            "status": "paid",
            "limits": {},
        },
        subscriptions={
            "HW_LAZY_SYNC": {
                "status": "paid",
                "stripe_status": "active",
                "stripe_subscription_id": "sub_123",
                "stripe_customer_id": "cus_123",
                "cancel_at_period_end": False,
                "current_period_end": None,
            }
        },
    )
    stripe = _StripeStub(
        {
            "status": "active",
            "cancel_at_period_end": True,
            "current_period_end": datetime(2026, 4, 30, 12, 0, tzinfo=timezone.utc),
        }
    )
    module._stripe_service = stripe

    status = await module.get_subscription_status("HW_LAZY_SYNC")

    assert status["cancel_at_period_end"] is True
    assert status["current_period_end"] == "2026-04-30T12:00:00+00:00"
    assert stripe.calls == 1


@pytest.mark.asyncio
async def test_status_lazy_sync_is_rate_limited_per_hardware():
    module = _make_module(
        quota_result={
            "allowed": True,
            "reason": "paid_unlimited",
            "status": "paid",
            "limits": {},
        },
        subscriptions={
            "HW_LAZY_RATE_LIMIT": {
                "status": "paid",
                "stripe_status": "active",
                "stripe_subscription_id": "sub_456",
                "stripe_customer_id": "cus_456",
                "cancel_at_period_end": False,
                "current_period_end": None,
            }
        },
    )
    stripe = _StripeStub(
        {
            "status": "active",
            "cancel_at_period_end": False,
            "current_period_end": datetime(2026, 5, 31, 12, 0, tzinfo=timezone.utc),
        }
    )
    module._stripe_service = stripe

    await module.get_subscription_status("HW_LAZY_RATE_LIMIT")
    await module.get_subscription_status("HW_LAZY_RATE_LIMIT")

    assert stripe.calls == 1
