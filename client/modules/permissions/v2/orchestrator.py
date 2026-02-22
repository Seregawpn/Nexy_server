"""
Permission System V2 - Async Orchestrator

Main FSM that drives the permission wizard pipeline.
Runs all steps sequentially, handles restarts, and emits UI events.
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from enum import StrEnum
import logging
import os
import time
from typing import Any, Callable, Literal, Protocol
import uuid

from .ledger import LedgerRecord, LedgerStore, StepLedgerEntry
from .settings_nav import SettingsNavigator
from .types import (
    OutcomeKind,
    PermissionId,
    Phase,
    ProbeResult,
    RestartConfig,
    StepConfig,
    StepMode,
    StepOutcome,
    StepState,
)

logger = logging.getLogger(__name__)


# -----------------------------
# UI Events
# -----------------------------


class UIEventType(StrEnum):
    PHASE_CHANGED = "phase_changed"
    STEP_CHANGED = "step_changed"
    STEP_STATE_CHANGED = "step_state_changed"
    SETTINGS_OPENED = "settings_opened"
    RESTART_SCHEDULED = "restart_scheduled"
    RESTART_STARTED = "restart_started"
    POST_RESTART_VERIFY_STARTED = "post_restart_verify_started"
    COMPLETED = "completed"
    LIMITED_MODE_ENTERED = "limited_mode_entered"
    ERROR = "error"


@dataclass(frozen=True)
class UIEvent:
    type: UIEventType
    timestamp: float
    payload: dict[str, Any]


# -----------------------------
# Prober Protocol
# -----------------------------


class PermissionProber(Protocol):
    """Protocol for permission probers.

    All methods are async. If you need to wrap a sync prober,
    use AsyncProberWrapper.
    """

    async def trigger(self) -> None:
        """Trigger the permission request."""
        ...

    async def probe(self, probe_kind: Literal["light", "heavy"]) -> ProbeResult:
        """Probe the permission capability."""
        ...


class PermissionClassifier(Protocol):
    """Protocol for permission classifiers."""

    def classify(self, probe: ProbeResult, entry: StepLedgerEntry) -> StepOutcome:
        """Classify the probe result into an outcome."""
        ...


# -----------------------------
# Restart Handler Protocol
# -----------------------------


class RestartHandler(Protocol):
    """Protocol for restart handling."""

    async def trigger_restart(self, *, reason: str, permissions: list[str]) -> bool:
        """Trigger application restart."""
        ...


# -----------------------------
# Decision Helpers
# -----------------------------


def should_restart(
    ledger: LedgerRecord,
    hard_permissions: list[PermissionId],
    restart_cfg: RestartConfig,
) -> bool:
    """Check if restart is needed.

    Returns True if:
    - Any HARD permission is in NEEDS_RESTART state (safety guard), OR
    - All HARD are PASS/NEEDS_RESTART AND any has needs_restart_marked
    """
    hard_states = []
    for p in hard_permissions:
        if p not in ledger.steps:
            return False
        hard_states.append(ledger.steps[p].state)

    # Safety guard: any HARD in NEEDS_RESTART state => must restart
    # This catches edge cases where needs_restart_marked wasn't set
    if any(s == StepState.NEEDS_RESTART for s in hard_states):
        return True

    if restart_cfg.require_all_hard_pass:
        # Normal path: all HARD must be PASS/NEEDS_RESTART
        if not all(s in (StepState.PASS_, StepState.NEEDS_RESTART) for s in hard_states):
            return False

    if restart_cfg.require_needs_restart:
        return any(s.needs_restart_marked for s in ledger.steps.values())

    # Restart requested after all HARD passed (no needs_restart requirement)
    return bool(hard_permissions)


def should_enter_limited_mode(ledger: LedgerRecord, hard_permissions: list[PermissionId]) -> bool:
    """Check if any HARD permission failed."""
    for p in hard_permissions:
        if p not in ledger.steps:
            continue
        if ledger.steps[p].state in (StepState.FAIL, StepState.FAIL_AFTER_RESTART):
            return True
    return False


def can_restart_safely(ledger: LedgerRecord, restart_cfg: RestartConfig) -> bool:
    """Check if restart is safe (user not in Settings)."""
    if not ledger.current_step:
        return True

    cur = ledger.steps.get(ledger.current_step)
    if not cur:
        return True

    if cur.state in (StepState.WAITING_USER, StepState.WAITING_LONG) and cur.settings_opened_at:
        elapsed = time.time() - cur.settings_opened_at
        if elapsed < restart_cfg.settings_safety_window_sec:
            return False

    return True


# -----------------------------
# Orchestrator
# -----------------------------


class PermissionOrchestrator:
    """
    Async FSM orchestrator for permission wizard.

    Pipeline mode: all permissions run sequentially.
    Restart only if: all HARD pass + any needs_restart_marked.
    """

    def __init__(
        self,
        *,
        order: list[PermissionId],
        step_configs: dict[PermissionId, StepConfig],
        probers: dict[PermissionId, PermissionProber],
        classifiers: dict[PermissionId, PermissionClassifier],
        hard_permissions: list[PermissionId],
        restart_cfg: RestartConfig,
        settings_nav: SettingsNavigator,
        ledger_store: LedgerStore,
        emit: Callable[[UIEvent], None],
        restart_handler: RestartHandler | None = None,
        should_abort_restart: Callable[[], bool] | None = None,
        is_gui_process: bool = True,
        session_id: str | None = None,
        inter_step_pause_s: float = 0.0,
        advance_on_timeout: bool = False,
    ):
        self.order = order
        self.step_configs = step_configs
        self.probers = probers
        self.classifiers = classifiers
        self.hard_permissions = hard_permissions
        self.restart_cfg = restart_cfg
        self.settings_nav = settings_nav
        self.ledger_store = ledger_store
        self.emit = emit
        self.restart_handler = restart_handler
        self.should_abort_restart = should_abort_restart
        self.is_gui_process = is_gui_process
        self.session_id = session_id or str(uuid.uuid4())
        self.inter_step_pause_s = inter_step_pause_s
        self.advance_on_timeout = advance_on_timeout
        self._restart_limit = 5  # Allow up to 5 restarts to break TCC zombie state

        self._running = False
        self._cancelled = False
        self._idx = 0
        self.ledger: LedgerRecord | None = None

    # ---------- Lifecycle ----------

    async def start(self) -> None:
        """Start the permission wizard."""
        if self._running:
            logger.warning("[ORCHESTRATOR] Already running")
            return

        self._running = True
        self._cancelled = False

        # Check GUI process
        if not self.is_gui_process:
            self._emit_error(
                "NOT_GUI_PROCESS", "Permission orchestrator must run in GUI .app process."
            )
            await self._enter_limited_mode()
            return

        # Load or create ledger
        self.ledger = self._init_or_load_ledger()

        # If ledger is already completed (e.g., after restart completed)
        if self.ledger.phase in (Phase.COMPLETED, Phase.LIMITED_MODE):
            if self.ledger.phase == Phase.LIMITED_MODE:
                # Policy: limited_mode is deprecated; normalize persisted state to completed.
                self.ledger.phase = Phase.COMPLETED
                self._save()
            hard_permissions_still_pass = await self._revalidate_hard_permissions()
            if hard_permissions_still_pass:
                logger.info(
                    "[ORCHESTRATOR] Ledger already %s (restart_count=%d) and hard permissions verified - emitting completion event and exiting",
                    self.ledger.phase.value,
                    self.ledger.restart_count,
                )
                # Re-emit completion event for integrations that started after restart
                await self._emit_completion_from_ledger()
                return

            logger.warning(
                "[ORCHESTRATOR] Ledger marked completed, but hard permissions are not active. Restarting first-run pipeline."
            )
            self.ledger.phase = Phase.FIRST_RUN
            self._save()
            self._emit_phase_changed(Phase.FIRST_RUN)
            self._idx = 0
            await self._run_pipeline()
            return

        # If we're resuming after restart
        if self.ledger.phase == Phase.POST_RESTART_VERIFY:
            await self._enter_post_restart_verify()
            return

        # Normal first run
        self.ledger.phase = Phase.FIRST_RUN
        self._save()
        self._emit_phase_changed(Phase.FIRST_RUN)

        self._idx = 0
        await self._run_pipeline()

    async def resume_after_restart(self) -> None:
        """Resume after application restart."""
        loaded = self.ledger_store.load()
        if loaded:
            self.ledger = loaded
        else:
            logger.warning("[ORCHESTRATOR] No ledger found after restart")
            return

        self._running = True
        self._cancelled = False

        if self.ledger.phase != Phase.POST_RESTART_VERIFY:
            # Already completed or not in restart state
            await self._complete(full_mode=True)
            return

        await self._enter_post_restart_verify()

    def stop(self) -> None:
        """Stop the wizard."""
        self._cancelled = True
        self._running = False

    # ---------- Pipeline Execution ----------

    async def _run_pipeline(self) -> None:
        """Run all permission steps sequentially."""
        if not self.ledger:
            logger.error("[ORCHESTRATOR] Ledger not initialized, cannot run pipeline")
            return

        while self._idx < len(self.order) and not self._cancelled:
            perm = self.order[self._idx]
            cfg = self.step_configs[perm]
            entry = self.ledger.steps[perm]

            self.ledger.current_step = perm
            self._save()
            self._emit_step_changed(perm)

            # For FDA, run a pre-probe to force TCC to create an entry
            # so the app appears in the Full Disk Access list.
            # This must run regardless of advance_on_timeout mode.
            if (
                perm == PermissionId.FULL_DISK_ACCESS
                and entry.state not in (StepState.PASS_, StepState.SKIPPED)
                and entry.last_probe_at is None
            ):
                try:
                    await self.probers[perm].probe("heavy")
                except Exception as e:
                    logger.error("[ORCHESTRATOR] Pre-probe failed for %s: %s", perm.value, e)

            # Open Settings for OPEN_SETTINGS mode.
            # Retry on subsequent runs if permission is still not PASS/SKIPPED.
            should_open_settings = cfg.mode == StepMode.OPEN_SETTINGS and (
                entry.settings_opened_at is None
                or entry.state not in (StepState.PASS_, StepState.SKIPPED)
            )
            if should_open_settings:
                target = cfg.settings_target or "privacy_and_security"
                opened = self.settings_nav.open(target)
                if opened:
                    entry.settings_opened_at = time.time()
                    self._save()
                    self._emit_settings_opened(perm, target)
                else:
                    logger.warning(
                        "[ORCHESTRATOR] Failed to open Settings for %s (target=%s)",
                        perm.value,
                        target,
                    )

            # Trigger permission request.
            # Retry on subsequent runs if permission is still not PASS/SKIPPED.
            should_trigger = entry.triggered_at is None or entry.state not in (
                StepState.PASS_,
                StepState.SKIPPED,
            )
            if should_trigger:
                if entry.triggered_at is None:
                    self._set_step_state(perm, StepState.TRIGGERED, "TRIGGERED", "Step triggered")
                try:
                    await self.probers[perm].trigger()
                except Exception as e:
                    logger.error("[ORCHESTRATOR] Failed to trigger %s: %s", perm.value, e)
                entry.triggered_at = time.time()
                self._save()

            # Grace period
            if entry.grace_started_at is None:
                entry.grace_started_at = time.time()
                self._set_step_state(perm, StepState.GRACE, "GRACE", f"Grace {cfg.timing.grace_s}s")
                self._save()

            await asyncio.sleep(cfg.timing.grace_s)

            if self._cancelled:
                break

            step_deadline: float | None = None
            if self.advance_on_timeout and cfg.timing.step_timeout_s:
                step_start = entry.grace_started_at or time.time()
                step_deadline = step_start + cfg.timing.step_timeout_s

            if self.advance_on_timeout:
                if step_deadline is not None:
                    await self._wait_until_deadline(perm, step_deadline)
                else:
                    self._mark_timeout(perm, "TIMEOUT", "Step timeout reached")
            else:
                if cfg.mode == StepMode.AUTO_DIALOG:
                    await self._poll_until_done(perm, cfg, step_deadline)
                else:
                    await self._probe_once(perm, cfg)
                    if step_deadline is not None:
                        await self._wait_until_deadline(perm, step_deadline)
            if self._cancelled:
                break

            if self.inter_step_pause_s > 0:
                await asyncio.sleep(self.inter_step_pause_s)

            self._idx += 1

        if not self._cancelled:
            await self._decide_after_first_run()

    async def _probe_once(self, perm: PermissionId, cfg: StepConfig) -> None:
        """Probe once after grace and move on (no polling loop)."""
        if not self.ledger:
            logger.error("[ORCHESTRATOR] Ledger not initialized, cannot probe")
            return

        entry = self.ledger.steps[perm]
        if entry.polling_started_at is None:
            entry.polling_started_at = time.time()
            self._set_step_state(perm, StepState.POLLING, "POLLING", "Probing capability once")
            self._save()
        try:
            pr = await self.probers[perm].probe("heavy")
        except Exception as e:
            logger.error("[ORCHESTRATOR] Probe failed for %s: %s", perm.value, e)
            self._set_step_state(perm, StepState.WAITING_USER, "PROBE_ERROR", "Probe failed")
            self._save()
            return
        try:
            out = self.classifiers[perm].classify(pr, entry)
        except Exception as e:
            logger.error("[ORCHESTRATOR] Classify failed for %s: %s", perm.value, e)
            self._set_step_state(
                perm, StepState.WAITING_USER, "CLASSIFY_ERROR", "Classification failed"
            )
            self._save()
            return
        entry.last_probe_at = time.time()
        entry.attempts += 1
        entry.last_reason_code = out.reason_code
        entry.last_reason = out.reason
        self._save()
        if out.kind == OutcomeKind.PASS_:
            self._set_step_state(perm, StepState.PASS_, out.reason_code, out.reason)
            self._save()
            return
        if out.kind == OutcomeKind.NEEDS_RESTART and cfg.supports_needs_restart:
            self._set_step_state(perm, StepState.NEEDS_RESTART, out.reason_code, out.reason)
            entry.needs_restart_marked = True
            entry.needs_restart_marked_at = time.time()
            self.ledger.needs_restart = True
            self._save()
            return
        if out.kind == OutcomeKind.FAIL:
            self._set_step_state(perm, StepState.FAIL, out.reason_code, out.reason)
            self._save()
            return
        if out.kind == OutcomeKind.FAIL_AFTER_RESTART:
            self._set_step_state(perm, StepState.FAIL_AFTER_RESTART, out.reason_code, out.reason)
            self._save()
            return
        if out.kind == OutcomeKind.SKIP:
            self._set_step_state(perm, StepState.SKIPPED, out.reason_code, out.reason)
            self._save()
            return
        # WAITING / WAITING_USER
        if out.kind == OutcomeKind.WAITING_USER:
            self._set_step_state(perm, StepState.WAITING_USER, out.reason_code, out.reason)
            self._maybe_open_settings(perm, cfg, entry)
            self._save()
            return
        self._set_step_state(perm, StepState.WAITING_USER, out.reason_code, out.reason)
        self._maybe_open_settings(perm, cfg, entry)
        self._save()

    async def _poll_until_done(
        self, perm: PermissionId, cfg: StepConfig, deadline: float | None
    ) -> bool:
        """Poll until step is done (PASS/FAIL/etc) or timeout."""
        if not self.ledger:
            logger.error("[ORCHESTRATOR] Ledger not initialized, cannot poll")
            return False

        entry = self.ledger.steps[perm]
        start = entry.polling_started_at or time.time()

        while not self._cancelled:
            now = time.time()
            elapsed = now - start

            if deadline is not None and now >= deadline:
                logger.warning(
                    f"[ORCHESTRATOR] Step {perm.value} timed out - treating as NEEDS_RESTART (fail-fast)"
                )
                # [FIXED BY AI] Fail-Fast: Treat timeout as a signal to restart
                self._set_step_state(
                    perm, StepState.NEEDS_RESTART, "TIMEOUT_RESTART", "Timeout reached - restarting"
                )
                entry.needs_restart_marked = True
                entry.needs_restart_marked_at = now
                self.ledger.needs_restart = True
                self._save()
                return True

            # Transition to WAITING_LONG for Settings steps
            if cfg.mode == StepMode.OPEN_SETTINGS:
                if (
                    entry.state == StepState.WAITING_USER
                    and elapsed >= cfg.timing.waiting_long_after_s
                ):
                    entry.waiting_long_entered_at = now
                    self._set_step_state(
                        perm, StepState.WAITING_LONG, "WAITING_LONG", "Long waiting mode"
                    )
                    self._save()

            # Choose probe kind
            probe_kind: Literal["light", "heavy"] = "light"
            if entry.next_heavy_allowed_at is None or now >= entry.next_heavy_allowed_at:
                probe_kind = "heavy"
                entry.next_heavy_allowed_at = now + cfg.timing.heavy_cooldown_s

            # Run probe
            try:
                pr = await self.probers[perm].probe(probe_kind)
            except Exception as e:
                logger.error("[ORCHESTRATOR] Probe failed for %s: %s", perm.value, e)
                await asyncio.sleep(cfg.timing.poll_s)
                continue

            # Classify
            try:
                out = self.classifiers[perm].classify(pr, entry)
            except Exception as e:
                logger.error("[ORCHESTRATOR] Classify failed for %s: %s", perm.value, e)
                await asyncio.sleep(cfg.timing.poll_s)
                continue

            entry.last_probe_at = now
            entry.attempts += 1
            entry.last_reason_code = out.reason_code
            entry.last_reason = out.reason
            self._save()

            # Handle outcome
            if out.kind == OutcomeKind.PASS_:
                self._set_step_state(perm, StepState.PASS_, out.reason_code, out.reason)
                self._save()
                return True

            if out.kind == OutcomeKind.NEEDS_RESTART and cfg.supports_needs_restart:
                self._set_step_state(perm, StepState.NEEDS_RESTART, out.reason_code, out.reason)
                entry.needs_restart_marked = True
                entry.needs_restart_marked_at = now
                self.ledger.needs_restart = True
                self._save()
                return True

            if out.kind == OutcomeKind.FAIL:
                self._set_step_state(perm, StepState.FAIL, out.reason_code, out.reason)
                self._save()
                return True

            if out.kind == OutcomeKind.FAIL_AFTER_RESTART:
                self._set_step_state(
                    perm, StepState.FAIL_AFTER_RESTART, out.reason_code, out.reason
                )
                self._save()
                return True

            if out.kind == OutcomeKind.SKIP:
                self._set_step_state(perm, StepState.SKIPPED, out.reason_code, out.reason)
                self._save()
                return True

            # WAITING_USER
            if out.kind == OutcomeKind.WAITING_USER:
                if entry.state != StepState.WAITING_USER:
                    self._set_step_state(perm, StepState.WAITING_USER, out.reason_code, out.reason)
                    self._save()

            # Sleep and continue polling
            poll_interval = (
                cfg.timing.waiting_long_poll_s
                if entry.state == StepState.WAITING_LONG
                else cfg.timing.poll_s
            )
            await asyncio.sleep(poll_interval)

        return False

    # ---------- Phase Decisions ----------

    async def _decide_after_first_run(self) -> None:
        """Decide next phase after all steps complete."""
        if not self.ledger:
            logger.error("[ORCHESTRATOR] Ledger not initialized, cannot decide")
            return

        if self.advance_on_timeout:
            if self.ledger.restart_count >= 1:
                await self._complete(full_mode=True)
                return
            if self._should_abort_restart():
                logger.info("[ORCHESTRATOR] Restart skipped: user quit intent is active")
                await self._complete(full_mode=True)
                return
            await self._enter_restart_sequence(force_restart=True)
            return

        # Hard guard: V2 policy allows multiple restarts to break TCC zombie state
        if self.ledger.restart_count >= self._restart_limit:
            logger.info(
                "[ORCHESTRATOR] Restart limit reached (%d) - exiting loop",
                self.ledger.restart_count,
            )
            await self._complete(full_mode=True)
            return

        # Check if restart needed and safe
        if should_restart(self.ledger, self.hard_permissions, self.restart_cfg):
            if can_restart_safely(self.ledger, self.restart_cfg):
                # However, to satisfy "Restart only after actual completion of first-run (all steps processed)",
                # we are already there.

                # The issue is likely that RESTART_PENDING is not "COMPLETED".
                # Let's perform the restart logic but ensure we don't block.
                # Or better: emit a "completion-like" event before restarting?

                await self._enter_restart_sequence()
                return

        # Complete immediately
        await self._complete(full_mode=True)

    async def _enter_restart_sequence(self, *, force_restart: bool = False) -> None:
        """
        Prepare for and trigger restart.

        Changed in V2 Fix:
        We now treat this as the end of the first run. We emit restart-related events,
        but we ensure the system knows we are 'done' with the wizard steps.
        """
        if not self.ledger:
            logger.error("[ORCHESTRATOR] Ledger not initialized, cannot enter restart sequence")
            return

        if self._should_abort_restart():
            logger.info("[ORCHESTRATOR] Restart sequence aborted: user quit intent is active")
            await self._complete(full_mode=True)
            return

        if self.ledger.restart_count >= 1:
            logger.info(
                "[ORCHESTRATOR] Restart sequence skipped: restart already performed (restart_count=%d)",
                self.ledger.restart_count,
            )
            await self._complete(full_mode=True)
            return

        self.ledger.phase = Phase.RESTART_PENDING
        self._save()
        self._emit_phase_changed(Phase.RESTART_PENDING)

        self.emit(
            UIEvent(
                UIEventType.RESTART_SCHEDULED,
                time.time(),
                {"reason": "Restart required to activate permissions"},
            )
        )

        # Explicitly emit a 'completed' event for compatibility if needed,
        # or rely on the fact that we are about to restart.
        # User goal: "Restart only after actual completion of first-run".
        # We are here => all steps processed.

        await asyncio.sleep(self.restart_cfg.delay_sec)

        if self._cancelled:
            return
        if self._should_abort_restart():
            logger.info(
                "[ORCHESTRATOR] Restart cancelled before trigger: user quit intent is active"
            )
            await self._complete(full_mode=True)
            return

        # Only proceed to restart if handler is present
        if self.restart_handler:
            self.emit(
                UIEvent(
                    UIEventType.RESTART_STARTED,
                    time.time(),
                    {"restart_count": self.ledger.restart_count + 1},
                )
            )

            self.ledger.restart_count += 1
            # Next boot should verify permissions
            self.ledger.phase = Phase.POST_RESTART_VERIFY
            self._save()

            permissions = [p.value for p in self.order if self.ledger.steps[p].needs_restart_marked]

            # Fire restart
            await self.restart_handler.trigger_restart(
                reason="permission_activation", permissions=permissions
            )
        else:
            # No restart handler - cannot restart
            logger.warning("[ORCHESTRATOR] No restart handler available")
            if force_restart:
                await self._complete(full_mode=True)
                return

            # Check if any HARD permission needs restart
            hard_needs_restart = any(
                self.ledger.steps[p].state == StepState.NEEDS_RESTART
                for p in self.hard_permissions
                if p in self.ledger.steps
            )

            if hard_needs_restart:
                logger.warning(
                    "[ORCHESTRATOR] HARD permissions need restart but no handler - continue in full mode"
                )
                self.ledger.restart_unavailable = True
            else:
                logger.info("[ORCHESTRATOR] Only soft permissions need restart - completing anyway")
            await self._complete(full_mode=True)

    async def _enter_post_restart_verify(self) -> None:
        """Verify permissions after restart."""
        if not self.ledger:
            logger.error("[ORCHESTRATOR] Ledger not initialized, cannot enter post restart verify")
            return

        if self.advance_on_timeout:
            # Timeout-driven flow treats each step as received by timebox,
            # so post-restart verify should not re-open failure branches.
            await self._complete(full_mode=True)
            return

        self.ledger.phase = Phase.POST_RESTART_VERIFY
        self._save()
        self._emit_phase_changed(Phase.POST_RESTART_VERIFY)

        self.emit(UIEvent(UIEventType.POST_RESTART_VERIFY_STARTED, time.time(), {"window_s": 20}))

        # Verify only permissions that needed restart
        to_verify = [p for p, s in self.ledger.steps.items() if s.needs_restart_marked]

        for p in to_verify:
            if self._cancelled:
                return
            cfg = self.step_configs[p]
            await self._verify_with_window(p, cfg)

        # Policy: do not enter limited mode after restart verification.
        await self._complete(full_mode=True)

    async def _verify_with_window(self, perm: PermissionId, cfg: StepConfig) -> None:
        """Verify a permission within a time window after restart."""
        if not self.ledger:
            logger.error("[ORCHESTRATOR] Ledger not initialized, cannot verify")
            return

        entry = self.ledger.steps[perm]
        start = time.time()
        window = cfg.timing.post_restart_verify_window_s
        tick = cfg.timing.post_restart_verify_tick_s

        entry.next_heavy_allowed_at = None

        while time.time() - start <= window and not self._cancelled:
            try:
                pr = await self.probers[perm].probe("heavy")
                out = self.classifiers[perm].classify(pr, entry)
            except Exception as e:
                logger.error("[ORCHESTRATOR] Verify probe failed for %s: %s", perm.value, e)
                await asyncio.sleep(tick)
                continue

            entry.last_probe_at = time.time()
            entry.last_reason_code = out.reason_code
            entry.last_reason = out.reason
            self._save()

            if out.kind == OutcomeKind.PASS_:
                self._set_step_state(
                    perm, StepState.PASS_, out.reason_code, "Verified after restart"
                )
                entry.needs_restart_marked = False
                self._save()
                return

            await asyncio.sleep(tick)

        # Window exhausted
        self._set_step_state(
            perm, StepState.FAIL_AFTER_RESTART, "VERIFY_TIMEOUT", "Not active after restart"
        )
        self._save()

    # ---------- Completion ----------

    async def _enter_limited_mode(self) -> None:
        """Enter limited mode due to hard failures."""
        logger.info("[ORCHESTRATOR] limited_mode disabled by policy; normalizing to completed")
        await self._complete(full_mode=True)

    async def _complete(self, *, full_mode: bool) -> None:
        """Complete the wizard."""
        if not self.ledger:
            logger.error("[ORCHESTRATOR] Ledger not initialized, cannot complete")
            return

        self.ledger.phase = Phase.COMPLETED
        self._save()
        self._emit_phase_changed(Phase.COMPLETED)
        self._running = False

        self.emit(UIEvent(UIEventType.COMPLETED, time.time(), {"full_mode": full_mode}))

    async def _emit_completion_from_ledger(self) -> None:
        """Re-emit completion event from existing completed ledger state."""
        if not self.ledger:
            logger.error("[ORCHESTRATOR] Ledger not initialized, cannot emit completion")
            return

        if self.ledger.phase == Phase.LIMITED_MODE:
            self.ledger.phase = Phase.COMPLETED
            self._save()

        is_full_mode = True
        event_type = UIEventType.COMPLETED

        # Build summary
        summary = {}
        for perm_id, entry in self.ledger.steps.items():
            summary[perm_id.value] = {
                "state": entry.state.value,
                "mode": entry.mode.value,
            }

        self.emit(
            UIEvent(
                event_type,
                time.time(),
                {
                    "full_mode": is_full_mode,
                    "phase": self.ledger.phase.value,
                    "summary": summary,
                    "restart_count": self.ledger.restart_count,
                },
            )
        )

        logger.info(
            "[ORCHESTRATOR] Re-emitted %s from ledger (restart_count=%d)",
            event_type.value,
            self.ledger.restart_count,
        )

    async def _revalidate_hard_permissions(self) -> bool:
        """
        Re-probe hard permissions against runtime TCC state.

        This prevents stale ledger=completed from bypassing real permission checks
        after reinstall/revocation.
        """
        if not self.ledger:
            logger.error("[ORCHESTRATOR] Ledger not initialized, cannot revalidate hard permissions")
            return False

        all_hard_pass = True
        for perm in self.hard_permissions:
            entry = self.ledger.steps.get(perm)
            if entry is None:
                logger.warning("[ORCHESTRATOR] Hard permission missing in ledger: %s", perm.value)
                all_hard_pass = False
                continue

            try:
                probe = await self.probers[perm].probe("heavy")
                outcome = self.classifiers[perm].classify(probe, entry)
            except Exception as e:
                logger.error(
                    "[ORCHESTRATOR] Hard permission revalidation failed for %s: %s",
                    perm.value,
                    e,
                )
                self._set_step_state(
                    perm, StepState.WAITING_USER, "REVALIDATE_ERROR", "Revalidation failed"
                )
                self._save()
                all_hard_pass = False
                continue

            entry.last_probe_at = time.time()
            entry.attempts += 1
            entry.last_reason_code = outcome.reason_code
            entry.last_reason = outcome.reason

            if outcome.kind == OutcomeKind.PASS_:
                self._set_step_state(perm, StepState.PASS_, outcome.reason_code, outcome.reason)
                entry.needs_restart_marked = False
                self._save()
                continue

            all_hard_pass = False
            if outcome.kind == OutcomeKind.NEEDS_RESTART:
                self._set_step_state(
                    perm, StepState.NEEDS_RESTART, outcome.reason_code, outcome.reason
                )
                entry.needs_restart_marked = True
                entry.needs_restart_marked_at = time.time()
                self.ledger.needs_restart = True
            elif outcome.kind == OutcomeKind.FAIL_AFTER_RESTART:
                self._set_step_state(
                    perm, StepState.FAIL_AFTER_RESTART, outcome.reason_code, outcome.reason
                )
            elif outcome.kind == OutcomeKind.FAIL:
                self._set_step_state(perm, StepState.FAIL, outcome.reason_code, outcome.reason)
            else:
                self._set_step_state(
                    perm, StepState.WAITING_USER, outcome.reason_code, outcome.reason
                )
            self._save()

        return all_hard_pass

    # ---------- Helpers ----------

    def _init_or_load_ledger(self) -> LedgerRecord:
        """Load existing ledger or create new one."""
        existing = self.ledger_store.load()
        if existing:
            # FIX: Ensure all permissions in current config are present in the ledger
            # This handles cases where new permissions were added to config but not yet in ledger,
            # or if a permission was dropped (though we don't delete extra keys here to be safe).
            dirty = False
            for p in self.order:
                if p not in existing.steps:
                    cfg = self.step_configs[p]
                    existing.steps[p] = StepLedgerEntry(permission=p, mode=cfg.mode)
                    logger.info(
                        "[ORCHESTRATOR] Backfilled missing permission in ledger: %s", p.value
                    )
                    dirty = True

            if dirty:
                self.ledger_store.save(existing)

            return existing

        now = time.time()
        steps: dict[PermissionId, StepLedgerEntry] = {}
        for p in self.order:
            cfg = self.step_configs[p]
            steps[p] = StepLedgerEntry(permission=p, mode=cfg.mode)

        return LedgerRecord(
            session_id=self.session_id,
            phase=Phase.FIRST_RUN,
            created_at=now,
            updated_at=now,
            steps=steps,
            gui_process_pid=os.getpid(),
        )

    def _save(self) -> None:
        """Save ledger to disk."""
        if self.ledger:
            self.ledger_store.save(self.ledger)

    def _set_step_state(
        self, perm: PermissionId, state: StepState, reason_code: str, reason: str
    ) -> None:
        """Update step state and emit event (with dedup)."""
        if not self.ledger:
            logger.error("[ORCHESTRATOR] Ledger not initialized, cannot set step state")
            return

        entry = self.ledger.steps[perm]
        if entry.state == state:
            return  # UIUpdateGate

        entry.state = state
        entry.last_reason_code = reason_code
        entry.last_reason = reason
        self._save()

        self.emit(
            UIEvent(
                UIEventType.STEP_STATE_CHANGED,
                time.time(),
                {
                    "permission": perm.value,
                    "state": state.value,
                    "reason_code": reason_code,
                    "reason": reason,
                },
            )
        )

    def _mark_timeout(self, perm: PermissionId, reason_code: str, reason: str) -> None:
        if not self.ledger:
            return
        entry = self.ledger.steps[perm]
        if entry.state in (
            StepState.PASS_,
            StepState.FAIL,
            StepState.NEEDS_RESTART,
            StepState.FAIL_AFTER_RESTART,
            StepState.SKIPPED,
        ):
            return
        if self.advance_on_timeout:
            self._set_step_state(
                perm, StepState.PASS_, "TIMEBOX_RECEIVED", "Step completed by timebox"
            )
            return
        self._set_step_state(perm, StepState.SKIPPED, reason_code, reason)

    def _should_abort_restart(self) -> bool:
        if not self.should_abort_restart:
            return False
        try:
            return bool(self.should_abort_restart())
        except Exception:
            return False

    async def _wait_until_deadline(self, perm: PermissionId, deadline: float) -> None:
        if deadline <= 0:
            return
        if not self.ledger:
            return
        entry = self.ledger.steps.get(perm)
        if entry and entry.state in (
            StepState.PASS_,
            StepState.FAIL,
            StepState.NEEDS_RESTART,
            StepState.FAIL_AFTER_RESTART,
            StepState.SKIPPED,
        ):
            return
        remaining = deadline - time.time()
        if remaining > 0:
            await asyncio.sleep(remaining)
        self._mark_timeout(perm, "TIMEOUT", "Step timeout reached")

    def _emit_phase_changed(self, phase: Phase) -> None:
        self.emit(UIEvent(UIEventType.PHASE_CHANGED, time.time(), {"phase": phase.value}))

    def _emit_step_changed(self, perm: PermissionId) -> None:
        self.emit(UIEvent(UIEventType.STEP_CHANGED, time.time(), {"permission": perm.value}))

    def _emit_settings_opened(self, perm: PermissionId, target: str) -> None:
        self.emit(
            UIEvent(
                UIEventType.SETTINGS_OPENED,
                time.time(),
                {"permission": perm.value, "settings_target": target},
            )
        )

    def _maybe_open_settings(
        self, perm: PermissionId, cfg: StepConfig, entry: StepLedgerEntry
    ) -> None:
        if perm == PermissionId.CONTACTS:
            return
        if cfg.mode == StepMode.OPEN_SETTINGS:
            return
        if not cfg.settings_target:
            return
        if entry.settings_opened_at is not None:
            return
        if self.settings_nav.open(cfg.settings_target):
            entry.settings_opened_at = time.time()
            self._save()
            self._emit_settings_opened(perm, cfg.settings_target)

    def _emit_error(self, code: str, message: str) -> None:
        self.emit(UIEvent(UIEventType.ERROR, time.time(), {"code": code, "message": message}))
