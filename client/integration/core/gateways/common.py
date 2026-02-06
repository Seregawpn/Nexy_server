"""
Common decision gateways used across integrations.
"""

from __future__ import annotations

import logging

from integration.core.selectors import (
    Snapshot,
    can_process_audio,
    can_start_listening,
    device_busy,
    is_first_run_restart_pending,
    is_restart_pending,
    mic_ready,
    network_offline,
    should_degrade_offline,
)

# DecisionEngine integration
from .base import create_ctx_from_snapshot
from .engine_loader import get_engine
from .types import Decision

logger = logging.getLogger(__name__)


def _log_decision(
    *,
    level: str,
    decision: "Decision | str",
    s: Snapshot,
    source: str,
    reason: str | None = None,
    duration_ms: int | None = None,
) -> None:
    """Unified decision log formatter.

    Always logs ctx={mic, screen, device, network, firstRun, appMode} with optional duration_ms.
    Also includes new axes if present in Snapshot: restart_pending, update_in_progress.
    """
    # Include all axes in context: mic, screen, device, network, firstRun, appMode
    # Also include new axes if present in Snapshot: restart_pending, update_in_progress
    restart_pending_val = getattr(s, 'restart_pending', None)
    update_in_progress_val = getattr(s, 'update_in_progress', None)
    
    ctx_parts = [
        f"mic={s.perm_mic.value}",
        f"screen={s.perm_screen.value}",
        f"device={s.device_input.value}",
        f"network={s.network.value}",
        f"firstRun={s.first_run}",
        f"appMode={s.app_mode.value}",
    ]
    
    if restart_pending_val is not None:
        ctx_parts.append(f"restart_pending={restart_pending_val}")
    if update_in_progress_val is not None:
        ctx_parts.append(f"update_in_progress={update_in_progress_val}")
    
    ctx = f"ctx={{{','.join(ctx_parts)}}}"
    reason_part = f" reason={reason}" if reason else ""
    duration_part = f" duration_ms={int(duration_ms)}" if duration_ms is not None else ""
    msg = f"decision={(decision.value if isinstance(decision, Decision) else decision)}{reason_part} {ctx} source={source}{duration_part}"

    log_fn = getattr(logger, level, logger.info)
    log_fn(msg)


def decide_start_listening(s: Snapshot) -> Decision:
    """
    Decide whether to start listening based on current state.

    Uses DecisionEngine with rules from interaction_matrix.yaml.
    Rules are applied in priority order: hard_stop → graceful → preference.
    """
    try:
        engine = get_engine("decide_start_listening")
        ctx = create_ctx_from_snapshot(s)
        return engine.decide(s, source="listening_gateway", ctx=ctx, extra=None)
    except Exception as exc:
        # Fallback to legacy logic if engine fails
        logger.warning(
            f"decision_engine_fallback gateway=decide_start_listening "
            f"ctx={create_ctx_from_snapshot(s).to_log_string()} "
            f"error={exc} fallback_to=legacy"
        )
        if s.first_run:
            _log_decision(level="info", decision=Decision.ABORT, s=s, source="listening_gateway", reason="first_run_in_progress")
            return Decision.ABORT
        if not mic_ready(s):
            _log_decision(level="debug", decision=Decision.ABORT, s=s, source="listening_gateway")
            return Decision.ABORT
        if device_busy(s):
            _log_decision(level="debug", decision=Decision.RETRY, s=s, source="listening_gateway")
            return Decision.RETRY
        if network_offline(s):
            _log_decision(level="debug", decision=Decision.DEGRADE, s=s, source="listening_gateway")
            return Decision.DEGRADE
        if can_start_listening(s):
            _log_decision(level="debug", decision=Decision.START, s=s, source="listening_gateway")
            return Decision.START
        _log_decision(level="debug", decision=Decision.ABORT, s=s, source="listening_gateway")
        return Decision.ABORT


def decide_process_audio(s: Snapshot) -> Decision:
    """
    Decide whether to process audio based on current state.

    Uses DecisionEngine with rules from interaction_matrix.yaml.
    """
    try:
        engine = get_engine("decide_process_audio")
        ctx = create_ctx_from_snapshot(s)
        return engine.decide(s, source="processing_gateway", ctx=ctx, extra=None)
    except Exception as exc:
        # Fallback to legacy logic if engine fails
        logger.warning(
            f"decision_engine_fallback gateway=decide_process_audio "
            f"ctx={create_ctx_from_snapshot(s).to_log_string()} "
            f"error={exc} fallback_to=legacy"
        )
        if not mic_ready(s):
            _log_decision(level="debug", decision=Decision.ABORT, s=s, source="processing_gateway")
            return Decision.ABORT
        if should_degrade_offline(s):
            _log_decision(level="debug", decision=Decision.DEGRADE, s=s, source="processing_gateway")
            return Decision.DEGRADE
        if can_process_audio(s):
            _log_decision(level="debug", decision=Decision.START, s=s, source="processing_gateway")
            return Decision.START
        _log_decision(level="debug", decision=Decision.ABORT, s=s, source="processing_gateway")
        return Decision.ABORT


