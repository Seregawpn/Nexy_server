from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class ActiveContextState:
    """Request-scoped experimental state for v2 task lifecycle."""

    session_id: str
    domain: Optional[str] = None
    goal: Optional[str] = None
    intent: Optional[str] = None
    filled_slots: Dict[str, Any] = field(default_factory=dict)
    missing_slots: list[str] = field(default_factory=list)
    last_question: Optional[str] = None
    status: str = "idle"
    awaiting_reply: bool = False
    last_user_text: str = ""
    turn_version: int = 0


class ActiveContextStore:
    """In-memory experimental store. Single owner stays in the v2 runtime."""

    def __init__(self) -> None:
        self._by_session: dict[str, ActiveContextState] = {}

    def get_or_create(self, session_id: str) -> ActiveContextState:
        state = self._by_session.get(session_id)
        if state is None:
            state = ActiveContextState(session_id=session_id)
            self._by_session[session_id] = state
        return state

    def clear(self, session_id: str) -> None:
        self._by_session.pop(session_id, None)
