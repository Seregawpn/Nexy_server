
import asyncio
import logging

from modules.permissions.v2.probers.messages import MessagesProber
from modules.permissions.v2.types import PermissionId, StepConfig, StepTiming

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

async def test_messages_prober():
    print("--- Starting Messages Prober Test ---")
    
    # Create timing config
    timing = StepTiming(grace_s=2.0, poll_s=0.5)
    
    # Create step config
    config = StepConfig(
        permission=PermissionId.MESSAGES,
        mode="auto_dialog",
        timing=timing,
        criticality="hard"
    )
    
    prober = MessagesProber(config)
    
    print("1. Triggering 'trigger()' (should launch background request)...")
    await prober.trigger()
    
    print("2. Sleeping 2 seconds to let trigger run...")
    await asyncio.sleep(2.0)
    
    print("3. Probing 'heavy' (actual check)...")
    result = await prober.probe("heavy")
    
    print("\n--- Result ---")
    print(f"Status: {'PASS' if result.evidence.messages_access_ok else 'FAIL'}")
    print(f"Evidence: {result.evidence}")
    print("----------------")

if __name__ == "__main__":
    asyncio.run(test_messages_prober())
