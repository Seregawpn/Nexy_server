"""
Permission System V2 - Configuration Loader

Loads V2 configuration from unified_config.yaml and creates StepConfig instances.
"""

from __future__ import annotations

import logging
from typing import Any

from .types import (
    PermissionCriticality,
    PermissionId,
    RestartConfig,
    StepConfig,
    StepMode,
    StepTiming,
)

logger = logging.getLogger(__name__)


def load_v2_config(config: dict[str, Any]) -> dict[str, Any] | None:
    """
    Load V2 permission config from unified config.
    
    Args:
        config: Full unified config dict
        
    Returns:
        Dict with: order, step_configs, hard_permissions, restart_config
        or None if V2 is disabled
    """
    integrations = config.get("integrations", {})
    v2_config = integrations.get("permissions_v2", {})
    
    if not v2_config.get("enabled", False):
        logger.info("[V2_CONFIG] permissions_v2 is disabled")
        return None
    
    # Parse order
    order_strs = v2_config.get("order", [])
    order = []
    for s in order_strs:
        try:
            order.append(PermissionId(s))
        except ValueError:
            logger.warning("[V2_CONFIG] Unknown permission: %s", s)
    
    if not order:
        logger.error("[V2_CONFIG] No valid permissions in order")
        return None
    
    # Parse steps
    steps_raw = v2_config.get("steps", {})
    default_step_timeout_s = v2_config.get("default_step_timeout_s")
    step_configs: dict[PermissionId, StepConfig] = {}
    hard_permissions: list[PermissionId] = []
    
    for perm in order:
        step_raw = steps_raw.get(perm.value, {})
        
        # Mode
        mode_str = step_raw.get("mode", "auto_dialog")
        try:
            mode = StepMode(mode_str)
        except ValueError:
            mode = StepMode.AUTO_DIALOG
        
        # Criticality
        crit_str = step_raw.get("criticality", "feature")
        try:
            criticality = PermissionCriticality(crit_str)
        except ValueError:
            criticality = PermissionCriticality.FEATURE
        
        if criticality == PermissionCriticality.HARD:
            hard_permissions.append(perm)
        
        # Timing
        raw_step_timeout_s = step_raw.get("step_timeout_s", default_step_timeout_s)
        step_timeout_s = float(raw_step_timeout_s) if raw_step_timeout_s is not None else None
        timing = StepTiming(
            grace_s=float(step_raw.get("grace_s", 2.0)),
            poll_s=float(step_raw.get("poll_s", 2.0)),
            heavy_cooldown_s=float(step_raw.get("heavy_cooldown_s", 10.0)),
            waiting_long_after_s=float(step_raw.get("waiting_long_after_s", 300.0)),
            waiting_long_poll_s=float(step_raw.get("waiting_long_poll_s", 15.0)),
            post_restart_verify_window_s=float(step_raw.get("post_restart_verify_window_s", 20.0)),
            post_restart_verify_tick_s=float(step_raw.get("post_restart_verify_tick_s", 2.0)),
            step_timeout_s=step_timeout_s,
        )
        
        step_configs[perm] = StepConfig(
            permission=perm,
            mode=mode,
            timing=timing,
            supports_needs_restart=bool(step_raw.get("supports_needs_restart", False)),
            settings_target=step_raw.get("settings_target"),
            criticality=criticality,
        )
    
    # Restart config
    restart_raw = v2_config.get("restart", {})
    restart_config = RestartConfig(
        delay_sec=float(restart_raw.get("delay_sec", 1.0)),
        settings_safety_window_sec=float(restart_raw.get("settings_safety_window_sec", 30.0)),
        require_all_hard_pass=bool(restart_raw.get("require_all_hard_pass", True)),
        require_needs_restart=bool(restart_raw.get("require_needs_restart", True)),
    )

    inter_step_pause_s = float(v2_config.get("inter_step_pause_s", 0.0))
    advance_on_timeout = bool(v2_config.get("advance_on_timeout", False))
    
    logger.info(
        "[V2_CONFIG] Loaded: %d permissions, %d hard, order=%s",
        len(order),
        len(hard_permissions),
        [p.value for p in order]
    )
    
    return {
        "order": order,
        "step_configs": step_configs,
        "hard_permissions": hard_permissions,
        "restart_config": restart_config,
        "inter_step_pause_s": inter_step_pause_s,
        "advance_on_timeout": advance_on_timeout,
    }