def decide_route_manager_reconcile(s: Snapshot) -> Decision:
    """
    Decide whether to reconcile audio route manager based on current state.

    Uses DecisionEngine with rules from interaction_matrix.yaml.
    """
    try:
        engine = get_engine("decide_route_manager_reconcile")
        ctx = create_ctx_from_snapshot(s)
        return engine.decide(s, source="route_manager_gateway", ctx=ctx, extra=None)
    except Exception as exc:
        logger.warning(
            f"decision_engine_fallback gateway=decide_route_manager_reconcile "
            f"ctx={create_ctx_from_snapshot(s).to_log_string()} "
            f"error={exc} fallback_to=legacy"
        )
        if s.first_run or s.restart_pending or s.update_in_progress:
            _log_decision(level="info", decision=Decision.ABORT, s=s, source="route_manager_gateway")
            return Decision.ABORT
        if device_busy(s):
            _log_decision(level="debug", decision=Decision.RETRY, s=s, source="route_manager_gateway")
            return Decision.RETRY
        if network_offline(s):
            _log_decision(level="debug", decision=Decision.DEGRADE, s=s, source="route_manager_gateway")
            return Decision.DEGRADE
        _log_decision(level="debug", decision=Decision.START, s=s, source="route_manager_gateway")
        return Decision.START


def decide_update_launch(s: Snapshot) -> Decision:
    """
    Decide whether it's safe to launch an update based on current state.

    Uses DecisionEngine with rules from interaction_matrix.yaml.
    """
    try:
        engine = get_engine("decide_update_launch")
        ctx = create_ctx_from_snapshot(s)
        extra = {"update_in_progress": s.update_in_progress}
        return engine.decide(s, source="updater_gateway", ctx=ctx, extra=extra)
    except Exception as exc:
        logger.warning(
            f"decision_engine_fallback gateway=decide_update_launch "
            f"ctx={create_ctx_from_snapshot(s).to_log_string()} "
            f"error={exc} fallback_to=legacy"
        )
        if s.update_in_progress and s.app_mode.value.lower() in ("listening", "processing"):
            _log_decision(level="info", decision=Decision.ABORT, s=s, source="updater_gateway")
            return Decision.ABORT
        _log_decision(level="debug", decision=Decision.START, s=s, source="updater_gateway")
        return Decision.START


def decide_with_backoff(s: Snapshot, retry_count: int, max_retries: int = 3) -> Decision:
    """Decide with exponential backoff for retry scenarios."""
    if retry_count >= max_retries:
        logger.debug(
            f"decision=abort ctx={{retry_count={retry_count},max_retries={max_retries}}} source=backoff_gateway"
        )
        return Decision.ABORT

    if device_busy(s) and retry_count < max_retries:
        logger.debug(
            f"decision=retry ctx={{retry_count={retry_count},device={s.device_input.value}}} source=backoff_gateway"
        )
        return Decision.RETRY

    return decide_start_listening(s)


def decide_continue_integration_startup(s: Snapshot) -> Decision:
    """
    Decide whether to continue launching integrations after first_run_permissions.

    Uses DecisionEngine with rules from interaction_matrix.yaml.
    """
    try:
        engine = get_engine("decide_continue_integration_startup")
        ctx = create_ctx_from_snapshot(s)
        return engine.decide(s, source="coordinator_gateway", ctx=ctx, extra=None)
    except Exception as exc:
        # Fallback to legacy logic if engine fails
        logger.warning(
            f"decision_engine_fallback gateway=decide_continue_integration_startup "
            f"ctx={create_ctx_from_snapshot(s).to_log_string()} "
            f"error={exc} fallback_to=legacy"
        )
        if is_first_run_restart_pending(s):
            _log_decision(
                level="info",
                decision=Decision.ABORT,
                s=s,
                source="coordinator_gateway",
                reason="first_run_restart_pending",
                duration_ms=0,
            )
            return Decision.ABORT
        if is_restart_pending(s):
            _log_decision(
                level="warning",
                decision=Decision.ABORT,
                s=s,
                source="coordinator_gateway",
                reason="restart_pending_without_first_run",
                duration_ms=0,
            )
            return Decision.ABORT
        _log_decision(level="debug", decision=Decision.START, s=s, source="coordinator_gateway")
        return Decision.START
