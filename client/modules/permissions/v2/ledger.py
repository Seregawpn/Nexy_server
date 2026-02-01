"""
Permission System V2 - Ledger Persistence

Stores permission wizard state to disk for recovery after restarts.
"""

from __future__ import annotations

import json
import logging
import os
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Optional

from .types import Phase, PermissionId, StepMode, StepState

logger = logging.getLogger(__name__)


@dataclass
class StepLedgerEntry:
    """Persistent state for a single permission step."""
    permission: PermissionId
    mode: StepMode
    state: StepState = StepState.UNKNOWN

    triggered_at: Optional[float] = None
    grace_started_at: Optional[float] = None
    polling_started_at: Optional[float] = None

    settings_opened_at: Optional[float] = None
    waiting_long_entered_at: Optional[float] = None

    last_probe_at: Optional[float] = None
    next_heavy_allowed_at: Optional[float] = None

    attempts: int = 0

    # Error counters
    consecutive_denied: int = 0
    consecutive_transient: int = 0
    consecutive_needs_restart: int = 0

    last_reason_code: Optional[str] = None
    last_reason: Optional[str] = None
    last_error_domain: Optional[str] = None
    last_error_code: Optional[str] = None

    needs_restart_marked: bool = False
    needs_restart_marked_at: Optional[float] = None


@dataclass
class LedgerRecord:
    """Complete wizard state stored to disk."""
    session_id: str
    phase: Phase
    created_at: float
    updated_at: float

    restart_count: int = 0
    needs_restart: bool = False
    restart_unavailable: bool = False  # True if restart was needed but handler unavailable

    current_step: Optional[PermissionId] = None

    steps: Dict[PermissionId, StepLedgerEntry] = field(default_factory=dict)

    app_bundle_id: Optional[str] = None
    app_path: Optional[str] = None
    gui_process_pid: Optional[int] = None


class LedgerStore:
    """
    JSON persistence with atomic replace.
    Stores ledger under Application Support.
    """
    def __init__(self, path: str):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> Optional[LedgerRecord]:
        """Load ledger from disk. Returns None if not found or corrupt."""
        if not self.path.exists():
            return None

        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, IOError) as e:
            logger.warning("Failed to load ledger from %s: %s", self.path, e)
            return None

        try:
            # Reconstruct enums
            steps: Dict[PermissionId, StepLedgerEntry] = {}
            for k, v in data.get("steps", {}).items():
                pid = PermissionId(k)
                steps[pid] = StepLedgerEntry(
                    permission=pid,
                    mode=StepMode(v["mode"]),
                    state=StepState(v["state"]),
                    triggered_at=v.get("triggered_at"),
                    grace_started_at=v.get("grace_started_at"),
                    polling_started_at=v.get("polling_started_at"),
                    settings_opened_at=v.get("settings_opened_at"),
                    waiting_long_entered_at=v.get("waiting_long_entered_at"),
                    last_probe_at=v.get("last_probe_at"),
                    next_heavy_allowed_at=v.get("next_heavy_allowed_at"),
                    attempts=v.get("attempts", 0),
                    consecutive_denied=v.get("consecutive_denied", 0),
                    consecutive_transient=v.get("consecutive_transient", 0),
                    consecutive_needs_restart=v.get("consecutive_needs_restart", 0),
                    last_reason_code=v.get("last_reason_code"),
                    last_reason=v.get("last_reason"),
                    last_error_domain=v.get("last_error_domain"),
                    last_error_code=v.get("last_error_code"),
                    needs_restart_marked=v.get("needs_restart_marked", False),
                    needs_restart_marked_at=v.get("needs_restart_marked_at"),
                )

            return LedgerRecord(
                session_id=data["session_id"],
                phase=Phase(data["phase"]),
                created_at=data["created_at"],
                updated_at=data["updated_at"],
                restart_count=data.get("restart_count", 0),
                needs_restart=data.get("needs_restart", False),
                restart_unavailable=data.get("restart_unavailable", False),
                current_step=PermissionId(data["current_step"]) if data.get("current_step") else None,
                steps=steps,
                app_bundle_id=data.get("app_bundle_id"),
                app_path=data.get("app_path"),
                gui_process_pid=data.get("gui_process_pid"),
            )
        except (KeyError, ValueError) as e:
            logger.warning("Failed to parse ledger from %s: %s", self.path, e)
            return None

    def save(self, ledger: LedgerRecord) -> None:
        """Save ledger atomically (write to tmp, then rename)."""
        ledger.updated_at = time.time()

        def step_to_dict(s: StepLedgerEntry) -> dict:
            return {
                "permission": s.permission.value,
                "mode": s.mode.value,
                "state": s.state.value,
                "triggered_at": s.triggered_at,
                "grace_started_at": s.grace_started_at,
                "polling_started_at": s.polling_started_at,
                "settings_opened_at": s.settings_opened_at,
                "waiting_long_entered_at": s.waiting_long_entered_at,
                "last_probe_at": s.last_probe_at,
                "next_heavy_allowed_at": s.next_heavy_allowed_at,
                "attempts": s.attempts,
                "consecutive_denied": s.consecutive_denied,
                "consecutive_transient": s.consecutive_transient,
                "consecutive_needs_restart": s.consecutive_needs_restart,
                "last_reason_code": s.last_reason_code,
                "last_reason": s.last_reason,
                "last_error_domain": s.last_error_domain,
                "last_error_code": s.last_error_code,
                "needs_restart_marked": s.needs_restart_marked,
                "needs_restart_marked_at": s.needs_restart_marked_at,
            }

        data = {
            "session_id": ledger.session_id,
            "phase": ledger.phase.value,
            "created_at": ledger.created_at,
            "updated_at": ledger.updated_at,
            "restart_count": ledger.restart_count,
            "needs_restart": ledger.needs_restart,
            "restart_unavailable": ledger.restart_unavailable,
            "current_step": ledger.current_step.value if ledger.current_step else None,
            "steps": {pid.value: step_to_dict(s) for pid, s in ledger.steps.items()},
            "app_bundle_id": ledger.app_bundle_id,
            "app_path": ledger.app_path,
            "gui_process_pid": ledger.gui_process_pid,
        }

        tmp = self.path.with_suffix(self.path.suffix + ".tmp")
        try:
            tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            os.replace(tmp, self.path)
            logger.debug("Saved ledger to %s", self.path)
        except IOError as e:
            logger.error("Failed to save ledger to %s: %s", self.path, e)
            raise

    def delete(self) -> None:
        """Delete the ledger file if it exists."""
        if self.path.exists():
            try:
                self.path.unlink()
                logger.debug("Deleted ledger at %s", self.path)
            except IOError as e:
                logger.warning("Failed to delete ledger at %s: %s", self.path, e)
