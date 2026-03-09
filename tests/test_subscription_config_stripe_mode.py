#!/usr/bin/env python3
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config.unified_config import SubscriptionConfig


def _clear_stripe_env(monkeypatch):
    keys = [
        "STRIPE_MODE",
        "STRIPE_SECRET_KEY",
        "STRIPE_PUBLISHABLE_KEY",
        "STRIPE_WEBHOOK_SECRET",
        "STRIPE_PRICE_ID",
        "STRIPE_TEST_SECRET_KEY",
        "STRIPE_TEST_PUBLISHABLE_KEY",
        "STRIPE_TEST_WEBHOOK_SECRET",
        "STRIPE_TEST_PRICE_ID",
        "STRIPE_LIVE_SECRET_KEY",
        "STRIPE_LIVE_PUBLISHABLE_KEY",
        "STRIPE_LIVE_WEBHOOK_SECRET",
        "STRIPE_LIVE_PRICE_ID",
    ]
    for key in keys:
        monkeypatch.delenv(key, raising=False)


def test_subscription_config_uses_test_keys_when_mode_test(monkeypatch):
    _clear_stripe_env(monkeypatch)
    monkeypatch.setenv("STRIPE_MODE", "test")
    monkeypatch.setenv("STRIPE_TEST_SECRET_KEY", "sk_test_mode")
    monkeypatch.setenv("STRIPE_TEST_PUBLISHABLE_KEY", "pk_test_mode")
    monkeypatch.setenv("STRIPE_TEST_WEBHOOK_SECRET", "whsec_test_mode")
    monkeypatch.setenv("STRIPE_TEST_PRICE_ID", "price_test_mode")

    cfg = SubscriptionConfig.from_env()

    assert cfg.stripe_mode == "test"
    assert cfg.stripe_secret_key == "sk_test_mode"
    assert cfg.stripe_publishable_key == "pk_test_mode"
    assert cfg.stripe_webhook_secret == "whsec_test_mode"
    assert cfg.stripe_price_id == "price_test_mode"


def test_subscription_config_uses_live_keys_when_mode_live(monkeypatch):
    _clear_stripe_env(monkeypatch)
    monkeypatch.setenv("STRIPE_MODE", "live")
    monkeypatch.setenv("STRIPE_LIVE_SECRET_KEY", "sk_live_mode")
    monkeypatch.setenv("STRIPE_LIVE_PUBLISHABLE_KEY", "pk_live_mode")
    monkeypatch.setenv("STRIPE_LIVE_WEBHOOK_SECRET", "whsec_live_mode")
    monkeypatch.setenv("STRIPE_LIVE_PRICE_ID", "price_live_mode")

    cfg = SubscriptionConfig.from_env()

    assert cfg.stripe_mode == "live"
    assert cfg.stripe_secret_key == "sk_live_mode"
    assert cfg.stripe_publishable_key == "pk_live_mode"
    assert cfg.stripe_webhook_secret == "whsec_live_mode"
    assert cfg.stripe_price_id == "price_live_mode"


def test_subscription_config_does_not_use_legacy_keys(monkeypatch):
    _clear_stripe_env(monkeypatch)
    monkeypatch.setenv("STRIPE_SECRET_KEY", "sk_legacy")
    monkeypatch.setenv("STRIPE_PUBLISHABLE_KEY", "pk_legacy")
    monkeypatch.setenv("STRIPE_WEBHOOK_SECRET", "whsec_legacy")
    monkeypatch.setenv("STRIPE_PRICE_ID", "price_legacy")

    cfg = SubscriptionConfig.from_env()

    assert cfg.stripe_mode == "test"
    assert cfg.stripe_secret_key == ""
    assert cfg.stripe_publishable_key == ""
    assert cfg.stripe_webhook_secret == ""
    assert cfg.stripe_price_id == ""
