"""
Rule-based decision engine for gateways.

Loads rules from interaction_matrix.yaml and applies them in priority order:
hard_stop → graceful → preference.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
import logging
import time
from typing import Any, Callable, Iterable

from integration.core.selectors import Snapshot

from . import predicates as pred
from .base import DecisionCtx, log_decision
from .types import Decision

logger = logging.getLogger(__name__)


class Priority(StrEnum):
    """Priority levels for rules."""

    HARD_STOP = "hard_stop"
    GRACEFUL = "graceful"
    PREFERENCE = "preference"


@dataclass(frozen=True)
class Rule:
    """A decision rule with conditions and outcome."""

    when: dict[str, Any]  # Conditions keyed by predicate names
    decision: Decision  # Outcome decision
    priority: Priority  # Rule priority
    gateway: str  # Gateway name (for filtering)


class DecisionEngine:
    """
    Rule-based decision engine.

    Rules are pre-filtered for a specific gateway and applied in priority order:
    hard_stop → graceful → preference.

    Returns only Decision (for backward compatibility).
    """

    def __init__(self, gateway_name: str, rules: Iterable[Rule]):
        self.gateway_name = gateway_name
        # Order rules by priority: hard_stop → graceful → preference
        prio_order = {Priority.HARD_STOP: 0, Priority.GRACEFUL: 1, Priority.PREFERENCE: 2}
        self.rules: list[Rule] = sorted(list(rules), key=lambda r: prio_order[r.priority])

    def _match(self, s: Snapshot, when: dict[str, Any], extra: dict[str, Any] | None) -> bool:
        """
        Check if snapshot matches rule conditions.

        Each entry in 'when' is key=predicate_name, value=expected_value.
        Predicate names are looked up in pred.REGISTRY.
        """
        for name, expected in when.items():
            fn: Callable[[Snapshot, Any, dict[str, Any] | None], bool] | None = pred.REGISTRY.get(
                name
            )
            if fn is None:
                # Unknown condition is treated as not matched (safe default)
                return False
            if not fn(s, expected, extra):
                return False
        return True

    def decide(
        self,
        s: Snapshot,
        *,
        source: str,
        ctx: DecisionCtx,
        extra: dict[str, Any] | None = None,
    ) -> Decision:
        """
        Make decision based on rules and snapshot.

        Args:
            s: System state snapshot
            source: Source domain (e.g., "audio", "permission_restart")
            ctx: Decision context for logging
            extra: Additional context (e.g., update_in_progress flag)

        Returns:
            Decision outcome
        """
        started = time.time()

        # Check rules in priority order; first match wins
        for rule in self.rules:
            if self._match(s, rule.when, extra):
                log_decision(
                    self.gateway_name,
                    rule.decision,
                    ctx,
                    source=source,
                    started_at=started,
                    reason=f"rule_{rule.priority.value}",
                )
                return rule.decision

        # If no rule matched, log warning and default to START (safe path)
        logger.warning(
            f"decision_engine_rule_miss gateway={self.gateway_name} "
            f"ctx={ctx.to_log_string()} source={source} "
            f"available_rules={len(self.rules)} "
            f"fallback_to=START"
        )
        default_decision = Decision.START
        log_decision(
            self.gateway_name,
            default_decision,
            ctx,
            source=source,
            started_at=started,
            reason="no_rule_matched",
        )
        return default_decision
