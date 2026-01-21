import sys
import os

# Set PYTHONPATH to include project root
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), "client"))

print("Running import verification...")

try:
    print("Importing state_manager...")
    from client.integration.core import state_manager
    print("✅ state_manager imported")
    
    print("Importing event_bus...")
    from client.integration.core import event_bus
    print("✅ event_bus imported")
    
    print("Importing selectors...")
    from client.integration.core import selectors
    print("✅ selectors imported")

    print("Importing simple_module_coordinator...")
    from client.integration.core import simple_module_coordinator
    print("✅ simple_module_coordinator imported")

    # Integrations (these might have dependencies, so we catch ImportError just in case dependencies are missing in this isolated test, but syntax errors should still be caught)
    print("Importing hardware_id_integration...")
    from client.integration.integrations import hardware_id_integration
    print("✅ hardware_id_integration imported")

    print("Importing input_processing_integration...")
    try:
        from client.integration.integrations import input_processing_integration
        print("✅ input_processing_integration imported")
    except ImportError as e:
         print(f"⚠️ input_processing_integration import failed (dependency?): {e}")

    print("Importing tray_controller_integration...")
    try:
        from client.integration.integrations import tray_controller_integration
        print("✅ tray_controller_integration imported")
    except ImportError as e:
        print(f"⚠️ tray_controller_integration import failed (dependency?): {e}")

    print("Importing instance_manager_integration...")
    from client.integration.integrations import instance_manager_integration
    print("✅ instance_manager_integration imported")

    print("Importing grpc_client_integration...")
    try:
        from client.integration.integrations import grpc_client_integration
        print("✅ grpc_client_integration imported")
    except ImportError as e:
        print(f"⚠️ grpc_client_integration import failed (dependency?): {e}")

    print("\n🎉 All critical modules imported successfully!")

except Exception as e:
    print(f"\n❌ Verification Failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
