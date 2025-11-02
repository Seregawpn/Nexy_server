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
        logger.info(
            "decision=abort reason=first_run_in_progress "
            f"ctx={{firstRun={s.first_run},mic={s.perm_mic.value},device={s.device_input.value}}} "
            "source=listening_gateway"
        )
        return Decision.ABORT

    if not mic_ready(s):
        logger.debug(
            "decision=abort "
            f"ctx={{mic={s.perm_mic.value},device={s.device_input.value},network={s.network.value}}} "
            "source=listening_gateway"
        )
        return Decision.ABORT

    if device_busy(s):
        logger.debug(
            "decision=retry "
            f"ctx={{mic={s.perm_mic.value},device={s.device_input.value},network={s.network.value}}} "
            "source=listening_gateway"
        )
        return Decision.RETRY

    if network_offline(s):
        logger.debug(
            "decision=degrade "
            f"ctx={{mic={s.perm_mic.value},device={s.device_input.value},network={s.network.value}}} "
            "source=listening_gateway"
        )
        return Decision.DEGRADE

    if can_start_listening(s):
        logger.debug(
            "decision=start "
            f"ctx={{mic={s.perm_mic.value},device={s.device_input.value},network={s.network.value},appMode={s.app_mode.value}}} "
            "source=listening_gateway"
        )
        return Decision.START

    logger.debug(
        "decision=abort "
        f"ctx={{mic={s.perm_mic.value},device={s.device_input.value},network={s.network.value},appMode={s.app_mode.value}}} "
        "source=listening_gateway"
    )
    return Decision.ABORT


def decide_process_audio(s: Snapshot) -> Decision:
    """Decide whether to process audio based on current state."""
    if not mic_ready(s):
        logger.debug(
            "decision=abort "
            f"ctx={{mic={s.perm_mic.value},network={s.network.value},appMode={s.app_mode.value}}} "
            "source=processing_gateway"
        )
        return Decision.ABORT

    if should_degrade_offline(s):
        logger.debug(
            "decision=degrade "
            f"ctx={{mic={s.perm_mic.value},network={s.network.value},appMode={s.app_mode.value}}} "
            "source=processing_gateway"
        )
        return Decision.DEGRADE

    if can_process_audio(s):
        logger.debug(
            "decision=start "
            f"ctx={{mic={s.perm_mic.value},network={s.network.value},appMode={s.app_mode.value}}} "
            "source=processing_gateway"
        )
        return Decision.START

    logger.debug(
        "decision=abort "
        f"ctx={{mic={s.perm_mic.value},network={s.network.value},appMode={s.app_mode.value}}} "
        "source=processing_gateway"
    )
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
        logger.info(
            "decision=abort reason=first_run_restart_pending "
            f"ctx={{firstRun={s.first_run},restart_pending={s.restart_pending},"
            f"appMode={s.app_mode.value}}} source=coordinator_gateway duration_ms=0"
        )
        return Decision.ABORT

    if is_restart_pending(s):
        logger.warning(
            "decision=abort reason=restart_pending_without_first_run "
            f"ctx={{firstRun={s.first_run},restart_pending={s.restart_pending},"
            f"appMode={s.app_mode.value}}} source=coordinator_gateway duration_ms=0"
        )
        return Decision.ABORT

    logger.debug(
        "decision=start "
        f"ctx={{firstRun={s.first_run},restart_pending={s.restart_pending},appMode={s.app_mode.value}}} "
        "source=coordinator_gateway"
    )
    return Decision.START

