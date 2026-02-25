#!/usr/bin/env python3
from api.webhooks.stripe_webhook import _resolve_hardware_id_from_repo


class _RepoStub:
    def __init__(self):
        self.by_sub = {}
        self.by_customer = {}

    def get_subscription_by_stripe_subscription_id(self, subscription_id):
        return self.by_sub.get(subscription_id)

    def get_subscription_by_stripe_customer_id(self, customer_id):
        return self.by_customer.get(customer_id)


def test_resolve_hardware_id_prefers_subscription_id():
    repo = _RepoStub()
    repo.by_sub["sub_123"] = {"hardware_id": "HW_SUB"}
    repo.by_customer["cus_123"] = {"hardware_id": "HW_CUS"}

    event_data = {"subscription": "sub_123", "customer": "cus_123"}
    assert _resolve_hardware_id_from_repo(event_data, repo) == "HW_SUB"


def test_resolve_hardware_id_falls_back_to_customer_id():
    repo = _RepoStub()
    repo.by_customer["cus_123"] = {"hardware_id": "HW_CUS"}

    event_data = {"subscription": "sub_missing", "customer": "cus_123"}
    assert _resolve_hardware_id_from_repo(event_data, repo) == "HW_CUS"


def test_resolve_hardware_id_handles_dict_refs():
    repo = _RepoStub()
    repo.by_sub["sub_abc"] = {"hardware_id": "HW_DICT"}

    event_data = {"subscription": {"id": "sub_abc"}}
    assert _resolve_hardware_id_from_repo(event_data, repo) == "HW_DICT"
