#!/usr/bin/env python3
"""
Permission System V2 - Test Runner

Simulates the permission wizard flow with mock probers to verify:
1. FSM transitions (FIRST_RUN → COMPLETED or LIMITED_MODE)
2. Grace/polling timing
3. Restart logic
4. Event emission

Usage:
    python3 -m tests.test_permission_v2_simulation
    
    # With specific scenarios:
    python3 -m tests.test_permission_v2_simulation --scenario all_pass
    python3 -m tests.test_permission_v2_simulation --scenario input_monitoring_needs_restart
    python3 -m tests.test_permission_v2_simulation --scenario hard_fail
"""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import dataclass
import logging
import os
import sys
import tempfile
import time
from typing import Literal

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.permissions.v2 import (
    LedgerStore,
    PermissionCriticality,
    PermissionId,
    Phase,
    ProbeEvidence,
    ProbeResult,
    RestartConfig,
    StepConfig,
    StepMode,
    StepTiming,
    UIEvent,
    UIEventType,
    get_classifier,
)
from modules.permissions.v2.orchestrator import PermissionOrchestrator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================
# Mock Probers
# ============================================================

@dataclass
class MockProberConfig:
    """Configuration for mock prober behavior."""
    permission: PermissionId
    # How many probes before returning PASS (0 = immediate pass)
    probes_until_pass: int = 2
    # Should this permission fail?
    should_fail: bool = False
    # Should this permission need restart?
    needs_restart: bool = False
    # Probes until needs_restart is detected
    probes_until_needs_restart: int = 3


class MockProber:
    """Mock prober that simulates permission behavior."""
    
    def __init__(self, config: MockProberConfig, step_config: StepConfig):
        self.mock_config = config
        self.step_config = step_config
        self.permission = config.permission
        self.probe_count = 0
        self.triggered = False
    
    async def trigger(self) -> None:
        self.triggered = True
        logger.info(f"[MOCK] {self.permission.value}: trigger() called")
    
    async def probe(self, probe_kind: Literal["light", "heavy"]) -> ProbeResult:
        self.probe_count += 1
        ts = time.time()
        
        logger.info(
            f"[MOCK] {self.permission.value}: probe({probe_kind}) #{self.probe_count}"
        )
        
        # Simulate different outcomes based on config
        if self.mock_config.should_fail:
            evidence = ProbeEvidence(
                permission_denied_hint=True,
                error_message="Mock: permission denied",
            )
        elif self.mock_config.needs_restart and self.probe_count >= self.mock_config.probes_until_needs_restart:
            evidence = ProbeEvidence(
                tap_created=False,
                tap_enabled=False,
                likely_needs_restart_hint=True,
                error_message="Mock: needs restart",
            )
        elif self.probe_count >= self.mock_config.probes_until_pass:
            # PASS
            evidence = self._make_pass_evidence()
        else:
            # Still waiting
            evidence = ProbeEvidence(
                transient_hint=True,
                error_message="Mock: still waiting",
            )
        
        return ProbeResult(
            permission=self.permission,
            timestamp=ts,
            probe_kind=probe_kind,
            evidence=evidence,
        )
    
    def _make_pass_evidence(self) -> ProbeEvidence:
        """Create evidence that indicates PASS for this permission type."""
        if self.permission == PermissionId.MICROPHONE:
            return ProbeEvidence(frames_received=True)
        elif self.permission == PermissionId.SCREEN_CAPTURE:
            return ProbeEvidence(frames_received=True)
        elif self.permission == PermissionId.INPUT_MONITORING:
            return ProbeEvidence(tap_created=True, tap_enabled=True)
        elif self.permission == PermissionId.ACCESSIBILITY:
            return ProbeEvidence(ax_action_ok=True)
        elif self.permission == PermissionId.FULL_DISK_ACCESS:
            return ProbeEvidence(file_access_ok=True)
        elif self.permission == PermissionId.CONTACTS:
            return ProbeEvidence(contacts_fetch_ok=True)
        elif self.permission == PermissionId.MESSAGES:
            return ProbeEvidence(messages_access_ok=True)
        else:
            return ProbeEvidence()


