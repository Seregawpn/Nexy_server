#!/usr/bin/env python3
import sys
from pathlib import Path
from datetime import datetime, timedelta, timezone

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.subscription.subscription_module import SubscriptionModule


class _ConfigStub:
    trial_days = None

    @staticmethod
    def is_active() -> bool:
        return True


class _RepoStub:
    def __init__(self, row):
        self.row = row
        self.updates = []
        self.created = []

    def get_subscription(self, hardware_id: str):
        if self.row and self.row.get("hardware_id") == hardware_id:
            return dict(self.row)
        return None

    def update_subscription(self, hardware_id: str, **kwargs):
        self.updates.append({"hardware_id": hardware_id, **kwargs})
        if self.row and self.row.get("hardware_id") == hardware_id:
            self.row.update(kwargs)
            return True
        return False

    def create_subscription(self, hardware_id: str, status: str = "paid_trial", **kwargs):
        self.created.append({"hardware_id": hardware_id, "status": status, **kwargs})
        self.row = {"hardware_id": hardware_id, "status": status}
        return dict(self.row)


class _StripeStub:
    def __init__(self, existing=None):
        self.existing = existing or {}
        self.create_calls = 0

    def get_checkout_session(self, session_id: str):
        return self.existing.get(session_id)

    def get_subscription(self, subscription_id: str):
        return {
            "status": "active",
            "current_period_end": datetime(2026, 3, 23, tzinfo=timezone.utc),
            "cancel_at_period_end": False,
        }

    async def create_checkout_session(self, **kwargs):
        self.create_calls += 1
        return {
            "checkout_url": "https://checkout.stripe.test/new",
            "session_id": "cs_new",
            "customer_id": "cus_new",
            "subscription_id": "sub_new",
        }


def _make_module(repo, stripe):
    module = SubscriptionModule()
    module.config = _ConfigStub()
    module._initialized = True
    module._repository = repo
    module._stripe_service = stripe
    module.invalidate_all_cache()
    return module


@pytest.mark.asyncio
async def test_create_checkout_reuses_recent_open_session():
    now_utc = datetime.now(timezone.utc)
    repo = _RepoStub(
        {
            "hardware_id": "HW1",
            "stripe_customer_id": "cus_existing",
            "last_checkout_session_id": "cs_recent",
            "last_checkout_created_at": now_utc - timedelta(minutes=2),
        }
    )
    stripe = _StripeStub(
        existing={
            "cs_recent": {
                "id": "cs_recent",
                "status": "open",
                "customer_id": "cus_existing",
                "subscription_id": None,
                "url": "https://checkout.stripe.test/recent",
            }
        }
    )
    module = _make_module(repo, stripe)

    result = await module.create_checkout_session("HW1", base_url="http://127.0.0.1:8080")

    assert result is not None
    assert result["reused"] is True
    assert result["session_id"] == "cs_recent"
    assert stripe.create_calls == 0


@pytest.mark.asyncio
async def test_create_checkout_persists_customer_and_checkout_metadata():
    repo = _RepoStub({"hardware_id": "HW2", "stripe_customer_id": None})
    stripe = _StripeStub()
    module = _make_module(repo, stripe)

    result = await module.create_checkout_session("HW2", base_url="http://127.0.0.1:8080")

    assert result is not None
    assert result["session_id"] == "cs_new"
    assert stripe.create_calls == 1
    assert repo.updates, "Expected checkout metadata update"
    last_update = repo.updates[-1]
    assert last_update["hardware_id"] == "HW2"
    assert last_update["stripe_customer_id"] == "cus_new"
    assert last_update["last_checkout_session_id"] == "cs_new"
    assert isinstance(last_update["last_checkout_created_at"], datetime)


@pytest.mark.asyncio
async def test_reconcile_creates_missing_subscription_row_after_reset():
    repo = _RepoStub(row=None)  # simulates DB reset (no subscriptions row)
    stripe = _StripeStub(
        existing={
            "cs_paid": {
                "status": "complete",
                "payment_status": "paid",
                "metadata": {"hardware_id": "HW_MISSING"},
                "subscription_id": "sub_paid",
                "customer_id": "cus_paid",
            }
        }
    )
    module = _make_module(repo, stripe)

    result = await module.reconcile_checkout_success("cs_paid")

    assert result["ok"] is True
    assert result["status"] == "paid"
    assert repo.created, "Expected create_subscription fallback"
    assert repo.row is not None
    assert repo.row["hardware_id"] == "HW_MISSING"
    assert repo.row["status"] == "paid"
