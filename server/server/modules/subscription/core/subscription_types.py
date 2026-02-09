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


def map_status_to_tier(status: Optional[str]) -> AccessTier:
    if not status:
        return AccessTier.LIMITED
    normalized = status.lower()
    if normalized in UNLIMITED_STATUSES:
        return AccessTier.UNLIMITED
    if normalized in LIMITED_STATUSES:
        return AccessTier.LIMITED
    return AccessTier.LIMITED