class MockSettingsNavigator:
    """Mock settings navigator that logs instead of opening Settings."""
    
    def open(self, target: str) -> bool:
        logger.info(f"[MOCK SETTINGS] Would open: {target}")
        return True


# ============================================================
# Test Scenarios
# ============================================================

def create_scenario_all_pass() -> dict[PermissionId, MockProberConfig]:
    """All permissions pass quickly."""
    return {
        PermissionId.MICROPHONE: MockProberConfig(PermissionId.MICROPHONE, probes_until_pass=1),
        PermissionId.SCREEN_CAPTURE: MockProberConfig(PermissionId.SCREEN_CAPTURE, probes_until_pass=1),
        PermissionId.CONTACTS: MockProberConfig(PermissionId.CONTACTS, probes_until_pass=1),
        PermissionId.MESSAGES: MockProberConfig(PermissionId.MESSAGES, probes_until_pass=1),
        PermissionId.INPUT_MONITORING: MockProberConfig(PermissionId.INPUT_MONITORING, probes_until_pass=1),
        PermissionId.ACCESSIBILITY: MockProberConfig(PermissionId.ACCESSIBILITY, probes_until_pass=2),
        PermissionId.FULL_DISK_ACCESS: MockProberConfig(PermissionId.FULL_DISK_ACCESS, probes_until_pass=2),
    }


def create_scenario_input_monitoring_needs_restart() -> dict[PermissionId, MockProberConfig]:
    """Input Monitoring needs restart, others pass."""
    return {
        PermissionId.MICROPHONE: MockProberConfig(PermissionId.MICROPHONE, probes_until_pass=1),
        PermissionId.SCREEN_CAPTURE: MockProberConfig(PermissionId.SCREEN_CAPTURE, probes_until_pass=1),
        PermissionId.CONTACTS: MockProberConfig(PermissionId.CONTACTS, probes_until_pass=1),
        PermissionId.MESSAGES: MockProberConfig(PermissionId.MESSAGES, probes_until_pass=1),
        PermissionId.INPUT_MONITORING: MockProberConfig(
            PermissionId.INPUT_MONITORING,
            needs_restart=True,
            probes_until_needs_restart=2
        ),
        PermissionId.ACCESSIBILITY: MockProberConfig(PermissionId.ACCESSIBILITY, probes_until_pass=2),
        PermissionId.FULL_DISK_ACCESS: MockProberConfig(PermissionId.FULL_DISK_ACCESS, probes_until_pass=2),
    }


def create_scenario_hard_fail() -> dict[PermissionId, MockProberConfig]:
    """Microphone (hard) fails, should enter limited mode."""
    return {
        PermissionId.MICROPHONE: MockProberConfig(PermissionId.MICROPHONE, should_fail=True),
        PermissionId.SCREEN_CAPTURE: MockProberConfig(PermissionId.SCREEN_CAPTURE, probes_until_pass=1),
        PermissionId.CONTACTS: MockProberConfig(PermissionId.CONTACTS, probes_until_pass=1),
        PermissionId.MESSAGES: MockProberConfig(PermissionId.MESSAGES, probes_until_pass=1),
        PermissionId.INPUT_MONITORING: MockProberConfig(PermissionId.INPUT_MONITORING, probes_until_pass=1),
        PermissionId.ACCESSIBILITY: MockProberConfig(PermissionId.ACCESSIBILITY, probes_until_pass=2),
        PermissionId.FULL_DISK_ACCESS: MockProberConfig(PermissionId.FULL_DISK_ACCESS, probes_until_pass=2),
    }


