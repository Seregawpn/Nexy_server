"""
[POC] Verify Cookbook Workflow
This script simulates adding a new feature using the standardized templates.
It creates temporary files, initializes the integration, and verifies EventBus communication.
"""

import asyncio
import os
import shutil
import sys
import logging
from pathlib import Path

# Add project root to path
CLIENT_ROOT = Path(__file__).resolve().parent.parent / "client"
INTEGRATION_ROOT = Path(__file__).resolve().parent.parent / "integration"
ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(INTEGRATION_ROOT))

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(name)s - %(message)s")
logger = logging.getLogger("POC_VERIFIER")

async def run_poc():
    logger.info("🚀 Starting POC Verification...")
    
    # 1. Define paths
    template_module_src = CLIENT_ROOT / "modules" / "_module_template"
    poc_module_dst = CLIENT_ROOT / "modules" / "poc_feature"
    
    template_integration_src = INTEGRATION_ROOT / "integrations" / "_template_integration.py"
    poc_integration_dst = INTEGRATION_ROOT / "integrations" / "poc_integration.py"

    try:
        # 2. "Copy-Paste" (Phase 1 & 2 of Cookbook)
        logger.info("Phase 1: Creating POC Module...")
        if poc_module_dst.exists():
            shutil.rmtree(poc_module_dst)
        shutil.copytree(template_module_src, poc_module_dst)
        
        # Modify logic to mark it as POC
        with open(poc_module_dst / "core" / "logic.py", "r") as f:
             content = f.read()
        content = content.replace("TemplateLogic", "PocLogic")
        content = content.replace("TemplateConfig", "PocConfig")
        with open(poc_module_dst / "core" / "logic.py", "w") as f:
             f.write(content)
             
        # Modify types
        with open(poc_module_dst / "core" / "types.py", "r") as f:
            content = f.read()
        content = content.replace("class TemplateEvent:", "class PocEvent:")
        content = content.replace('template.start_process', 'poc.start')
        content = content.replace('template.process_completed', 'poc.completed')
        content = content.replace('TemplateConfig', 'PocConfig')
        with open(poc_module_dst / "core" / "types.py", "w") as f:
            f.write(content)

        # Update init
        with open(poc_module_dst / "__init__.py", "w") as f:
            f.write("from .core.logic import PocLogic\nfrom .core.types import PocConfig, PocEvent\n")


        logger.info("Phase 2: Creating POC Integration...")
        if poc_integration_dst.exists():
            os.remove(poc_integration_dst)
            
        with open(template_integration_src, "r") as f:
            content = f.read()
            
        # Customize integration
        content = content.replace("TemplateIntegration", "PocIntegration")
        content = content.replace("client.modules._module_template", "client.modules.poc_feature")
        content = content.replace("TemplateLogic", "PocLogic")
        content = content.replace("TemplateConfig", "PocConfig")
        content = content.replace("TemplateEvent", "PocEvent")
        content = content.replace("START_PROCESS", "START_PROCESS") # Keeps same name for var, but value changed in types
        
        with open(poc_integration_dst, "w") as f:
            f.write(content)

        # 3. Dynamic Import & Verification (Phase 3)
        logger.info("Phase 3: Runtime Verification...")
        
        # Import needs to happen AFTER files are created
        from integration.core.event_bus import EventBus
        # We need to dynamically import the new integration
        import importlib
        
        # Invalida caches to ensure we pick up new files
        importlib.invalidate_caches()
        
        spec = importlib.util.spec_from_file_location("poc_integration", str(poc_integration_dst))
        poc_integration_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(poc_integration_module)
        
        PocIntegration = poc_integration_module.PocIntegration
        
        # 4. Run Test
        event_bus = EventBus()
        # Mock ErrorHandler
        class MockErrorHandler:
            async def handle_error(self, e, ctx):
                logger.error(f"[MockErrorHandler] {ctx}: {e}")
        
        error_handler = MockErrorHandler()
        
        # Mock UnifiedConfigLoader to return enabled feature config
        
        # Mock UnifiedConfigLoader
        import client.config.unified_config_loader as ucl
        
        # Create a mock instance
        class MockConfigLoader:
            def get_feature_config(self, feature_name):
                 return {"enabled": True, "name": "poc_test"}
                 
        original_get_instance = ucl.UnifiedConfigLoader.get_instance
        ucl.UnifiedConfigLoader.get_instance = lambda: MockConfigLoader()

        try:
            integration = PocIntegration(event_bus, error_handler)
            
            logger.info("[Test] Initializing Integration...")
            await integration.initialize()
            
            # Subscribe to result
            future_result = asyncio.Future()
            async def on_complete(data):
                future_result.set_result(data)
            
            await event_bus.subscribe("poc.completed", on_complete)
            
            # Trigger
            logger.info("[Test] Publishing Trigger Event...")
            await event_bus.publish("poc.start", {"session_id": "test_session_123", "value": "Hello POC"})
            
            # Wait for result
            try:
                result = await asyncio.wait_for(future_result, timeout=2.0)
                logger.info(f"✅ [Test] Success! Received result: {result}")
            except asyncio.TimeoutError:
                logger.error("❌ [Test] Timeout! Did not receive completion event.")
                return False

            return True
        finally:
            # Restore mock
            ucl.UnifiedConfigLoader.get_instance = original_get_instance

    except Exception as e:
        logger.error(f"❌ [Test] Exception: {e}")
        import traceback
        traceback.print_exc()
        return False
        
    finally:
        logger.info("🧹 Cleanup...")
        if poc_module_dst.exists():
            shutil.rmtree(poc_module_dst)
        if poc_integration_dst.exists():
            os.remove(poc_integration_dst)

if __name__ == "__main__":
    success = asyncio.run(run_poc())
    if success:
        print("POC_VERIFIED")
        sys.exit(0)
    else:
        print("POC_FAILED")
        sys.exit(1)
