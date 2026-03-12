"""
Shared intent route constants.

Single source of truth for allowed primary routes used by routing and
workflow-level compatibility checks.
"""

from typing import FrozenSet

ALLOWED_PRIMARY_ROUTES: FrozenSet[str] = frozenset(
    {
        "none",
        "system_control",
        "messages",
        "whatsapp",
        "browser",
        "payment",
        "google_search",
        "describe",
        "capability",
    }
)