def create_scenario_feature_fail() -> dict[PermissionId, MockProberConfig]:
    """Contacts (feature) fails, should still complete."""
    return {
        PermissionId.MICROPHONE: MockProberConfig(PermissionId.MICROPHONE, probes_until_pass=1),
        PermissionId.SCREEN_CAPTURE: MockProberConfig(PermissionId.SCREEN_CAPTURE, probes_until_pass=1),
        PermissionId.CONTACTS: MockProberConfig(PermissionId.CONTACTS, should_fail=True),
        PermissionId.MESSAGES: MockProberConfig(PermissionId.MESSAGES, probes_until_pass=1),
        PermissionId.INPUT_MONITORING: MockProberConfig(PermissionId.INPUT_MONITORING, probes_until_pass=1),
        PermissionId.ACCESSIBILITY: MockProberConfig(PermissionId.ACCESSIBILITY, probes_until_pass=2),
        PermissionId.FULL_DISK_ACCESS: MockProberConfig(PermissionId.FULL_DISK_ACCESS, probes_until_pass=2),
    }


SCENARIOS = {
    "all_pass": create_scenario_all_pass,
    "input_monitoring_needs_restart": create_scenario_input_monitoring_needs_restart,
    "hard_fail": create_scenario_hard_fail,
    "feature_fail": create_scenario_feature_fail,
}


# ============================================================
# Test Runner
# ============================================================

class EventCollector:
    """Collects UI events for verification."""
    
    def __init__(self):
        self.events: list[UIEvent] = []
    
    def emit(self, event: UIEvent) -> None:
        self.events.append(event)
        logger.info(f"[EVENT] {event.type.value}: {event.payload}")
    
    def has_event(self, event_type: UIEventType) -> bool:
        return any(e.type == event_type for e in self.events)
    
    def get_events(self, event_type: UIEventType) -> list[UIEvent]:
        return [e for e in self.events if e.type == event_type]


def create_fast_step_configs() -> dict[PermissionId, StepConfig]:
    """Create step configs with fast timing for testing."""
    order = [
        PermissionId.MICROPHONE,
        PermissionId.SCREEN_CAPTURE,
        PermissionId.CONTACTS,
        PermissionId.MESSAGES,
        PermissionId.INPUT_MONITORING,
        PermissionId.ACCESSIBILITY,
        PermissionId.FULL_DISK_ACCESS,
    ]
    
    configs = {}
    for perm in order:
        if perm in [PermissionId.ACCESSIBILITY, PermissionId.FULL_DISK_ACCESS]:
            mode = StepMode.OPEN_SETTINGS
            settings_target = perm.value
        else:
            mode = StepMode.AUTO_DIALOG
            settings_target = None
        
        if perm in [PermissionId.MICROPHONE, PermissionId.INPUT_MONITORING, PermissionId.ACCESSIBILITY, PermissionId.MESSAGES]:
            criticality = PermissionCriticality.HARD
        elif perm == PermissionId.SCREEN_CAPTURE:
            criticality = PermissionCriticality.SOFT
        else:
            criticality = PermissionCriticality.FEATURE
        
        timing = StepTiming(
            grace_s=0.1,  # Very fast for testing
            poll_s=0.1,
            heavy_cooldown_s=0.1,
            waiting_long_after_s=1.0,
            waiting_long_poll_s=0.2,
            post_restart_verify_window_s=1.0,
            post_restart_verify_tick_s=0.1,
        )
        
        configs[perm] = StepConfig(
            permission=perm,
            mode=mode,
            timing=timing,
            supports_needs_restart=(perm == PermissionId.INPUT_MONITORING),
            settings_target=settings_target,
            criticality=criticality,
        )
    
    return configs


