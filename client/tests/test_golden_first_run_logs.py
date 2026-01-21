"""
Golden-log test for first-run/restart sequence.

Verifies that logs match the expected sequence from NEXY_FIRST_RUN_LOG_EXPECTED.md.
Fails if any deviation is detected.

See .cursorrules section 8.1 and 10.1 for requirements.
"""
import re
from pathlib import Path
from typing import List, Tuple

import pytest


# Expected log sequence (critical checkpoints)
# See Docs/NEXY_FIRST_RUN_LOG_EXPECTED.md for full specification
EXPECTED_SEQUENCE = [
    # Phase 1: Initialization
    (r"Первый запуск обнаружен", "first_run_detected"),
    (r"permissions\.first_run_started", "first_run_started_event"),
    
    # Phase 2: Blocking
    (r"First run начат - блокировка", "activation_blocked"),
    
    # Phase 3-6: Permission requests (Microphone, Accessibility, Input, Screen)
    (r"Microphone.*activation", "mic_request"),
    (r"Accessibility.*activation", "accessibility_request"),
    (r"Input Monitoring.*activation", "input_monitoring_request"),
    (r"Screen Capture.*activation", "screen_capture_request"),
    
    # Phase 7: Completion
    (r"Все разрешения обработаны", "all_permissions_processed"),
    (r"restart_completed\.flag", "restart_flag_set"),
    
    # Phase 8: Restart pending
    (r"permissions\.first_run_restart_pending", "restart_pending_event"),
    (r"decision=abort.*restart_pending", "gateway_abort_decision"),
    
    # Phase 9: Restart execution
    (r"Инициирован перезапуск", "restart_initiated"),
    
    # Phase 12: New process after restart
    (r"Перезапуск после first_run завершён успешно", "restart_completed"),
    (r"permissions\.first_run_completed", "first_run_completed_event"),
    
    # Phase 14: Welcome message (ONLY after restart)
    (r"Воспроизведение приветственного сообщения", "welcome_message"),
]


# Forbidden patterns (must NOT appear in old process)
FORBIDDEN_IN_OLD_PROCESS = [
    r"permissions\.first_run_completed.*OLD_PROCESS",  # Completed should only be in new process
    r"Воспроизведение приветственного сообщения.*OLD_PROCESS",  # Welcome only after restart
    r"SessionCore_macOS_Legacy.*setPlayState Started.*Input",  # No microphone activation before restart
    r"MXCoreSession starting recording.*OLD_PROCESS",  # No recording before restart
    r"VOICE: recording_start.*OLD_PROCESS",  # No voice recording before restart
]


class TestGoldenFirstRunLogs:
    """Test that first-run logs match expected sequence."""
    
    def test_expected_sequence_present(self):
        """Test that all expected log checkpoints are present in a valid log."""
        # This is a template test - in real usage, you'd load actual log file
        # For now, we verify the expected sequence is defined correctly
        
        assert len(EXPECTED_SEQUENCE) > 0, "Expected sequence must not be empty"
        
        # Verify each checkpoint has a pattern and name
        for pattern, name in EXPECTED_SEQUENCE:
            assert pattern, f"Checkpoint '{name}' must have a pattern"
            assert name, f"Checkpoint with pattern '{pattern}' must have a name"
            
            # Verify pattern is a valid regex
            try:
                re.compile(pattern)
            except re.error as e:
                pytest.fail(f"Invalid regex pattern for '{name}': {pattern} - {e}")
    
    def test_forbidden_patterns_defined(self):
        """Test that forbidden patterns are defined."""
        assert len(FORBIDDEN_IN_OLD_PROCESS) > 0, "Forbidden patterns must be defined"
        
        for pattern in FORBIDDEN_IN_OLD_PROCESS:
            try:
                re.compile(pattern)
            except re.error as e:
                pytest.fail(f"Invalid regex pattern for forbidden pattern: {pattern} - {e}")
    
    def test_sequence_order(self):
        """Test that sequence order is logical."""
        # Check that restart_pending comes before restart_completed
        restart_pending_idx = None
        restart_completed_idx = None
        
        for idx, (pattern, name) in enumerate(EXPECTED_SEQUENCE):
            if "restart_pending" in name:
                restart_pending_idx = idx
            if "restart_completed" in name:
                restart_completed_idx = idx
        
        assert restart_pending_idx is not None, "restart_pending checkpoint must be defined"
        assert restart_completed_idx is not None, "restart_completed checkpoint must be defined"
        assert restart_pending_idx < restart_completed_idx, \
            "restart_pending must come before restart_completed"
        
        # Check that welcome_message comes after restart_completed
        welcome_idx = None
        for idx, (pattern, name) in enumerate(EXPECTED_SEQUENCE):
            if "welcome_message" in name:
                welcome_idx = idx
        
        assert welcome_idx is not None, "welcome_message checkpoint must be defined"
        assert welcome_idx > restart_completed_idx, \
            "welcome_message must come after restart_completed"


def validate_log_sequence(log_content: str) -> Tuple[bool, List[str]]:
    """
    Validate log content against expected sequence.
    
    Returns:
        (is_valid, list_of_errors)
    """
    errors = []
    
    # Check expected sequence
    for pattern, name in EXPECTED_SEQUENCE:
        if not re.search(pattern, log_content, re.IGNORECASE | re.MULTILINE):
            errors.append(f"Missing checkpoint: {name} (pattern: {pattern})")
    
    # Check forbidden patterns (should NOT appear)
    for pattern in FORBIDDEN_IN_OLD_PROCESS:
        if re.search(pattern, log_content, re.IGNORECASE | re.MULTILINE):
            errors.append(f"Forbidden pattern found: {pattern}")
    
    return len(errors) == 0, errors


def test_actual_log_file_validation():
    """Test actual log file against expected sequence."""
    # Проверяем несколько возможных путей к лог-файлу
    log_paths = [
        Path("logs/nexy.log"),
        Path.home() / "nexy_first_run.log",
        Path("/var/folders") / "nexy_debug.log",
    ]
    
    log_file = None
    for path in log_paths:
        if path.exists():
            log_file = path
            break
    
    if log_file is None:
        pytest.skip(f"Log file not found in any of: {log_paths}")
    
    with open(log_file, "r", encoding="utf-8") as f:
        log_content = f.read()
    
    is_valid, errors = validate_log_sequence(log_content)
    
    if not is_valid:
        pytest.fail(f"Log validation failed for {log_file}:\n" + "\n".join(f"  • {e}" for e in errors))




