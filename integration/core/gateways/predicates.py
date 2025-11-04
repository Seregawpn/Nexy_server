"""
Predicate registry for rule-based decision making.

All predicates use existing selectors from integration.core.selectors to avoid duplication.
"""
from __future__ import annotations

from typing import Callable, Dict, Any, Optional

from integration.core.selectors import Snapshot
from integration.core import selectors as sel


REGISTRY: Dict[str, Callable[[Snapshot, Any, Optional[Dict[str, Any]]], bool]] = {}


def _register(name: str):
    """Decorator to register a predicate in the registry."""
    def deco(fn: Callable[[Snapshot, Any, Optional[Dict[str, Any]]], bool]):
        REGISTRY[name] = fn
        return fn
    return deco


# ===== Basic permissions =====

@_register("perm.mic")
def perm_mic(s: Snapshot, expected: str, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if microphone permission matches expected value."""
    return s.perm_mic.value.lower() == str(expected).lower()


@_register("perm.screen")
def perm_screen(s: Snapshot, expected: str, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if screen capture permission matches expected value."""
    return s.perm_screen.value.lower() == str(expected).lower()


@_register("perm.accessibility")
def perm_accessibility(s: Snapshot, expected: str, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if accessibility permission matches expected value."""
    return s.perm_accessibility.value.lower() == str(expected).lower()


# ===== Composite selectors (using existing selectors) =====

@_register("permissions.missing_any")
def permissions_missing_any(s: Snapshot, expected: bool, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if any critical permissions are missing."""
    missing = not (sel.mic_ready(s) and sel.screen_ready(s) and sel.accessibility_ready(s))
    return missing == bool(expected)


@_register("permissions.all_ready")
def permissions_all_ready(s: Snapshot, expected: bool, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if all critical permissions are ready."""
    ready = sel.all_permissions_ready(s)
    return ready == bool(expected)


@_register("device.idle")
def device_idle_predicate(s: Snapshot, expected: bool, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if device is idle."""
    idle = sel.device_idle(s)
    return idle == bool(expected)


@_register("device.busy")
def device_busy_predicate(s: Snapshot, expected: bool, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if device is busy."""
    busy = sel.device_busy(s)
    return busy == bool(expected)


@_register("network.online")
def network_online_predicate(s: Snapshot, expected: bool, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if network is online."""
    online = sel.network_online(s)
    return online == bool(expected)


@_register("network.offline")
def network_offline_predicate(s: Snapshot, expected: bool, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if network is offline."""
    offline = sel.network_offline(s)
    return offline == bool(expected)


# ===== Application state =====

@_register("app.first_run")
def app_first_run(s: Snapshot, expected: bool, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if this is first run."""
    return bool(s.first_run) == bool(expected)


@_register("app.mode")
def app_mode_predicate(s: Snapshot, expected: str | list, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if app mode matches expected value (string or list of modes)."""
    current_mode = s.app_mode.value.lower()
    if isinstance(expected, list):
        # Check if current mode is in the list
        expected_lower = [str(m).lower() for m in expected]
        return current_mode in expected_lower
    return current_mode == str(expected).lower()


@_register("app.restart_pending")
def app_restart_pending(s: Snapshot, expected: bool, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if restart is pending (without first_run check)."""
    return bool(s.restart_pending) == bool(expected)


@_register("app.first_run_restart_pending")
def app_first_run_restart_pending(s: Snapshot, expected: bool, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if first run AND restart is pending."""
    pending = sel.is_first_run_restart_pending(s)
    return bool(pending) == bool(expected)


# ===== Extra context (from extra dict) =====

@_register("update.in_progress")
def update_in_progress(_s: Snapshot, expected: bool, extra: Optional[Dict[str, Any]]) -> bool:
    """Check if update is in progress (from extra context or snapshot)."""
    if extra and "update_in_progress" in extra:
        return bool(extra["update_in_progress"]) == bool(expected)
    # Fallback to snapshot if available
    update_in_progress_val = getattr(_s, "update_in_progress", False)
    return bool(update_in_progress_val) == bool(expected)

