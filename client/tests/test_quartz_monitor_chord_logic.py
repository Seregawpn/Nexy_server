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


# Function to setup the mock environment
def setup_quartz_mock():
    mock_quartz = MagicMock()
    mock_quartz.kCGEventKeyDown = kCGEventKeyDown
    mock_quartz.kCGEventKeyUp = kCGEventKeyUp
    mock_quartz.kCGEventFlagsChanged = kCGEventFlagsChanged
    mock_quartz.kCGKeyboardEventKeycode = kCGKeyboardEventKeycode
    mock_quartz.kCGEventFlagMaskControl = kCGEventFlagMaskControl
    mock_quartz.kCGEventFlagMaskShift = kCGEventFlagMaskShift
    mock_quartz.kCGEventFlagMaskAlternate = kCGEventFlagMaskAlternate
    mock_quartz.kCGEventFlagMaskCommand = kCGEventFlagMaskCommand

    # Mock specific functions that are imported from flags
    mock_quartz.CGEventGetFlags = MagicMock()
    mock_quartz.CGEventGetIntegerValueField = MagicMock()

    return mock_quartz


# Context manager to patch modules
class MockQuartzContext:
    def __enter__(self):
        self.patcher = patch.dict("sys.modules", {"Quartz": setup_quartz_mock()})
        self.patcher.start()

        # We need to reload the module if it was already imported, or import it now
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
        # Helper to create events
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
        return monitor

    def test_strict_chord_suppression(self):
        """Verify that ONLY Ctrl+N is suppressed, and others pass through."""
        with MockQuartzContext() as ctx:
            monitor = self._create_monitor(ctx.QuartzKeyboardMonitor)

            # Setup Event Mocks (we need to patch the imported functions in the module namespace)
            # Because the module does 'from Quartz import ...', patching sys.modules['Quartz']
            # works for the initial import. But we need to control the return values of
            # CGEventGetFlags and CGEventGetIntegerValueField which are bound at import time.

            # Actually, `quartz_monitor.py` imports them by name.
            # We can patch them on the module itself.
            from modules.input_processing.keyboard.mac import quartz_monitor

            with (
                patch.object(quartz_monitor, "CGEventGetFlags") as mock_get_flags,
                patch.object(quartz_monitor, "CGEventGetIntegerValueField") as mock_get_keycode,
            ):
                # Case 1: Pure Ctrl+N (Strictly allowed)
                # ---------------------------------------
                # 1. FlagsChanged: Control Down
                mock_get_flags.return_value = kCGEventFlagMaskControl
                mock_get_keycode.return_value = 59  # Left Control
                # We need to simulate the event processing
                monitor._handle_combo_event(kCGEventFlagsChanged, self.mock_event)

                # Verify state
                self.assertTrue(monitor._control_pressed, "Control should be pressed")
                self.assertFalse(monitor._combo_blocked_by_modifiers, "Should NOT be blocked")

                # 2. KeyDown: N (45)
                # Ensure flags are still Control
                mock_get_flags.return_value = kCGEventFlagMaskControl
                mock_get_keycode.return_value = 45  # N_KEYCODE

                # Check KeyDown
                result = monitor._handle_combo_event(kCGEventKeyDown, self.mock_event)
                # Should return None (suppressed)
                self.assertIsNone(result, "Ctrl+N should be suppressed")
                self.assertTrue(monitor._combo_active, "Combo should be active")

                # Reset
                monitor._deactivate_combo_locked(time.time(), "test")
                monitor._control_pressed = False  # Reset manually for next test

                # Case 2: Ctrl+Shift+N (Should pass through)
                # ------------------------------------------
                # 1. FlagsChanged: Ctrl + Shift
                mock_get_flags.return_value = kCGEventFlagMaskControl | kCGEventFlagMaskShift
                mock_get_keycode.return_value = 59
                monitor._handle_combo_event(kCGEventFlagsChanged, self.mock_event)

                self.assertTrue(monitor._control_pressed, "Control should be pressed")
                self.assertTrue(monitor._combo_blocked_by_modifiers, "Should be blocked by Shift")

                # 2. KeyDown: N
                mock_get_keycode.return_value = 45
                result = monitor._handle_combo_event(kCGEventKeyDown, self.mock_event)
                self.assertIsNotNone(result, "Ctrl+Shift+N should Pass-Through")
                self.assertFalse(
                    monitor._combo_active, "Combo should NOT be active for Ctrl+Shift+N"
                )

                monitor._control_pressed = False

                # Case 3: Ctrl+Cmd+N (Should pass through)
                # ------------------------------------------
                mock_get_flags.return_value = kCGEventFlagMaskControl | kCGEventFlagMaskCommand
                mock_get_keycode.return_value = 59
                monitor._handle_combo_event(kCGEventFlagsChanged, self.mock_event)

                mock_get_keycode.return_value = 45
                result = monitor._handle_combo_event(kCGEventKeyDown, self.mock_event)
                self.assertIsNotNone(result, "Ctrl+Cmd+N should Pass-Through")

                monitor._control_pressed = False

                # Case 4: Ctrl+Alt+N (Should pass through)
                # ------------------------------------------
                mock_get_flags.return_value = kCGEventFlagMaskControl | kCGEventFlagMaskAlternate
                mock_get_keycode.return_value = 59
                monitor._handle_combo_event(kCGEventFlagsChanged, self.mock_event)

                mock_get_keycode.return_value = 45
                result = monitor._handle_combo_event(kCGEventKeyDown, self.mock_event)
                self.assertIsNotNone(result, "Ctrl+Alt+N should Pass-Through")

    def test_debounce_logic_fix(self):
        """Verify the debounce logic correctly uses event flags instead of stale state."""
        with MockQuartzContext() as ctx:
            monitor = self._create_monitor(ctx.QuartzKeyboardMonitor)
            from modules.input_processing.keyboard.mac import quartz_monitor

            with (
                patch.object(quartz_monitor, "CGEventGetFlags") as mock_get_flags,
                patch.object(quartz_monitor, "CGEventGetIntegerValueField") as mock_get_keycode,
            ):
                # Setup:
                # 1. State thinks Control is pressed (stale)
                monitor._control_pressed = True

                # 2. But Event says Control is NOT pressed (user released it, but flagsChanged was missed or processed later)
                mock_get_flags.return_value = 0  # No flags
                mock_get_keycode.return_value = 45  # N

                # Set N pressed to trigger debounce check path
                monitor._n_pressed = True
                monitor.last_event_time = time.time()  # Recent event to trigger cooldown
                monitor.event_cooldown = 1.0  # Large cooldown

                # 3. Trigger KeyDown
                result = monitor._handle_combo_event(kCGEventKeyDown, self.mock_event)

                # 4. Expectation:
                # If using stale state: _control_pressed=True -> Suppress (None)
                # If using event flags: control_in_event=False -> Pass-through (result=event)
                self.assertIsNotNone(
                    result, "Should pass-through because Control is not in event flags"
                )


if __name__ == "__main__":
    unittest.main()
