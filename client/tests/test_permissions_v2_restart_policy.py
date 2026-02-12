from __future__ import annotations

import os
import sys
from unittest.mock import AsyncMock

import pytest

sys.path.insert(0, os.getcwd())

from modules.permissions.v2.ledger import LedgerRecord, StepLedgerEntry
from modules.permissions.v2.orchestrator import PermissionOrchestrator, should_restart
from modules.permissions.v2.types import PermissionId, Phase, RestartConfig, StepMode, StepState


def _ledger_with_hard_step(
    *,
    state: StepState,
    needs_restart_marked: bool,
    restart_count: int = 0,
) -> LedgerRecord:
    entry = StepLedgerEntry(
        permission=PermissionId.INPUT_MONITORING,
        mode=StepMode.AUTO_DIALOG,
        state=state,
        needs_restart_marked=needs_restart_marked,
    )
    return LedgerRecord(
        session_id="sid",
        phase=Phase.FIRST_RUN,
        created_at=0.0,
        updated_at=0.0,
        restart_count=restart_count,
        steps={PermissionId.INPUT_MONITORING: entry},
    )


def test_should_restart_requires_needs_restart_mark_when_enabled() -> None:
    ledger = _ledger_with_hard_step(
        state=StepState.PASS_,
        needs_restart_marked=False,
    )
    cfg = RestartConfig(
        delay_sec=1.0,
        settings_safety_window_sec=30.0,
        require_all_hard_pass=True,
        require_needs_restart=True,
    )

    assert should_restart(ledger, [PermissionId.INPUT_MONITORING], cfg) is False


def test_should_restart_true_when_needs_restart_mark_present() -> None:
    ledger = _ledger_with_hard_step(
        state=StepState.PASS_,
        needs_restart_marked=True,
    )
    cfg = RestartConfig(
        delay_sec=1.0,
        settings_safety_window_sec=30.0,
        require_all_hard_pass=True,
        require_needs_restart=True,
    )

    assert should_restart(ledger, [PermissionId.INPUT_MONITORING], cfg) is True


@pytest.mark.asyncio
async def test_decide_after_first_run_timeout_mode_completes_without_restart() -> None:
    orch = PermissionOrchestrator.__new__(PermissionOrchestrator)
    orch.ledger = _ledger_with_hard_step(
        state=StepState.SKIPPED,
        needs_restart_marked=False,
        restart_count=0,
    )
    orch.advance_on_timeout = True
    orch.restart_cfg = RestartConfig()
    orch.hard_permissions = [PermissionId.INPUT_MONITORING]
    orch._restart_limit = 5
    orch._enter_restart_sequence = AsyncMock()
    orch._complete = AsyncMock()

    await orch._decide_after_first_run()

    orch._enter_restart_sequence.assert_not_awaited()
    orch._complete.assert_awaited_once_with(full_mode=True)


@pytest.mark.asyncio
async def test_decide_after_first_run_timeout_mode_no_second_restart() -> None:
    orch = PermissionOrchestrator.__new__(PermissionOrchestrator)
    orch.ledger = _ledger_with_hard_step(
        state=StepState.SKIPPED,
        needs_restart_marked=False,
        restart_count=1,
    )
    orch.advance_on_timeout = True
    orch.restart_cfg = RestartConfig()
    orch.hard_permissions = [PermissionId.INPUT_MONITORING]
    orch._restart_limit = 5
    orch._enter_restart_sequence = AsyncMock()
    orch._complete = AsyncMock()

    await orch._decide_after_first_run()

    orch._enter_restart_sequence.assert_not_awaited()
    orch._complete.assert_awaited_once_with(full_mode=True)
