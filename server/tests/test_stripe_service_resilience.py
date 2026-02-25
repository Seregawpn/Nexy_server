#!/usr/bin/env python3
import sys
from pathlib import Path
from datetime import datetime, timezone

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.subscription.providers.stripe_service import StripeService
from modules.subscription.repository.subscription_repository import SubscriptionRepository


class _SubscriptionNoPeriod:
    id = "sub_no_period"
    status = "active"
    customer = "cus_123"
    cancel_at_period_end = False


class _SubscriptionWithEpoch:
    id = "sub_epoch"
    status = "active"
    customer = "cus_456"
    current_period_end = 1798041600
    cancel_at_period_end = True


class _SubscriptionWithCancelAtOnly:
    id = "sub_cancel_at"
    status = "active"
    customer = "cus_789"
    current_period_end = None
    cancel_at_period_end = False
    cancel_at = 1774239576


def test_get_subscription_does_not_fail_when_current_period_end_missing(monkeypatch):
    def _fake_retrieve(_subscription_id):
        return _SubscriptionNoPeriod()

    monkeypatch.setattr("stripe.Subscription.retrieve", _fake_retrieve)

    service = StripeService(api_key="sk_test_dummy")
    data = service.get_subscription("sub_no_period")

    assert data["id"] == "sub_no_period"
    assert data["status"] == "active"
    assert data["customer_id"] == "cus_123"
    assert data["current_period_end"] is None
    assert data["cancel_at_period_end"] is False


def test_get_subscription_normalizes_epoch_to_utc_datetime(monkeypatch):
    def _fake_retrieve(_subscription_id):
        return _SubscriptionWithEpoch()

    monkeypatch.setattr("stripe.Subscription.retrieve", _fake_retrieve)

    service = StripeService(api_key="sk_test_dummy")
    data = service.get_subscription("sub_epoch")

    assert isinstance(data["current_period_end"], datetime)
    assert data["current_period_end"].tzinfo == timezone.utc
    assert int(data["current_period_end"].timestamp()) == 1798041600
    assert data["cancel_at_period_end"] is True


def test_repository_normalize_datetime_accepts_stripe_epoch():
    ts = 1798041600
    normalized = SubscriptionRepository._normalize_datetime(ts)
    assert isinstance(normalized, datetime)
    assert normalized.tzinfo == timezone.utc
    assert int(normalized.timestamp()) == ts


def test_get_subscription_treats_cancel_at_as_scheduled_cancellation(monkeypatch):
    def _fake_retrieve(_subscription_id):
        return _SubscriptionWithCancelAtOnly()

    monkeypatch.setattr("stripe.Subscription.retrieve", _fake_retrieve)

    service = StripeService(api_key="sk_test_dummy")
    data = service.get_subscription("sub_cancel_at")

    assert data["id"] == "sub_cancel_at"
    assert data["status"] == "active"
    assert data["cancel_at_period_end"] is True
