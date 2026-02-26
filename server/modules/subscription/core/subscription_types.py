#!/usr/bin/env python3
"""
Subscription type helpers.

Source of Truth for mapping Stripe/DB statuses to access tiers.
"""
from enum import Enum
from typing import Optional


class AccessTier(str, Enum):
    UNLIMITED = "unlimited"
    LIMITED = "limited"
    BLOCKED = "blocked"


UNLIMITED_STATUSES = {
    "paid",
    "active",
    "paid_trial",
    "trialing",
    "admin_active",
    "grandfathered",
}

TRIAL_STATUSES = {
    "paid_trial",
    "trialing",
}

PAID_STATUSES = {
    "paid",
    "active",
    "admin_active",
    "grandfathered",
}

LIMITED_STATUSES = {
    "canceled",
    "unpaid",
    "past_due",
    "incomplete",
    "incomplete_expired",
    "paused",
    "limited_free_trial",
    "trialing_expired",
    "none",
    "unknown",
}


def map_status_to_tier(status: Optional[str], grandfathered_enabled: bool = True) -> AccessTier:
    if not status:
        return AccessTier.LIMITED
    normalized = status.lower()
    if normalized == "grandfathered" and not grandfathered_enabled:
        return AccessTier.LIMITED
    if normalized in UNLIMITED_STATUSES:
        return AccessTier.UNLIMITED
    if normalized in LIMITED_STATUSES:
        return AccessTier.LIMITED
    return AccessTier.LIMITED


def map_stripe_status_to_local_status(
    stripe_status: Optional[str],
    fallback_status: Optional[str] = None,
) -> str:
    """
    Single mapping source: Stripe subscription status -> local subscription status.
    """
    normalized = (stripe_status or "").strip().lower()
    if normalized == "active":
        return "paid"
    if normalized == "trialing":
        return "paid_trial"
    if normalized in {"past_due", "unpaid", "incomplete"}:
        return "billing_problem"
    if normalized in {"canceled", "incomplete_expired", "deleted"}:
        return "limited_free_trial"
    return fallback_status or "limited_free_trial"
