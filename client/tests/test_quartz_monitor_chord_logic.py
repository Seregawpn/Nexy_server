import time
import unittest
from unittest.mock import MagicMock, patch

# Define constants for the mock
kCGEventKeyDown = 10
kCGEventKeyUp = 11
kCGEventFlagsChanged = 12
kCGKeyboardEventKeycode = 0
kCGEventFlagMaskControl = 0x40000
kCGEventFlagMaskShift = 0x20000
kCGEventFlagMaskAlternate = 0x80000
kCGEventFlagMaskCommand = 0x100000


# Context manager to patch modules
class MockQuartzContext:
    def __enter__(self):
        # We need to mock the Quartz module structure
        mock_quartz = MagicMock()
        mock_quartz.kCGEventKeyDown = kCGEventKeyDown
        mock_quartz.kCGEventKeyUp = kCGEventKeyUp
        mock_quartz.kCGEventFlagsChanged = kCGEventFlagsChanged
        mock_quartz.kCGKeyboardEventKeycode = kCGKeyboardEventKeycode
        mock_quartz.kCGEventFlagMaskControl = kCGEventFlagMaskControl
        mock_quartz.kCGEventFlagMaskShift = kCGEventFlagMaskShift
        mock_quartz.kCGEventFlagMaskAlternate = kCGEventFlagMaskAlternate
        mock_quartz.kCGEventFlagMaskCommand = kCGEventFlagMaskCommand
        
        self.patcher = patch.dict("sys.modules", {"Quartz": mock_quartz})
        self.patcher.start()

        # Reload/Import the module under test
        import sys
        if "modules.input_processing.keyboard.mac.quartz_monitor" in sys.modules:
            del sys.modules["modules.input_processing.keyboard.mac.quartz_monitor"]

        from modules.input_processing.keyboard.mac.quartz_monitor import QuartzKeyboardMonitor
        self.QuartzKeyboardMonitor = QuartzKeyboardMonitor
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.patcher.stop()


class TestQuartzMonitorChordLogic(unittest.TestCase):
    def setUp(self):
        self.mock_event = MagicMock()

    def _create_monitor(self, quartz_cls):
        from modules.input_processing.keyboard.types import KeyboardConfig

        config = KeyboardConfig(
            key_to_monitor="ctrl_n",
            short_press_threshold=0.2,
            long_press_threshold=0.5,
            event_cooldown=0.0,
            hold_check_interval=0.1,
            debounce_time=0.1,
        )
        monitor = quartz_cls(config)
        monitor._tap = MagicMock()  # Fake enabled tap
        # Mock callbacks to verify event emission
        monitor._trigger_event = MagicMock()
        return monitor

    def test_strict_chord_suppression(self):
        """Verify strict suppression logic: Only pure Ctrl+N is intercepted."""
        with MockQuartzContext() as ctx:
            monitor = self._create_monitor(ctx.QuartzKeyboardMonitor)
            
            # We need to patch the imported functions in the module namespace
            from modules.input_processing.keyboard.mac import quartz_monitor

            with (
                patch.object(quartz_monitor, "CGEventGetFlags") as mock_get_flags,
                patch.object(quartz_monitor, "CGEventGetIntegerValueField") as mock_get_keycode,
            ):
                # --- SCENARIO 1: Target Combo (Ctrl+N) ---
                # Should be SUPPRESSED (return None) and EMIT press event
                
                # 1. Setup State (Ctrl pressed via FlagsChanged)
                mock_get_flags.return_value = kCGEventFlagMaskControl
                mock_get_keycode.return_value = 59 # Left Ctrl
                monitor._handle_combo_event(kCGEventFlagsChanged, self.mock_event)
                
                # 2. Press N
                mock_get_flags.return_value = kCGEventFlagMaskControl
                mock_get_keycode.return_value = 45 # N
                result = monitor._handle_combo_event(kCGEventKeyDown, self.mock_event)
                
                self.assertIsNone(result, "Target Combo (Ctrl+N) should be suppressed")
                self.assertTrue(monitor._n_pressed)
                self.assertTrue(monitor._control_pressed)
                monitor._trigger_event.assert_called() # Should emit event
                
                # Reset for next scenario
                monitor._deactivate_combo_locked(time.time(), "reset")
                monitor._trigger_event.reset_mock()

                # --- SCENARIO 2: Non-Target Modifier (Ctrl+Shift+N) ---
                # Should be PASSED THROUGH (return event) and NOT emit event
                
                # 1. Setup State (Ctrl + Shift)
                mock_get_flags.return_value = kCGEventFlagMaskControl | kCGEventFlagMaskShift
                mock_get_keycode.return_value = 59 
                monitor._handle_combo_event(kCGEventFlagsChanged, self.mock_event)
                
                # 2. Press N
                mock_get_flags.return_value = kCGEventFlagMaskControl | kCGEventFlagMaskShift
                mock_get_keycode.return_value = 45
                result = monitor._handle_combo_event(kCGEventKeyDown, self.mock_event)
                
                self.assertIsNotNone(result, "Non-Target (Ctrl+Shift+N) should pass through")
                monitor._trigger_event.assert_not_called() # Should NOT emit event

                # --- SCENARIO 3: Non-Target Modifier (Ctrl+Cmd+N) ---
                # Should be PASSED THROUGH
                
                mock_get_flags.return_value = kCGEventFlagMaskControl | kCGEventFlagMaskCommand
                result = monitor._handle_combo_event(kCGEventKeyDown, self.mock_event)
                self.assertIsNotNone(result, "Non-Target (Ctrl+Cmd+N) should pass through")
                monitor._trigger_event.assert_not_called()

                # --- SCENARIO 4: Just N (No Ctrl) ---
                
                mock_get_flags.return_value = 0
                result = monitor._handle_combo_event(kCGEventKeyDown, self.mock_event)
                self.assertIsNotNone(result, "Just N should pass through")
                monitor._trigger_event.assert_not_called()

    def test_pass_through_safety(self):
        """Verify that strictly non-target events are untouched."""
        with MockQuartzContext() as ctx:
            monitor = self._create_monitor(ctx.QuartzKeyboardMonitor)
            from modules.input_processing.keyboard.mac import quartz_monitor

            with (
                patch.object(quartz_monitor, "CGEventGetFlags") as mock_get_flags,
                patch.object(quartz_monitor, "CGEventGetIntegerValueField") as mock_get_keycode,
            ):
                 # Case: Ctrl+Shift+N
                 # Even if we have some internal state messiness, the strict check on the event itself
                 # must ensure pass-through coverage.
                 
                 monitor._control_pressed = True # Internal state says Ctrl is down
                 
                 # Event says Ctrl+Shift
                 mock_get_flags.return_value = kCGEventFlagMaskControl | kCGEventFlagMaskShift
                 mock_get_keycode.return_value = 45 # N
                 
                 result = monitor._handle_combo_event(kCGEventKeyDown, self.mock_event)
                 
                 self.assertIsNotNone(result, "Must pass-through if Shift is present in event")
                 self.assertFalse(monitor._combo_active, "Combo must NOT activate")

if __name__ == "__main__":
    unittest.main()
