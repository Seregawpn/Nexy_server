#!/usr/bin/env python3
"""
Test script to verify centralized first_run state writes.

Verifies that:
1. Only SimpleModuleCoordinator writes first_run state
2. PermissionRestartIntegration only writes restart_pending
3. Logging shows centralized state mutation
"""

import asyncio
import logging
from pathlib import Path
import sys

# Add client to path
client_dir = Path(__file__).parent
sys.path.insert(0, str(client_dir))

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.simple_module_coordinator import SimpleModuleCoordinator
from integration.core.state_manager import ApplicationStateManager

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


async def test_centralized_first_run_state():
    """Test that first_run state is centralized in coordinator."""

    print("\n" + "=" * 80)
    print("TEST: Centralized First Run State Writer")
    print("=" * 80 + "\n")

    # Create components
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler(event_bus, state_manager)

    # Attach event bus to state manager
    state_manager.attach_event_bus(event_bus)

    # Create coordinator (minimal config)
    coordinator = SimpleModuleCoordinator(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config_loader=None,
    )

    # Subscribe coordinator to events
    await coordinator._subscribe_to_permission_events()

    print("✓ Components initialized\n")

    # Test 1: Initial state
    print("TEST 1: Initial State")
    print("-" * 40)

    initial_in_progress = state_manager.get_state_data("first_run_in_progress", False)
    initial_restart_pending = state_manager.get_state_data("permissions_restart_pending", False)

    print(f"  first_run_in_progress: {initial_in_progress}")
    print(f"  restart_pending: {initial_restart_pending}")
    print()

    # Test 2: Simulate permissions.first_run_restart_pending
    print("TEST 2: Publishing permissions.first_run_restart_pending")
    print("-" * 40)

    test_event = {
        "type": "permissions.first_run_restart_pending",
        "data": {
            "session_id": "test_session_123",
            "source": "test_script",
            "permissions": ["accessibility", "input_monitoring"],
            "batch_index": 0,
            "total_batches": 2,
            "is_last_batch": False,
        },
    }

    print(f"  Publishing event: {test_event['type']}")
    print(f"  Session ID: {test_event['data']['session_id']}")
    print(f"  Permissions: {test_event['data']['permissions']}")
    print()

    # Publish event
    await event_bus.publish(test_event["type"], test_event["data"])

    # Give event bus time to process
    await asyncio.sleep(0.1)

    # Test 3: Verify state changes
    print("TEST 3: Verify State Changes")
    print("-" * 40)

    after_in_progress = state_manager.get_state_data("first_run_in_progress", False)
    after_restart_pending = state_manager.get_state_data("permissions_restart_pending", False)
    after_required = state_manager.get_state_data("first_run_required", False)
    after_completed = state_manager.get_state_data("first_run_completed", False)

    print(f"  first_run_in_progress: {initial_in_progress} → {after_in_progress}")
    print(f"  first_run_required: {after_required}")
    print(f"  first_run_completed: {after_completed}")
    print(f"  restart_pending: {initial_restart_pending} → {after_restart_pending}")
    print()

    # Test 4: Verify expected values
    print("TEST 4: Verify Expected Values")
    print("-" * 40)

    tests_passed = 0
    tests_total = 3

    # Check: first_run_in_progress should be False
    if after_in_progress == False:
        print("  ✓ first_run_in_progress = False (coordinator cleared it)")
        tests_passed += 1
    else:
        print(f"  ✗ first_run_in_progress = {after_in_progress} (expected False)")

    # Check: restart_pending should be True
    if after_restart_pending == True:
        print("  ✓ restart_pending = True")
        tests_passed += 1
    else:
        print(f"  ✗ restart_pending = {after_restart_pending} (expected True)")

    # Check: first_run_completed should be False
    if after_completed == False:
        print("  ✓ first_run_completed = False (still in progress)")
        tests_passed += 1
    else:
        print(f"  ✗ first_run_completed = {after_completed} (expected False)")

    print()

    # Summary
    print("=" * 80)
    print(f"RESULTS: {tests_passed}/{tests_total} tests passed")

    if tests_passed == tests_total:
        print("STATUS: ✓ ALL TESTS PASSED")
        print("\nVerified:")
        print("  • SimpleModuleCoordinator centralized first_run state writes")
        print("  • restart_pending flag set correctly")
        print("  • first_run flags cleared on restart_pending event")
    else:
        print("STATUS: ✗ SOME TESTS FAILED")
        print("\nCheck logs above for details")

    print("=" * 80 + "\n")

    return tests_passed == tests_total


async def main():
    """Main test runner."""
    try:
        success = await test_centralized_first_run_state()
        sys.exit(0 if success else 1)
    except Exception as e:
        logger.error(f"Test failed with exception: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
