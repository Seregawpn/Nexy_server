"""
Centralized keyword-only routing policy for TextProcessor Tier A.

Data-only module: keeps category token rules outside runtime resolver code while
preserving a single route-decision owner in TextProcessor.
"""

from typing import Dict, Set, FrozenSet

NEGATION_TOKENS: FrozenSet[str] = frozenset(
    {"not", "dont", "don't", "no", "stop", "cancel"}
)

CATEGORY_RULES: Dict[str, Dict[str, object]] = {
    "whatsapp": {
        "domains": {"whatsapp"},
        "actions": {"read", "send", "reply", "open", "check"},
        "requires_action": True,
        "excludes": {"imessage"},
    },
    "messages": {
        "domains": {"message", "messages", "imessage", "sms", "text", "msg", "msgs", "mesage", "mesg"},
        "actions": {"read", "send", "reply", "open", "check", "text", "snd", "smd"},
        "requires_action": True,
        "excludes": {"whatsapp"},
    },
    "describe": {
        "domains": {"screen", "display", "monitor", "window"},
        "actions": {"describe", "show", "read", "what"},
        "requires_action": True,
        "excludes": set(),
    },
    "browser": {
        "domains": {"browser", "site", "website", "page", "tab", "youtube"},
        "actions": {"open", "go", "navigate", "visit"},
        "requires_action": True,
        "excludes": set(),
    },
    "google_search": {
        "domains": {"search", "google", "news", "price", "compare", "find", "lookup"},
        "actions": set(),
        "requires_action": False,
        "excludes": set(),
    },
    "system_control": {
        "domains": {"app", "application"},
        "actions": {"open", "close", "quit", "launch"},
        "requires_action": True,
        "excludes": set(),
    },
    "payment": {
        "domains": {"subscription", "billing", "plan", "payment"},
        "actions": {"check", "upgrade", "cancel", "renew"},
        "requires_action": True,
        "excludes": set(),
    },
    "capability": {
        "domains": {"help", "capabilities"},
        "actions": set(),
        "requires_action": False,
        "excludes": set(),
    },
}
