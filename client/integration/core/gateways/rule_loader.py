"""
Load rules from interaction_matrix.yaml for specific gateways.
"""
from __future__ import annotations

from pathlib import Path as PathType
import sys
from typing import Any

from .decision_engine import Priority, Rule
from .types import Decision

# Import existing loader - add config to path for import
config_path = PathType(__file__).parent.parent.parent.parent / "config"
if str(config_path) not in sys.path:
    sys.path.insert(0, str(config_path))

try:
    from interaction_matrix_loader import load_interaction_matrix  # type: ignore
except ImportError:
    # Fallback: direct import if config is in PYTHONPATH
    import yaml
    def load_interaction_matrix(dev_only: bool = False) -> dict[str, Any]:
        """Fallback loader if interaction_matrix_loader not available."""
        matrix_path = PathType(__file__).parent.parent.parent.parent / "config" / "interaction_matrix.yaml"
        if not matrix_path.exists():
            return {}
        try:
            with open(matrix_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
        except Exception:
            return {}


def _to_priority(raw: str) -> Priority:
    """Convert string priority to Priority enum."""
    raw = (raw or "").strip().lower()
    if raw in ("hard_stop", "hardstop", "hard-stop"):
        return Priority.HARD_STOP
    if raw in ("graceful",):
        return Priority.GRACEFUL
    return Priority.PREFERENCE


def _to_decision(raw: str) -> Decision:
    """Convert string decision to Decision enum."""
    raw = (raw or "").strip().lower()
    decision_map = {
        "start": Decision.START,
        "abort": Decision.ABORT,
        "retry": Decision.RETRY,
        "degrade": Decision.DEGRADE,
        # Map common YAML decision strings
        "abort_listen": Decision.ABORT,
        "abort_processing": Decision.ABORT,
        "abort_permission_restart": Decision.ABORT,
        "abort_update_launch": Decision.ABORT,
        "abort_integration_startup": Decision.ABORT,
        "retry_backoff": Decision.RETRY,
        "delay_restart": Decision.RETRY,
        "degrade_offline": Decision.DEGRADE,
        "skip_restart": Decision.ABORT,
        "notify_user": Decision.NOTIFY_USER,
    }
    return decision_map.get(raw, Decision.DEGRADE)


def load_rules_for_gateway(gateway_name: str) -> list[Rule]:
    """
    Load rules for a specific gateway from interaction_matrix.yaml.
    
    Args:
        gateway_name: Name of the gateway (e.g., "decide_start_listening", "decide_permission_restart_safety")
    
    Returns:
        List of Rule objects for the gateway
    """
    matrix = load_interaction_matrix(dev_only=False)  # Load in all environments
    raw_rules = matrix.get("rules", [])
    
    out: list[Rule] = []
    for rr in raw_rules:
        # Match gateway name (exact or partial match)
        rule_gateway = rr.get("gateway", "")
        if rule_gateway != gateway_name:
            # Try partial match for gateway names like "decide_start_listening"
            if gateway_name not in rule_gateway and rule_gateway not in gateway_name:
                continue
        
        out.append(Rule(
            when=rr.get("when", {}) or {},
            decision=_to_decision(rr.get("decision", "degrade")),
            priority=_to_priority(rr.get("priority", "preference")),
            gateway=gateway_name,
        ))
    
    return out
