#!/usr/bin/env python3
import sys
from pathlib import Path

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.subscription.subscription_module import SubscriptionModule


class _ConfigStub:
    grandfathered_enabled = True

    @staticmethod
    def is_active() -> bool:
        return True


class _RepoStub:
    def __init__(self, sub):
        self._sub = sub
        self.updates = []

    def get_subscription(self, hardware_id: str):
        return self._sub.get(hardware_id)

    def update_subscription(self, hardware_id: str, **kwargs):
        row = self._sub.get(hardware_id)
        if not row:
            return False
        row.update(kwargs)
        self.updates.append((hardware_id, dict(kwargs)))
        return True


class _StripePortalMissingCustomerStub:
    def create_portal_session(self, customer_id: str, email=None):
        raise Exception("No such customer: cus_missing")


@pytest.mark.asyncio
async def test_portal_missing_customer_clears_stale_customer_id_for_checkout_recovery():
    hw = "HW_PORTAL_RECOVERY"
    repo = _RepoStub(
        {
            hw: {
                "status": "limited_free_trial",
                "stripe_customer_id": "cus_missing",
                "email": "user@example.com",
            }
        }
    )

    module = SubscriptionModule()
    module.config = _ConfigStub()
    module._initialized = True
    module._repository = repo
    module._stripe_service = _StripePortalMissingCustomerStub()

    result = await module.create_portal_session(hw)

    assert result is None
    assert repo._sub[hw]["stripe_customer_id"] is None

    status = await module.get_subscription_status(hw)
    assert status["recommended_billing_route"] == "checkout"
    assert status["billing_action"] == "checkout"
