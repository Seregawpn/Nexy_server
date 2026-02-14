import logging
import os
import sys
import unittest

# Add current directory to path
sys.path.insert(0, os.getcwd())

# Mock rumps BEFORE importing menu_handler
from unittest.mock import MagicMock

sys.modules['rumps'] = MagicMock()

# Setup basic logging
logging.basicConfig(level=logging.INFO)

# Mock config loader to avoid dependency issues
sys.modules['config.unified_config_loader'] = MagicMock()
from config.unified_config_loader import UnifiedConfigLoader

UnifiedConfigLoader.get_instance = MagicMock()

# Import the class to test
# We need to mock tray_icon and other dependencies if they are imported at top level
sys.modules['modules.tray_controller.macos.tray_icon'] = MagicMock()

from modules.tray_controller.macos.menu_handler import MacOSTrayMenu


class TestMenuQuitLogic(unittest.TestCase):
    def setUp(self):
        # Create a mock for the rumps application
        self.mock_app = MagicMock()
        # Initialize the menu handler (constructor takes app_name, not app object)
        self.menu_handler = MacOSTrayMenu("TestApp")
        # Manually assign the mock app
        self.menu_handler.app = self.mock_app
        
        # Initialize the quit handler
        self.menu_handler._setup_quit_handler()

    def test_default_termination_blocked(self):
        """Test that termination is blocked by default"""
        print("\nTesting default termination behavior...")
        # Get the custom handler installed on the app
        handler = self.mock_app.applicationShouldTerminate
        
        # Check if it returns False (blocking termination)
        result = handler(None)
        print(f"custom_should_terminate returned: {result}")
        self.assertFalse(result, "Termination should be blocked by default")

    def test_quit_allows_termination(self):
        """Test that calling quit() allows termination"""
        print("\nTesting quit() behavior...")
        
        # 1. Verify flag is False initially
        self.assertFalse(getattr(self.menu_handler, '_quit_allowed', False), "Flag should be False initially")
        
        # 2. Call quit()
        print("Calling menu_handler.quit()...")
        self.menu_handler.quit()
        
        # 3. Verify flag is True
        self.assertTrue(self.menu_handler._quit_allowed, "Flag should be True after quit()")
        
        # 4. Verify handler now returns True
        handler = self.mock_app.applicationShouldTerminate
        result = handler(None)
        print(f"custom_should_terminate returned: {result}")
        self.assertTrue(result, "Termination should be allowed after quit()")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
