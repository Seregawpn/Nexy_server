"""Canonical allowlist builder for assistant action commands."""

from __future__ import annotations

from typing import Any, List


def get_allowed_commands(
    *,
    system_control_enabled: bool = True,
    messages_enabled: bool = True,
    whatsapp_enabled: bool = False,
    browser_enabled: bool = False,
    payment_enabled: bool = False,
) -> List[str]:
    """Build a deterministic command allowlist from feature flags."""
    allowed_commands: List[str] = []

    if system_control_enabled:
        allowed_commands.extend(["open_app", "close_app"])
    if messages_enabled:
        allowed_commands.extend(["send_message", "read_messages", "find_contact"])
    if whatsapp_enabled:
        allowed_commands.extend(["send_whatsapp_message", "read_whatsapp_messages"])
    if browser_enabled:
        allowed_commands.extend(["browser_use", "close_browser"])
    if payment_enabled:
        allowed_commands.extend(["manage_subscription", "buy_subscription"])

    return allowed_commands


def get_allowed_commands_from_config(config: Any) -> List[str]:
    """
    Build allowlist from unified config object.
    Expected attributes:
      - config.features.messages_enabled
      - config.whatsapp.enabled
      - config.browser_use.enabled
      - config.subscription.is_active()
    """
    return get_allowed_commands(
        system_control_enabled=True,
        messages_enabled=bool(getattr(config.features, "messages_enabled", False)),
        whatsapp_enabled=bool(getattr(config.whatsapp, "enabled", False)),
        browser_enabled=bool(getattr(config.browser_use, "enabled", False)),
        payment_enabled=bool(getattr(config.subscription, "is_active", lambda: False)()),
    )
