from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from server.config import unified_config as unified_config_module


def test_whatsapp_server_config_uses_shared_feature_owner(monkeypatch) -> None:
    monkeypatch.setattr(
        unified_config_module,
        "_get_shared_feature_enabled",
        lambda _name: True,
    )
    monkeypatch.setenv("WHATSAPP_ENABLED", "false")

    cfg = unified_config_module.WhatsappConfig.from_env()

    assert cfg.enabled is True


def test_whatsapp_server_config_falls_back_to_env_when_shared_owner_missing(monkeypatch) -> None:
    monkeypatch.setattr(
        unified_config_module,
        "_get_shared_feature_enabled",
        lambda _name: None,
    )
    monkeypatch.setenv("WHATSAPP_ENABLED", "true")

    cfg = unified_config_module.WhatsappConfig.from_env()

    assert cfg.enabled is True


def test_server_messages_feature_uses_shared_owner(monkeypatch) -> None:
    monkeypatch.setattr(
        unified_config_module,
        "_get_shared_feature_enabled",
        lambda name: False if name == "messages" else None,
    )
    monkeypatch.setenv("MESSAGES_ENABLED", "true")

    cfg = unified_config_module.FeaturesConfig.from_env()

    assert cfg.messages_enabled is False


def test_server_browser_feature_uses_shared_owner(monkeypatch) -> None:
    monkeypatch.setattr(
        unified_config_module,
        "_get_shared_feature_enabled_any",
        lambda *_names: False,
    )
    monkeypatch.setenv("BROWSER_USE_ENABLED", "true")

    cfg = unified_config_module.BrowserUseConfig.from_env()

    assert cfg.enabled is False


def test_server_payment_feature_uses_shared_owner(monkeypatch) -> None:
    monkeypatch.setattr(
        unified_config_module,
        "_get_shared_feature_enabled",
        lambda name: False if name == "payment" else None,
    )
    monkeypatch.setenv("SUBSCRIPTION_ENABLED", "true")

    cfg = unified_config_module.SubscriptionConfig.from_env()

    assert cfg.enabled is False
