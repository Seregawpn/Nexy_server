"""
Golden tests for permission-restart gateway decisions.

Uses YAML fixtures with fixed snapshots → expected decisions.
Quickly catches regressions in "small conditions".
"""
import pytest
import yaml
from pathlib import Path

from integration.core.gateways import Decision, decide_start_listening
from integration.core.selectors import (
    AppMode,
    DeviceStatus,
    NetworkStatus,
    PermissionStatus,
    Snapshot,
)


def load_golden_test(filepath: Path) -> dict:
    """Load golden test YAML file."""
    with open(filepath, "r") as f:
        return yaml.safe_load(f)


def snapshot_from_dict(data: dict) -> Snapshot:
    """Create Snapshot from dict."""
    return Snapshot(
        perm_mic=PermissionStatus[data["perm_mic"].upper()],
        perm_screen=PermissionStatus[data["perm_screen"].upper()],
        perm_accessibility=PermissionStatus[data["perm_accessibility"].upper()],
        device_input=DeviceStatus[data["device_input"].upper()],
        network=NetworkStatus[data["network"].upper()],
        first_run=data["first_run"],
        app_mode=AppMode[data["app_mode"]],
    )


@pytest.mark.golden
class TestGoldenPermissionRestart:
    """Golden tests for permission-restart gateway decisions."""
    
    @pytest.fixture(scope="class")
    def golden_dir(self):
        """Path to golden test directory."""
        return Path(__file__).parent / "golden" / "permission_restart"
    
    @pytest.mark.parametrize(
        "test_file",
        [
            "mic_denied_abort.yaml",
            "first_run_blocks_activation.yaml",
            "network_offline_degrade.yaml",
        ],
    )
    def test_golden_decision(self, golden_dir, test_file, caplog):
        """Test golden decision snapshot."""
        test_path = golden_dir / test_file
        if not test_path.exists():
            pytest.skip(f"Golden test file not found: {test_path}")
        
        test_data = load_golden_test(test_path)
        snapshot = snapshot_from_dict(test_data["snapshot"])
        
        with caplog.at_level("DEBUG"):
            decision = decide_start_listening(snapshot)
        
        # Verify expected decision
        expected_decision = Decision[test_data["expected_decision"].upper()]
        assert decision == expected_decision, (
            f"Expected {expected_decision}, got {decision}\n"
            f"Test: {test_data['name']}\n"
            f"Snapshot: {test_data['snapshot']}"
        )
        
        # Verify decision log format
        logs = caplog.text
        assert f"decision={test_data['expected_decision']}" in logs
        assert f"source={test_data['expected_source']}" in logs
        
        # Verify context keys
        if "expected_ctx_keys" in test_data:
            for key in test_data["expected_ctx_keys"]:
                assert f"{key}=" in logs, f"Context key '{key}' not found in logs"

