"""
Common decision gateways used across integrations.
"""

from __future__ import annotations

import logging
from enum import Enum

from integration.core.selectors import (
    Snapshot,
    can_process_audio,
    can_start_listening,
    device_busy,
    is_first_run_restart_pending,
    is_restart_pending,
    mic_ready,
    network_offline,
    network_online,
    should_degrade_offline,
)

logger = logging.getLogger(__name__)


class Decision(Enum):
    """Decision outcomes for state transitions."""

    START = "start"
    RETRY = "retry"
    ABORT = "abort"
    DEGRADE = "degrade"


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
    """
    ctx = (
        f"ctx={{mic={s.perm_mic.value},screen={s.perm_screen.value},device={s.device_input.value},"
        f"network={s.network.value},firstRun={s.first_run},appMode={s.app_mode.value}}}"
    )
    reason_part = f" reason={reason}" if reason else ""
    duration_part = f" duration_ms={int(duration_ms)}" if duration_ms is not None else ""
    msg = f"decision={(decision.value if isinstance(decision, Decision) else decision)}{reason_part} {ctx} source={source}{duration_part}"

    log_fn = getattr(logger, level, logger.info)
    log_fn(msg)


def decide_start_listening(s: Snapshot) -> Decision:
    """
    Decide whether to start listening based on current state.

    Rules:
    - hard_stop: if first_run is in progress, abort (блокировка активации)
    - hard_stop: if mic permission is denied, abort
    - graceful: if device is busy, retry
    - graceful: if network is offline, degrade (offline mode)
    - start: if all conditions are met
    """
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
    """Decide whether to process audio based on current state."""
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
    """
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

