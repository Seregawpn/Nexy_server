"""
Helper for loading and caching DecisionEngine instances.
"""
from __future__ import annotations

from typing import Dict, Optional

from .decision_engine import DecisionEngine
from .rule_loader import load_rules_for_gateway


# Cache engines per gateway
_ENGINES: Dict[str, DecisionEngine] = {}


def get_engine(gateway_name: str) -> DecisionEngine:
    """
    Get or create DecisionEngine for a gateway (cached).
    
    Args:
        gateway_name: Name of the gateway (e.g., "decide_start_listening")
    
    Returns:
        Cached DecisionEngine instance
    """
    if gateway_name not in _ENGINES:
        rules = load_rules_for_gateway(gateway_name)
        _ENGINES[gateway_name] = DecisionEngine(gateway_name, rules)
    return _ENGINES[gateway_name]


