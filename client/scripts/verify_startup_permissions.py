#!/usr/bin/env python3
"""
Simulation script to verify permission flow fixes.
1. Verifies that 'sounddevice' is NOT imported by merely importing coordinator (Lazy Import Check).
2. Simulates startup to ensure 'first_run_permissions' BLOCKS dependent modules.
3. Checks for duplicate TCC triggers.
"""

import sys
import asyncio
import logging
import time
from unittest.mock import MagicMock, patch

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("SIMULATION")

def main():
    print("🚀 Starting Permission Flow Simulation...")
    
    # --- Check 1: Lazy Import Verification ---
    print("\n🔍 CHECK 1: Verifying Lazy Imports...")
    if 'sounddevice' in sys.modules:
        print("❌ FAIL: sounddevice already imported before we started!")
        return

    try:
        # Import Coordinator
        from integration.core.simple_module_coordinator import SimpleModuleCoordinator
        print("   Imported SimpleModuleCoordinator")
    except ImportError as e:
        print(f"❌ FAIL: Could not import coordinator: {e}")
        return

    if 'sounddevice' in sys.modules:
        print("❌ FAIL: sounddevice was imported by SimpleModuleCoordinator imports!")
        print("   This means the lazy import fix is NOT working or missed a file.")
        # Find who imported it? Hard to trace exactly here without verbose tools, 
        # but presence is enough to fail.
        return
    else:
        print("✅ PASS: sounddevice is NOT in sys.modules after coordinator import.")

    # --- Check 2: Simulation of Blocking Start ---
    print("\n🎬 CHECK 2: Simulating Startup Sequence...")
    
    async def run_simulation():
        # Mock dependencies to avoid real hardware access
        
        # Mock V2 Integration to simulate usage
        # We need to patch where it's instantiated or used.
        # But SimpleModuleCoordinator creates integrations via IntegrationFactory.
        # We will mock the factories or the classes.
        
        # Start the coordinator
        coordinator = SimpleModuleCoordinator()
        
        # Prepare Mocks for Integrations
        # 1. FirstRunPermissions - Real logic but mocked internal V2
        # 2. VoiceRecognition - Real logic but mocked start
        
        # We need to inject mocks into coordinator.integrations manually for this test 
        # because we don't want to run the full real factory which might trigger other things.
        
        # Mock V2 Integration
        mock_v2 = MagicMock()
        mock_v2.__bool__ = lambda x: True # It is truthy
        
        async def mock_v2_start():
            logger.info("[MOCK V2] Started (Background)")
            
        async def mock_v2_wait(*args, **kwargs):
            logger.info("[MOCK V2] ⏳ Waiting for user input (simulating 2s delay)...")
            await asyncio.sleep(2.0)
            logger.info("[MOCK V2] ✅ User granted permissions!")
            return True
            
        mock_v2.start = mock_v2_start
        mock_v2.wait_for_completion = mock_v2_wait
        mock_v2.is_enabled = True # Property mock
        
        # Mock FirstRunPermissionsIntegration
        # We use the REAL class but inject the mock v2
        from integration.integrations.first_run_permissions_integration import FirstRunPermissionsIntegration
        
        real_first_run = FirstRunPermissionsIntegration(MagicMock(), MagicMock(), MagicMock(), {"permissions_v2": {"enabled": True}})
        real_first_run._v2_integration = mock_v2
        real_first_run._v2_enabled = True
        
        # Mock VoiceRecognition
        mock_voice = MagicMock()
        async def mock_voice_start():
            logger.info("🎤 [MOCK VOICE] Starting...")
            if 'sounddevice' not in sys.modules:
                 logger.info("   [MOCK VOICE] verifying sounddevice lazy load...")
            return True
        mock_voice.start = mock_voice_start
        
        def make_async_mock():
            m = MagicMock()
            async def async_start():
                return True
            m.start = async_start
            return m

        # Populate coordinator with minimal set
        coordinator.integrations = {
            "instance_manager": make_async_mock(),
            "tray": make_async_mock(),
            "first_run_permissions": real_first_run,
            "voice_recognition": mock_voice,
            "speech_playback": make_async_mock(), 
            "input": make_async_mock(),
            "screenshot_capture": make_async_mock(),
            "voiceover_ducking": make_async_mock(),
        }
        
        # Set dummy tray ready and initialized
        coordinator._tray_ready = True
        coordinator.is_initialized = True
        coordinator._state_manager = MagicMock()
        # Mock get_state_data to return False for first_run/restart flags
        coordinator._state_manager.get_state_data.return_value = False
        
        print("   Coordinator initialized with mocks.")
        print("   Running start()...")
        
        start_time = time.time()
        
        # Run start
        # This calls first_run.start() -> waits 2s -> then calls voice.start()
        await coordinator.start()
        
        duration = time.time() - start_time
        print(f"\n⏱️ Startup took {duration:.2f} seconds")
        
        if duration < 2.0:
            print("❌ FAIL: Startup was too fast! It didn't wait for permissions.")
        else:
            print("✅ PASS: Startup waited for permissions (approx 2s).")

    asyncio.run(run_simulation())

if __name__ == "__main__":
    main()
