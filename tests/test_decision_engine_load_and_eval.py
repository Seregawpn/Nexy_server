"""
Tests for DecisionEngine rule loading and evaluation.

Tests that rules from interaction_matrix.yaml are correctly loaded and applied.
"""
from __future__ import annotations

import pytest

from integration.core.gateways.decision_engine import DecisionEngine, Rule, Priority
from integration.core.gateways.rule_loader import load_rules_for_gateway
from integration.core.gateways.base import DecisionCtx, create_ctx_from_snapshot
from integration.core.gateways.types import Decision
from integration.core.selectors import (
    Snapshot,
    PermissionStatus,
    DeviceStatus,
    NetworkStatus,
    AppMode,
)


def mk_snapshot(
    granted: bool = True,
    first_run: bool = True,
    online: bool = True,
    idle: bool = True,
    app_mode: AppMode = AppMode.SLEEPING,
    restart_pending: bool = False,
    update_in_progress: bool = False,
) -> Snapshot:
    """Create a test snapshot with specified values."""
    return Snapshot(
        perm_mic=PermissionStatus.GRANTED if granted else PermissionStatus.DENIED,
        perm_screen=PermissionStatus.GRANTED if granted else PermissionStatus.DENIED,
        perm_accessibility=PermissionStatus.GRANTED if granted else PermissionStatus.DENIED,
        device_input=DeviceStatus.DEFAULT_OK if idle else DeviceStatus.BUSY,
        network=NetworkStatus.ONLINE if online else NetworkStatus.OFFLINE,
        first_run=first_run,
        app_mode=app_mode,
        restart_pending=restart_pending,
        update_in_progress=update_in_progress,
    )


@pytest.mark.skip(reason="Requires interaction_matrix.yaml with test rules")
def test_permission_restart_rules_apply_graceful_on_update():
    """Test that permission_restart rules apply graceful on update_in_progress."""
    eng = DecisionEngine("decide_permission_restart_safety", load_rules_for_gateway("decide_permission_restart_safety"))
    s = mk_snapshot(granted=True, update_in_progress=True)
    ctx = create_ctx_from_snapshot(s)
    d = eng.decide(s, source="permission_restart", ctx=ctx, extra={"update_in_progress": True})
    # Should return RETRY or ABORT depending on rule priority
    assert d in (Decision.RETRY, Decision.ABORT)


@pytest.mark.skip(reason="Requires interaction_matrix.yaml with test rules")
def test_permission_restart_rules_abort_when_missing_perms():
    """Test that permission_restart rules abort when permissions are missing."""
    eng = DecisionEngine("decide_permission_restart_safety", load_rules_for_gateway("decide_permission_restart_safety"))
    s = mk_snapshot(granted=False)
    ctx = create_ctx_from_snapshot(s)
    d = eng.decide(s, source="permission_restart", ctx=ctx, extra={"update_in_progress": False})
    # Should return ABORT if missing permissions
    assert d == Decision.ABORT


@pytest.mark.skip(reason="Requires interaction_matrix.yaml with test rules")
def test_start_listening_starts_when_ready():
    """Test that start_listening returns START when all conditions are met."""
    eng = DecisionEngine("decide_start_listening", load_rules_for_gateway("decide_start_listening"))
    s = mk_snapshot(granted=True, online=True, idle=True, first_run=False)
    ctx = create_ctx_from_snapshot(s)
    d = eng.decide(s, source="audio", ctx=ctx)
    # Should return START when all conditions are met
    assert d == Decision.START


def test_decision_engine_priority_order():
    """Test that rules are applied in priority order (hard_stop → graceful → preference)."""
    rules = [
        Rule(when={"app.first_run": True}, decision=Decision.ABORT, priority=Priority.HARD_STOP, gateway="test"),
        Rule(when={"device.busy": True}, decision=Decision.RETRY, priority=Priority.GRACEFUL, gateway="test"),
        Rule(when={"network.online": True}, decision=Decision.START, priority=Priority.PREFERENCE, gateway="test"),
    ]
    
    eng = DecisionEngine("test", rules)
    s = mk_snapshot(first_run=True, idle=False, online=True)
    ctx = create_ctx_from_snapshot(s)
    
    # First rule (hard_stop) should match
    d = eng.decide(s, source="test", ctx=ctx)
    assert d == Decision.ABORT


def test_decision_engine_no_match_defaults_to_start():
    """Test that engine returns START when no rules match."""
    rules = [
        Rule(when={"app.first_run": True}, decision=Decision.ABORT, priority=Priority.HARD_STOP, gateway="test"),
    ]
    
    eng = DecisionEngine("test", rules)
    s = mk_snapshot(first_run=False)  # No rules match
    ctx = create_ctx_from_snapshot(s)
    
    d = eng.decide(s, source="test", ctx=ctx)
    assert d == Decision.START
