#!/usr/bin/env python3
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.subscription.subscription_module import SubscriptionModule


class _Cfg:
    def __init__(self, mode, sk, pk, wh, price):
        self.stripe_mode = mode
        self.stripe_secret_key = sk
        self.stripe_publishable_key = pk
        self.stripe_webhook_secret = wh
        self.stripe_price_id = price


def _module_with_cfg(cfg):
    module = SubscriptionModule()
    module.config = cfg
    return module


def test_mode_config_validation_accepts_test_keys():
    m = _module_with_cfg(
        _Cfg(
            "test",
            "sk_test_x",
            "pk_test_x",
            "whsec_x",
            "price_x",
        )
    )
    assert m._validate_active_mode_config() is True


def test_mode_config_validation_rejects_live_mode_with_test_secret():
    m = _module_with_cfg(
        _Cfg(
            "live",
            "sk_test_x",
            "pk_live_x",
            "whsec_x",
            "price_x",
        )
    )
    assert m._validate_active_mode_config() is False


def test_mode_config_validation_accepts_live_restricted_key_prefix():
    m = _module_with_cfg(
        _Cfg(
            "live",
            "rk_live_x",
            "pk_live_x",
            "whsec_x",
            "price_x",
        )
    )
    assert m._validate_active_mode_config() is True
