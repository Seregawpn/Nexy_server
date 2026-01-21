"""
Test helpers for asserting decision logs in canonical format.

See .cursorrules section 8.x for canonical format:
decision=<start|abort|retry|degrade> ctx={mic=...,screen=...,device=...,network=...,firstRun=...,appMode=...} source=<domain> duration_ms=<int>
"""
import re
import logging
from typing import List, Optional
from unittest.mock import MagicMock

from integration.core.selectors import Snapshot


def assert_decision_logged(
    caplog,
    decision: str,
    source: str,
    ctx_keys: Optional[List[str]] = None,
    snapshot: Optional[Snapshot] = None,
) -> None:
    """
    Assert that a decision log in canonical format was written.
    
    Args:
        caplog: pytest caplog fixture
        decision: Expected decision value (start|abort|retry|degrade)
        source: Expected source domain (e.g., "listening_gateway")
        ctx_keys: Expected context keys (e.g., ["mic", "screen", "device"])
        snapshot: Optional snapshot to verify context values
    
    Raises:
        AssertionError: If decision log not found or format invalid
    """
    # Canonical format pattern (reason is optional and appears between decision and ctx)
    pattern = rf"decision={decision}(\s+reason=\w+)?\s+ctx=\{{[^}}]+\}}\s+source={source}(\s+duration_ms=\d+)?"
    
    logs = caplog.text
    match = re.search(pattern, logs)
    
    if not match:
        raise AssertionError(
            f"Decision log not found in canonical format.\n"
            f"Expected: decision={decision} ctx={{...}} source={source}\n"
            f"Logs: {logs[:500]}"
        )
    
    # Extract context from matched log
    ctx_match = re.search(r"ctx=\{([^}]+)\}", match.group(0))
    if not ctx_match:
        raise AssertionError("Context not found in decision log")
    
    ctx_str = ctx_match.group(1)
    
    # Verify context keys if provided
    if ctx_keys:
        for key in ctx_keys:
            if f"{key}=" not in ctx_str:
                raise AssertionError(
                    f"Context key '{key}' not found in decision log.\n"
                    f"Context: {ctx_str}\n"
                    f"Expected keys: {ctx_keys}"
                )
    
    # Verify snapshot values if provided
    if snapshot:
        if "mic=" in ctx_str:
            expected_mic = snapshot.perm_mic.value
            if f"mic={expected_mic}" not in ctx_str:
                raise AssertionError(
                    f"Snapshot mic value mismatch.\n"
                    f"Expected: mic={expected_mic}\n"
                    f"Found in log: {ctx_str}"
                )


def extract_decision_from_logs(caplog) -> List[dict]:
    """
    Extract all decision logs from caplog in structured format.
    
    Returns:
        List of dicts with keys: decision, ctx, source, duration_ms
    """
    pattern = r"decision=(\w+)\s+ctx=\{([^}]+)\}\s+source=(\w+)(\s+duration_ms=(\d+))?"
    
    decisions = []
    for match in re.finditer(pattern, caplog.text):
        decisions.append({
            "decision": match.group(1),
            "ctx": match.group(2),
            "source": match.group(3),
            "duration_ms": int(match.group(5)) if match.group(5) else None,
        })
    
    return decisions

