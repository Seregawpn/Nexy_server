from __future__ import annotations

from pathlib import Path
import tempfile
import time

import pytest

from modules.permissions.v2.ledger import LedgerStore
from modules.permissions.v2.orchestrator import PermissionOrchestrator
from modules.permissions.v2.types import (
    OutcomeKind,
    PermissionId,
    Phase,
    ProbeEvidence,
    ProbeResult,
    RestartConfig,
    StepConfig,
    StepMode,
    StepOutcome,
    StepTiming,
)


class _NoopSettingsNav:
    def open(self, _target: str) -> bool:
        return True


class _NoopProber:
    async def trigger(self) -> None:
        return None

    async def probe(self, probe_kind: str) -> ProbeResult:
        return ProbeResult(
            permission=PermissionId.MICROPHONE,
            timestamp=time.time(),
            probe_kind=probe_kind,  # type: ignore[arg-type]
            evidence=ProbeEvidence(),
        )


class _NoopClassifier:
    def classify(self, probe: ProbeResult, _entry) -> StepOutcome:
        return StepOutcome(
            permission=probe.permission,
            kind=OutcomeKind.WAITING,
            reason="noop",
            reason_code="NOOP",
        )


class _RestartRecorder:
    def __init__(self) -> None:
        self.calls: list[tuple[str, list[str]]] = []

    async def trigger_restart(self, *, reason: str, permissions: list[str]) -> bool:
        self.calls.append((reason, permissions))
        return True


class _EventRecorder:
    def __init__(self) -> None:
        self.events: list[tuple[str, dict[str, object]]] = []

    def __call__(self, event) -> None:
        self.events.append((event.type.value, dict(event.payload)))


def _create_orchestrator(
    *,
    ledger_path: Path,
    restart_handler,
    should_abort_restart,
    emit=None,
) -> PermissionOrchestrator:
    perm = PermissionId.MICROPHONE
    step_cfg = StepConfig(
        permission=perm,
        mode=StepMode.AUTO_DIALOG,
        timing=StepTiming(
            grace_s=0.0,
            poll_s=0.0,
            step_timeout_s=0.01,
        ),
        supports_needs_restart=False,
    )
    return PermissionOrchestrator(
        order=[perm],
        step_configs={perm: step_cfg},
        probers={perm: _NoopProber()},
        classifiers={perm: _NoopClassifier()},
        hard_permissions=[perm],
        restart_cfg=RestartConfig(
            delay_sec=0.0,
            settings_safety_window_sec=0.0,
            require_all_hard_pass=True,
            require_needs_restart=False,
        ),
        settings_nav=_NoopSettingsNav(),
        ledger_store=LedgerStore(str(ledger_path)),
        emit=emit or (lambda _event: None),
        restart_handler=restart_handler,
        should_abort_restart=should_abort_restart,
        is_gui_process=True,
        advance_on_timeout=True,
    )


@pytest.mark.asyncio
async def test_advance_on_timeout_triggers_single_restart_once() -> None:
    with tempfile.TemporaryDirectory() as td:
        recorder = _RestartRecorder()
        orchestrator = _create_orchestrator(
            ledger_path=Path(td) / "ledger.json",
            restart_handler=recorder,
            should_abort_restart=lambda: False,
        )

        await orchestrator.start()

        assert orchestrator.ledger is not None
        assert orchestrator.ledger.restart_count == 1
        assert orchestrator.ledger.phase == Phase.POST_RESTART_VERIFY
        assert len(recorder.calls) == 1


@pytest.mark.asyncio
async def test_quit_intent_cancels_restart_in_timeout_mode() -> None:
    with tempfile.TemporaryDirectory() as td:
        recorder = _RestartRecorder()
        orchestrator = _create_orchestrator(
            ledger_path=Path(td) / "ledger.json",
            restart_handler=recorder,
            should_abort_restart=lambda: True,
        )

        await orchestrator.start()

        assert orchestrator.ledger is not None
        assert orchestrator.ledger.restart_count == 0
        assert orchestrator.ledger.phase == Phase.COMPLETED
        assert len(recorder.calls) == 0


@pytest.mark.asyncio
async def test_post_restart_verify_does_not_restart_again_in_timeout_mode() -> None:
    with tempfile.TemporaryDirectory() as td:
        recorder = _RestartRecorder()
        orchestrator = _create_orchestrator(
            ledger_path=Path(td) / "ledger.json",
            restart_handler=recorder,
            should_abort_restart=lambda: False,
        )

        await orchestrator.start()
        assert orchestrator.ledger is not None
        assert orchestrator.ledger.restart_count == 1
        assert len(recorder.calls) == 1

        await orchestrator.resume_after_restart()

        assert orchestrator.ledger is not None
        assert orchestrator.ledger.restart_count == 1
        assert orchestrator.ledger.phase == Phase.COMPLETED
        assert len(recorder.calls) == 1


@pytest.mark.asyncio
async def test_full_flow_restart_count_transitions_once_and_resume_completes() -> None:
    with tempfile.TemporaryDirectory() as td:
        ledger_path = Path(td) / "ledger.json"
        ledger_store = LedgerStore(str(ledger_path))
        recorder = _RestartRecorder()
        events = _EventRecorder()
        orchestrator = _create_orchestrator(
            ledger_path=ledger_path,
            restart_handler=recorder,
            should_abort_restart=lambda: False,
            emit=events,
        )

        assert ledger_store.load() is None

        await orchestrator.start()

        after_start = ledger_store.load()
        assert after_start is not None
        assert after_start.restart_count == 1
        assert after_start.phase == Phase.POST_RESTART_VERIFY
        assert len(recorder.calls) == 1

        await orchestrator.resume_after_restart()

        after_resume = ledger_store.load()
        assert after_resume is not None
        assert after_resume.restart_count == 1
        assert after_resume.phase == Phase.COMPLETED
        assert len(recorder.calls) == 1

        event_types = [event_type for event_type, _payload in events.events]
        assert "phase_changed" in event_types
        assert "restart_scheduled" in event_types
        assert "restart_started" in event_types
        assert "completed" in event_types