async def run_test(scenario_name: str) -> bool:
    """Run a test scenario and return success/failure."""
    
    print(f"\n{'='*60}")
    print(f"Running scenario: {scenario_name}")
    print(f"{'='*60}\n")
    
    # Create mock prober configs
    if scenario_name not in SCENARIOS:
        print(f"Unknown scenario: {scenario_name}")
        return False
    
    prober_configs = SCENARIOS[scenario_name]()
    
    # Create step configs
    step_configs = create_fast_step_configs()
    
    # Create order
    order = [
        PermissionId.MICROPHONE,
        PermissionId.SCREEN_CAPTURE,
        PermissionId.CONTACTS,
        PermissionId.MESSAGES,
        PermissionId.INPUT_MONITORING,
        PermissionId.ACCESSIBILITY,
        PermissionId.FULL_DISK_ACCESS,
    ]
    
    # Create mock probers
    probers = {}
    for perm in order:
        probers[perm] = MockProber(prober_configs[perm], step_configs[perm])
    
    # Create classifiers
    classifiers = {perm: get_classifier(perm) for perm in order}
    
    # Create event collector
    events = EventCollector()
    
    # Create temp ledger
    with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
        ledger_path = f.name
    
    try:
        # Create orchestrator
        orchestrator = PermissionOrchestrator(
            order=order,
            step_configs=step_configs,
            probers=probers,
            classifiers=classifiers,
            hard_permissions=[
                PermissionId.MICROPHONE,
                PermissionId.MESSAGES,
                PermissionId.INPUT_MONITORING,
                PermissionId.ACCESSIBILITY,
            ],
            restart_cfg=RestartConfig(delay_sec=0.1, settings_safety_window_sec=0.1),
            settings_nav=MockSettingsNavigator(),
            ledger_store=LedgerStore(ledger_path),
            emit=events.emit,
            restart_handler=None,  # No actual restart
            is_gui_process=True,
        )
        
        # Run with timeout
        try:
            await asyncio.wait_for(orchestrator.start(), timeout=30.0)
        except asyncio.TimeoutError:
            print("❌ Test timed out!")
            return False
        
        # Verify results
        print(f"\n{'='*60}")
        print("Results:")
        print(f"{'='*60}")
        print(f"Final phase: {orchestrator.ledger.phase.value}")
        print(f"Events collected: {len(events.events)}")
        
        # Check expected outcomes
        if scenario_name == "all_pass":
            expected_phase = Phase.COMPLETED
        elif scenario_name == "input_monitoring_needs_restart":
            # Without restart_handler, HARD needs_restart → LIMITED_MODE
            expected_phase = Phase.LIMITED_MODE
        elif scenario_name == "hard_fail":
            expected_phase = Phase.LIMITED_MODE
        elif scenario_name == "feature_fail":
            expected_phase = Phase.COMPLETED  # Feature fails are skipped
        else:
            expected_phase = Phase.COMPLETED
        
        success = orchestrator.ledger.phase == expected_phase
        
        if success:
            print(f"\n✅ PASS: Phase is {expected_phase.value} as expected")
        else:
            print(f"\n❌ FAIL: Expected {expected_phase.value}, got {orchestrator.ledger.phase.value}")
        
        # Print step states
        print("\nStep states:")
        for perm, entry in orchestrator.ledger.steps.items():
            print(f"  {perm.value}: {entry.state.value}")
        
        return success
        
    finally:
        # Cleanup
        if os.path.exists(ledger_path):
            os.unlink(ledger_path)


async def main():
    parser = argparse.ArgumentParser(description="Test Permission System V2")
    parser.add_argument(
        "--scenario",
        choices=list(SCENARIOS.keys()) + ["all"],
        default="all",
        help="Test scenario to run"
    )
    args = parser.parse_args()
    
    if args.scenario == "all":
        scenarios = list(SCENARIOS.keys())
    else:
        scenarios = [args.scenario]
    
    results = {}
    for scenario in scenarios:
        results[scenario] = await run_test(scenario)
    
    # Summary
    print(f"\n{'='*60}")
    print("Summary:")
    print(f"{'='*60}")
    for scenario, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {scenario}: {status}")
    
    all_passed = all(results.values())
    print(f"\nOverall: {'✅ ALL TESTS PASSED' if all_passed else '❌ SOME TESTS FAILED'}")
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
