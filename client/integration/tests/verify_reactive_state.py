import asyncio
import logging
import sys
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler
from integration.integrations.action_execution_integration import ActionExecutionIntegration

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_reactive_cancellation():
    logger.info("🧪 Testing Reactive Action Cancellation...")
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    integration = ActionExecutionIntegration(event_bus, state_manager, error_handler)
    await integration.initialize()
    await integration.start()
    
    # Mock executor to stay active
    async def mock_execute(action_data):
        logger.info("Mock executor started, sleeping...")
        try:
            await asyncio.sleep(2.0)
            from modules.action_executor import ActionResult
            return ActionResult(success=True, message="Mock success")
        except asyncio.CancelledError:
            logger.info("Mock executor cancelled!")
            raise

    integration._executor.execute = mock_execute

    # Set initial mode to something OTHER than SLEEPING
    logger.info("Setting initial mode to PROCESSING...")
    state_manager.set_mode(AppMode.PROCESSING)
    await asyncio.sleep(0.1)

    session_id = "test_session_123"
    logger.info("Simulating started action...")
    # Manually trigger the reception of an action
    await event_bus.publish("grpc.response.action", {
        "session_id": session_id,
        "action_json": '{"command": "open_app", "args": {"app_name": "TestApp"}}'
    })
    
    # Wait a bit for the task to be created
    await asyncio.sleep(0.5)
    
    if session_id in integration._active_actions:
        logger.info(f"✅ Action is active for session {session_id}")
    else:
        logger.error("❌ Action failed to start")
        return

    # Now change mode to SLEEPING
    logger.info("Changing mode to SLEEPING...")
    state_manager.set_mode(AppMode.SLEEPING)
    
    # Wait for the event to be processed
    await asyncio.sleep(0.5)
    
    if session_id not in integration._active_actions:
        logger.info("✅ Action was successfully cancelled on mode change!")
    else:
        logger.error("❌ Action is still active after mode change to SLEEPING")

    await integration.stop()

def test_app_mode_consistency():
    logger.info("🧪 Testing AppMode Consistency...")
    try:
        from integration.core.state_manager import AppMode as SMAppMode
        from modules.mode_management import AppMode as MMAppMode
        
        if SMAppMode is MMAppMode:
            logger.info("✅ AppMode is consistently imported from modules.mode_management")
        else:
            logger.error("❌ AppMode mismatch between StateManager and ModeManager")
    except ImportError as e:
        logger.error(f"❌ Import error: {e}")

if __name__ == "__main__":
    test_app_mode_consistency()
    asyncio.run(test_reactive_cancellation())
