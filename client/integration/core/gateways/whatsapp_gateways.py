"""
Whatsapp Gateway
Decides actions based on WhatsApp state via DecisionEngine.
"""

from integration.core.selectors import Snapshot

from .base import create_ctx_from_snapshot
from .engine_loader import get_engine
from .types import Decision


def decide_whatsapp_action(snapshot: Snapshot) -> Decision:
    """
    Decide what action to take based on WhatsApp status.
    
    Uses centralized DecisionEngine and rules from interaction_matrix.yaml.
    Canonical logging is handled by the engine.
    """
    engine = get_engine("decide_whatsapp_action")
    
    # Use standard context creation which now includes whatsapp status
    ctx = create_ctx_from_snapshot(snapshot)
    
    return engine.decide(
        snapshot,
        source="whatsapp",
        ctx=ctx
    )
