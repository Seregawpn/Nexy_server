from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from integration.core.gateways import Decision, decide_continue_integration_startup
from integration.core.selectors import create_snapshot_from_state

try:
    from mode_management import AppMode  # type: ignore[reportMissingImports]
except Exception:  # pragma: no cover - fallback for repo layout
    from modules.mode_management import AppMode  # type: ignore[reportMissingImports]


class _FakeStateManager:
    def __init__(self) -> None:
        self._data: dict[str, object] = {"first_run_required": True}

    def get_current_mode(self) -> AppMode:
        return AppMode.SLEEPING

    def get_state_data(self, key: str, default: object = None) -> object:
        return self._data.get(key, default)


def test_snapshot_has_no_restart_pending_legacy_axis() -> None:
    snapshot = create_snapshot_from_state(_FakeStateManager())
    assert not hasattr(snapshot, "restart_pending")


def test_gateway_abort_when_first_run_is_active() -> None:
    snapshot = create_snapshot_from_state(_FakeStateManager())
    assert decide_continue_integration_startup(snapshot) == Decision.ABORT
